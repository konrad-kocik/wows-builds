from model.ships.ship import Ship

from model.ships.amagi import Amagi
from model.ships.blyskawica import Blyskawica
from model.ships.devonshire import Devonshire
from model.ships.gneisenau import Gneisenau
from model.ships.hawkins import Hawkins
from model.ships.helena import Helena
from model.ships.hipper import Hipper
from model.ships.iron_duke import IronDuke
from model.ships.izumo import Izumo
from model.ships.minsk import Minsk
from model.ships.nagato import Nagato
from model.ships.north_carolina import NorthCarolina
from model.ships.queen_elizabeth import QueenElizabeth
from model.ships.vauquelin import Vauquelin
from model.ships.yamato import Yamato

ships = {'Amagi': Amagi,
         'Błyskawica': Blyskawica,
         'Devonshire': Devonshire,
         'Gneisenau': Gneisenau,
         'Hawkins': Hawkins,
         'Helena': Helena,
         'Hipper': Hipper,
         'Iron Duke': IronDuke,
         'Izumo': Izumo,
         'Minsk': Minsk,
         'Nagato': Nagato,
         'North Carolina': NorthCarolina,
         'Queen Elizabeth': QueenElizabeth,
         'Vauquelin': Vauquelin,
         'Yamato': Yamato}


def create_ship(name: str) -> Ship:
    return ships[name]()
