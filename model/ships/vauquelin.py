from model.ships.ship import Ship
from model.skills.destroyer_skills import DESTROYER_SKILLS


class Vauquelin(Ship):
    def __init__(self):
        super().__init__()
        self._name = 'Vauquelin'
        self._nation = 'France'
        self._class = 'Destroyer'
        self._tier = 7
        self._skills = DESTROYER_SKILLS
        self._upgrades = {'slot_1': ['Main Armaments Modification 1',
                                     'Auxiliary Armaments Modification 1',
                                     'Magazine Modification 1',
                                     'Damage Control Party Modification 1'],
                          'slot_2': ['Damage Control System Modification 1',
                                     'Engine Boost Modification 1',
                                     'Engine Room Protection'],
                          'slot_3': ['Main Battery Modification 2',
                                     'AA Guns Modification 1',
                                     'Aiming Systems Modification 1',
                                     'Torpedo Tubes Modification 1'],
                          'slot_4': ['Damage Control System Modification 2',
                                     'Propulsion Modification 1',
                                     'Steering Gears Modification 1',
                                     'Depth Charges Modification 1']}
        self._consumables = {'slot_1': ['Damage Control Party'],
                             'slot_2': ['Main Battery Reload Booster'],
                             'slot_3': ['Engine Boost']}
