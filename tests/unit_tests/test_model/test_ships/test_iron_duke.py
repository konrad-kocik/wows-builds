from unittest.mock import Mock, patch

from model.ships.iron_duke import IronDuke


def test_iron_duke_has_correct_attributes():
    battleship_skills = [Mock(), Mock()]

    with patch('model.ships.iron_duke.BATTLESHIP_SKILLS', battleship_skills):
        iron_duke = IronDuke()

    assert iron_duke._name == 'Iron Duke'
    assert iron_duke._nation == 'UK'
    assert iron_duke._class == 'Battleship'
    assert iron_duke._tier == 5
    assert iron_duke._skills == battleship_skills
    assert iron_duke._upgrades == {'slot_1': ['Main Armaments Modification 1',
                                              'Auxiliary Armaments Modification 1',
                                              'Magazine Modification 1',
                                              'Spotting Aircraft Modification 1',
                                              'Damage Control Party Modification 1'],
                                   'slot_2': ['Damage Control System Modification 1',
                                              'Engine Room Protection'],
                                   'slot_3': ['Main Battery Modification 2',
                                              'Secondary Battery Modification 1',
                                              'AA Guns Modification 1',
                                              'Aiming Systems Modification 1']}
    assert iron_duke._consumables == {'slot_1': ['Damage Control Party'],
                                      'slot_2': ['Repair Party'],
                                      'slot_3': ['Spotting Aircraft']}
