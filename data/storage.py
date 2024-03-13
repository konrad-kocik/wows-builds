from typing import List
from pathlib import Path
from json import dump
from sys import platform

from model.build import Build


def save_builds(builds: List[Build], target_dir_path: Path = None):
    target_dir_path = target_dir_path or _get_default_dir_path()
    target_file_path = target_dir_path.joinpath('builds.json')

    if not target_dir_path.exists():
        target_dir_path.mkdir(parents=True)

    serialized_builds = [build.serialize() for build in builds]

    with open(target_file_path, 'w') as file:
        dump(serialized_builds, file)


def _get_default_dir_path() -> Path:
    if platform == 'win32':
        return Path.home().joinpath('AppData', 'Local', 'WoWSBuilds')
    else:
        return Path.home().joinpath('.wows_builds')
