from unittest.mock import Mock, patch

from model.ships.helena import Helena


def test_helena_has_correct_attributes():
    cruiser_skills = [Mock(), Mock()]

    with patch('model.ships.helena.CRUISER_SKILLS', cruiser_skills):
        helena = Helena()

    assert helena._name == 'Helena'
    assert helena._nation == 'USA'
    assert helena._class == 'Cruiser'
    assert helena._tier == 7
    assert helena._skills == cruiser_skills
    assert helena._upgrades == {'slot_1': ['Main Armaments Modification 1',
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
                                           'Aiming Systems Modification 1'],
                                'slot_4': ['Damage Control System Modification 2',
                                           'Propulsion Modification 1',
                                           'Steering Gears Modification 1',
                                           'Airstrike Modification 1']}
    assert helena._consumables == {'slot_1': ['Damage Control Party'],
                                   'slot_2': ['Defensive AA Fire'],
                                   'slot_3': ['Catapult Fighter'],
                                   'slot_4': ['Hydroacoustic Search']}
