# File for Character Class

import random

class Character:
    """Character Object Class"""
    def __init__(self, name, strength, dexterity, wisdom, intelligence, charisma, constitution, classChoice, raceChoice, sex):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma
        self.constitution = constitution
        self.classChoice = classChoice
        self.race = raceChoice
        self.sex = sex
        self.armorClass = 10
        self.equippedWeaponRight = None
        self.equippedWeaponLeft = None
        self.equippedArmorRight = None
        self.equippedArmorLeft = None
        self.equippedArmorTorso = None
        self.equippedArmorLegs = None
        self.equippedArmorArms = None
        self.equippedArmorWrists = None
        self.equippedArmorHead = None
        self.inventory = []
        self.description = ""
        self.background = ""
        self.gp = 0
        self.sp = 0
        self.pp = 0
        self.cp = 0
        self.level = 1
        self.hp = 0
        self.experiencePoints = 0

    def __repr__(self):
        print("Character, " + self.name + ".  Class, " + self.classChoice)

    def __str__(self):
        print(self.name + "\nSex: " + self.sex + "\nStrength: " + str(self.strength) + "\nDexterity: " + str(self.dexterity))
        print("Wisdom: " + str(self.wisdom) + "\nIntelligence: " + str(self.intelligence) + "\nCharisma: " + str(self.charisma))
        print("Constitution: " + str(self.constitution) +"\nRace: " + self.race + "\nClass: " + self.classChoice)

    def attack(self, targetEnemy, minDamage, maxDamage, damageType, unblockableDamage):
        """Attack with equipped weapon"""
        potDamage = random.randint(minDamage, maxDamage)

        if potDamage > 0:
            if potDamage > targetEnemy.armorClass:
                damageDealt = potDamage - targetEnemy.armorClass
            else:
                damageDealt = unblockableDamage

        else:
            damageDealt = unblockableDamage

        print(self.name + " attacked " + targetEnemy.name + " for " + str(damageDealt) + " " + damageType + " damage!")
        targetEnemy.hp -= damageDealt

    def equipWeaponRight(self, Weapon):
        """Equip Weapon Right Hand"""
        self.equippedWeaponRight = Weapon
        print(Weapon.name + " equipped to right hand")

    def equipWeaponLeft(self, Weapon):
        """Equip Weapon Left Hand"""
        self.equippedWeaponLeft = Weapon
        print(Weapon.name + " equipped to left hand")

    def unequipWeaponLeft(self, Weapon):
        """Unequip Weapon from Left Hand"""
        print(Weapon.name + " unequipped")
        self.equipWeaponLeft(None)

    def unequipWeaponRight(self, Weapon):
        """Unequip Weapon from Right Hand"""
        print(Weapon.name + " unequipped")
        self.equipWeaponRight(None)

    def equipArmorRight(self, Armor):
        """Equip Shield to Right Hand"""
        self.equippedArmorRight = Armor
        if Armor != None:
            print(Armor.name + " equipped")
            self.armorClass += Armor.armorClassModifier
            print("AC is " + str(self.armorClass))

    def equipArmorLeft(self, Armor):
        """Equip Shield to Left Hand"""
        self.equippedArmorLeft = Armor
        if Armor != None:
            print(Armor.name + " equipped")
            self.armorClass += Armor.armorClassModifier
            print("AC is " + str(self.armorClass))

    def equipArmorTorso(self, Armor):
        """Equip Armor to Torso"""
        self.equippedArmorTorso = Armor
        if Armor != None:
            print(Armor.name + " equipped")
            self.armorClass += Armor.armorClassModifier
            print("AC is " + str(self.armorClass))

    def equipArmorLegs(self, Armor):
        """Equip Armor to Legs"""
        self.equippedArmorLegs = Armor
        if Armor != None:
            print(Armor.name + " equipped")
            self.armorClass += Armor.armorClassModifier
            print("AC is " + str(self.armorClass))

    def equipArmorArms(self, Armor):
        """Equip Armor to Arms"""
        self.equippedArmorArms = Armor
        if Armor != None:
            print(Armor.name + " equipped")
            self.armorClass += Armor.armorClassModifier
            print("AC is " + str(self.armorClass))

    def equipArmorWrists(self, Armor):
        """Equip Armor to Wrists"""
        self.equippedArmorWrists = Armor
        if Armor != None:
            print(Armor.name + " equipped")
            self.armorClass += Armor.armorClassModifier
            print("AC is " + str(self.armorClass))

    def equipArmorHead(self, Armor):
        """Equip Armor to Head"""
        self.equippedArmorHead = Armor
        if Armor != None:
            print(Armor.name + " equipped")
            self.armorClass += Armor.armorClassModifier
            print("AC is " + str(self.armorClass))

    def unequipArmorTorso(self, Armor):
        """Unequip Armor from Torso"""
        self.armorClass -= Armor.armorClassModifier
        print(Armor.name + " unequipped")
        self.equipArmorTorso(None)
        print("AC is " + str(self.armorClass))

    def unequipArmorLegs(self, Armor):
        """Unequip Armor from Legs"""
        self.armorClass -= Armor.armorClassModifier
        print(Armor.name + " unequipped")
        self.equipArmorLegs(None)
        print("AC is " + str(self.armorClass))

    def unequipArmorArms(self, Armor):
        """Unequip Armor from Arms"""
        self.armorClass -= Armor.armorClassModifier
        print(Armor.name + " unequipped")
        self.equipArmorArms(None)
        print("AC is " + str(self.armorClass))

    def unequipArmorWrists(self, Armor):
        """Unequip Armor from Wrists"""
        self.armorClass -= Armor.armorClassModifier
        print(Armor.name + " unequipped")
        self.equipArmorWrists(None)
        print("AC is " + str(self.armorClass))

    def unequipArmorHead(self, Armor):
        """Unequip Armor from Head"""
        self.armorClass -= Armor.armorClassModifier
        print(Armor.name + " unequipped")
        self.equipArmorHead(None)
        print("AC is " + str(self.armorClass))

    def addGP(self, gp):
        """adds to current gp"""
        self.gp += gp

    def addSP(self, sp):
        """adds to current sp"""
        self.sp += sp

    def addPP(self, pp):
        """adds to current pp"""
        self.pp += pp

    def addCP(self, cp):
        """adds to current cp"""
        self.cp += cp

    def addXP(self, xp):
        """adds to current xp"""
        self.experiencePoints += xp

    def addHP(self, hp):
        """adds hp to current value"""
        self.hp += hp

    def getHp(self):
        hitpoints = self.name + " Current HP=" + str(self.hp)
        return hitpoints

    def getMoney(self):
        money = "PP=" + str(self.pp) + ", GP=" + str(self.gp) + ", SP=" + str(self.sp) + ", CP=" + str(self.cp)
        return money

# MAKE MONSTERS A CHILD CLASS OF CHARACTER CLASS, SINCE CHARACTERS CAN BE ENEMIES ALSO
class Monster(Character):

    def __init__(self, name, strength, dexterity, wisdom, intelligence, charisma, constitution, classChoice, raceChoice, sex):
        Character.__init__(self, name, strength, dexterity, wisdom, intelligence, charisma, constitution, classChoice, raceChoice, sex)
        self.item = None
