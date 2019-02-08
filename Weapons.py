# File for Weapons Class

class Weapon:
    """Weapon Object Class"""
    # will need inheritance for different types of weapons could even break down by damage type
    def __init__(self, name, minDamage, maxDamage, damageType):
        self.name = name
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.damageType = damageType