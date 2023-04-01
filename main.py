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

    def __repr__(self):
        """
        Returns a complete representation of the object
        """
        return ("Weapons(" + str(self.__weapon_name) + "," +
                str(self.__weapon_tier) + "," + str(self.__fire_rate) +
                "," + str(self.__damage) + ")")

    def __str__(self):
        """
        Returns a human readable string
        """
        return ("(" + str(self.__weapon_name) + "," +
                str(self.__weapon_tier) + "," + str(self.__fire_rate) +
                "," + str(self.__damage) + ")")

    def __eq__(self, other):
        """
        Weapons are the same
        """
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return (self.__weapon_name == other.__weapon_name and
        self.__weapon_tier == other.__weapon_tier and self.__fire_rate == other.__fire_rate
        and self.__damage == other.__damage)

    def __lt__(self, other):
        """
        Compares if one weapon's tier is less than the other
        """
        if type(self) != type(other):
            return False
        return self.__weapon_tier < other.__weapon_tier

    def __gt__(self, other):
        """
        Compares if one weapon's tier is greater than the other
        """
        if type(self) != type(other):
            return False
        return self.__weapon_tier > other.__weapon_tier

    def weapon_choice(self):
        """
        States the weapon choice and tier of that weapon
        """
        return (
            f"You chose a "
            f"{self.__weapon_name}, "
            f"which is a tier {self.__weapon_tier} weapon"
        )

    def dps_calculations(self):
        """
        Calculates DPS for the chosen weapon
        """
        dps = self.__fire_rate * self.__damage
        return dps


class Pistol(Weapons):
    """
    Weapons of Rust that use pistol ammunition
    """

    def __init__(
        self,
        weapon_name,
        weapon_tier,
        fire_rate,
        damage,
        pistol_ammo=9,
        gunpowder=5,
        metal_frags=10,
    ):
        self.pistol_ammo = pistol_ammo
        self.__gunpowder = gunpowder
        self.__metal_frags = metal_frags
        super().__init__(weapon_name, weapon_tier, fire_rate, damage)

    def ammo_choice(self):
        """
        States the weapon choice summary and that this uses pistol ammo
        """
        weapon_summary = super().weapon_choice()
        weapon_summary = (
            f"{weapon_summary} and that uses "
            f"{self.pistol_ammo}mm ammo "
            f"which costs {self.__gunpowder} gunpowder "
            f"and {self.__metal_frags} metal frags to craft 4 bullets"
        )
        return weapon_summary

    def craft_stack(self):
        """
        Calculates the amount of resources needed to craft a stack of 128 pistol bullets
        """
        stack = (
            f"{self.__gunpowder*32} gunpowder and {self.__metal_frags*32} metal frags"
        )
        return stack


class Primative(Weapons):
    """
    Weapons of Rust that are considered primative and use arrows
    """

    def __init__(
        self, weapon_name, weapon_tier, fire_rate, damage, arrows=2, wood=25, stones=10
    ):
        self.arrows = arrows
        self.__wood = wood
        self.__stones = stones
        super().__init__(weapon_name, weapon_tier, fire_rate, damage)

    def wooden_arrows(self):
        """
        States the weapon choice summary and that this uses arrows
        """
        arrow_summary = super().weapon_choice()
        arrow_summary = (
            f"{arrow_summary} and that uses "
            f"arrows which are crafted {self.arrows} arrows "
            f"per {self.__wood} wood and {self.__stones} stones"
        )
        return arrow_summary

    def craft_stack_arrows(self):
        """
        Calculates the amount of resources needed to craft a stack of 64 arrows
        """
        stack = f"{self.__wood*32} wood and {self.__stones*32} stones"
        return stack


if __name__ == "__main__":
    hunting_bow = Primative("Hunting Bow", weapon_tier=1, fire_rate=1, damage=30)
    tommy = Pistol("Tommy", weapon_tier=2, fire_rate=5, damage=10)
    ak = Weapons("Ak", weapon_tier=3, fire_rate=6, damage=18)
    print(ak.weapon_choice())
    print(ak.dps_calculations())
    print(tommy.ammo_choice())
    print(tommy.craft_stack())
    print(hunting_bow.wooden_arrows())
    print(hunting_bow.craft_stack_arrows())
