# File for Character Class

import random

class Character:
    """Character Object Class"""
    def __init__(self, characterName, strength, dexterity, wisdom, intelligence, charisma, constitution, classChoice, raceChoice, sex):
        self.characterName = characterName
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
        self.equippedWeapon1 = None
        self.equippedWeapon2 = None
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
        print("Character, " + self.characterName + ".  Class, " + self.classChoice)

    def __str__(self):
        print(self.characterName + "\nSex: " + self.sex + "\nStrength: " + str(self.strength) + "\nDexterity: " + str(self.dexterity))
        print("Wisdom: " + str(self.wisdom) + "\nIntelligence: " + str(self.intelligence) + "\nCharisma: " + str(self.charisma))
        print("Constitution: " + str(self.constitution) +"\nRace: " + self.race + "\nClass: " + self.classChoice)

    def attack(self, targetEnemy, minDamage, maxDamage):
        """Attack with equipped weapon"""
        print("attacked " + targetEnemy.characterName + " for " + str(random.randint(minDamage, maxDamage)) + " " + self.equippedWeapon1.damageType + " damage!")

    def equipWeapon1(self, Weapon):
        """Equip weapon #1"""
        self.equippedWeapon1 = Weapon
        print(Weapon.name + " equipped")

    def equipWeapon2(self, Weapon):
        """Equip weapon #2"""
        self.equippedWeapon2 = Weapon
        print(Weapon.name + " equipped")

    def equipArmorTorso(self, Armor):
        """Equip Armor"""
        self.equippedArmorTorso = Armor
        print(Armor.name + " equipped")
        self.armorClass += Armor.armorClassModifier
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
        hitpoints = "Current HP=" + str(self.hp)
        return hitpoints

    def getMoney(self):
        money = "PP=" + str(self.pp) + ", GP=" + str(self.gp) + ", SP=" + str(self.sp) + ", CP=" + str(self.cp)
        return money
