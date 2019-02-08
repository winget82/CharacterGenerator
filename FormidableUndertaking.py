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

longsword = wp.Weapon("longsword", 50, 100, "slashing")

breastplate = arm.Armor("breastplate", 5)

pc.equipWeapon1(longsword)
pc.equipArmorTorso(breastplate)
pc.attack(npc,pc.equippedWeapon1.minDamage, pc.equippedWeapon1.maxDamage)
pc.attack(npc,pc.equippedWeapon1.minDamage, pc.equippedWeapon1.maxDamage)
pc.attack(npc,pc.equippedWeapon1.minDamage, pc.equippedWeapon1.maxDamage)
pc.attack(npc,pc.equippedWeapon1.minDamage, pc.equippedWeapon1.maxDamage)
pc.addHP(5)
print(pc.getHp())
print(pc.getMoney())
pc.addGP(100)
print(pc.getMoney())