# File for Weapons Class

class Weapon:
    """Weapon Object Class"""
    # will need inheritance for different types of weapons could even break down by damage type
    def __init__(self, name, minDamage, maxDamage, damageType, unblockableDamage):
        self.name = name
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.damageType = damageType
        self.unblockableDamage = unblockableDamage


# need to do inheritance for different type weapons - swords, hammers, axes, bows, etc.
# BUT first break down to one-handed, two-handed, ranged, etc.