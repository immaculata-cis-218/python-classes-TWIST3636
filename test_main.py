"""
Tests for my Weapons of Rust class
"""

from main import Weapons

def test_weapon_choice():
    test_weapon = Weapons("Ray Gun", 4, 10000, 100)
    summary = test_weapon.weapon_choice()
    assert "Ray Gun" in summary

def test_dps_calculations():
    test_weapon = Weapons("Ray Gun", 4, 10000, 100)
    assert test_weapon.dps_calculations() == 1000000

    test_weapon2 = Weapons("Rock", 0, 1, 2)
    assert test_weapon2.dps_calculations() == 2