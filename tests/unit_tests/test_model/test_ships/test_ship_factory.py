from pytest import mark

from model.ships.ship_factory import create_ship
from model.ships.amagi import Amagi
from model.ships.gneisenau import Gneisenau
from model.ships.helena import Helena
from model.ships.hipper import Hipper
from model.ships.minsk import Minsk
from model.ships.nagato import Nagato
from model.ships.north_carolina import NorthCarolina
from model.ships.vauquelin import Vauquelin


@mark.parametrize('ship_name, ship_type',
                  [('Amagi', Amagi),
                   ('Gneisenau', Gneisenau),
                   ('Helena', Helena),
                   ('Hipper', Hipper),
                   ('Minsk', Minsk),
                   ('Nagato', Nagato),
                   ('North Carolina', NorthCarolina),
                   ('Vauquelin', Vauquelin)])
def test_create_ship_returns_correct_ship(ship_name, ship_type):
    ship = create_ship(name=ship_name)

    assert isinstance(ship, ship_type)
    assert ship.name == ship_name
