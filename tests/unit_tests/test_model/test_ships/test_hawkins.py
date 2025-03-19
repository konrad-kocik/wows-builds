from unittest.mock import Mock, patch

from model.ships.hawkins import Hawkins


def test_hawkins_has_correct_attributes():
    cruiser_skills = [Mock(), Mock()]

    with patch('model.ships.hawkins.CRUISER_SKILLS', cruiser_skills):
        hawkins = Hawkins()

    assert hawkins._name == 'Hawkins'
    assert hawkins._nation == 'UK'
    assert hawkins._class == 'Cruiser'
    assert hawkins._tier == 5
    assert hawkins._skills == cruiser_skills
    assert hawkins._upgrades == {'slot_1': ['Main Armaments Modification 1',
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
                                            'Torpedo Tubes Modification 1']}
    assert hawkins._consumables == {'slot_1': ['Damage Control Party'],
                                    'slot_2': ['Repair Party'],
                                    'slot_3': ['Defensive AA Fire',
                                               'Hydroacoustic Search']}
