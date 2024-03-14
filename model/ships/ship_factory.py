from model.ships.ship import Ship
from model.ships.amagi import Amagi
from model.ships.gneisenau import Gneisenau
from model.ships.helena import Helena
from model.ships.hipper import Hipper
from model.ships.minsk import Minsk
from model.ships.nagato import Nagato
from model.ships.north_carolina import NorthCarolina
from model.ships.vauquelin import Vauquelin

ships = {'Amagi': Amagi,
         'Gneisenau': Gneisenau,
         'Helena': Helena,
         'Hipper': Hipper,
         'Minsk': Minsk,
         'Nagato': Nagato,
         'North Carolina': NorthCarolina,
         'Vauquelin': Vauquelin}


def create_ship(name: str) -> Ship:
    return ships[name]()
