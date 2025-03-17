from typing import List
from collections import namedtuple

from model.ships.ship import Ship
from model.ships import ships
from model.build import Build
from data.storage import can_builds_be_loaded, load_builds, save_builds

Transition = namedtuple('Transition', ['id', 'name', 'next_state'])


class State:

    _builds = []

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

    def _print_build(self, build: Build):
        if build.ship:
            print(f'Ship: {build.ship.name}')
            print(f'Nation: {build.ship.nation}')
            print(f'Class: {build.ship.ship_class}')
            print(f'Tier: {build.ship.tier}')

        if build.skills:
            print('Skills:')
            for skill in build.sorted_skills:
                print(f'  {skill.cost} {skill.name}')

        if build.upgrades:
            print('Upgrades:')
            for slot, upgrade in build.sorted_upgrades.items():
                print(f'  {slot[-1]} {upgrade}')

        if build.consumables:
            print('Consumables:')
            for slot, consumable in build.sorted_consumables.items():
                print(f'  {slot[-1]} {consumable}')


class Start(State):
    def __init__(self):
        super().__init__()
        self._header = 'MAIN MENU'
        State._builds = load_builds() if not State._builds and can_builds_be_loaded() else State._builds
        self._transitions = [Transition(1, 'List builds', self._list_builds),
                             Transition(2, 'Create build', self._create_build),
                             Transition(0, 'Exit', self._exit)]

    def _list_builds(self) -> State:
        return ListBuilds()

    def _create_build(self) -> State:
        return EditBuild()

    def _exit(self) -> State:
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
        self._transitions = []

    def _execute(self):
        print(f'{self._header}')
        self._show_grouped_builds()
        self._transitions.append(Transition(0, 'Back', self._start))
        print(f'\n[0] Back\n')

    def _show_grouped_builds(self):
        self._builds = sorted(self._builds, key=lambda build: build.ship.ship_class)
        ship_classes = sorted(set([build.ship.ship_class for build in self._builds]))

        for ship_class in ship_classes:
            print(f'\n{ship_class}s:')
            for build_id, build in enumerate(self._builds, start=1):
                if build.ship.ship_class == ship_class:
                    self._transitions.append(Transition(build_id, build.name, self._show_build))
                    print(f'  [{build_id}] {build.name}')

    def _go_to(self, transition_id: int) -> State:
        for transition in self._transitions:
            if transition.id == transition_id:
                return transition.next_state(build=State._builds[transition_id - 1]) if transition_id != 0 else transition.next_state()
        return self

    def _start(self) -> State:
        return Start()

    def _show_build(self, build: Build) -> State:
        return ShowBuild(build)


class ShowBuild(State):
    def __init__(self, build):
        super().__init__()
        self._header = build.name.upper()
        self._build = build
        self._transitions = [Transition(1, 'Edit', self._edit_build),
                             Transition(2, 'Delete', self._delete_build),
                             Transition(0, 'Back', self._back)]

    def _execute(self):
        print(f'{self._header}\n')
        self._print_build(self._build)
        print()
        self._show_transitions()

    def _edit_build(self) -> State:
        return EditBuild(self._build)

    def _delete_build(self) -> State:
        return State()

    def _back(self) -> State:
        return ListBuilds()


class EditBuild(State):
    def __init__(self, build: Build = None, build_backup: Build = None):
        super().__init__()
        self._header = 'BUILD CREATOR'
        self._build = build or Build()
        self._build_backup = build_backup or self._build.copy()
        self._transitions = [Transition(1, 'Choose name', self._choose_name),
                             Transition(2, 'Choose ship', self._choose_ship),
                             Transition(0, 'Discard', self._discard)]

        if self._build.ship and self._build.total_skills_cost < 21:
            self._transitions.insert(-1, Transition(3, 'Add skill', self._add_skill))

        if self._build.skills:
            self._transitions.insert(-1, Transition(4, 'Remove skill', self._remove_skill))

        if self._build.ship:
            self._transitions.insert(-1, Transition(5, 'Add upgrade', self._add_upgrade))

        if self._build.upgrades:
            self._transitions.insert(-1, Transition(6, 'Remove upgrade', self._remove_upgrade))

        if self._build.ship:
            self._transitions.insert(-1, Transition(7, 'Add consumable', self._add_consumable))

        if self._build.name and self._build.ship:
            self._transitions.insert(-1, Transition(9, 'Save', self._save))

    def _execute(self):
        print(f'{self._header}')
        print() if self._build.name or self._build.ship else None
        print(f'Name: {self._build.name}') if self._build.name else None
        self._print_build(self._build)
        print()
        self._show_transitions()

    def _choose_name(self) -> State:
        return EditBuildName(self._build, self._build_backup)

    def _choose_ship(self) -> State:
        return EditBuildShip(self._build, self._build_backup)

    def _add_skill(self) -> State:
        return EditBuildAddSkill(self._build, self._build_backup)

    def _remove_skill(self) -> State:
        return EditBuildRemoveSkill(self._build, self._build_backup)

    def _add_upgrade(self) -> State:
        return EditBuildAddUpgrade(self._build, self._build_backup)

    def _remove_upgrade(self) -> State:
        return EditBuildRemoveUpgrade(self._build, self._build_backup)

    def _add_consumable(self) -> State:
        return EditBuildAddConsumable(self._build, self._build_backup)

    def _save(self) -> State:
        if self._build not in State._builds:
            State._builds.append(self._build)
        save_builds(State._builds)
        return Start()

    def _discard(self) -> State:
        if self._build in State._builds:
            State._builds.insert(State._builds.index(self._build), self._build_backup)
            State._builds.remove(self._build)
        return Start()


class EditBuildName(State):
    def __init__(self, build: Build, build_backup: Build):
        super().__init__()
        self._header = 'BUILD CREATOR - NAME'
        self._build = build
        self._build_backup = build_backup
        self._name = None
        self._transitions = [Transition(1, 'Confirm', self._confirm),
                             Transition(0, 'Discard', self._discard)]

    def _execute(self):
        print(f'{self._header}\n')
        self._name = input('Enter build name: ')
        print()
        self._show_transitions()

    def _confirm(self) -> State:
        self._build.name = self._name
        return EditBuild(self._build, self._build_backup)

    def _discard(self) -> State:
        return EditBuild(self._build, self._build_backup)


class EditBuildShip(State):
    def __init__(self, build: Build, build_backup: Build):
        super().__init__()
        self._header = 'BUILD CREATOR - SHIP'
        self._build = build
        self._build_backup = build_backup
        self._ship = None
        self._transitions = [Transition(1, 'Confirm', self._confirm),
                             Transition(0, 'Discard', self._discard)]

    def _execute(self):
        print(f'{self._header}\n')
        grouped_ships = self._show_grouped_ships()
        self._select_ship(grouped_ships)
        self._show_transitions()

    def _show_grouped_ships(self) -> List[Ship]:
        ship_classes = sorted(set([ship.ship_class for ship in ships]))
        ship_nations = sorted(set([ship.nation for ship in ships]))
        grouped_ships = []

        for ship_class in ship_classes:
            print(f'{ship_class}s:')
            for ship_nation in ship_nations:
                print(f'  {ship_nation}:') if any([ship for ship in ships if ship.ship_class == ship_class and ship.nation == ship_nation]) else None
                for ship in ships:
                    if ship.ship_class == ship_class and ship.nation == ship_nation:
                        grouped_ships.append(ship)
                        print(f'    [{grouped_ships.index(ship) + 1}] {ship.name}')

        return grouped_ships

    def _select_ship(self, grouped_ships: List[Ship]):
        ship_id = int(input('\nChoose ship: '))
        self._ship = grouped_ships[ship_id - 1]

        if self._build.ship:
            print('\nWARNING: changing ship will reset build skills, upgrades and consumables')

        print()

    def _confirm(self) -> State:
        self._build.ship = self._ship
        return EditBuild(self._build, self._build_backup)

    def _discard(self) -> State:
        return EditBuild(self._build, self._build_backup)


class EditBuildAddSkill(State):
    def __init__(self, build: Build, build_backup: Build):
        super().__init__()
        self._header = 'BUILD CREATOR - ADD SKILL'
        self._build = build
        self._build_backup = build_backup
        self._skill = None
        self._transitions = [Transition(1, 'Confirm', self._confirm),
                             Transition(0, 'Discard', self._discard)]

    def _execute(self):
        print(f'{self._header}\n')
        self._show_grouped_skills()
        self._select_skill()
        self._show_transitions()

    def _show_grouped_skills(self):
        total_skill_cost = self._build.total_skills_cost
        print(f'Total skill cost: {total_skill_cost}\n')
        skill_costs = sorted(set([skill.cost for skill in self._build.ship.skills if total_skill_cost + skill.cost <= 21]))

        for skill_cost in skill_costs:
            print(f'{skill_cost} point skills:')
            for skill_id, skill in enumerate(self._build.ship.skills, start=1):
                if skill.cost == skill_cost and not self._build.has_skill(skill):
                    print(f'  [{skill_id}] {skill.name}')

    def _select_skill(self):
        skill_id = int(input('\nChoose skill: '))
        skill = self._build.ship.skills[skill_id - 1]
        self._skill = skill
        print()

    def _confirm(self) -> State:
        self._build.add_skill(self._skill)
        return EditBuild(self._build, self._build_backup)

    def _discard(self) -> State:
        return EditBuild(self._build, self._build_backup)


class EditBuildRemoveSkill(State):
    def __init__(self, build: Build, build_backup: Build):
        super().__init__()
        self._header = 'BUILD CREATOR - REMOVE SKILL'
        self._build = build
        self._build_backup = build_backup
        self._skill = None
        self._transitions = [Transition(1, 'Confirm', self._confirm),
                             Transition(0, 'Discard', self._discard)]

    def _execute(self):
        print(f'{self._header}\n')
        self._show_grouped_skills()
        self._select_skill()
        self._show_transitions()

    def _show_grouped_skills(self):
        skill_costs = sorted(set([skill.cost for skill in self._build.skills]))

        for skill_cost in skill_costs:
            print(f'{skill_cost} point skills:')
            for skill_id, skill in enumerate(self._build.skills, start=1):
                if skill.cost == skill_cost:
                    print(f'  [{skill_id}] {skill.name}')

    def _select_skill(self):
        skill_id = int(input('\nChoose skill: '))
        skill = self._build.skills[skill_id - 1]
        self._skill = skill
        print()

    def _confirm(self) -> State:
        self._build.remove_skill(self._skill)
        return EditBuild(self._build, self._build_backup)

    def _discard(self) -> State:
        return EditBuild(self._build, self._build_backup)


class EditBuildAddUpgrade(State):
    def __init__(self, build: Build, build_backup: Build):
        super().__init__()
        self._header = 'BUILD CREATOR - ADD UPGRADE'
        self._build = build
        self._build_backup = build_backup
        self._upgrade = None
        self._upgrades = []
        self._transitions = [Transition(1, 'Confirm', self._confirm),
                             Transition(0, 'Discard', self._discard)]

    def _execute(self):
        print(f'{self._header}\n')
        self._show_grouped_upgrades()
        self._select_upgrade()
        self._show_transitions()

    def _show_grouped_upgrades(self):
        upgrade_slots = sorted([slot_name for slot_name in self._build.ship.upgrades.keys()])
        upgrade_id = 0

        for upgrade_slot in upgrade_slots:
            print(f'Slot {upgrade_slot[-1]} upgrades:')
            for upgrade in self._build.ship.upgrades[upgrade_slot]:
                if not self._build.has_upgrade(upgrade):
                    self._upgrades.append(upgrade)
                    upgrade_id += 1
                    print(f'  [{upgrade_id}] {upgrade}')

    def _select_upgrade(self):
        upgrade_id = int(input('\nChoose upgrade: '))
        upgrade = self._upgrades[upgrade_id - 1]
        self._upgrade = upgrade
        print()

    def _confirm(self) -> State:
        self._build.add_upgrade(self._upgrade)
        return EditBuild(self._build, self._build_backup)

    def _discard(self) -> State:
        return EditBuild(self._build, self._build_backup)


class EditBuildRemoveUpgrade(State):
    def __init__(self, build: Build, build_backup: Build):
        super().__init__()
        self._header = 'BUILD CREATOR - REMOVE UPGRADE'
        self._build = build
        self._build_backup = build_backup
        self._upgrade = None
        self._upgrades = []
        self._transitions = [Transition(1, 'Confirm', self._confirm),
                             Transition(0, 'Discard', self._discard)]

    def _execute(self):
        print(f'{self._header}\n')
        self._show_grouped_upgrades()
        self._select_upgrade()
        self._show_transitions()

    def _show_grouped_upgrades(self):
        upgrade_slots = sorted([slot_name for slot_name in self._build.upgrades.keys()])
        upgrade_id = 0

        for upgrade_slot in upgrade_slots:
            print(f'Slot {upgrade_slot[-1]} upgrade:')
            upgrade = self._build.upgrades[upgrade_slot]
            self._upgrades.append(upgrade)
            upgrade_id += 1
            print(f'  [{upgrade_id}] {upgrade}')

    def _select_upgrade(self):
        upgrade_id = int(input('\nChoose upgrade: '))
        upgrade = self._upgrades[upgrade_id - 1]
        self._upgrade = upgrade
        print()

    def _confirm(self) -> State:
        self._build.remove_upgrade(self._upgrade)
        return EditBuild(self._build, self._build_backup)

    def _discard(self) -> State:
        return EditBuild(self._build, self._build_backup)


class EditBuildAddConsumable(State):
    def __init__(self, build: Build, build_backup: Build):
        super().__init__()
        self._header = 'BUILD CREATOR - ADD CONSUMABLE'
        self._build = build
        self._build_backup = build_backup
        self._consumable = None
        self._consumables = []
        self._transitions = [Transition(1, 'Confirm', self._confirm),
                             Transition(0, 'Discard', self._discard)]

    def _execute(self):
        print(f'{self._header}\n')
        self._show_grouped_consumables()
        self._select_consumable()
        self._show_transitions()

    def _show_grouped_consumables(self):
        consumable_slots = sorted([slot_name for slot_name in self._build.ship.consumables.keys()])
        consumable_id = 0

        for consumable_slot in consumable_slots:
            print(f'Slot {consumable_slot[-1]} consumables:')
            for consumable in self._build.ship.consumables[consumable_slot]:
                if not self._build.has_consumable(consumable):
                    self._consumables.append(consumable)
                    consumable_id += 1
                    print(f'  [{consumable_id}] {consumable}')

    def _select_consumable(self):
        consumable_id = int(input('\nChoose consumable: '))
        consumable = self._consumables[consumable_id - 1]
        self._consumable = consumable
        print()

    def _confirm(self) -> State:
        self._build.add_consumable(self._consumable)
        return EditBuild(self._build, self._build_backup)

    def _discard(self) -> State:
        return EditBuild(self._build, self._build_backup)
