"""
Tests for my Weapons of Rust class
"""

from main import Weapons
from main import Pistol
from main import Primative

def test_weapon_choice():
    """
    Tests the weapon name is inserted correctly
    """
    test_weapon = Weapons("Ray Gun", 4, 10000, 100)
    summary = test_weapon.weapon_choice()
    assert "Ray Gun" in summary

def test_dps_calculations():
    """
    Tests for accurate dps calculations
    """
    test_weapon = Weapons("Ray Gun", 4, 10000, 100)
    assert test_weapon.dps_calculations() == 1000000

    test_weapon2 = Weapons("Rock", 0, 1, 2)
    assert test_weapon2.dps_calculations() == 2

def test_ammo_choice():
    """
    Tests the name of the weapon and the caliber is stated correctly 
    """
    test_weapon = Pistol("M9", weapon_tier=2, fire_rate=3,
                          damage=14, pistol_ammo=45, gunpowder=10, metal_frags=20)
    summary = test_weapon.ammo_choice()
    assert "M9" in summary
    assert str(45) in summary

def test_craft_stack():
    """
    Tests for accurate resource calculations
    """
    test_weapon = Pistol("M9", weapon_tier=2, fire_rate=3,
                          damage=14, pistol_ammo=45, gunpowder=10, metal_frags=20)
    assert test_weapon.craft_stack() == f"{320} gunpowder and {640} metal frags"

    test_weapon1 = Pistol("Revolver", weapon_tier=1, fire_rate=2, damage=4)
    assert test_weapon1.craft_stack() == f"{160} gunpowder and {320} metal frags"

def test_wooden_arrows():
    """
    Tests the name of the weapon and resources needed are reflected
    """
    test_weapon = Primative("Crossbow", weapon_tier=1, fire_rate=1,
                          damage=45, arrows=4, wood=50, stones=20)
    summary = test_weapon.wooden_arrows()
    assert "Crossbow" in summary
    assert str(50) in summary
    assert str(20) in summary

def test_craft_stack_arrows():
    """
    Tests the accurate output of resources need to craft a stack of arrows
    """
    test_weapon = Primative("Crossbow", weapon_tier=1, fire_rate=1,
                          damage=45, arrows=4, wood=50, stones=20)
    assert test_weapon.craft_stack_arrows() == f"{1600} wood and {640} stones"
