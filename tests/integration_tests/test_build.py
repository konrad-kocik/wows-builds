from pytest import raises, fixture

from model.build import Build
from model.ships.nagato import Nagato
from model.skills.submarine_skills import enhanced_sonar
from model.skills.battleship_skills import (gun_feeder,
                                            emergency_repair_specialist,
                                            grease_the_gears,
                                            adrenaline_rush,
                                            basics_of_survivability,
                                            emergency_repair_expert,
                                            concealment_expert,
                                            fire_prevention_expert)
from model.exceptions import (SkillNotAvailable,
                              SkillAlreadyAdded,
                              TotalSkillsCostExceeded,
                              UpgradeNotAvailable,
                              UpgradeAlreadyAdded,
                              ConsumableNotAvailable,
                              ConsumableAlreadyAdded)


@fixture
def build():
    return Build(name='Sniping Nagato', ship=Nagato())


def test_integrate_build_with_ship(build):
    assert build.ship.name == 'Nagato'
    assert build.ship.nation == 'Japan'
    assert build.ship.ship_class == 'Battleship'
    assert build.ship.tier == 7


def test_integrate_build_with_skills(build):
    assert build.skills == []

    with raises(SkillNotAvailable):
        build.add_skill(skill=enhanced_sonar)

    build.add_skill(skill=emergency_repair_specialist)

    with raises(SkillAlreadyAdded):
        build.add_skill(skill=emergency_repair_specialist)

    build.add_skill(skill=grease_the_gears)
    build.add_skill(skill=adrenaline_rush)
    build.add_skill(skill=basics_of_survivability)
    build.add_skill(skill=emergency_repair_expert)
    build.add_skill(skill=concealment_expert)
    build.add_skill(skill=fire_prevention_expert)

    with raises(TotalSkillsCostExceeded):
        build.add_skill(skill=gun_feeder)

    assert build.skills == [emergency_repair_specialist,
                            grease_the_gears,
                            adrenaline_rush,
                            basics_of_survivability,
                            emergency_repair_expert,
                            concealment_expert,
                            fire_prevention_expert]


def test_integrate_build_with_upgrades(build):
    assert build.upgrades == {}

    with raises(UpgradeNotAvailable):
        build.add_upgrade(upgrade='Defensive AA Fire Modification 1')

    build.add_upgrade(upgrade='Spotting Aircraft Modification 1')

    with raises(UpgradeAlreadyAdded):
        build.add_upgrade(upgrade='Spotting Aircraft Modification 1')

    build.add_upgrade(upgrade='Main Armaments Modification 1')
    build.add_upgrade(upgrade='Damage Control System Modification 1')
    build.add_upgrade(upgrade='Aiming Systems Modification 1')
    build.add_upgrade(upgrade='Damage Control System Modification 2')

    assert build.upgrades == {'slot_1': 'Main Armaments Modification 1',
                              'slot_2': 'Damage Control System Modification 1',
                              'slot_3': 'Aiming Systems Modification 1',
                              'slot_4': 'Damage Control System Modification 2'}


def test_integrate_build_with_consumables(build):
    assert build.consumables == {}

    with raises(ConsumableNotAvailable):
        build.add_consumable(consumable='Smoke Generator')

    build.add_consumable(consumable='Catapult Fighter')

    with raises(ConsumableAlreadyAdded):
        build.add_consumable(consumable='Catapult Fighter')

    build.add_consumable(consumable='Damage Control Party')
    build.add_consumable(consumable='Repair Party')
    build.add_consumable(consumable='Spotting Aircraft')

    assert build.consumables == {'slot_1': 'Damage Control Party',
                                 'slot_2': 'Repair Party',
                                 'slot_3': 'Spotting Aircraft'}
