from pytest import fixture
from unittest.mock import Mock, patch, call

from cli.states import (Transition,
                        State,
                        Start,
                        Exit,
                        ListBuilds,
                        ShowBuild,
                        EditBuild,
                        EditBuildName,
                        EditBuildShip,
                        EditBuildAddSkill,
                        EditBuildAddUpgrade,
                        EditBuildAddConsumable)


@fixture
def build():
    build = Mock()
    build.name = 'build name'
    build.total_skills_cost = 0
    build.ship = Mock()
    return build


@fixture
def builds(build):
    return [build, Mock()]


@fixture
def state():
    return State()


@fixture
def start():
    return Start()


@fixture
def exit():
    return Exit()


@fixture
def list_builds():
    return ListBuilds()


@fixture
def show_build(build):
    return ShowBuild(build=build)


@fixture
def edit_build(build):
    return EditBuild(build=build)


@fixture
def edit_build_name(build):
    return EditBuildName(build=build)


@fixture
def edit_build_ship(build):
    return EditBuildShip(build=build)


@fixture
def edit_build_add_skill(build):
    return EditBuildAddSkill(build=build)


@fixture
def edit_build_add_upgrade(build):
    return EditBuildAddUpgrade(build=build)


@fixture
def edit_build_add_consumable(build):
    return EditBuildAddConsumable(build=build)


def test_state_has_correct_attributes(state):
    assert state._builds == []
    assert state._header == ''
    assert state._transitions == []


def test_state_transitions_return_correct_value(state):
    state._transitions = [Transition(1, 'Transition 1', Mock()),
                          Transition(2, 'Transition 2', Mock())]

    assert state.transitions == state._transitions


def test_state_execute_does_correct_execution(state):
    state._execute = Mock()

    state.execute()

    state._execute.assert_called_once_with()


def test_go_to_navigates_through_correct_transition(state):
    transition_id = 1
    state._go_to = Mock()

    state.go_to(transition_id=transition_id)

    state._go_to.assert_called_once_with(transition_id)


def test_go_to_returns_correct_state(state):
    next_state = State()
    state._go_to = Mock(return_value=next_state)

    returned_state = state.go_to(transition_id=1)

    assert returned_state == next_state


def test_state__execute_does_correct_execution(state):
    state._header = 'Header'
    state._show_transitions = Mock()
    mocked_print = Mock()

    with patch('builtins.print', mocked_print):
        state._execute()

    mocked_print.assert_called_once_with(f'{state._header}\n')
    state._show_transitions.assert_called_once_with()


def test_state__show_transitions_prints_correct_transitions(state):
    state._transitions = [Transition(1, 'Transition 1', Mock()),
                          Transition(2, 'Transition 2', Mock())]
    mocked_print = Mock()

    with patch('builtins.print', mocked_print):
        state._show_transitions()

    mocked_print.assert_has_calls([call(f'[{state._transitions[0].id}] {state._transitions[0].name}'),
                                   call(f'[{state._transitions[1].id}] {state._transitions[1].name}')])


def test_state__go_to_when_transition_is_found_then_next_state_is_returned(state):
    next_state = State()
    state._transitions = [Transition(1, 'Transition 1', Mock(return_value=None)),
                          Transition(2, 'Transition 2', Mock(return_value=next_state))]

    returned_state = state._go_to(transition_id=2)

    assert returned_state == next_state


def test_state__go_to_when_transition_is_not_found_then_state_returns_itself(state):
    state._transitions = [Transition(1, 'Transition 1', Mock()),
                          Transition(2, 'Transition 2', Mock())]

    returned_state = state._go_to(transition_id=3)

    assert returned_state is state


def test_state__print_build_when_build_is_empty_then_nothing_is_printed(state):
    build = Mock()
    build.ship = None
    build.skills = []
    build.upgrades = {}
    build.consumables = {}
    mocked_print = Mock()

    with patch('builtins.print', mocked_print):
        state._print_build(build=build)

    mocked_print.assert_not_called()


def test_state__print_build_when_build_is_not_empty_then_it_is_printed(state):
    build = Mock()
    skill_1, skill_2 = Mock(), Mock()
    build.skills = [skill_2, skill_1]
    build.sorted_skills = [skill_1, skill_2]
    upgrade_1, upgrade_2 = Mock(), Mock()
    build.upgrades = {'slot_2': upgrade_2, 'slot_1': upgrade_1}
    build.sorted_upgrades = {'slot_1': upgrade_1, 'slot_2': upgrade_2}
    consumable_1, consumable_2 = Mock(), Mock()
    build.consumables = {'slot_2': consumable_2, 'slot_1': consumable_1}
    build.sorted_consumables = {'slot_1': consumable_1, 'slot_2': consumable_2}
    mocked_print = Mock()

    with patch('builtins.print', mocked_print):
        state._print_build(build=build)

    mocked_print.assert_has_calls([call(f'Ship: {build.ship.name}'),
                                   call(f'Nation: {build.ship.nation}'),
                                   call(f'Class: {build.ship.ship_class}'),
                                   call(f'Tier: {build.ship.tier}'),
                                   call('Skills:'),
                                   call(f'  {skill_1.cost} {skill_1.name}'),
                                   call(f'  {skill_2.cost} {skill_2.name}'),
                                   call('Upgrades:'),
                                   call(f'  1 {upgrade_1}'),
                                   call(f'  2 {upgrade_2}'),
                                   call('Consumables:'),
                                   call(f'  1 {consumable_1}'),
                                   call(f'  2 {consumable_2}')])


def test_start_has_correct_attributes(builds):
    State._builds = builds
    start = Start()

    assert start._header == 'MAIN MENU'
    assert start._builds == builds
    assert start._transitions == [Transition(1, 'List builds', start._list_builds),
                                  Transition(2, 'Create build', start._create_build),
                                  Transition(0, 'Exit', start._exit)]


def test_start_when_no_builds_and_they_can_be_loaded_then_they_are_loaded(builds):
    State._builds = []
    can_builds_be_loaded = Mock(return_value=True)
    load_builds = Mock(return_value=builds)

    with patch('cli.states.can_builds_be_loaded', can_builds_be_loaded), patch('cli.states.load_builds', load_builds):
        start = Start()

    can_builds_be_loaded.assert_called_once_with()
    load_builds.assert_called_once_with()
    assert start._builds == builds


def test_start_when_no_builds_and_they_cannot_be_loaded_then_they_are_not_loaded():
    State._builds = []
    can_builds_be_loaded = Mock(return_value=False)
    load_builds = Mock()

    with patch('cli.states.can_builds_be_loaded', can_builds_be_loaded), patch('cli.states.load_builds', load_builds):
        start = Start()

    can_builds_be_loaded.assert_called_once_with()
    load_builds.assert_not_called()
    assert start._builds == []


def test_start__list_builds_returns_correct_state(start):
    returned_state = start._list_builds()

    assert isinstance(returned_state, ListBuilds)


def test_start__create_build_returns_correct_state(start):
    returned_state = start._create_build()

    assert isinstance(returned_state, EditBuild)


def test_start__exit_returns_correct_state(start):
    returned_state = start._exit()

    assert isinstance(returned_state, Exit)


def test_exit_has_correct_attributes(exit):
    assert exit._header == 'FAIR WINDS AND FOLLOWING SEAS!'


def test_exit__execute_does_correct_execution(exit):
    mocked_print = Mock()
    mocked_exit = Mock()

    with patch('builtins.print', mocked_print), patch('builtins.exit', mocked_exit):
        exit._execute()

    mocked_print.assert_called_once_with(f'{exit._header}\n')
    mocked_exit.assert_called_once_with()


def test_list_builds_has_correct_attributes(list_builds):
    assert list_builds._header == 'BUILDS'
    assert list_builds._transitions == []


def test_list_builds__execute_does_correct_execution(list_builds):
    list_builds._show_grouped_builds = Mock()
    mocked_print = Mock()

    with patch('builtins.print', mocked_print):
        list_builds._execute()

    mocked_print.assert_has_calls([call(f'{list_builds._header}'),
                                   call(f'\n[0] Back\n')])
    list_builds._show_grouped_builds.assert_called_once_with()
    assert Transition(0, 'Back', list_builds._start) in list_builds._transitions


def test_list_builds__show_grouped_builds_groups_builds_in_correct_order(list_builds):
    build_battleship_1 = Mock()
    build_battleship_1.ship.ship_class = 'Battleship'
    build_battleship_1.name = 'build_battleship_1'
    build_battleship_2 = Mock()
    build_battleship_2.ship.ship_class = 'Battleship'
    build_battleship_2.name = 'build_battleship_2'
    build_cruiser_1 = Mock()
    build_cruiser_1.ship.ship_class = 'Cruiser'
    build_cruiser_1.name = 'build_cruiser_1'
    build_cruiser_2 = Mock()
    build_cruiser_2.ship.ship_class = 'Cruiser'
    build_cruiser_2.name = 'build_cruiser_2'
    list_builds._builds = [build_cruiser_1, build_battleship_1, build_cruiser_2, build_battleship_2]
    mocked_print = Mock()

    with patch('builtins.print', mocked_print):
        list_builds._show_grouped_builds()

    mocked_print.assert_has_calls([call(f'\nBattleships:'),
                                   call(f'  [1] {build_battleship_1.name}'),
                                   call(f'  [2] {build_battleship_2.name}'),
                                   call(f'\nCruisers:'),
                                   call(f'  [3] {build_cruiser_1.name}'),
                                   call(f'  [4] {build_cruiser_2.name}')])
    assert list_builds._transitions == [Transition(1, build_battleship_1.name, list_builds._show_build),
                                        Transition(2, build_battleship_2.name, list_builds._show_build),
                                        Transition(3, build_cruiser_1.name, list_builds._show_build),
                                        Transition(4, build_cruiser_2.name, list_builds._show_build)]


def test_list_builds__go_to_when_transition_is_found_and_its_id_is_not_a_zero_then_build_is_used_and_next_state_is_returned(list_builds):
    build = Mock()
    State._builds = [build]
    next_state = State()
    transition_id = 1
    list_builds._transitions = [Transition(0, 'Transition 0', Mock(return_value=None)),
                                Transition(1, 'Transition 1', Mock(return_value=next_state))]

    returned_state = list_builds._go_to(transition_id=transition_id)

    list_builds._transitions[transition_id].next_state.assert_called_once_with(build=build)
    assert returned_state == next_state


def test_list_builds__go_to_when_transition_is_found_and_its_id_is_a_zero_then_build_is_not_used_and_next_state_is_returned(list_builds):
    next_state = State()
    transition_id = 0
    list_builds._transitions = [Transition(0, 'Transition 0', Mock(return_value=next_state)),
                                Transition(1, 'Transition 1', Mock(return_value=None))]

    returned_state = list_builds._go_to(transition_id=transition_id)

    list_builds._transitions[transition_id].next_state.assert_called_once_with()
    assert returned_state == next_state


def test_list_builds__go_to_when_transition_is_not_found_then_state_returns_itself(list_builds):
    list_builds._transitions = [Transition(0, 'Transition 0', Mock()),
                                Transition(1, 'Transition 1', Mock())]

    returned_state = list_builds._go_to(transition_id=3)

    assert returned_state is list_builds


def test_list_builds__start_returns_correct_state(list_builds):
    returned_state = list_builds._start()

    assert isinstance(returned_state, Start)


def test_list_builds__show_build_returns_correct_state(list_builds):
    returned_state = list_builds._show_build(build=Mock())

    assert isinstance(returned_state, ShowBuild)


def test_list_builds__show_build_uses_correct_build(list_builds, build):
    show_build_state = Mock()

    with patch('cli.states.ShowBuild', show_build_state):
        list_builds._show_build(build=build)

    show_build_state.assert_called_once_with(build)


def test_show_build_has_correct_attributes(show_build, build):
    assert show_build._header == 'BUILD NAME'
    assert show_build._build == build
    assert show_build._transitions == [Transition(1, 'Edit', show_build._edit_build),
                                       Transition(2, 'Delete', show_build._delete_build),
                                       Transition(0, 'Back', show_build._back)]


def test_show_build__execute_does_correct_execution(show_build):
    show_build._print_build = Mock()
    show_build._show_transitions = Mock()
    mocked_print = Mock()

    with patch('builtins.print', mocked_print):
        show_build._execute()

    show_build._print_build.assert_called_once_with(show_build._build)
    show_build._show_transitions.assert_called_once_with()
    mocked_print.assert_has_calls([call(f'{show_build._header}\n'),
                                   call()])


def test_show_build__edit_build_returns_correct_state(show_build):
    returned_state = show_build._edit_build()

    assert isinstance(returned_state, EditBuild)


def test_show_build__edit_build_uses_correct_build(show_build, build):
    edit_build_state = Mock()

    with patch('cli.states.EditBuild', edit_build_state):
        show_build._edit_build()

    edit_build_state.assert_called_once_with(build)


def test_show_build__delete_build_returns_correct_state(show_build):
    returned_state = show_build._delete_build()

    assert isinstance(returned_state, State)


def test_show_build__back_returns_correct_state(show_build):
    returned_state = show_build._back()

    assert isinstance(returned_state, ListBuilds)


def test_edit_build_when_build_not_provided_then_has_correct_attributes(build):
    build.ship = None
    build.name = None
    build_ctor = Mock(return_value=build)

    with patch('cli.states.Build', build_ctor):
        edit_build = EditBuild()

    assert edit_build._header == 'BUILD CREATOR'
    build_ctor.assert_called_once_with()
    assert edit_build._build == build
    assert edit_build._transitions == [Transition(1, 'Choose name', edit_build._choose_name),
                                       Transition(2, 'Choose ship', edit_build._choose_ship),
                                       Transition(0, 'Discard', edit_build._discard)]


def test_edit_build_when_build_provided_then_has_correct_attributes(edit_build, build):
    assert edit_build._header == 'BUILD CREATOR'
    assert edit_build._build == build
    assert edit_build._transitions == [Transition(1, 'Choose name', edit_build._choose_name),
                                       Transition(2, 'Choose ship', edit_build._choose_ship),
                                       Transition(3, 'Add skill', edit_build._add_skill),
                                       Transition(4, 'Add upgrade', edit_build._add_upgrade),
                                       Transition(5, 'Add consumable', edit_build._add_consumable),
                                       Transition(9, 'Save', edit_build._save),
                                       Transition(0, 'Discard', edit_build._discard)]


def test_edit_build__execute_when_build_has_name_then_correct_execution_is_done(edit_build, build):
    edit_build._print_build = Mock()
    edit_build._show_transitions = Mock()
    mocked_print = Mock()

    with patch('builtins.print', mocked_print):
        edit_build._execute()

    edit_build._print_build.assert_called_once_with(edit_build._build)
    edit_build._show_transitions.assert_called_once_with()
    mocked_print.assert_has_calls([call(f'{edit_build._header}'),
                                   call(),
                                   call(f'Name: {edit_build._build.name}'),
                                   call()])
    assert mocked_print.call_count == 4


def test_edit_build__execute_when_build_has_no_name_but_has_ship_then_correct_execution_is_done(edit_build, build):
    build.name = None
    edit_build._print_build = Mock()
    edit_build._show_transitions = Mock()
    mocked_print = Mock()

    with patch('builtins.print', mocked_print):
        edit_build._execute()

    edit_build._print_build.assert_called_once_with(edit_build._build)
    edit_build._show_transitions.assert_called_once_with()
    mocked_print.assert_has_calls([call(f'{edit_build._header}'),
                                   call(),
                                   call()])
    assert mocked_print.call_count == 3


def test_edit_build__execute_when_build_has_no_name_and_no_ship_then_correct_execution_is_done(edit_build, build):
    build.name = None
    build.ship = None
    edit_build._print_build = Mock()
    edit_build._show_transitions = Mock()
    mocked_print = Mock()

    with patch('builtins.print', mocked_print):
        edit_build._execute()

    edit_build._print_build.assert_called_once_with(edit_build._build)
    edit_build._show_transitions.assert_called_once_with()
    mocked_print.assert_has_calls([call(f'{edit_build._header}'),
                                   call()])
    assert mocked_print.call_count == 2


def test_edit_build__choose_name_returns_correct_state(edit_build):
    returned_state = edit_build._choose_name()

    assert isinstance(returned_state, EditBuildName)


def test_edit_build__choose_name_uses_correct_build(edit_build, build):
    edit_build_name_state = Mock()

    with patch('cli.states.EditBuildName', edit_build_name_state):
        edit_build._choose_name()

    edit_build_name_state.assert_called_once_with(build)


def test_edit_build__choose_ship_returns_correct_state(edit_build):
    returned_state = edit_build._choose_ship()

    assert isinstance(returned_state, EditBuildShip)


def test_edit_build__choose_ship_uses_correct_build(edit_build, build):
    edit_build_ship_state = Mock()

    with patch('cli.states.EditBuildShip', edit_build_ship_state):
        edit_build._choose_ship()

    edit_build_ship_state.assert_called_once_with(build)


def test_edit_build__add_skill_returns_correct_state(edit_build):
    returned_state = edit_build._add_skill()

    assert isinstance(returned_state, EditBuildAddSkill)


def test_edit_build__add_skill_uses_correct_build(edit_build, build):
    edit_build_add_skill_state = Mock()

    with patch('cli.states.EditBuildAddSkill', edit_build_add_skill_state):
        edit_build._add_skill()

    edit_build_add_skill_state.assert_called_once_with(build)


def test_edit_build__add_upgrade_returns_correct_state(edit_build):
    returned_state = edit_build._add_upgrade()

    assert isinstance(returned_state, EditBuildAddUpgrade)


def test_edit_build__add_upgrade_uses_correct_build(edit_build, build):
    edit_build_add_upgrade_state = Mock()

    with patch('cli.states.EditBuildAddUpgrade', edit_build_add_upgrade_state):
        edit_build._add_upgrade()

    edit_build_add_upgrade_state.assert_called_once_with(build)


def test_edit_build__add_consumable_returns_correct_state(edit_build):
    returned_state = edit_build._add_consumable()

    assert isinstance(returned_state, EditBuildAddConsumable)


def test_edit_build__add_consumable_uses_correct_build(edit_build, build):
    edit_build_add_consumable_state = Mock()

    with patch('cli.states.EditBuildAddConsumable', edit_build_add_consumable_state):
        edit_build._add_consumable()

    edit_build_add_consumable_state.assert_called_once_with(build)


def test_edit_build__save_returns_correct_state(edit_build):
    with patch('cli.states.save_builds'):
        returned_state = edit_build._save()

    assert isinstance(returned_state, Start)


def test_edit_build__save_saves_correct_build(edit_build, build):
    State._builds = []
    save_builds = Mock()

    with patch('cli.states.save_builds', save_builds):
        edit_build._save()

    save_builds.assert_called_once_with([build])


def test_edit_build__discard_returns_correct_state(edit_build):
    returned_state = edit_build._discard()

    assert isinstance(returned_state, Start)


def test_edit_build_name_has_correct_attributes(edit_build_name, build):
    assert edit_build_name._header == 'BUILD CREATOR - NAME'
    assert edit_build_name._build == build
    assert edit_build_name._name is None
    assert edit_build_name._transitions == [Transition(1, 'Confirm', edit_build_name._confirm),
                                            Transition(0, 'Discard', edit_build_name._discard)]


def test_edit_build_name__execute_does_correct_execution(edit_build_name):
    name = 'Sniping Nagato'
    edit_build_name._show_transitions = Mock()
    mocked_input = Mock(return_value=name)
    mocked_print = Mock()

    with patch('builtins.print', mocked_print), patch('builtins.input', mocked_input):
        edit_build_name._execute()

    assert edit_build_name._name == name
    edit_build_name._show_transitions.assert_called_once_with()
    mocked_input.assert_called_once_with('Enter build name: ')
    mocked_print.assert_has_calls([call(f'{edit_build_name._header}\n'),
                                   call()])


def test_edit_build_name__confirm_returns_correct_state(edit_build_name):
    returned_state = edit_build_name._confirm()

    assert isinstance(returned_state, EditBuild)


def test_edit_build_name__confirm_uses_correct_build(edit_build_name, build):
    edit_build_state = Mock()

    with patch('cli.states.EditBuild', edit_build_state):
        edit_build_name._confirm()

    edit_build_state.assert_called_once_with(build)


def test_edit_build_name__confirm_changes_build_name(edit_build_name, build):
    name = 'Sniping Nagato'
    edit_build_name._name = name

    edit_build_name._confirm()

    assert build.name == name


def test_edit_build_name__discard_returns_correct_state(edit_build_name):
    returned_state = edit_build_name._discard()

    assert isinstance(returned_state, EditBuild)


def test_edit_build_name__discard_uses_correct_build(edit_build_name, build):
    edit_build_state = Mock()

    with patch('cli.states.EditBuild', edit_build_state):
        edit_build_name._discard()

    edit_build_state.assert_called_once_with(build)


def test_edit_build_ship_has_correct_attributes(edit_build_ship, build):
    assert edit_build_ship._header == 'BUILD CREATOR - SHIP'
    assert edit_build_ship._build == build
    assert edit_build_ship._ship is None
    assert edit_build_ship._transitions == [Transition(1, 'Confirm', edit_build_ship._confirm),
                                            Transition(0, 'Discard', edit_build_ship._discard)]


def test_edit_build_ship__execute_does_correct_execution(edit_build_ship):
    grouped_ships = [Mock(), Mock()]
    edit_build_ship._show_grouped_ships = Mock(return_value=grouped_ships)
    edit_build_ship._select_ship = Mock()
    edit_build_ship._show_transitions = Mock()
    mocked_print = Mock()

    with patch('builtins.print', mocked_print):
        edit_build_ship._execute()

    edit_build_ship._show_grouped_ships.assert_called_once_with()
    edit_build_ship._select_ship.assert_called_once_with(grouped_ships)
    edit_build_ship._show_transitions.assert_called_once_with()
    mocked_print.assert_called_once_with(f'{edit_build_ship._header}\n')


def test_edit_build_ship__show_grouped_ships_groups_builds_in_correct_order(edit_build_ship):
    ship_1 = Mock()
    ship_1.ship_class = 'Destroyer'
    ship_1.nation = 'Japan'
    ship_2 = Mock()
    ship_2.ship_class = 'Battleship'
    ship_2.nation = 'USA'
    ship_2.name = 'North Carolina'
    ship_3 = Mock()
    ship_3.ship_class = 'Battleship'
    ship_3.nation = 'Germany'
    ship_3.name = 'Gneisenau'
    ship_4 = Mock()
    ship_4.ship_class = 'Cruiser'
    ship_4.nation = 'USA'
    ship_5 = Mock()
    ship_5.ship_class = 'Destroyer'
    ship_5.nation = 'Japan'
    ships = [ship_1,
             ship_2,
             ship_3,
             ship_4,
             ship_5]
    mocked_print = Mock()

    with patch('cli.states.ships', ships), patch('builtins.print', mocked_print):
        grouped_ships = edit_build_ship._show_grouped_ships()

    assert grouped_ships == [ship_3,
                             ship_2,
                             ship_4,
                             ship_1,
                             ship_5]
    mocked_print.assert_has_calls([call('Battleships:'),
                                   call(f'  Germany:'),
                                   call(f'    [1] {ship_3.name}'),
                                   call('  USA:'),
                                   call(f'    [2] {ship_2.name}'),
                                   call('Cruisers:'),
                                   call('  USA:'),
                                   call(f'    [3] {ship_4.name}'),
                                   call('Destroyers:'),
                                   call('  Japan:'),
                                   call(f'    [4] {ship_1.name}'),
                                   call(f'    [5] {ship_5.name}')])


def test_edit_build_ship__select_ship_selects_correct_ship(edit_build_ship, build):
    ship_1 = Mock()
    ship_2 = Mock()
    grouped_ships = [ship_1,
                     ship_2]
    build.ship = None
    mocked_input = Mock(return_value='2')
    mocked_print = Mock()

    with patch('builtins.print', mocked_print), patch('builtins.input', mocked_input):
        edit_build_ship._select_ship(grouped_ships=grouped_ships)

    assert edit_build_ship._ship == ship_2
    mocked_input.assert_called_once_with('\nChoose ship: ')
    mocked_print.assert_called_once_with()


def test_edit_build_ship__select_ship_prints_warning_when_overriding_ship(edit_build_ship):
    mocked_input = Mock(return_value='1')
    mocked_print = Mock()

    with patch('builtins.print', mocked_print), patch('builtins.input', mocked_input):
        edit_build_ship._select_ship(grouped_ships=[Mock()])

    mocked_print.assert_has_calls([call('\nWARNING: changing ship will reset build skills, upgrades and consumables'),
                                   call()])


def test_edit_build_ship__confirm_returns_correct_state(edit_build_ship):
    returned_state = edit_build_ship._confirm()

    assert isinstance(returned_state, EditBuild)


def test_edit_build_ship__confirm_uses_correct_build(edit_build_ship, build):
    edit_build_state = Mock()

    with patch('cli.states.EditBuild', edit_build_state):
        edit_build_ship._confirm()

    edit_build_state.assert_called_once_with(build)


def test_edit_build_ship__confirm_changes_build_ship(edit_build_ship, build):
    ship = Mock()
    edit_build_ship._ship = ship

    edit_build_ship._confirm()

    assert build.ship == ship


def test_edit_build_ship__discard_returns_correct_state(edit_build_ship):
    returned_state = edit_build_ship._discard()

    assert isinstance(returned_state, EditBuild)


def test_edit_build_ship__discard_uses_correct_build(edit_build_ship, build):
    edit_build_state = Mock()

    with patch('cli.states.EditBuild', edit_build_state):
        edit_build_ship._discard()

    edit_build_state.assert_called_once_with(build)


def test_edit_build_add_skill_has_correct_attributes(edit_build_add_skill, build):
    assert edit_build_add_skill._header == 'BUILD CREATOR - ADD SKILL'
    assert edit_build_add_skill._build == build
    assert edit_build_add_skill._skill is None
    assert edit_build_add_skill._transitions == [Transition(1, 'Confirm', edit_build_add_skill._confirm),
                                                 Transition(0, 'Discard', edit_build_add_skill._discard)]


def test_edit_build_add_skill__execute_does_correct_execution(edit_build_add_skill):
    edit_build_add_skill._show_grouped_skills = Mock()
    edit_build_add_skill._select_skill = Mock()
    edit_build_add_skill._show_transitions = Mock()
    mocked_print = Mock()

    with patch('builtins.print', mocked_print):
        edit_build_add_skill._execute()

    edit_build_add_skill._show_grouped_skills.assert_called_once_with()
    edit_build_add_skill._select_skill.assert_called_once_with()
    edit_build_add_skill._show_transitions.assert_called_once_with()
    mocked_print.assert_called_once_with(f'{edit_build_add_skill._header}\n')


def test_edit_build_add_skill__show_grouped_skills_groups_valid_skills_in_correct_order(edit_build_add_skill, build):
    skill_1 = Mock()
    skill_1.cost = 3
    skill_1.name = 'Super-Heavy AP Shells'
    skill_2 = Mock()
    skill_2.cost = 1
    skill_2.name = 'Gun Feeder'
    skill_3 = Mock()
    skill_3.cost = 1
    skill_3.name = 'Demolition Expert'
    skill_4 = Mock()
    skill_4.cost = 2
    skill_4.name = 'Vigilance'
    skill_5 = Mock()
    skill_5.cost = 4
    skill_5.name = 'Manual Secondary Battery Aiming'
    skill_6 = Mock()
    skill_6.cost = 1
    skill_6.name = 'Incoming Fire Alert'
    build.ship.skills = [skill_1,
                         skill_2,
                         skill_3,
                         skill_4,
                         skill_5,
                         skill_6]
    build.total_skills_cost = 18
    build.has_skill = Mock(side_effect=[False,
                                        False,
                                        True,
                                        False,
                                        False,
                                        False])
    mocked_print = Mock()

    with patch('builtins.print', mocked_print):
        edit_build_add_skill._show_grouped_skills()

    mocked_print.assert_has_calls([call(f'Total skill cost: {build.total_skills_cost}\n'),
                                   call('1 point skills:'),
                                   call(f'  [2] {skill_2.name}'),
                                   call(f'  [3] {skill_3.name}'),
                                   call('2 point skills:'),
                                   call(f'  [4] {skill_4.name}'),
                                   call('3 point skills:'),
                                   call(f'  [1] {skill_1.name}')])


def test_edit_build_add_skill__select_skill_selects_correct_skill(edit_build_add_skill, build):
    skill_1 = Mock()
    skill_2 = Mock()
    build.ship.skills = {0: skill_1,
                         1: skill_2}
    mocked_input = Mock(return_value='2')
    mocked_print = Mock()

    with patch('builtins.print', mocked_print), patch('builtins.input', mocked_input):
        edit_build_add_skill._select_skill()

    assert edit_build_add_skill._skill == skill_2
    mocked_input.assert_called_once_with('\nChoose skill: ')
    mocked_print.assert_called_once_with()


def test_edit_build_add_skill__confirm_returns_correct_state(edit_build_add_skill):
    returned_state = edit_build_add_skill._confirm()

    assert isinstance(returned_state, EditBuild)


def test_edit_build_add_skill__confirm_uses_correct_build(edit_build_add_skill, build):
    edit_build_state = Mock()

    with patch('cli.states.EditBuild', edit_build_state):
        edit_build_add_skill._confirm()

    edit_build_state.assert_called_once_with(build)


def test_edit_build_add_skill__confirm_adds_skill_to_build(edit_build_add_skill, build):
    skill = Mock()
    edit_build_add_skill._skill = skill

    edit_build_add_skill._confirm()

    build.add_skill.assert_called_once_with(skill)


def test_edit_build_add_skill__discard_returns_correct_state(edit_build_add_skill):
    returned_state = edit_build_add_skill._discard()

    assert isinstance(returned_state, EditBuild)


def test_edit_build_add_skill__discard_uses_correct_build(edit_build_add_skill, build):
    edit_build_state = Mock()

    with patch('cli.states.EditBuild', edit_build_state):
        edit_build_add_skill._discard()

    edit_build_state.assert_called_once_with(build)


def test_edit_build_add_upgrade_has_correct_attributes(edit_build_add_upgrade, build):
    assert edit_build_add_upgrade._header == 'BUILD CREATOR - ADD UPGRADE'
    assert edit_build_add_upgrade._build == build
    assert edit_build_add_upgrade._upgrade is None
    assert edit_build_add_upgrade._upgrades == []
    assert edit_build_add_upgrade._transitions == [Transition(1, 'Confirm', edit_build_add_upgrade._confirm),
                                                   Transition(0, 'Discard', edit_build_add_upgrade._discard)]


def test_edit_build_add_upgrade__execute_does_correct_execution(edit_build_add_upgrade):
    edit_build_add_upgrade._show_grouped_upgrades = Mock()
    edit_build_add_upgrade._select_upgrade = Mock()
    edit_build_add_upgrade._show_transitions = Mock()
    mocked_print = Mock()

    with patch('builtins.print', mocked_print):
        edit_build_add_upgrade._execute()

    edit_build_add_upgrade._show_grouped_upgrades.assert_called_once_with()
    edit_build_add_upgrade._select_upgrade.assert_called_once_with()
    edit_build_add_upgrade._show_transitions.assert_called_once_with()
    mocked_print.assert_called_once_with(f'{edit_build_add_upgrade._header}\n')


def test_edit_build_add_upgrade__show_grouped_skills_groups_valid_upgrades_in_correct_order(edit_build_add_upgrade, build):
    upgrade_1 = 'Main Battery Modification 2'
    upgrade_2 = 'Main Armaments Modification 1'
    upgrade_3 = 'Auxiliary Armaments Modification 1'
    upgrade_4 = 'Engine Room Protection'
    upgrade_5 = 'Hydroacoustic Search Modification 1'

    build.ship.upgrades = {'slot_3': [upgrade_1],
                           'slot_1': [upgrade_2, upgrade_3],
                           'slot_2': [upgrade_4, upgrade_5]}
    build.has_upgrade = Mock(side_effect=[False,
                                          False,
                                          False,
                                          True,
                                          False])
    mocked_print = Mock()

    with patch('builtins.print', mocked_print):
        edit_build_add_upgrade._show_grouped_upgrades()

    assert edit_build_add_upgrade._upgrades == [upgrade_2,
                                                upgrade_3,
                                                upgrade_4,
                                                upgrade_1]
    mocked_print.assert_has_calls([call('Slot 1 upgrades:'),
                                   call(f'  [1] {upgrade_2}'),
                                   call(f'  [2] {upgrade_3}'),
                                   call('Slot 2 upgrades:'),
                                   call(f'  [3] {upgrade_4}'),
                                   call('Slot 3 upgrades:'),
                                   call(f'  [4] {upgrade_1}')])


def test_edit_build_add_upgrade__select_upgrade_selects_correct_upgrade(edit_build_add_upgrade, build):
    upgrade_1 = Mock()
    upgrade_2 = Mock()
    edit_build_add_upgrade._upgrades = {0: upgrade_1,
                                        1: upgrade_2}
    mocked_input = Mock(return_value='2')
    mocked_print = Mock()

    with patch('builtins.print', mocked_print), patch('builtins.input', mocked_input):
        edit_build_add_upgrade._select_upgrade()

    assert edit_build_add_upgrade._upgrade == upgrade_2
    mocked_input.assert_called_once_with('\nChoose upgrade: ')
    mocked_print.assert_called_once_with()


def test_edit_build_add_upgrade__confirm_returns_correct_state(edit_build_add_upgrade):
    returned_state = edit_build_add_upgrade._confirm()

    assert isinstance(returned_state, EditBuild)


def test_edit_build_add_upgrade__confirm_uses_correct_build(edit_build_add_upgrade, build):
    edit_build_state = Mock()

    with patch('cli.states.EditBuild', edit_build_state):
        edit_build_add_upgrade._confirm()

    edit_build_state.assert_called_once_with(build)


def test_edit_build_add_upgrade__confirm_adds_upgrade_to_build(edit_build_add_upgrade, build):
    upgrade = Mock()
    edit_build_add_upgrade._upgrade = upgrade

    edit_build_add_upgrade._confirm()

    build.add_upgrade.assert_called_once_with(upgrade)


def test_edit_build_add_upgrade__discard_returns_correct_state(edit_build_add_upgrade):
    returned_state = edit_build_add_upgrade._discard()

    assert isinstance(returned_state, EditBuild)


def test_edit_build_add_upgrade__discard_uses_correct_build(edit_build_add_upgrade, build):
    edit_build_state = Mock()

    with patch('cli.states.EditBuild', edit_build_state):
        edit_build_add_upgrade._discard()

    edit_build_state.assert_called_once_with(build)


def test_edit_build_add_consumable_has_correct_attributes(edit_build_add_consumable, build):
    assert edit_build_add_consumable._header == 'BUILD CREATOR - ADD CONSUMABLE'
    assert edit_build_add_consumable._build == build
    assert edit_build_add_consumable._consumable is None
    assert edit_build_add_consumable._consumables == []
    assert edit_build_add_consumable._transitions == [Transition(1, 'Confirm', edit_build_add_consumable._confirm),
                                                      Transition(0, 'Discard', edit_build_add_consumable._discard)]


def test_edit_build_add_consumable__execute_does_correct_execution(edit_build_add_consumable):
    edit_build_add_consumable._show_grouped_consumables = Mock()
    edit_build_add_consumable._select_consumable = Mock()
    edit_build_add_consumable._show_transitions = Mock()
    mocked_print = Mock()

    with patch('builtins.print', mocked_print):
        edit_build_add_consumable._execute()

    edit_build_add_consumable._show_grouped_consumables.assert_called_once_with()
    edit_build_add_consumable._select_consumable.assert_called_once_with()
    edit_build_add_consumable._show_transitions.assert_called_once_with()
    mocked_print.assert_called_once_with(f'{edit_build_add_consumable._header}\n')


def test_edit_build_add_consumable__show_grouped_consumables_groups_valid_consumables_in_correct_order(edit_build_add_consumable, build):
    consumable_1 = 'Catapult Fighter'
    consumable_2 = 'Spotting Aircraft'
    consumable_3 = 'Defensive AA Fire'
    consumable_4 = 'Hydroacoustic Search'
    consumable_5 = 'Damage Control Party'

    build.ship.consumables = {'slot_3': [consumable_1],
                              'slot_1': [consumable_2, consumable_3],
                              'slot_2': [consumable_4, consumable_5]}
    build.has_consumable = Mock(side_effect=[False,
                                             False,
                                             False,
                                             True,
                                             False])
    mocked_print = Mock()

    with patch('builtins.print', mocked_print):
        edit_build_add_consumable._show_grouped_consumables()

    assert edit_build_add_consumable._consumables == [consumable_2,
                                                      consumable_3,
                                                      consumable_4,
                                                      consumable_1]
    mocked_print.assert_has_calls([call('Slot 1 consumables:'),
                                   call(f'  [1] {consumable_2}'),
                                   call(f'  [2] {consumable_3}'),
                                   call('Slot 2 consumables:'),
                                   call(f'  [3] {consumable_4}'),
                                   call('Slot 3 consumables:'),
                                   call(f'  [4] {consumable_1}')])


def test_edit_build_add_consumable__select_consumable_selects_correct_consumable(edit_build_add_consumable, build):
    consumable_1 = Mock()
    consumable_2 = Mock()
    edit_build_add_consumable._consumables = {0: consumable_1,
                                              1: consumable_2}
    mocked_input = Mock(return_value='2')
    mocked_print = Mock()

    with patch('builtins.print', mocked_print), patch('builtins.input', mocked_input):
        edit_build_add_consumable._select_consumable()

    assert edit_build_add_consumable._consumable == consumable_2
    mocked_input.assert_called_once_with('\nChoose consumable: ')
    mocked_print.assert_called_once_with()


def test_edit_build_add_consumable__confirm_returns_correct_state(edit_build_add_consumable):
    returned_state = edit_build_add_consumable._confirm()

    assert isinstance(returned_state, EditBuild)


def test_edit_build_add_consumable__confirm_uses_correct_build(edit_build_add_consumable, build):
    edit_build_state = Mock()

    with patch('cli.states.EditBuild', edit_build_state):
        edit_build_add_consumable._confirm()

    edit_build_state.assert_called_once_with(build)


def test_edit_build_add_consumable__confirm_adds_consumable_to_build(edit_build_add_consumable, build):
    consumable = Mock()
    edit_build_add_consumable._consumable = consumable

    edit_build_add_consumable._confirm()

    build.add_consumable.assert_called_once_with(consumable)


def test_edit_build_add_consumable__discard_returns_correct_state(edit_build_add_consumable):
    returned_state = edit_build_add_consumable._discard()

    assert isinstance(returned_state, EditBuild)


def test_edit_build_add_consumable__discard_uses_correct_build(edit_build_add_consumable, build):
    edit_build_state = Mock()

    with patch('cli.states.EditBuild', edit_build_state):
        edit_build_add_consumable._discard()

    edit_build_state.assert_called_once_with(build)
