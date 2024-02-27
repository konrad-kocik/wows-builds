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
emergency_repair_specialist = Skill('Emergency Repair Specialist', 1)
grease_the_gears = Skill('Grease the Gears', 2)
adrenaline_rush = Skill('Adrenaline Rush', 3)
