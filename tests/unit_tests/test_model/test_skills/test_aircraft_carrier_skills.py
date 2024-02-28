from model.skills.aircraft_carrier_skills import (last_gasp,
                                                  improved_engine_boost,
                                                  engine_techie,
                                                  air_supremacy,
                                                  direction_center_for_fighters,
                                                  search_and_destroy,
                                                  torpedo_bomber,
                                                  swift_fish,
                                                  improved_engines,
                                                  repair_specialist,
                                                  secondary_armament_expert,
                                                  patrol_group_leader,
                                                  sight_stabilization,
                                                  enhanced_armor_piercing_ammunition,
                                                  pyrotechnician,
                                                  aircraft_armor,
                                                  survivability_expert,
                                                  interceptor,
                                                  bomber_flight_control,
                                                  proximity_fuze,
                                                  close_quarters_expert,
                                                  enhanced_aircraft_armor,
                                                  hidden_menace,
                                                  enhanced_reactions,
                                                  AIRCRAFT_CARRIER_SKILLS)


def test_last_gasp_has_correct_attributes():
    assert last_gasp._name == 'Last Gasp'
    assert last_gasp._cost == 1


def test_improved_engine_boost_has_correct_attributes():
    assert improved_engine_boost._name == 'Improved Engine Boost'
    assert improved_engine_boost._cost == 1


def test_engine_techie_has_correct_attributes():
    assert engine_techie._name == 'Engine Techie'
    assert engine_techie._cost == 1


def test_air_supremacy_has_correct_attributes():
    assert air_supremacy._name == 'Air Supremacy'
    assert air_supremacy._cost == 1


def test_direction_center_for_fighters_has_correct_attributes():
    assert direction_center_for_fighters._name == 'Direction Center for Fighters'
    assert direction_center_for_fighters._cost == 1


def test_search_and_destroy_has_correct_attributes():
    assert search_and_destroy._name == 'Search and Destroy'
    assert search_and_destroy._cost == 1


def test_torpedo_bomber_has_correct_attributes():
    assert torpedo_bomber._name == 'Torpedo Bomber'
    assert torpedo_bomber._cost == 2


def test_swift_fish_has_correct_attributes():
    assert swift_fish._name == 'Swift Fish'
    assert swift_fish._cost == 2


def test_improved_engines_has_correct_attributes():
    assert improved_engines._name == 'Improved Engines'
    assert improved_engines._cost == 2


def test_repair_specialist_has_correct_attributes():
    assert repair_specialist._name == 'Repair Specialist'
    assert repair_specialist._cost == 2


def test_secondary_armament_expert_has_correct_attributes():
    assert secondary_armament_expert._name == 'Secondary Armament Expert'
    assert secondary_armament_expert._cost == 2


def test_patrol_group_leader_has_correct_attributes():
    assert patrol_group_leader._name == 'Patrol Group Leader'
    assert patrol_group_leader._cost == 2


def test_sight_stabilization_has_correct_attributes():
    assert sight_stabilization._name == 'Sight Stabilization'
    assert sight_stabilization._cost == 3


def test_enhanced_armor_piercing_ammunition_has_correct_attributes():
    assert enhanced_armor_piercing_ammunition._name == 'Enhanced Armor-Piercing Ammunition'
    assert enhanced_armor_piercing_ammunition._cost == 3


def test_pyrotechnician_has_correct_attributes():
    assert pyrotechnician._name == 'Pyrotechnician'
    assert pyrotechnician._cost == 3


def test_aircraft_armor_has_correct_attributes():
    assert aircraft_armor._name == 'Aircraft Armor'
    assert aircraft_armor._cost == 3


def test_survivability_expert_has_correct_attributes():
    assert survivability_expert._name == 'Survivability Expert'
    assert survivability_expert._cost == 3


def test_interceptor_has_correct_attributes():
    assert interceptor._name == 'Interceptor'
    assert interceptor._cost == 3


def test_bomber_flight_control_has_correct_attributes():
    assert bomber_flight_control._name == 'Bomber Flight Control'
    assert bomber_flight_control._cost == 4


def test_proximity_fuze_has_correct_attributes():
    assert proximity_fuze._name == 'Proximity Fuze'
    assert proximity_fuze._cost == 4


def test_close_quarters_expert_has_correct_attributes():
    assert close_quarters_expert._name == 'Close Quarters Expert'
    assert close_quarters_expert._cost == 4


def test_enhanced_aircraft_armor_has_correct_attributes():
    assert enhanced_aircraft_armor._name == 'Enhanced Aircraft Armor'
    assert enhanced_aircraft_armor._cost == 4


def test_hidden_menace_has_correct_attributes():
    assert hidden_menace._name == 'Hidden Menace'
    assert hidden_menace._cost == 4


def test_enhanced_reactions_has_correct_attributes():
    assert enhanced_reactions._name == 'Enhanced Reactions'
    assert enhanced_reactions._cost == 4


def test_aircraft_carrier_skills_are_correct():
    assert AIRCRAFT_CARRIER_SKILLS == [last_gasp,
                                       improved_engine_boost,
                                       engine_techie,
                                       air_supremacy,
                                       direction_center_for_fighters,
                                       search_and_destroy,
                                       torpedo_bomber,
                                       swift_fish,
                                       improved_engines,
                                       repair_specialist,
                                       secondary_armament_expert,
                                       patrol_group_leader,
                                       sight_stabilization,
                                       enhanced_armor_piercing_ammunition,
                                       pyrotechnician,
                                       aircraft_armor,
                                       survivability_expert,
                                       interceptor,
                                       bomber_flight_control,
                                       proximity_fuze,
                                       close_quarters_expert,
                                       enhanced_aircraft_armor,
                                       hidden_menace,
                                       enhanced_reactions]
