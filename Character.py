# File for Character Class

import random

#SEE THIS FOR UPDATES THAT MAY NEED MADE TO THIS CLASS TO KEEP FROM PASSING THROUGH WALLS
#https://github.com/justinmeister/PyTMX-Examples/blob/master/Make%20Collideable%20Rects/main.py

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
        self.equippedArmorFeet = None
        self.inventory = []
        self.description = ""
        self.background = ""
        self.gp = 0
        self.sp = 0
        self.pp = 0
        self.cp = 0
        self.level = 1
        self.hp = 0
        self.mp = 0
        self.experiencePoints = 0
        self.alive = True

    def __repr__(self):
        print("Character, " + self.name + ".  Class, " + self.classChoice)

    def __str__(self):
        print(self.name + "\nSex: " + self.sex + "\nStrength: " + str(self.strength) + "\nDexterity: " + str(self.dexterity))
        print("Wisdom: " + str(self.wisdom) + "\nIntelligence: " + str(self.intelligence) + "\nCharisma: " + str(self.charisma))
        print("Constitution: " + str(self.constitution) +"\nRace: " + self.race + "\nClass: " + self.classChoice)

    def attack(self, targetEnemy, minDamage, maxDamage, damageType, unblockableDamage):
        """Attack with equipped weapon"""
        if targetEnemy.alive == True:

            potDamage = random.randint(minDamage, maxDamage)

            if potDamage > 0:
                if potDamage > targetEnemy.armorClass:
                    damageDealt = potDamage - targetEnemy.armorClass
                    targetEnemy.deadOrAlive()
                else:
                    damageDealt = unblockableDamage
                    targetEnemy.deadOrAlive()

            else:
                damageDealt = unblockableDamage
                targetEnemy.deadOrAlive()

            print(self.name + " attacked " + targetEnemy.name + " for " + str(damageDealt) + " " + damageType + " damage!")
            targetEnemy.hp -= damageDealt
            if targetEnemy.hp < 0:
                targetEnemy.hp = 0
                targetEnemy.deadOrAlive()

        else:
            print(targetEnemy.name + " is already dead.")

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

    def equipArmorFeet(self, Armor):
        """Equip Armor to Feet"""
        self.equippedArmorFeet = Armor
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

    def unequipArmorFeet(self, Armor):
        """Unequip Armor from Feet"""
        self.armorClass -= Armor.armorClassModifier
        print(Armor.name + " unequipped")
        self.equipArmorFeet(None)
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

    def checkLevels(self, characterClass):
        if characterClass.upper() == "FIGHTER":
            lvlXP = {1000:2, 3000:3, 6000:4, 10000:5, 15000:6, 21000:7}
        elif characterClass.upper() == "CLERIC":
            lvlXP = {1000:2, 4000:3, 8000:4, 13000:5, 19000:6, 26000:7}
        elif characterClass.upper() == "ROGUE":
            lvlXP = {1000:2, 3000:3, 5000:4, 9000:5, 14000:6, 20000:7}
        elif characterClass.upper() == "WIZARD":
            lvlXP = {1000:2, 3000:3, 7000:4, 12500:5, 19500:6, 27000:7}
        elif characterClass.upper() == "BARD":
            lvlXP = {1000:2, 3000:3, 6000:4, 10000:5, 15000:6, 21000:7}

        return lvlXP

    def levelUp(self, lvlXP):
        for i in lvlXP:
            if self.experiencePoints > i:
                self.level = lvlXP[i]
        print(self.name + " is now level " + str(self.level))

    def deadOrAlive(self):
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
            print(self.name + " has died...")

    def addItemToInventory(self, item):
        """Add and Item to Inventory"""
        self.inventory.append(item)
        print(item.name + " was added to inventory")

    def useItem(self, item):
        """Use an Item from Inventory"""
        print("Used " + item.name)
        self.inventory.remove(item)

    def pickUpItem(self, item):
        pickup = input("Would you like to pick up " + item.name + " ? (Y/N)")
        if pickup.upper() == 'Y':
            self.addItemToInventory(item)
        else:
            pass

# MAKE MONSTERS A CHILD CLASS OF CHARACTER CLASS, SINCE CHARACTERS CAN BE ENEMIES ALSO
class Monster(Character):

    def __init__(self, name, strength, dexterity, wisdom, intelligence, charisma, constitution, classChoice, raceChoice, sex):
        Character.__init__(self, name, strength, dexterity, wisdom, intelligence, charisma, constitution, classChoice, raceChoice, sex)
        self.item = None
