from model.ships.nagato import Nagato


def test_nagato_has_correct_attributes():
    nagato = Nagato()

    assert nagato._name == 'Nagato'
    assert nagato._nation == 'Japan'
    assert nagato._class == 'Battleship'
    assert nagato._tier == 7
    assert nagato._upgrades == {'slot_1': ['Main Armaments Modification 1',
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
    assert nagato._consumables == {'slot_1': ['Damage Control Party'],
                                   'slot_2': ['Repair Party'],
                                   'slot_3': ['Spotting Aircraft',
                                              'Catapult Fighter']}
