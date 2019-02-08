# Testing object oriented classes in a game setup

import Character as c
import Weapons as wp
import Armor as arm
import Monsters as mon

# LOAD CHARACTER SAVED FROM CHARACTER GENERATOR OR SAVE FILE
pc = c.Character("Nin",8,8,8,8,8,8,"Fighter","Human","Male")
npc = c.Character("Jeffery",8,8,8,8,8,8,"Bard","Elven","Male")

pc.__repr__()
pc.__str__()
targetEnemy = npc

longsword = wp.Weapon("longsword", 1, 80, "slashing", 5)
knife = wp.Weapon("knife", 1, 60, "piercing", 1)

breastplate = arm.Armor("breastplate", 20, "torso")
helmet = arm.Armor("helmet", 5, "head")
gauntlets = arm.Armor("gauntlets", 10, "wrists")
leggings = arm.Armor("leggings", 2, "legs")
elbowpads = arm.Armor("elbowpads", 2, "arms")


pc.equipWeaponRight(longsword)
pc.equipWeaponLeft(knife)
pc.equipArmorTorso(breastplate)

npc.equipArmorTorso(breastplate)
npc.equipArmorArms(elbowpads)
npc.equipArmorHead(helmet)
npc.equipArmorLegs(leggings)
npc.equipArmorWrists(gauntlets)

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
