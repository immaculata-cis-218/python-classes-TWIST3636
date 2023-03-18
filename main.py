"""
Taylor Brown Python Classes
"""


class Weapons:
    """
    Weapons of Rust
    """

    def __init__(self, weapon_name, weapon_tier, fire_rate, damage):
        self.__weapon_name = weapon_name
        self.__weapon_tier = weapon_tier
        self.__fire_rate = fire_rate
        self.__damage = damage

    def weapon_choice(self):
        """
        States the weapon choice and tier of that weapon
        """
        return (
            f"You have chosen to use,"
            f"{self.__weapon_name},"
            f"which is a tier {self.__weapon_tier} weapon"
        )

    def dps_calculations(self):
        """
        Calculates DPS for the chosen weapon
        """
        dps = self.__fire_rate * self.__damage
        return dps


if __name__ == "__main__":
    hunting_bow = Weapons("Hunting Bow", 1, 1, 30)
    tommy = Weapons("Tommy", 2, 5, 10)
    ak = Weapons("Ak", 3, 6, 18)
    print(ak.weapon_choice())
    print(ak.dps_calculations())
