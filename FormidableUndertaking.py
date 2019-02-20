# Testing object oriented classes in a game setup

import Character as c
import Weapons as wp
import Armor as arm
from Character import Monster as mnstr
import _pickle as cpickle
from WeaponInstances import *
from ArmorInstances import *
from ItemInstances import *

# LOAD CHARACTER SAVED FROM CHARACTER GENERATOR OR SAVE FILE
loadName = input("What character would you like to load? ")
with open(loadName + '.dat', 'rb') as f:
    pc = cpickle.load(f)

# pc = c.Character("Nin",8,8,8,8,8,8,"Fighter","Human","Male")
npc = c.Character("Jeffery",8,8,8,8,8,8,"Bard","Elven","Male")

pc.__repr__()
pc.__str__()
targetEnemy = npc

pc.equipWeaponRight(axe)
pc.equipWeaponLeft(knife)
pc.equipArmorTorso(breastplate)

npc.equipArmorTorso(breastplate)
npc.equipArmorArms(elbowpads)
npc.equipArmorHead(helmet)
npc.equipArmorLegs(leggings)
npc.equipArmorWrists(gauntlets)
npc.unequipArmorTorso(breastplate)

npc.addHP(50)
pc.attack(npc,pc.equippedWeaponRight.minDamage, pc.equippedWeaponRight.maxDamage, pc.equippedWeaponRight.damageType, pc.equippedWeaponRight.unblockableDamage)
print(npc.getHp())

pc.attack(npc,pc.equippedWeaponLeft.minDamage, pc.equippedWeaponLeft.maxDamage, pc.equippedWeaponLeft.damageType, pc.equippedWeaponLeft.unblockableDamage)
print(npc.getHp())

pc.attack(npc,pc.equippedWeaponRight.minDamage, pc.equippedWeaponRight.maxDamage, pc.equippedWeaponRight.damageType, pc.equippedWeaponRight.unblockableDamage)
print(npc.getHp())

pc.attack(npc,pc.equippedWeaponLeft.minDamage, pc.equippedWeaponLeft.maxDamage, pc.equippedWeaponLeft.damageType, pc.equippedWeaponLeft.unblockableDamage)
print(npc.getHp())


pc.addHP(5)
print(pc.getHp())
print(pc.getMoney())
pc.addGP(100)
print(pc.getMoney())

pc.addXP(16100)
pc.levelUp(pc.checkLevels(pc.classChoice))
print(pc.getWeaponTypeRight() + " is current weapon type")