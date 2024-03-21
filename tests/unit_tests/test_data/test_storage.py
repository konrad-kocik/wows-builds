from unittest.mock import Mock, patch, call
from pytest import fixture, mark, raises
from pathlib import Path
from json import load, dump

from data.storage import save_builds, load_builds, can_builds_be_loaded, _get_default_dir_path

custom_dir_path = Path(__file__).parent.resolve()
custom_file_path = custom_dir_path.joinpath('builds.json')
custom_new_dir_path = Path(__file__).parent.resolve().joinpath('storage')
custom_file_path_in_new_dir = custom_new_dir_path.joinpath('builds.json')
default_dir_path = Path.home().joinpath('.wows_builds')
default_file_path = default_dir_path.joinpath('builds.json')


@fixture
def builds():
    build_1 = Mock()
    serialized_build_1 = {'name': 'AA Helena',
                          'ship': 'Helena',
                          'skills': ['Grease the Gears',
                                     'Fly in the Sky'],
                          'upgrades': {'slot_1': 'Main Armaments Modification 1',
                                       'slot_2': 'Defensive AA Fire Modification 1'},
                          'consumables': {'slot_1': 'Damage Control Party',
                                          'slot_2': 'Defensive AA Fire'}}
    build_1.serialize.return_value = serialized_build_1
    build_2 = Mock()
    serialized_build_2 = {'name': 'Sniping Nagato',
                          'ship': 'Nagato',
                          'skills': ['Emergency Repair Specialist',
                                     'Vigilance'],
                          'upgrades': {'slot_2': 'Damage Control System Modification 1',
                                       'slot_3': 'Aiming Systems Modification 1'},
                          'consumables': {'slot_2': 'Repair Party',
                                          'slot_3': 'Spotting Aircraft'}}
    build_2.serialize.return_value = serialized_build_2
    build_3 = Mock()
    serialized_build_3 = {'name': 'Flanking Minsk',
                          'ship': 'Minsk',
                          'skills': ['Incoming Fire Alert',
                                     'Last Stand'],
                          'upgrades': {'slot_1': 'Magazine Modification 1',
                                       'slot_3': 'Smoke Generator Modification 1'},
                          'consumables': {'slot_1': 'Damage Control Party',
                                          'slot_3': 'Engine Boost'}}
    build_3.serialize.return_value = serialized_build_3

    raw_builds = [build_1, build_2, build_3]
    serialized_builds = [serialized_build_1, serialized_build_2, serialized_build_3]

    return raw_builds, serialized_builds


@fixture
def before_save_builds_in_custom_directory(builds):
    _, serialized_builds = builds

    with open(custom_file_path, 'w') as file:
        dump(serialized_builds, file)


@fixture
def before_save_builds_in_default_directory(builds):
    _, serialized_builds = builds

    default_dir_path.mkdir(parents=True)

    with open(default_file_path, 'w') as file:
        dump(serialized_builds, file)


@fixture
def after_remove_custom_file(request):
    def teardown():
        custom_file_path.unlink(missing_ok=True)

    request.addfinalizer(teardown)


@fixture
def after_remove_custom_new_dir(request):
    def teardown():
        if custom_file_path_in_new_dir.exists():
            custom_file_path_in_new_dir.unlink()
            custom_new_dir_path.rmdir()

    request.addfinalizer(teardown)


@fixture
def after_remove_default_dir(request):
    def teardown():
        if default_file_path.exists():
            default_file_path.unlink()
            default_dir_path.rmdir()

    request.addfinalizer(teardown)


def test_save_builds_stores_builds_in_custom_directory(builds, after_remove_custom_file):
    raw_builds, serialized_builds = builds

    save_builds(builds=raw_builds, target_dir_path=custom_dir_path)

    assert custom_file_path.exists()

    with open(custom_file_path, 'r') as file:
        assert load(file) == serialized_builds


def test_save_builds_stores_builds_in_default_directory(builds, after_remove_default_dir):
    raw_builds, serialized_builds = builds

    save_builds(builds=raw_builds)

    assert default_file_path.exists()

    with open(default_file_path, 'r') as file:
        assert load(file) == serialized_builds


def test_save_builds_when_directory_does_not_exist_then_it_is_created(after_remove_custom_new_dir):
    save_builds(builds=[], target_dir_path=custom_new_dir_path)

    assert custom_file_path_in_new_dir.exists()


def test_load_builds_restores_builds_from_custom_directory(before_save_builds_in_custom_directory,
                                                           builds,
                                                           after_remove_custom_file):
    raw_builds, serialized_builds = builds
    ship_1, ship_2, ship_3 = Mock(), Mock(), Mock()
    create_ship = Mock(side_effect=[ship_1, ship_2, ship_3])
    build_1, build_2, build_3 = Mock(), Mock(), Mock()
    build = Mock(side_effect=[build_1, build_2, build_3])
    _add_skills_to_build = Mock()
    _add_upgrades_to_build = Mock()
    _add_consumables_to_build = Mock()

    with patch('data.storage.create_ship', create_ship), \
         patch('data.storage.Build', build), \
         patch('data.storage._add_skills_to_build', _add_skills_to_build), \
         patch('data.storage._add_upgrades_to_build', _add_upgrades_to_build), \
         patch('data.storage._add_consumables_to_build', _add_consumables_to_build):
        loaded_builds = load_builds(source_dir_path=custom_dir_path)

    assert loaded_builds == [build_1, build_2, build_3]
    create_ship.assert_has_calls([call(serialized_builds[0]['ship']),
                                  call(serialized_builds[1]['ship']),
                                  call(serialized_builds[2]['ship'])])
    build.assert_has_calls([call(name=serialized_builds[0]['name'], ship=ship_1),
                            call(name=serialized_builds[1]['name'], ship=ship_2),
                            call(name=serialized_builds[2]['name'], ship=ship_3)])
    _add_skills_to_build.assert_has_calls([call(serialized_builds[0]['skills'], build_1, ship_1),
                                           call(serialized_builds[1]['skills'], build_2, ship_2),
                                           call(serialized_builds[2]['skills'], build_3, ship_3)])
    _add_upgrades_to_build.assert_has_calls([call(serialized_builds[0]['upgrades'], build_1),
                                            call(serialized_builds[1]['upgrades'], build_2),
                                            call(serialized_builds[2]['upgrades'], build_3)])
    _add_consumables_to_build.assert_has_calls([call(serialized_builds[0]['consumables'], build_1),
                                               call(serialized_builds[1]['consumables'], build_2),
                                               call(serialized_builds[2]['consumables'], build_3)])


def test_load_builds_restores_builds_from_default_directory(before_save_builds_in_default_directory,
                                                            builds,
                                                            after_remove_default_dir):
    raw_builds, serialized_builds = builds
    ship_1, ship_2, ship_3 = Mock(), Mock(), Mock()
    create_ship = Mock(side_effect=[ship_1, ship_2, ship_3])
    build_1, build_2, build_3 = Mock(), Mock(), Mock()
    build = Mock(side_effect=[build_1, build_2, build_3])
    _add_skills_to_build = Mock()
    _add_upgrades_to_build = Mock()
    _add_consumables_to_build = Mock()

    with patch('data.storage.create_ship', create_ship), \
         patch('data.storage.Build', build), \
         patch('data.storage._add_skills_to_build', _add_skills_to_build), \
         patch('data.storage._add_upgrades_to_build', _add_upgrades_to_build), \
         patch('data.storage._add_consumables_to_build', _add_consumables_to_build):
        loaded_builds = load_builds()

    assert loaded_builds == [build_1, build_2, build_3]
    create_ship.assert_has_calls([call(serialized_builds[0]['ship']),
                                  call(serialized_builds[1]['ship']),
                                  call(serialized_builds[2]['ship'])])
    build.assert_has_calls([call(name=serialized_builds[0]['name'], ship=ship_1),
                            call(name=serialized_builds[1]['name'], ship=ship_2),
                            call(name=serialized_builds[2]['name'], ship=ship_3)])
    _add_skills_to_build.assert_has_calls([call(serialized_builds[0]['skills'], build_1, ship_1),
                                           call(serialized_builds[1]['skills'], build_2, ship_2),
                                           call(serialized_builds[2]['skills'], build_3, ship_3)])
    _add_upgrades_to_build.assert_has_calls([call(serialized_builds[0]['upgrades'], build_1),
                                            call(serialized_builds[1]['upgrades'], build_2),
                                            call(serialized_builds[2]['upgrades'], build_3)])
    _add_consumables_to_build.assert_has_calls([call(serialized_builds[0]['consumables'], build_1),
                                               call(serialized_builds[1]['consumables'], build_2),
                                               call(serialized_builds[2]['consumables'], build_3)])


def test_load_builds_when_directory_does_not_exist_then_error_is_raised():
    with raises(FileNotFoundError) as exc:
        load_builds(source_dir_path=Path('/non/existing/directory'))

    assert str(exc.value) == "[Errno 2] No such file or directory: '/non/existing/directory/builds.json'"


def test_can_builds_be_loaded_when_builds_are_saved_in_custom_directory_then_returns_true(before_save_builds_in_custom_directory,
                                                                                          after_remove_custom_file):
    assert can_builds_be_loaded(source_dir_path=custom_dir_path) is True


def test_can_builds_be_loaded_when_builds_are_not_saved_in_custom_directory_then_returns_false():
    assert can_builds_be_loaded(source_dir_path=custom_dir_path) is False


def test_can_builds_be_loaded_when_builds_are_saved_in_default_directory_then_returns_true(before_save_builds_in_default_directory,
                                                                                           after_remove_default_dir):
    assert can_builds_be_loaded() is True


def test_can_builds_be_loaded_when_builds_are_not_saved_in_default_directory_then_returns_false():
    assert can_builds_be_loaded() is False


@mark.parametrize('platform, home, default_dir',
                  [('win32', Path('C:/Users/User'), Path('C:/Users/User/AppData/Local/WoWSBuilds')),
                   ('linux', Path('/home/user'), Path('/home/user/.wows_builds'))])
def test__get_default_dir_path_returns_correct_path_for_all_platforms(platform, home, default_dir):
    path = Mock()
    path.home.return_value = home

    with patch('data.storage.platform', platform), patch('data.storage.Path', path):
        assert _get_default_dir_path() == default_dir
