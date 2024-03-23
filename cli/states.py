from typing import List
from collections import namedtuple

from data.storage import can_builds_be_loaded, load_builds

Transition = namedtuple('Transition', ['id', 'name', 'next_state'])


class State:
    def __init__(self):
        self._header = ''
        self._transitions = []

    @property
    def transitions(self) -> List[Transition]:
        return self._transitions

    def show(self):
        self._show()

    def go_to(self, transition_id: int) -> 'State':
        return self._go_to(transition_id)

    def _show(self):
        print(f'{self._header}\n')
        self._show_transitions()

    def _show_transitions(self):
        for transition in self._transitions:
            print(f'[{transition.id}] {transition.name}')

    def _go_to(self, transition_id: int) -> 'State':
        for transition in self._transitions:
            if transition.id == transition_id:
                return transition.next_state()
        return self


class Start(State):
    def __init__(self):
        super().__init__()
        self._header = 'MAIN MENU'
        self._transitions = [Transition(1, 'List builds', ListBuilds),  # TODO: change all next_states into function references i.e. self._list_builds
                             Transition(2, 'Create build', CreateBuild),
                             Transition(0, 'Exit', Exit)]


class Exit(State):
    def __init__(self):
        super().__init__()
        self._header = 'FAIR WINDS AND FOLLOWING SEAS!'

    def _show(self):
        print(f'{self._header}\n')
        exit()


class ListBuilds(State):
    def __init__(self):
        super().__init__()
        self._header = 'BUILDS'
        self._builds = [] if not can_builds_be_loaded() else load_builds()
        self._transitions = []

    def _show(self):
        print(f'{self._header}')
        self._show_grouped_builds()
        self._transitions.append(Transition(0, 'Back', Start))
        print(f'\n[0] Back\n')

    def _show_grouped_builds(self):
        sorted_ship_classes = sorted(set([build.ship.ship_class for build in self._builds]))
        sorted_builds = sorted(self._builds, key=lambda build: build.ship.ship_class)

        for ship_class in sorted_ship_classes:
            print(f'\n{ship_class}s:')
            for build_id, build in enumerate(sorted_builds, start=1):
                if build.ship.ship_class == ship_class:
                    self._transitions.append(Transition(build_id, build.name, ShowBuild))
                    print(f'  [{build_id}] {build.name}')

    def _go_to(self, transition_id: int) -> State:
        for transition in self._transitions:
            if transition.id == transition_id:
                return transition.next_state(build=self._builds[transition_id - 1]) if transition_id != 0 else transition.next_state()
        return self


class ShowBuild(State):
    def __init__(self, build):
        super().__init__()
        self._header = build.name.upper()
        self._build = build
        self._transitions = [Transition(1, 'Edit', State),  # TODO: EditBuild
                             Transition(2, 'Delete', State),  # TODO: DeleteBuild
                             Transition(0, 'Back', ListBuilds)]

    def _show(self):
        print(f'{self._header}\n')
        print(f'Ship: {self._build.ship.name}')
        print(f'Nation: {self._build.ship.nation}')
        print(f'Class: {self._build.ship.ship_class}')
        print(f'Tier: {self._build.ship.tier}')

        print('Skills:')
        for skill in self._build.skills:
            print(f'  {skill.name}')

        print('Upgrades:')
        for upgrade in self._build.upgrades.values():
            print(f'  {upgrade}')

        print('Consumables:')
        for consumable in self._build.consumables.values():
            print(f'  {consumable}')

        print()
        self._show_transitions()


class CreateBuild(State):
    def __init__(self):
        super().__init__()
        self._header = 'BUILD CREATOR'
        self._transitions = [Transition(1, 'Save', Start),
                             Transition(0, 'Discard', Start)]

    def _show(self):
        print(f'{self._header}\n')
        build_name = input('Build name: ')
        print()
        self._show_transitions()
