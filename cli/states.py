from typing import List
from collections import namedtuple

from model.build import Build
from data.storage import can_builds_be_loaded, load_builds

Transition = namedtuple('Transition', ['id', 'name', 'next_state'])


class State:
    def __init__(self):
        self._header = ''
        self._transitions = []

    @property
    def transitions(self) -> List[Transition]:
        return self._transitions

    def execute(self):
        self._execute()

    def go_to(self, transition_id: int) -> 'State':
        return self._go_to(transition_id)

    def _execute(self):
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
        self._transitions = [Transition(1, 'List builds', self._transition_to_list_builds),
                             Transition(2, 'Create build', self._transition_to_edit_build),
                             Transition(0, 'Exit', self._transition_to_exit)]

    def _transition_to_list_builds(self) -> State:
        return ListBuilds()

    def _transition_to_edit_build(self) -> State:
        return EditBuild()

    def _transition_to_exit(self) -> State:
        return Exit()


class Exit(State):
    def __init__(self):
        super().__init__()
        self._header = 'FAIR WINDS AND FOLLOWING SEAS!'

    def _execute(self):
        print(f'{self._header}\n')
        exit()


class ListBuilds(State):
    def __init__(self):
        super().__init__()
        self._header = 'BUILDS'
        self._builds = [] if not can_builds_be_loaded() else load_builds()
        self._transitions = []

    def _execute(self):
        print(f'{self._header}')
        self._show_grouped_builds()
        self._transitions.append(Transition(0, 'Back', Start))
        print(f'\n[0] Back\n')

    def _show_grouped_builds(self):
        self._builds = sorted(self._builds, key=lambda build: build.ship.ship_class)
        ship_classes = sorted(set([build.ship.ship_class for build in self._builds]))

        for ship_class in ship_classes:
            print(f'\n{ship_class}s:')
            for build_id, build in enumerate(self._builds, start=1):
                if build.ship.ship_class == ship_class:
                    self._transitions.append(Transition(build_id, build.name, self._transition_to_show_build))
                    print(f'  [{build_id}] {build.name}')

    def _go_to(self, transition_id: int) -> State:
        for transition in self._transitions:
            if transition.id == transition_id:
                return transition.next_state(build=self._builds[transition_id - 1]) if transition_id != 0 else transition.next_state()
        return self

    def _transition_to_show_build(self, build: Build) -> State:
        return ShowBuild(build)


class ShowBuild(State):
    def __init__(self, build):
        super().__init__()
        self._header = build.name.upper()
        self._build = build
        self._transitions = [Transition(1, 'Edit', self._transition_to_edit_build),
                             Transition(2, 'Delete', self._transition_to_delete_build),
                             Transition(0, 'Back', self._transition_to_list_builds)]

    def _execute(self):
        print(f'{self._header}\n')
        print(f'Ship: {self._build.ship.name}')
        print(f'Nation: {self._build.ship.nation}')
        print(f'Class: {self._build.ship.ship_class}')
        print(f'Tier: {self._build.ship.tier}')

        print('Skills:')
        for skill in self._build.skills:
            print(f'  {skill.cost} {skill.name}')

        print('Upgrades:')
        for slot, upgrade in self._build.upgrades.items():
            print(f'  {slot[-1]} {upgrade}')

        print('Consumables:')
        for slot, consumable in self._build.consumables.items():
            print(f'  {slot[-1]} {consumable}')

        print()
        self._show_transitions()

    def _transition_to_edit_build(self) -> State:
        return EditBuild(self._build)

    def _transition_to_delete_build(self) -> State:
        return State()

    def _transition_to_list_builds(self) -> State:
        return ListBuilds()


class EditBuild(State):
    def __init__(self, build: Build = None):
        super().__init__()
        self._header = 'BUILD EDITOR'
        self._build = build
        self._transitions = [Transition(1, 'Edit name', State),  # TODO: EditBuildName
                             Transition(9, 'Save', Start),
                             Transition(0, 'Discard', Start)]

    def _execute(self):
        print(f'{self._header}\n')
        if self._build:
            print(f'Name: {self._build.name}\n')
            print(f'Ship: {self._build.ship.name}')
        self._show_transitions()
