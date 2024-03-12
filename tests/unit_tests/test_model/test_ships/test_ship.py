from pytest import fixture
from unittest.mock import Mock

from model.ships.ship import Ship


@fixture
def ship():
    return Ship()


def test_ship_has_correct_attributes(ship):
    assert ship._name is None
    assert ship._nation is None
    assert ship._class is None
    assert ship._tier is None
    assert ship._skills == []
    assert ship._upgrades == {}
    assert ship._consumables == {}


def test_name_returns_correct_value(ship):
    ship._name = 'North Carolina'

    assert ship.name == ship._name


def test_nation_returns_correct_value(ship):
    ship._nation = 'USA'

    assert ship.nation == ship._nation


def test_ship_class_returns_correct_value(ship):
    ship._class = 'Battleship'

    assert ship.ship_class == ship._class


def test_tier_returns_correct_value(ship):
    ship._tier = 8

    assert ship.tier == ship._tier


def test_skills_returns_correct_value(ship):
    ship._skills = [Mock()]

    assert ship.skills == ship._skills


def test_upgrades_returns_correct_value(ship):
    ship._upgrades = {'slot_1': ['Main Armaments Modification 1',
                                 'Auxiliary Armaments Modification 1', ],
                      'slot_2': ['Damage Control System Modification 1']}

    assert ship.upgrades == ship._upgrades


def test_consumables_returns_correct_value(ship):
    ship._consumables = {'slot_1': ['Damage Control Party'],
                         'slot_2': ['Repair Party']}

    assert ship.consumables == ship._consumables
