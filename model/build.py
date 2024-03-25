from typing import List, Dict, Collection, Union

from model.ships.ship import Ship
from model.skills.skill import Skill
from model.exceptions import (TotalSkillsCostExceeded,
                              SkillAlreadyAdded,
                              SkillNotAvailable,
                              UpgradeAlreadyAdded,
                              UpgradeNotAvailable,
                              ConsumableAlreadyAdded,
                              ConsumableNotAvailable)


class Build:
    def __init__(self, name: str = '', ship: Ship = None):
        self._name = name
        self._ship = ship
        self._skills = []
        self._upgrades = {}
        self._consumables = {}

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def ship(self) -> Ship:
        return self._ship

    @ship.setter
    def ship(self, ship: Ship):
        self._ship = ship
        self._skills = []
        self._upgrades = {}
        self._consumables = {}

    @property
    def skills(self) -> List[Skill]:
        return self._skills

    @property
    def upgrades(self) -> Dict[str, List[str]]:
        return self._upgrades

    @property
    def consumables(self) -> Dict[str, List[str]]:
        return self._consumables

    def add_skill(self, skill: Skill):
        self._check_if_skill_is_not_added_yet(skill)
        self._check_if_skill_is_available(skill)
        self._check_if_total_skills_cost_is_not_exceeded(skill)
        self._skills.append(skill)

    def add_upgrade(self, upgrade: str):
        self._check_if_upgrade_not_added_yet(upgrade)
        slot = self._check_if_upgrade_is_available(upgrade)
        self._upgrades[slot] = upgrade

    def add_consumable(self, consumable: str):
        self._check_if_consumable_not_added_yet(consumable)
        slot = self._check_if_consumable_is_available(consumable)
        self._consumables[slot] = consumable

    def serialize(self) -> Dict[str, Union[str, Collection]]:
        return {'name': self._name,
                'ship': self._ship.name,
                'skills': [skill.name for skill in self._skills],
                'upgrades': self._upgrades,
                'consumables': self._consumables}

    def _check_if_skill_is_not_added_yet(self, skill: Skill):
        if skill in self._skills:
            raise SkillAlreadyAdded(f'Skill {skill.name} is already added')

    def _check_if_skill_is_available(self, skill: Skill):
        if not self._ship:
            raise SkillNotAvailable(f'Skill {skill.name} cannot be added to build without a ship')

        if skill.name not in [available_skill.name for available_skill in self._ship.skills]:
            raise SkillNotAvailable(f'Skill {skill.name} is not available for ship {self._ship.name}')

    def _check_if_total_skills_cost_is_not_exceeded(self, skill: Skill):
        if sum([skill.cost for skill in self._skills]) + skill.cost > 21:
            raise TotalSkillsCostExceeded('Total cost of all skills has been exceeded')

    def _check_if_upgrade_not_added_yet(self, upgrade: str):
        if upgrade in self._upgrades.values():
            raise UpgradeAlreadyAdded(f'Upgrade {upgrade} is already added')

    def _check_if_upgrade_is_available(self, upgrade: str) -> str:
        if not self._ship:
            raise UpgradeNotAvailable(f'Upgrade {upgrade} cannot be added to build without a ship')

        for ship_upgrade_slot, ship_upgrades in self._ship.upgrades.items():
            for ship_upgrade in ship_upgrades:
                if ship_upgrade == upgrade:
                    return ship_upgrade_slot
        else:
            raise UpgradeNotAvailable(f'Upgrade {upgrade} is not available for ship {self._ship.name}')

    def _check_if_consumable_not_added_yet(self, consumable: str):
        if consumable in self._consumables.values():
            raise ConsumableAlreadyAdded(f'Consumable {consumable} is already added')

    def _check_if_consumable_is_available(self, consumable: str) -> str:
        if not self._ship:
            raise ConsumableNotAvailable(f'Consumable {consumable} cannot be added to build without a ship')

        for ship_consumable_slot, ship_consumables in self._ship.consumables.items():
            for ship_consumable in ship_consumables:
                if ship_consumable == consumable:
                    return ship_consumable_slot
        else:
            raise ConsumableNotAvailable(f'Consumable {consumable} is not available for ship {self._ship.name}')
