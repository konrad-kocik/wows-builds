from pathlib import Path
from pytest import fixture

from model.build import Build
from model.ships.nagato import Nagato
from model.ships.hipper import Hipper
from model.ships.minsk import Minsk
from model.skills.battleship_skills import grease_the_gears, adrenaline_rush
from model.skills.cruiser_skills import last_stand, priority_target
from model.skills.destroyer_skills import gun_feeder, consumables_enhancements
from data.storage import save_builds, load_builds

storage_dir_path = Path(__file__).parent.resolve()
storage_file_path = storage_dir_path.joinpath('builds.json')


@fixture
def sniping_nagato():
    sniping_nagato = Build(name='Sniping Nagato', ship=Nagato())
    sniping_nagato.add_skill(skill=grease_the_gears)
    sniping_nagato.add_skill(skill=adrenaline_rush)
    sniping_nagato.add_upgrade(upgrade='Main Armaments Modification 1')
    sniping_nagato.add_upgrade(upgrade='Damage Control System Modification 1')
    sniping_nagato.add_consumable(consumable='Repair Party')
    sniping_nagato.add_consumable(consumable='Spotting Aircraft')
    return sniping_nagato


@fixture
def after_remove_storage_file(request):
    def teardown():
        storage_file_path.unlink(missing_ok=True)

    request.addfinalizer(teardown)


@fixture
def kiting_hipper():
    kiting_hipper = Build(name='Kiting Hipper', ship=Hipper())
    kiting_hipper.add_skill(skill=last_stand)
    kiting_hipper.add_skill(skill=priority_target)
    kiting_hipper.add_upgrade(upgrade='Magazine Modification 1')
    kiting_hipper.add_upgrade(upgrade='AA Guns Modification 1')
    kiting_hipper.add_consumable(consumable='Defensive AA Fire')
    kiting_hipper.add_consumable(consumable='Catapult Fighter')
    return kiting_hipper


@fixture
def flanking_minsk():
    flanking_minsk = Build(name='Flanking Minsk', ship=Minsk())
    flanking_minsk.add_skill(skill=gun_feeder)
    flanking_minsk.add_skill(skill=consumables_enhancements)
    flanking_minsk.add_upgrade(upgrade='Main Armaments Modification 1')
    flanking_minsk.add_upgrade(upgrade='Propulsion Modification 1')
    flanking_minsk.add_consumable(consumable='Damage Control Party')
    flanking_minsk.add_consumable(consumable='Smoke Generator')
    flanking_minsk.add_consumable(consumable='Engine Boost')
    return flanking_minsk


def test_integrate_storage_with_builds(sniping_nagato, kiting_hipper, flanking_minsk, after_remove_storage_file):
    save_builds(builds=[sniping_nagato, kiting_hipper], target_dir_path=storage_dir_path)
    loaded_builds = load_builds(source_dir_path=storage_dir_path)

    loaded_sniping_nagato = loaded_builds[0]
    assert loaded_sniping_nagato.name == sniping_nagato.name
    assert loaded_sniping_nagato.ship.name == sniping_nagato.ship.name
    assert loaded_sniping_nagato.skills == sniping_nagato.skills
    assert loaded_sniping_nagato.upgrades == sniping_nagato.upgrades
    assert loaded_sniping_nagato.consumables == sniping_nagato.consumables

    loaded_kiting_hipper = loaded_builds[1]
    assert loaded_kiting_hipper.name == kiting_hipper.name
    assert loaded_kiting_hipper.ship.name == kiting_hipper.ship.name
    assert loaded_kiting_hipper.skills == kiting_hipper.skills
    assert loaded_kiting_hipper.upgrades == kiting_hipper.upgrades
    assert loaded_kiting_hipper.consumables == kiting_hipper.consumables

    save_builds(builds=[flanking_minsk, kiting_hipper], target_dir_path=storage_dir_path)
    loaded_builds = load_builds(source_dir_path=storage_dir_path)

    loaded_flanking_minsk = loaded_builds[0]
    assert loaded_flanking_minsk.name == flanking_minsk.name
    assert loaded_flanking_minsk.ship.name == flanking_minsk.ship.name
    assert loaded_flanking_minsk.skills == flanking_minsk.skills
    assert loaded_flanking_minsk.upgrades == flanking_minsk.upgrades
    assert loaded_flanking_minsk.consumables == flanking_minsk.consumables

    loaded_kiting_hipper = loaded_builds[1]
    assert loaded_kiting_hipper.name == kiting_hipper.name
    assert loaded_kiting_hipper.ship.name == kiting_hipper.ship.name
    assert loaded_kiting_hipper.skills == kiting_hipper.skills
    assert loaded_kiting_hipper.upgrades == kiting_hipper.upgrades
    assert loaded_kiting_hipper.consumables == kiting_hipper.consumables
