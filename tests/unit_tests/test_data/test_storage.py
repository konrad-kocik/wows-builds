from unittest.mock import Mock, patch
from pytest import fixture, mark
from pathlib import Path
from json import load

from data.storage import save_builds, _get_default_dir_path

custom_dir_path = Path(__file__).parent.resolve()
custom_file_path = custom_dir_path.joinpath('builds.json')
custom_new_dir_path = Path(__file__).parent.resolve().joinpath('storage')
custom_file_path_in_new_dir = custom_new_dir_path.joinpath('builds.json')
default_dir_path = Path.home().joinpath('.wows_builds')
default_file_path = default_dir_path.joinpath('builds.json')


@fixture
def builds():
    build_1 = Mock()
    serialized_build_1 = {'name': 'AA North Carolina',
                          'ship': 'North Carolina',
                          'skills': ['Gun Feeder',
                                     'Grease the Gears'],
                          'upgrades': {'slot_1': 'Main Armaments Modification 1',
                                       'slot_2': 'Damage Control System Modification 1'},
                          'consumables': {'slot_1': 'Damage Control Party',
                                          'slot_2': 'Repair Party'}}
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

    raw_builds = [build_1, build_2]
    serialized_builds = [serialized_build_1, serialized_build_2]

    return raw_builds, serialized_builds


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


@mark.parametrize('platform, home, default_dir',
                  [('win32', Path('C:/Users/User'), Path('C:/Users/User/AppData/Local/WoWSBuilds')),
                   ('linux', Path('/home/user'), Path('/home/user/.wows_builds'))])
def test__get_default_dir_path_returns_correct_path_for_all_platforms(platform, home, default_dir):
    path = Mock()
    path.home.return_value = home

    with patch('data.storage.platform', platform), patch('data.storage.Path', path):
        assert _get_default_dir_path() == default_dir
