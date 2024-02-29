from model.ships.minsk import Minsk


def test_minsk_has_correct_attributes():
    minsk = Minsk()

    assert minsk._name == 'Minsk'
    assert minsk._nation == 'USSR'
    assert minsk._class == 'Destroyer'
    assert minsk._tier == 7
    assert minsk._upgrades == {'slot_1': ['Main Armaments Modification 1',
                                          'Auxiliary Armaments Modification 1',
                                          'Magazine Modification 1',
                                          'Damage Control Party Modification 1'],
                               'slot_2': ['Damage Control System Modification 1',
                                          'Engine Boost Modification 1',
                                          'Engine Room Protection'],
                               'slot_3': ['Main Battery Modification 2',
                                          'AA Guns Modification 1',
                                          'Aiming Systems Modification 1',
                                          'Smoke Generator Modification 1',
                                          'Torpedo Tubes Modification 1'],
                               'slot_4': ['Damage Control System Modification 2',
                                          'Propulsion Modification 1',
                                          'Steering Gears Modification 1',
                                          'Depth Charges Modification 1']}
    assert minsk._consumables == {'slot_1': ['Damage Control Party'],
                                  'slot_2': ['Smoke Generator'],
                                  'slot_3': ['Engine Boost']}
