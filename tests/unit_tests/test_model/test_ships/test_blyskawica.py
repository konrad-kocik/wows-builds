from unittest.mock import Mock, patch

from model.ships.blyskawica import Blyskawica


def test_blyskawica_has_correct_attributes():
    destroyer_skills = [Mock(), Mock()]

    with patch('model.ships.blyskawica.DESTROYER_SKILLS', destroyer_skills):
        blyskawica = Blyskawica()

    assert blyskawica._name == 'Błyskawica'
    assert blyskawica._nation == 'Europe'
    assert blyskawica._class == 'Destroyer'
    assert blyskawica._tier == 7
    assert blyskawica._skills == destroyer_skills
    assert blyskawica._upgrades == {'slot_1': ['Main Armaments Modification 1',
                                               'Auxiliary Armaments Modification 1',
                                               'Magazine Modification 1',
                                               'Damage Control Party Modification 1'],
                                    'slot_2': ['Damage Control System Modification 1',
                                               'Engine Boost Modification 1',
                                               'Engine Room Protection'],
                                    'slot_3': ['Main Battery Modification 2',
                                               'AA Guns Modification 1',
                                               'Aiming Systems Modification 1',
                                               'Smoke Generator Modification 1'
                                               'Torpedo Tubes Modification 1'],
                                    'slot_4': ['Damage Control System Modification 2',
                                               'Propulsion Modification 1',
                                               'Steering Gears Modification 1',
                                               'Depth Charges Modification 1']}
    assert blyskawica._consumables == {'slot_1': ['Damage Control Party'],
                                       'slot_2': ['Smoke Generator'],
                                       'slot_3': ['Engine Boost']}
