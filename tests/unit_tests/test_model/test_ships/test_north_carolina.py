from unittest.mock import Mock, patch

from model.ships.north_carolina import NorthCarolina


def test_north_carolina_has_correct_attributes():
    battleship_skills = [Mock(), Mock()]

    with patch('model.ships.north_carolina.BATTLESHIP_SKILLS', battleship_skills):
        north_carolina = NorthCarolina()

    assert north_carolina._name == 'North Carolina'
    assert north_carolina._nation == 'USA'
    assert north_carolina._class == 'Battleship'
    assert north_carolina._tier == 8
    assert north_carolina._skills == battleship_skills
    assert north_carolina._upgrades == {'slot_1': ['Main Armaments Modification 1',
                                                   'Auxiliary Armaments Modification 1',
                                                   'Magazine Modification 1',
                                                   'Spotting Aircraft Modification 1',
                                                   'Damage Control Party Modification 1'],
                                        'slot_2': ['Damage Control System Modification 1',
                                                   'Engine Room Protection'],
                                        'slot_3': ['Main Battery Modification 2',
                                                   'Secondary Battery Modification 1',
                                                   'AA Guns Modification 1',
                                                   'Artillery Plotting Room Modification 1'],
                                        'slot_4': ['Damage Control System Modification 2',
                                                   'Propulsion Modification 1',
                                                   'Steering Gears Modification 1',
                                                   'Airstrike Modification 1'],
                                        'slot_5': ['Torpedo Lookout System',
                                                   'Concealment System Modification 1',
                                                   'Ship Consumables Modification 1']}
    assert north_carolina._consumables == {'slot_1': ['Damage Control Party'],
                                           'slot_2': ['Repair Party'],
                                           'slot_3': ['Spotting Aircraft',
                                                      'Catapult Fighter']}
