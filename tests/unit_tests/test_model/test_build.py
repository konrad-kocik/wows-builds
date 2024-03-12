from unittest.mock import Mock
from pytest import raises, fixture

from model.build import Build
from model.exceptions import (TotalSkillsCostExceeded,
                              SkillAlreadyAdded,
                              SkillNotAvailable,
                              UpgradeAlreadyAdded,
                              UpgradeNotAvailable,
                              ConsumableAlreadyAdded,
                              ConsumableNotAvailable)


@fixture
def skill():
    skill = Mock()
    skill.name = 'Demolition Expert'
    skill.cost = 1
    return skill


@fixture
def ship(skill, upgrade):
    ship = Mock()
    ship.name = 'North Carolina'
    ship.skills = [skill]
    ship.upgrades = {'slot_1': ['Magazine Modification 1',
                                upgrade],
                     'slot_2': ['Damage Control System Modification 1']}
    ship.consumables = {'slot_1': ['Damage Control Party'],
                        'slot_2': ['Repair Party'],
                        'slot_3': ['Spotting Aircraft',
                                   'Catapult Fighter']}
    return ship


@fixture
def upgrade():
    return 'Main Armaments Modification 1'


@fixture
def consumable():
    return 'Spotting Aircraft'


@fixture
def build(ship):
    return Build(name='AA North Carolina', ship=ship)


def test_build_has_correct_attributes(build, ship):
    assert build._name == 'AA North Carolina'
    assert build._ship is ship
    assert build._skills == []
    assert build._upgrades == {}
    assert build._consumables == {}


def test_add_skill_when_skill_already_added_then_error_is_raised(build, skill):
    build._skills = [skill]

    with raises(SkillAlreadyAdded) as exc:
        build.add_skill(skill=skill)

    assert str(exc.value) == f'Skill {skill.name} is already added'


def test_add_skill_when_skill_not_available_for_ship_then_error_is_raised(build, ship, skill):
    available_skill = Mock()
    available_skill.name = 'Gun Feeder'
    ship.skills = [available_skill]

    with raises(SkillNotAvailable) as exc:
        build.add_skill(skill=skill)

    assert str(exc.value) == f'Skill {skill.name} is not available for ship {ship.name}'


def test_add_skill_when_skill_is_not_already_added_then_it_is_added(build, skill):
    build.add_skill(skill=skill)

    assert build._skills == [skill]


def test_add_skill_when_total_cost_is_exceeded_then_error_is_raised(build, ship, skill):
    build._skills = [skill] * 21
    new_skill = Mock()
    new_skill.name = 'Consumables Specialist'
    new_skill.cost = 1
    ship.skills.append(new_skill)

    with raises(TotalSkillsCostExceeded) as exc:
        build.add_skill(skill=new_skill)

    assert str(exc.value) == 'Total cost of all skills has been exceeded'


def test_add_skill_when_total_cost_is_not_exceeded_then_skill_is_added(build, ship, skill):
    build._skills = [skill] * 19
    new_skill = Mock()
    new_skill.name = 'Vigilance'
    new_skill.cost = 2
    ship.skills.append(new_skill)

    build.add_skill(skill=new_skill)

    assert new_skill in build._skills


def test_add_upgrade_when_upgrade_already_added_then_error_is_raised(build, upgrade):
    build._upgrades = {'slot_1': upgrade}

    with raises(UpgradeAlreadyAdded) as exc:
        build.add_upgrade(upgrade=upgrade)

    assert str(exc.value) == f'Upgrade {upgrade} is already added'


def test_add_upgrade_when_upgrade_not_available_for_ship_then_error_is_raised(build, ship, upgrade):
    ship.upgrades = {'slot_1': ['Spotting Aircraft Modification 1',
                                'Damage Control Party Modification 1'],
                     'slot_2': ['Engine Room Protection']}

    with raises(UpgradeNotAvailable) as exc:
        build.add_upgrade(upgrade=upgrade)

    assert str(exc.value) == f'Upgrade {upgrade} is not available for ship {ship.name}'


def test_add_upgrade_when_slot_already_occupied_then_upgrade_is_replaced_in_this_slot(build, upgrade):
    build._upgrades = {'slot_1': 'Spotting Aircraft Modification 1'}

    build.add_upgrade(upgrade=upgrade)

    assert build._upgrades == {'slot_1': upgrade}


def test_add_upgrade_when_slot_is_empty_then_upgrade_is_added_to_correct_slot(build, upgrade):
    build.add_upgrade(upgrade=upgrade)

    assert build._upgrades == {'slot_1': upgrade}


def test_add_consumable_when_consumable_already_added_then_error_is_raised(build, consumable):
    build._consumables = {'slot_3': consumable}

    with raises(ConsumableAlreadyAdded) as exc:
        build.add_consumable(consumable=consumable)

    assert str(exc.value) == f'Consumable {consumable} is already added'


def test_add_consumable_when_consumable_not_available_for_ship_then_error_is_raised(build, ship, consumable):
    ship.consumables = {'slot_1': ['Damage Control Party'],
                        'slot_2': ['Repair Party'],
                        'slot_3': ['Catapult Fighter',
                                   'Hydroacoustic Search']}

    with raises(ConsumableNotAvailable) as exc:
        build.add_consumable(consumable=consumable)

    assert str(exc.value) == f'Consumable {consumable} is not available for ship {ship.name}'


def test_add_consumable_when_slot_already_occupied_then_consumable_is_replaced_in_this_slot(build, consumable):
    build._consumables = {'slot_3': 'Catapult Fighter'}

    build.add_consumable(consumable=consumable)

    assert build._consumables == {'slot_3': consumable}


def test_add_consumable_when_slot_is_empty_then_consumable_is_added_to_correct_slot(build, consumable):
    build.add_consumable(consumable=consumable)

    assert build._consumables == {'slot_3': consumable}
