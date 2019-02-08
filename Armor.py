# File for Armor Class

class Armor:
    """Armor Object Class"""
    # will need inheritance for different armor types and body parts
    def __init__(self, name, ac_mod):
        self.name = name
        self.armorClassModifier = ac_mod