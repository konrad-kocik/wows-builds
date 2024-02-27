from pytest import fixture

from model.skills import Skill
from model.skills import BATTLESHIP_SKILLS
from model.skills import (gun_feeder,
                          demolition_expert,
                          consumables_specialist,
                          emergency_repair_specialist,
                          incoming_fire_alert,
                          preventive_maintenance,
                          grease_the_gears,
                          inertia_fuse_for_he_shells,
                          brisk,
                          vigilance,
                          priority_target,
                          aa_defense_and_asw_expert,
                          super_heavy_ap_shells,
                          long_range_secondary_battery_shells,
                          adrenaline_rush,
                          basics_of_survivability,
                          improved_repair_party_readiness,
                          focus_fire_training,
                          furious,
                          manual_secondary_battery_aiming,
                          close_quarters_combat,
                          emergency_repair_expert,
                          concealment_expert,
                          fire_prevention_expert)


@fixture
def skill():
    return Skill(name='Demolition Expert', cost=1)


def test_skill_has_correct_attributes(skill):
    assert skill._name == 'Demolition Expert'
    assert skill._cost == 1


def test_skill_name_returns_correct_value(skill):
    assert skill.name == skill._name


def test_skill_cost_returns_correct_value(skill):
    assert skill.cost == skill._cost


def test_gun_feeder_has_correct_attributes():
    assert gun_feeder._name == 'Gun Feeder'
    assert gun_feeder._cost == 1


def test_demolition_expert_has_correct_attributes():
    assert demolition_expert._name == 'Demolition Expert'
    assert demolition_expert._cost == 1


def test_consumables_specialist_has_correct_attributes():
    assert consumables_specialist._name == 'Consumables Specialist'
    assert consumables_specialist._cost == 1


def test_emergency_repair_specialist_has_correct_attributes():
    assert emergency_repair_specialist._name == 'Emergency Repair Specialist'
    assert emergency_repair_specialist._cost == 1


def test_incoming_fire_alert_has_correct_attributes():
    assert incoming_fire_alert._name == 'Incoming Fire Alert'
    assert incoming_fire_alert._cost == 1


def test_preventive_maintenance_has_correct_attributes():
    assert preventive_maintenance._name == 'Preventive Maintenance'
    assert preventive_maintenance._cost == 1


def test_grease_the_gears_has_correct_attributes():
    assert grease_the_gears._name == 'Grease the Gears'
    assert grease_the_gears._cost == 2


def test_inertia_fuse_for_he_shells_has_correct_attributes():
    assert inertia_fuse_for_he_shells._name == 'Inertia Fuse for HE Shells'
    assert inertia_fuse_for_he_shells._cost == 2


def test_brisk_has_correct_attributes():
    assert brisk._name == 'Brisk'
    assert brisk._cost == 2


def test_vigilance_has_correct_attributes():
    assert vigilance._name == 'Vigilance'
    assert vigilance._cost == 2


def test_priority_target_has_correct_attributes():
    assert priority_target._name == 'Priority Target'
    assert priority_target._cost == 2


def test_aa_defense_and_asw_expert_has_correct_attributes():
    assert aa_defense_and_asw_expert._name == 'AA Defense and ASW Expert'
    assert aa_defense_and_asw_expert._cost == 2


def test_super_heavy_ap_shells_has_correct_attributes():
    assert super_heavy_ap_shells._name == 'Super-Heavy AP Shells'
    assert super_heavy_ap_shells._cost == 3


def test_long_range_secondary_battery_shells_has_correct_attributes():
    assert long_range_secondary_battery_shells._name == 'Long-Range Secondary Battery Shells'
    assert long_range_secondary_battery_shells._cost == 3


def test_adrenaline_rush_has_correct_attributes():
    assert adrenaline_rush._name == 'Adrenaline Rush'
    assert adrenaline_rush._cost == 3


def test_basics_of_survivability_has_correct_attributes():
    assert basics_of_survivability._name == 'Basics of Survivability'
    assert basics_of_survivability._cost == 3


def test_improved_repair_party_readiness_has_correct_attributes():
    assert improved_repair_party_readiness._name == 'Improved Repair Party Readiness'
    assert improved_repair_party_readiness._cost == 3


def test_focus_fire_training_has_correct_attributes():
    assert focus_fire_training._name == 'Focus Fire Training'
    assert focus_fire_training._cost == 3


def test_furious_has_correct_attributes():
    assert furious._name == 'Furious'
    assert furious._cost == 4


def test_manual_secondary_battery_aiming_has_correct_attributes():
    assert manual_secondary_battery_aiming._name == 'Manual Secondary Battery Aiming'
    assert manual_secondary_battery_aiming._cost == 4


def test_close_quarters_combat_has_correct_attributes():
    assert close_quarters_combat._name == 'Close Quarters Combat'
    assert close_quarters_combat._cost == 4


def test_emergency_repair_expert_has_correct_attributes():
    assert emergency_repair_expert._name == 'Emergency Repair Expert'
    assert emergency_repair_expert._cost == 4


def test_concealment_expert_has_correct_attributes():
    assert concealment_expert._name == 'Concealment Expert'
    assert concealment_expert._cost == 4


def test_fire_prevention_expert_has_correct_attributes():
    assert fire_prevention_expert._name == 'Fire Prevention Expert'
    assert fire_prevention_expert._cost == 4


def test_battleship_skills_are_correct():
    assert BATTLESHIP_SKILLS == [gun_feeder,
                                 demolition_expert,
                                 consumables_specialist,
                                 emergency_repair_specialist,
                                 incoming_fire_alert,
                                 preventive_maintenance,
                                 grease_the_gears,
                                 inertia_fuse_for_he_shells,
                                 brisk,
                                 vigilance,
                                 priority_target,
                                 aa_defense_and_asw_expert,
                                 super_heavy_ap_shells,
                                 long_range_secondary_battery_shells,
                                 adrenaline_rush,
                                 basics_of_survivability,
                                 improved_repair_party_readiness,
                                 focus_fire_training,
                                 furious,
                                 manual_secondary_battery_aiming,
                                 close_quarters_combat,
                                 emergency_repair_expert,
                                 concealment_expert,
                                 fire_prevention_expert]
