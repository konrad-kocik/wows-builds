from typing import List, Dict
from pathlib import Path
from json import dump, load
from sys import platform

from model.build import Build
from model.ships.ship import Ship
from model.ships.ship_factory import create_ship

STORAGE_FILE_NAME = 'builds.json'


def save_builds(builds: List[Build], target_dir_path: Path = None):
    target_dir_path = target_dir_path or _get_default_dir_path()

    if not target_dir_path.exists():
        target_dir_path.mkdir(parents=True)

    serialized_builds = [build.serialize() for build in builds]

    with open(target_dir_path.joinpath(STORAGE_FILE_NAME), 'w') as file:
        dump(serialized_builds, file)


def load_builds(source_dir_path: Path = None) -> List[Build]:
    source_dir_path = source_dir_path or _get_default_dir_path()

    with open(source_dir_path.joinpath(STORAGE_FILE_NAME), 'r') as file:
        serialized_builds = load(file)

    return _deserialize_builds(serialized_builds)


def can_builds_be_loaded(source_dir_path: Path = None) -> bool:
    source_dir_path = source_dir_path or _get_default_dir_path()
    return source_dir_path.joinpath(STORAGE_FILE_NAME).exists()


def _get_default_dir_path() -> Path:
    if platform == 'win32':
        return Path.home().joinpath('AppData', 'Local', 'WoWSBuilds')
    else:
        return Path.home().joinpath('.wows_builds')


def _deserialize_builds(serialized_builds: List[Dict]) -> List[Build]:
    builds = []

    for serialized_build in serialized_builds:
        ship = create_ship(serialized_build['ship'])
        build = Build(name=serialized_build['name'], ship=ship)
        _add_skills_to_build(serialized_build['skills'], build, ship)
        _add_upgrades_to_build(serialized_build['upgrades'], build)
        _add_consumables_to_build(serialized_build['consumables'], build)
        builds.append(build)

    return builds


def _add_skills_to_build(serialized_skills: List, build: Build, ship: Ship):
    for serialized_skill in serialized_skills:
        for skill in ship.skills:
            if skill.name == serialized_skill:
                build.add_skill(skill)
                break


def _add_upgrades_to_build(serialized_upgrades: Dict[str, str], build: Build):
    for upgrade_name in serialized_upgrades.values():
        build.add_upgrade(upgrade_name)


def _add_consumables_to_build(serialized_consumables: Dict[str, str], build: Build):
    for consumable_name in serialized_consumables.values():
        build.add_consumable(consumable_name)
