from unittest.mock import Mock, patch

from model.ships.queen_elizabeth import QueenElizabeth


def test_queen_elizabeth_has_correct_attributes():
    battleship_skills = [Mock(), Mock()]

    with patch('model.ships.queen_elizabeth.BATTLESHIP_SKILLS', battleship_skills):
        queen_elizabeth = QueenElizabeth()

    assert queen_elizabeth._name == 'Queen Elizabeth'
    assert queen_elizabeth._nation == 'UK'
    assert queen_elizabeth._class == 'Battleship'
    assert queen_elizabeth._tier == 6
    assert queen_elizabeth._skills == battleship_skills
    assert queen_elizabeth._upgrades == {'slot_1': ['Main Armaments Modification 1',
                                                    'Auxiliary Armaments Modification 1',
                                                    'Magazine Modification 1',
                                                    'Spotting Aircraft Modification 1',
                                                    'Damage Control Party Modification 1'],
                                         'slot_2': ['Damage Control System Modification 1',
                                                    'Engine Room Protection'],
                                         'slot_3': ['Main Battery Modification 2',
                                                    'Secondary Battery Modification 1',
                                                    'AA Guns Modification 1',
                                                    'Aiming Systems Modification 1'],
                                         'slot_4': ['Damage Control System Modification 2',
                                                    'Propulsion Modification 1',
                                                    'Steering Gears Modification 1',
                                                    'Airstrike Modification 1']}
    assert queen_elizabeth._consumables == {'slot_1': ['Damage Control Party'],
                                            'slot_2': ['Repair Party'],
                                            'slot_3': ['Spotting Aircraft']}
