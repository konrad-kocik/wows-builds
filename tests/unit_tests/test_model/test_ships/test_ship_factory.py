from pytest import mark

from model.ships.ship_factory import create_ship

from model.ships.amagi import Amagi
from model.ships.blyskawica import Blyskawica
from model.ships.devonshire import Devonshire
from model.ships.gneisenau import Gneisenau
from model.ships.hawkins import Hawkins
from model.ships.helena import Helena
from model.ships.hipper import Hipper
from model.ships.iron_duke import IronDuke
from model.ships.minsk import Minsk
from model.ships.nagato import Nagato
from model.ships.north_carolina import NorthCarolina
from model.ships.queen_elizabeth import QueenElizabeth
from model.ships.vauquelin import Vauquelin


@mark.parametrize('ship_name, ship_type',
                  [('Amagi', Amagi),
                   ('Błyskawica', Blyskawica),
                   ('Devonshire', Devonshire),
                   ('Gneisenau', Gneisenau),
                   ('Hawkins', Hawkins),
                   ('Helena', Helena),
                   ('Hipper', Hipper),
                   ('Iron Duke', IronDuke),
                   ('Minsk', Minsk),
                   ('Nagato', Nagato),
                   ('North Carolina', NorthCarolina),
                   ('Queen Elizabeth', QueenElizabeth),
                   ('Vauquelin', Vauquelin)])
def test_create_ship_returns_correct_ship(ship_name, ship_type):
    ship = create_ship(name=ship_name)

    assert isinstance(ship, ship_type)
    assert ship.name == ship_name
