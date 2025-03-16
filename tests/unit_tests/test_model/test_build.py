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
def new_skill():
    new_skill = Mock()
    new_skill.name = 'Consumables Specialist'
    new_skill.cost = 2
    return new_skill


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


def test_empty_build_has_correct_attributes():
    build = Build()

    assert build._name == ''
    assert build._ship is None
    assert build._skills == []
    assert build._upgrades == {}
    assert build._consumables == {}


def test_name_returns_correct_value(build):
    assert build.name == build._name


def test_name_can_be_set(build):
    new_name = 'Mighty Yamato'
    build.name = new_name

    assert build._name == new_name


def test_ship_returns_correct_value(build, ship):
    assert build.ship == ship


def test_ship_can_be_set(build):
    new_ship = Mock()
    new_ship.name = 'Yamato'
    build.ship = new_ship

    assert build._ship is new_ship
    assert build._ship.name == new_ship.name


def test_setting_new_ship_resets_skills_upgrades_and_consumables(build, ship, skill, upgrade, consumable):
    build._skills = [skill]
    build._upgrades = {'slot_1': upgrade}
    build._consumables = {'slot_2': consumable}

    build.ship = Mock()

    assert build._skills == []
    assert build._upgrades == {}
    assert build._consumables == {}


def test_skills_returns_correct_value(build):
    build._skills = [Mock()]

    assert build.skills == build._skills


def test_sorted_skills_returns_correct_value(build, skill, new_skill):
    build._skills = [new_skill, skill]

    assert build.sorted_skills == [skill, new_skill]


def test_total_skills_cost_returns_correct_value(build, skill, new_skill):
    build._skills = [skill, new_skill]

    assert build.total_skills_cost == 3


def test_upgrades_returns_correct_value(build):
    build._upgrades = {'slot_1': 'Main Armaments Modification 1',
                       'slot_2': 'Auxiliary Armaments Modification 1'}

    assert build.upgrades == build._upgrades


def test_sorted_upgrades_returns_correct_value(build):
    build._upgrades = {'slot_2': 'Damage Control System Modification 1',
                       'slot_1': 'Main Armaments Modification 1'}

    assert build.sorted_upgrades == {'slot_1': 'Main Armaments Modification 1',
                                     'slot_2': 'Damage Control System Modification 1'}


def test_consumables_returns_correct_value(build):
    build._consumables = {'slot_3': ['Spotting Aircraft',
                                     'Catapult Fighter']}

    assert build.consumables == build._consumables


def test_sorted_consumables_returns_correct_value(build):
    build._consumables = {'slot_2': 'Repair Party',
                          'slot_1': 'Damage Control Party'}

    assert build.sorted_consumables == {'slot_1': 'Damage Control Party',
                                        'slot_2': 'Repair Party'}


def test_add_skill_when_skill_already_added_then_error_is_raised(build, skill):
    build._skills = [skill]

    with raises(SkillAlreadyAdded) as exc:
        build.add_skill(skill=skill)

    assert str(exc.value) == f'Skill {skill.name} is already added'


def test_add_skill_when_ship_is_not_set_then_error_is_raised(build, skill):
    build._ship = None

    with raises(SkillNotAvailable) as exc:
        build.add_skill(skill=skill)

    assert str(exc.value) == f'Skill {skill.name} cannot be added to build without a ship'


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


def test_add_skill_when_total_cost_is_exceeded_then_error_is_raised(build, ship, skill, new_skill):
    build._skills = [skill] * 20
    ship.skills.append(new_skill)

    with raises(TotalSkillsCostExceeded) as exc:
        build.add_skill(skill=new_skill)

    assert str(exc.value) == 'Total cost of all skills has been exceeded'


def test_add_skill_when_total_cost_is_not_exceeded_then_skill_is_added(build, ship, skill, new_skill):
    build._skills = [skill] * 19
    ship.skills.append(new_skill)

    build.add_skill(skill=new_skill)

    assert new_skill in build._skills


def test_remove_skill_when_skill_is_not_available_then_error_is_raised(build, skill):
    with raises(SkillNotAvailable) as exc:
        build.remove_skill(skill=skill)

    assert str(exc.value) == f'Skill {skill.name} is not available in build {build.name}'


def test_remove_skill_when_skill_is_available_then_it_is_removed(build, skill):
    build._skills = [skill]

    build.remove_skill(skill=skill)

    assert build._skills == []


def test_has_skill_if_skill_present_then_returns_true(build, skill):
    build._skills = [skill]

    assert build.has_skill(skill=skill) is True


def test_has_skill_if_skill_not_present_then_returns_false(build, skill):
    build._skills = []

    assert build.has_skill(skill=skill) is False


def test_add_upgrade_when_upgrade_already_added_then_error_is_raised(build, upgrade):
    build._upgrades = {'slot_1': upgrade}

    with raises(UpgradeAlreadyAdded) as exc:
        build.add_upgrade(upgrade=upgrade)

    assert str(exc.value) == f'Upgrade {upgrade} is already added'


def test_add_upgrade_when_ship_is_not_set_then_error_is_raised(build, upgrade):
    build._ship = None

    with raises(UpgradeNotAvailable) as exc:
        build.add_upgrade(upgrade=upgrade)

    assert str(exc.value) == f'Upgrade {upgrade} cannot be added to build without a ship'


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


def test_has_upgrade_when_upgrade_present_then_returns_true(build, upgrade):
    build._upgrades = {'slot_1': upgrade}

    assert build.has_upgrade(upgrade=upgrade) is True


def test_has_upgrade_when_upgrade_not_present_then_returns_false(build, upgrade):
    build._upgrades = {}

    assert build.has_upgrade(upgrade=upgrade) is False


def test_remove_upgrade_when_upgrade_is_not_available_then_error_is_raised(build, upgrade):
    with raises(UpgradeNotAvailable) as exc:
        build.remove_upgrade(upgrade=upgrade)

    assert str(exc.value) == f'Upgrade {upgrade} is not available in build {build.name}'


def test_remove_upgrade_when_upgrade_is_available_then_it_is_removed(build, upgrade):
    build._upgrades = {'slot_1': upgrade}

    build.remove_upgrade(upgrade=upgrade)

    assert build._upgrades == {}


def test_add_consumable_when_consumable_already_added_then_error_is_raised(build, consumable):
    build._consumables = {'slot_3': consumable}

    with raises(ConsumableAlreadyAdded) as exc:
        build.add_consumable(consumable=consumable)

    assert str(exc.value) == f'Consumable {consumable} is already added'


def test_add_consumable_when_ship_is_not_set_then_error_is_raised(build, consumable):
    build._ship = None

    with raises(ConsumableNotAvailable) as exc:
        build.add_consumable(consumable=consumable)

    assert str(exc.value) == f'Consumable {consumable} cannot be added to build without a ship'


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


def test_has_consumable_when_consumable_present_then_returns_true(build, consumable):
    build._consumables = {'slot_3': consumable}

    assert build.has_consumable(consumable=consumable) is True


def test_has_consumable_when_consumable_not_present_then_returns_false(build, consumable):
    build._consumables = {}

    assert build.has_consumable(consumable=consumable) is False


def test_serialize_returns_correct_value(build, skill, new_skill):
    build._skills = [skill, new_skill]
    build._upgrades = {'slot_1': 'Main Armaments Modification 1',
                       'slot_2': 'Damage Control System Modification 1'}
    build._consumables = {'slot_1': 'Damage Control Party',
                          'slot_2': 'Repair Party'}

    assert build.serialize() == {'name': build._name,
                                 'ship': build._ship.name,
                                 'skills': [skill.name,
                                            new_skill.name],
                                 'upgrades': build._upgrades,
                                 'consumables': build._consumables}


def test_copy_returns_independent_build_copy(build, skill, new_skill, upgrade, consumable):
    build._skills = [skill]
    build._upgrades = {'slot_1': upgrade}
    build._consumables = {'slot_1': consumable}

    build_copy = build.copy()

    assert id(build_copy) != id(build)
    assert build_copy._name == build._name
    assert build_copy._ship == build._ship
    assert build_copy._skills == build._skills
    assert build_copy._upgrades == build._upgrades
    assert build_copy._consumables == build._consumables

    build._skills.append(new_skill)
    build._upgrades['slot_2'] = 'Damage Control System Modification 1'
    build._consumables['slot_2'] = 'Repair Party'

    assert build_copy._skills != build._skills
    assert build_copy._upgrades != build._upgrades
    assert build_copy._consumables != build._consumables
