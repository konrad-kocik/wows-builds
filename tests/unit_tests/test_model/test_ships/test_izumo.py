from unittest.mock import Mock, patch

from model.ships.izumo import Izumo


def test_izumo_has_correct_attributes():
    battleship_skills = [Mock(), Mock()]

    with patch('model.ships.izumo.BATTLESHIP_SKILLS', battleship_skills):
        izumo = Izumo()

    assert izumo._name == 'Izumo'
    assert izumo._nation == 'Japan'
    assert izumo._class == 'Battleship'
    assert izumo._tier == 9
    assert izumo._skills == battleship_skills
    assert izumo._upgrades == {'slot_1': ['Main Armaments Modification 1',
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
                                          'Airstrike Modification 1'],
                               'slot_5': ['Torpedo Lookout System',
                                          'Concealment System Modification 1',
                                          'Ship Consumables Modification 1'],
                               'slot_6': ['Main Battery Modification 3',
                                          'Gun Fire Control System Modification 2',
                                          'Auxiliary Armaments Modification 2']}
    assert izumo._consumables == {'slot_1': ['Damage Control Party'],
                                  'slot_2': ['Repair Party'],
                                  'slot_3': ['Spotting Aircraft',
                                             'Catapult Fighter']}
