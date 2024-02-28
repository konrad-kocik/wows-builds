from model.skills.submarine_skills import (enhanced_sonar,
                                           liquidator,
                                           helmsman,
                                           priority_target,
                                           incoming_fire_alert,
                                           improved_battery_capacity,
                                           torpedo_crew_training,
                                           consumables_enhancements,
                                           preventive_maintenance,
                                           last_stand,
                                           enhanced_impulse_generator,
                                           sonarman,
                                           consumables_specialist,
                                           watchful,
                                           superintendent,
                                           adrenaline_rush,
                                           torpedo_aiming_master,
                                           sonarman_expert,
                                           improved_battery_efficiency,
                                           enlarged_propeller_shaft,
                                           SUBMARINE_SKILLS)


def test_enhanced_sonar_has_correct_attributes():
    assert enhanced_sonar._name == 'Enhanced Sonar'
    assert enhanced_sonar._cost == 1


def test_liquidator_has_correct_attributes():
    assert liquidator._name == 'Liquidator'
    assert liquidator._cost == 1


def test_helmsman_has_correct_attributes():
    assert helmsman._name == 'Helmsman'
    assert helmsman._cost == 1


def test_priority_target_has_correct_attributes():
    assert priority_target._name == 'Priority Target'
    assert priority_target._cost == 1


def test_incoming_fire_alert_has_correct_attributes():
    assert incoming_fire_alert._name == 'Incoming Fire Alert'
    assert incoming_fire_alert._cost == 1


def test_improved_battery_capacity_has_correct_attributes():
    assert improved_battery_capacity._name == 'Improved Battery Capacity'
    assert improved_battery_capacity._cost == 2


def test_torpedo_crew_training_has_correct_attributes():
    assert torpedo_crew_training._name == 'Torpedo Crew Training'
    assert torpedo_crew_training._cost == 2


def test_consumables_enhancements_has_correct_attributes():
    assert consumables_enhancements._name == 'Consumables Enhancements'
    assert consumables_enhancements._cost == 2


def test_preventive_maintenance_has_correct_attributes():
    assert preventive_maintenance._name == 'Preventive Maintenance'
    assert preventive_maintenance._cost == 2


def test_last_stand_has_correct_attributes():
    assert last_stand._name == 'Last Stand'
    assert last_stand._cost == 2


def test_enhanced_impulse_generator_has_correct_attributes():
    assert enhanced_impulse_generator._name == 'Enhanced Impulse Generator'
    assert enhanced_impulse_generator._cost == 3


def test_sonarman_has_correct_attributes():
    assert sonarman._name == 'Sonarman'
    assert sonarman._cost == 3


def test_consumables_specialist_has_correct_attributes():
    assert consumables_specialist._name == 'Consumables Specialist'
    assert consumables_specialist._cost == 3


def test_watchful_has_correct_attributes():
    assert watchful._name == 'Watchful'
    assert watchful._cost == 3


def test_superintendent_has_correct_attributes():
    assert superintendent._name == 'Superintendent'
    assert superintendent._cost == 3


def test_adrenaline_rush_has_correct_attributes():
    assert adrenaline_rush._name == 'Adrenaline Rush'
    assert adrenaline_rush._cost == 4


def test_torpedo_aiming_master_has_correct_attributes():
    assert torpedo_aiming_master._name == 'Torpedo Aiming Master'
    assert torpedo_aiming_master._cost == 4


def test_sonarman_expert_has_correct_attributes():
    assert sonarman_expert._name == 'Sonarman Expert'
    assert sonarman_expert._cost == 4


def test_improved_battery_efficiency_has_correct_attributes():
    assert improved_battery_efficiency._name == 'Improved Battery Efficiency'
    assert improved_battery_efficiency._cost == 4


def test_enlarged_propeller_shaft_has_correct_attributes():
    assert enlarged_propeller_shaft._name == 'Enlarged Propeller Shaft'
    assert enlarged_propeller_shaft._cost == 4


def test_submarine_skills_are_correct():
    assert SUBMARINE_SKILLS == [enhanced_sonar,
                                liquidator,
                                helmsman,
                                priority_target,
                                incoming_fire_alert,
                                improved_battery_capacity,
                                torpedo_crew_training,
                                consumables_enhancements,
                                preventive_maintenance,
                                last_stand,
                                enhanced_impulse_generator,
                                sonarman,
                                consumables_specialist,
                                watchful,
                                superintendent,
                                adrenaline_rush,
                                torpedo_aiming_master,
                                sonarman_expert,
                                improved_battery_efficiency,
                                enlarged_propeller_shaft]
