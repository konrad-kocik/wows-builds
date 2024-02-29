from model.ships.ship import Ship


class Hipper(Ship):
    def __init__(self):
        super().__init__()
        self._name = 'Hipper'
        self._nation = 'Germany'
        self._class = 'Cruiser'
        self._tier = 8
        self._upgrades = {'slot_1': ['Main Armaments Modification 1',
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
        self._consumables = {'slot_1': ['Damage Control Party'],
                             'slot_2': ['Defensive AA Fire',
                                        'Hydroacoustic Search'],
                             'slot_3': ['Catapult Fighter']}
