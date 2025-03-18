from model.ships.ship import Ship
from model.skills.battleship_skills import BATTLESHIP_SKILLS


class IronDuke(Ship):
    def __init__(self):
        super().__init__()
        self._name = 'Iron Duke'
        self._nation = 'UK'
        self._class = 'Battleship'
        self._tier = 5
        self._skills = BATTLESHIP_SKILLS
        self._upgrades = {'slot_1': ['Main Armaments Modification 1',
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
        self._consumables = {'slot_1': ['Damage Control Party'],
                             'slot_2': ['Repair Party'],
                             'slot_3': ['Spotting Aircraft']}
