from pytest import fixture
from unittest.mock import Mock, patch, call

from cli.states import Transition, State, Start, Exit, ListBuilds, ShowBuild, EditBuild


@fixture
def builds():
    return [Mock(), Mock()]


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


def test_list_builds__show_grouped_builds_prints_builds_in_correct_order(list_builds):
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


def test_list_builds__show_build_uses_correct_build(list_builds):
    build = Mock()
    show_build_state = Mock()

    with patch('cli.states.ShowBuild', show_build_state):
        list_builds._show_build(build=build)

    show_build_state.assert_called_once_with(build)
