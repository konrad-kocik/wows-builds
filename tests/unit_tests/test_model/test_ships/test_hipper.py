from model.ships.hipper import Hipper


def test_hipper_has_correct_attributes():
    hipper = Hipper()

    assert hipper._name == 'Hipper'
    assert hipper._nation == 'Germany'
    assert hipper._class == 'Cruiser'
    assert hipper._tier == 8
    assert hipper._upgrades == {'slot_1': ['Main Armaments Modification 1',
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
                                           'Airstrike Modification 1'],
                                'slot_5': ['Torpedo Lookout System',
                                           'Concealment System Modification 1',
                                           'Steering Gears Modification 2'
                                           'Ship Consumables Modification 1']}
    assert hipper._consumables == {'slot_1': ['Damage Control Party'],
                                   'slot_2': ['Defensive AA Fire',
                                              'Hydroacoustic Search'],
                                   'slot_3': ['Catapult Fighter']}
