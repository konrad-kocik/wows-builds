class Skill:
    def __init__(self, name: str, cost: int):
        self._name = name
        self._cost = cost

    @property
    def name(self) -> str:
        return self._name

    @property
    def cost(self) -> int:
        return self._cost


gun_feeder = Skill('Gun Feeder', 1)
demolition_expert = Skill('Demolition Expert', 1)
consumables_specialist = Skill('Consumables Specialist', 1)
emergency_repair_specialist = Skill('Emergency Repair Specialist', 1)
incoming_fire_alert = Skill('Incoming Fire Alert', 1)
preventive_maintenance = Skill('Preventive Maintenance', 1)

grease_the_gears = Skill('Grease the Gears', 2)
inertia_fuse_for_he_shells = Skill('Inertia Fuse for HE Shells', 2)
brisk = Skill('Brisk', 2)
vigilance = Skill('Vigilance', 2)
priority_target = Skill('Priority Target', 2)
aa_defense_and_asw_expert = Skill('AA Defense and ASW Expert', 2)

super_heavy_ap_shells = Skill('Super-Heavy AP Shells', 3)
long_range_secondary_battery_shells = Skill('Long-Range Secondary Battery Shells', 3)
adrenaline_rush = Skill('Adrenaline Rush', 3)
basics_of_survivability = Skill('Basics of Survivability', 3)
improved_repair_party_readiness = Skill('Improved Repair Party Readiness', 3)
focus_fire_training = Skill('Focus Fire Training', 3)

furious = Skill('Furious', 4)
manual_secondary_battery_aiming = Skill('Manual Secondary Battery Aiming', 4)
close_quarters_combat = Skill('Close Quarters Combat', 4)
emergency_repair_expert = Skill('Emergency Repair Expert', 4)
concealment_expert = Skill('Concealment Expert', 4)
fire_prevention_expert = Skill('Fire Prevention Expert', 4)

BATTLESHIP_SKILLS = [gun_feeder,
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
