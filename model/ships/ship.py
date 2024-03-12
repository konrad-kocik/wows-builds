from typing import Dict, List

from model.skills.skill import Skill


class Ship:
    def __init__(self):
        self._name = None
        self._nation = None
        self._class = None
        self._tier = None
        self._skills = []
        self._upgrades = {}
        self._consumables = {}

    @property
    def name(self) -> str:
        return self._name

    @property
    def skills(self) -> List[Skill]:
        return self._skills

    @property
    def upgrades(self) -> Dict[str, List[str]]:
        return self._upgrades

    @property
    def consumables(self) -> Dict[str, List[str]]:
        return self._consumables
