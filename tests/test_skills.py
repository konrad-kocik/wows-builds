from pytest import fixture

from model.skills import Skill
from model.skills import (gun_feeder,
                          emergency_repair_specialist,
                          grease_the_gears,
                          adrenaline_rush)


@fixture
def skill():
    return Skill(name='Demolition Expert', cost=1)


def test_skill_has_correct_attributes(skill):
    assert skill._name == 'Demolition Expert'
    assert skill._cost == 1


def test_skill_name_returns_correct_value(skill):
    assert skill.name == skill._name


def test_skill_cost_returns_correct_value(skill):
    assert skill.cost == skill._cost


def test_gun_feeder_has_correct_attributes():
    assert gun_feeder._name == 'Gun Feeder'
    assert gun_feeder._cost == 1


def test_emergency_repair_specialist_has_correct_attributes():
    assert emergency_repair_specialist._name == 'Emergency Repair Specialist'
    assert emergency_repair_specialist._cost == 1


def test_grease_the_gears_has_correct_attributes():
    assert grease_the_gears._name == 'Grease the Gears'
    assert grease_the_gears._cost == 2


def test_adrenaline_rush_has_correct_attributes():
    assert adrenaline_rush._name == 'Adrenaline Rush'
    assert adrenaline_rush._cost == 3
