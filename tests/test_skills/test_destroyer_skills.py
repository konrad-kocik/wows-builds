from model.skills.destroyer_skills import (grease_the_gears,
                                           liquidator,
                                           consumables_specialist,
                                           gun_feeder,
                                           incoming_fire_alert,
                                           preventive_maintenance,
                                           demolition_expert,
                                           swift_fish,
                                           consumables_enhancements,
                                           extra_heavy_ammunition,
                                           priority_target,
                                           last_stand,
                                           main_battery_and_aa_specialist,
                                           fill_the_tubes,
                                           adrenaline_rush,
                                           inertia_fuse_for_he_shells,
                                           superintendent,
                                           survivability_expert,
                                           main_battery_and_aa_expert,
                                           swift_in_silence,
                                           radio_location,
                                           fearless_brawler,
                                           concealment_expert,
                                           dazzle,
                                           DESTROYER_SKILLS)


def test_grease_the_gears_has_correct_attributes():
    assert grease_the_gears._name == 'Grease the Gears'
    assert grease_the_gears._cost == 1


def test_liquidator_has_correct_attributes():
    assert liquidator._name == 'Liquidator'
    assert liquidator._cost == 1


def test_consumables_specialist_has_correct_attributes():
    assert consumables_specialist._name == 'Consumables Specialist'
    assert consumables_specialist._cost == 1


def test_gun_feeder_has_correct_attributes():
    assert gun_feeder._name == 'Gun Feeder'
    assert gun_feeder._cost == 1


def test_incoming_fire_alert_has_correct_attributes():
    assert incoming_fire_alert._name == 'Incoming Fire Alert'
    assert incoming_fire_alert._cost == 1


def test_preventive_maintenance_has_correct_attributes():
    assert preventive_maintenance._name == 'Preventive Maintenance'
    assert preventive_maintenance._cost == 1


def test_demolition_expert_has_correct_attributes():
    assert demolition_expert._name == 'Demolition Expert'
    assert demolition_expert._cost == 2


def test_swift_fish_has_correct_attributes():
    assert swift_fish._name == 'Swift Fish'
    assert swift_fish._cost == 2


def test_consumables_enhancements_has_correct_attributes():
    assert consumables_enhancements._name == 'Consumables Enhancements'
    assert consumables_enhancements._cost == 2


def test_extra_heavy_ammunition_has_correct_attributes():
    assert extra_heavy_ammunition._name == 'Extra-Heavy Ammunition'
    assert extra_heavy_ammunition._cost == 2


def test_priority_target_has_correct_attributes():
    assert priority_target._name == 'Priority Target'
    assert priority_target._cost == 2


def test_last_stand_has_correct_attributes():
    assert last_stand._name == 'Last Stand'
    assert last_stand._cost == 2


def test_main_battery_and_aa_specialist_has_correct_attributes():
    assert main_battery_and_aa_specialist._name == 'Main Battery and AA Specialist'
    assert main_battery_and_aa_specialist._cost == 3


def test_fill_the_tubes_has_correct_attributes():
    assert fill_the_tubes._name == 'Fill the Tubes'
    assert fill_the_tubes._cost == 3


def test_adrenaline_rush_has_correct_attributes():
    assert adrenaline_rush._name == 'Adrenaline Rush'
    assert adrenaline_rush._cost == 3


def test_inertia_fuse_for_he_shells_has_correct_attributes():
    assert inertia_fuse_for_he_shells._name == 'Inertia Fuse for HE Shells'
    assert inertia_fuse_for_he_shells._cost == 3


def test_superintendent_has_correct_attributes():
    assert superintendent._name == 'Superintendent'
    assert superintendent._cost == 3


def test_survivability_expert_has_correct_attributes():
    assert survivability_expert._name == 'Survivability Expert'
    assert survivability_expert._cost == 3


def test_main_battery_and_aa_expert_has_correct_attributes():
    assert main_battery_and_aa_expert._name == 'Main Battery and AA Expert'
    assert main_battery_and_aa_expert._cost == 4


def test_swift_in_silence_has_correct_attributes():
    assert swift_in_silence._name == 'Swift in Silence'
    assert swift_in_silence._cost == 4


def test_radio_location_has_correct_attributes():
    assert radio_location._name == 'Radio Location'
    assert radio_location._cost == 4


def test_fearless_brawler_has_correct_attributes():
    assert fearless_brawler._name == 'Fearless Brawler'
    assert fearless_brawler._cost == 4


def test_concealment_expert_has_correct_attributes():
    assert concealment_expert._name == 'Concealment Expert'
    assert concealment_expert._cost == 4


def test_dazzle_has_correct_attributes():
    assert dazzle._name == 'Dazzle'
    assert dazzle._cost == 4


def test_destroyer_skills_are_correct():
    assert DESTROYER_SKILLS == [grease_the_gears,
                                liquidator,
                                consumables_specialist,
                                gun_feeder,
                                incoming_fire_alert,
                                preventive_maintenance,
                                demolition_expert,
                                swift_fish,
                                consumables_enhancements,
                                extra_heavy_ammunition,
                                priority_target,
                                last_stand,
                                main_battery_and_aa_specialist,
                                fill_the_tubes,
                                adrenaline_rush,
                                inertia_fuse_for_he_shells,
                                superintendent,
                                survivability_expert,
                                main_battery_and_aa_expert,
                                swift_in_silence,
                                radio_location,
                                fearless_brawler,
                                concealment_expert,
                                dazzle]
