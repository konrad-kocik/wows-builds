from unittest.mock import Mock, patch

from model.ships.devonshire import Devonshire


def test_devonshire_has_correct_attributes():
    cruiser_skills = [Mock(), Mock()]

    with patch('model.ships.devonshire.CRUISER_SKILLS', cruiser_skills):
        devonshire = Devonshire()

    assert devonshire._name == 'Devonshire'
    assert devonshire._nation == 'UK'
    assert devonshire._class == 'Cruiser'
    assert devonshire._tier == 6
    assert devonshire._skills == cruiser_skills
    assert devonshire._upgrades == {'slot_1': ['Main Armaments Modification 1',
                                               'Auxiliary Armaments Modification 1',
                                               'Magazine Modification 1',
                                               'Damage Control Party Modification 1'],
                                    'slot_2': ['Damage Control System Modification 1',
                                               'Defensive AA Fire Modification 1',
                                               'Hydroacoustic Search Modification 1',
                                               'Engine Room Protection'],
                                    'slot_3': ['Main Battery Modification 2',
                                               'Secondary Battery Modification 1',
                                               'AA Guns Modification 1',
                                               'Aiming Systems Modification 1',
                                               'Torpedo Tubes Modification 1'],
                                    'slot_4': ['Damage Control System Modification 2',
                                               'Propulsion Modification 1',
                                               'Steering Gears Modification 1',
                                               'Airstrike Modification 1']}
    assert devonshire._consumables == {'slot_1': ['Damage Control Party'],
                                       'slot_2': ['Repair Party'],
                                       'slot_3': ['Defensive AA Fire',
                                                  'Hydroacoustic Search']}
