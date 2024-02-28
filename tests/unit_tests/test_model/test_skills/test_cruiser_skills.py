from model.skills.cruiser_skills import (grease_the_gears,
                                         swift_fish,
                                         consumables_specialist,
                                         gun_feeder,
                                         incoming_fire_alert,
                                         last_stand,
                                         demolition_expert,
                                         fill_the_tubes,
                                         consumables_enhancements,
                                         fly_in_the_sky,
                                         priority_target,
                                         focus_fire_training,
                                         heavy_he_and_sap_shells,
                                         pack_a_punch,
                                         adrenaline_rush,
                                         heavy_ap_shells,
                                         superintendent,
                                         survivability_expert,
                                         top_grade_gunner,
                                         outnumbered,
                                         radio_location,
                                         inertia_fuse_for_he_shells,
                                         concealment_expert,
                                         aa_defense_and_asw_expert,
                                         CRUISER_SKILLS)


def test_grease_the_gears_has_correct_attributes():
    assert grease_the_gears._name == 'Grease the Gears'
    assert grease_the_gears._cost == 1


def test_swift_fish_has_correct_attributes():
    assert swift_fish._name == 'Swift Fish'
    assert swift_fish._cost == 1


def test_consumables_specialist_has_correct_attributes():
    assert consumables_specialist._name == 'Consumables Specialist'
    assert consumables_specialist._cost == 1


def test_gun_feeder_has_correct_attributes():
    assert gun_feeder._name == 'Gun Feeder'
    assert gun_feeder._cost == 1


def test_incoming_fire_alert_has_correct_attributes():
    assert incoming_fire_alert._name == 'Incoming Fire Alert'
    assert incoming_fire_alert._cost == 1


def test_last_stand_has_correct_attributes():
    assert last_stand._name == 'Last Stand'
    assert last_stand._cost == 1


def test_demolition_expert_has_correct_attributes():
    assert demolition_expert._name == 'Demolition Expert'
    assert demolition_expert._cost == 2


def test_fill_the_tubes_has_correct_attributes():
    assert fill_the_tubes._name == 'Fill the Tubes'
    assert fill_the_tubes._cost == 2


def test_consumables_enhancements_has_correct_attributes():
    assert consumables_enhancements._name == 'Consumables Enhancements'
    assert consumables_enhancements._cost == 2


def test_fly_in_the_sky_has_correct_attributes():
    assert fly_in_the_sky._name == 'Fly in the Sky'
    assert fly_in_the_sky._cost == 2


def test_priority_target_has_correct_attributes():
    assert priority_target._name == 'Priority Target'
    assert priority_target._cost == 2


def test_focus_fire_training_has_correct_attributes():
    assert focus_fire_training._name == 'Focus Fire Training'
    assert focus_fire_training._cost == 2


def test_heavy_he_and_sap_shells_has_correct_attributes():
    assert heavy_he_and_sap_shells._name == 'Heavy HE and SAP Shells'
    assert heavy_he_and_sap_shells._cost == 3


def test_pack_a_punch_has_correct_attributes():
    assert pack_a_punch._name == 'Pack a Punch'
    assert pack_a_punch._cost == 3


def test_adrenaline_rush_has_correct_attributes():
    assert adrenaline_rush._name == 'Adrenaline Rush'
    assert adrenaline_rush._cost == 3


def test_heavy_ap_shells_has_correct_attributes():
    assert heavy_ap_shells._name == 'Heavy AP Shells'
    assert heavy_ap_shells._cost == 3


def test_superintendent_has_correct_attributes():
    assert superintendent._name == 'Superintendent'
    assert superintendent._cost == 3


def test_survivability_expert_has_correct_attributes():
    assert survivability_expert._name == 'Survivability Expert'
    assert survivability_expert._cost == 3


def test_top_grade_gunner_has_correct_attributes():
    assert top_grade_gunner._name == 'Top Grade Gunner'
    assert top_grade_gunner._cost == 4


def test_outnumbered_has_correct_attributes():
    assert outnumbered._name == 'Outnumbered'
    assert outnumbered._cost == 4


def test_radio_location_has_correct_attributes():
    assert radio_location._name == 'Radio Location'
    assert radio_location._cost == 4


def test_inertia_fuse_for_he_shells_has_correct_attributes():
    assert inertia_fuse_for_he_shells._name == 'Inertia Fuse for HE Shells'
    assert inertia_fuse_for_he_shells._cost == 4


def test_concealment_expert_has_correct_attributes():
    assert concealment_expert._name == 'Concealment Expert'
    assert concealment_expert._cost == 4


def test_aa_defense_and_asw_expert_has_correct_attributes():
    assert aa_defense_and_asw_expert._name == 'AA Defense and ASW Expert'
    assert aa_defense_and_asw_expert._cost == 4


def test_cruiser_skills_are_correct():
    assert CRUISER_SKILLS == [grease_the_gears,
                              swift_fish,
                              consumables_specialist,
                              gun_feeder,
                              incoming_fire_alert,
                              last_stand,
                              demolition_expert,
                              fill_the_tubes,
                              consumables_enhancements,
                              fly_in_the_sky,
                              priority_target,
                              focus_fire_training,
                              heavy_he_and_sap_shells,
                              pack_a_punch,
                              adrenaline_rush,
                              heavy_ap_shells,
                              superintendent,
                              survivability_expert,
                              top_grade_gunner,
                              outnumbered,
                              radio_location,
                              inertia_fuse_for_he_shells,
                              concealment_expert,
                              aa_defense_and_asw_expert]
