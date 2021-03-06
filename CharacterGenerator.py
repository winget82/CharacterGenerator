# A SIMPLE RPG CHARACTER GENERATOR

import random
import Character as c
import _pickle as cpickle

def d4():
    return random.randint(1,4)

def d6():
    return random.randint(1,6)

def d8():
    return random.randint(1,8)

def d10():
    return random.randint(1,10)

def d12():
    return random.randint(1,12)

def d20():
    return random.randint(1,20)

def d100():
    return random.randint(1,100)

def statsRoll():
    stats = {}
    dice1 = d6() + d6() + d6()
    dice2 = d6() + d6() + d6()
    dice3 = d6() + d6() + d6()
    dice4 = d6() + d6() + d6()
    dice5 = d6() + d6() + d6()
    dice6 = d6() + d6() + d6()
    stats.update({'dice1':dice1})
    stats.update({'dice2':dice2})
    stats.update({'dice3':dice3})
    stats.update({'dice4':dice4})
    stats.update({'dice5':dice5})
    stats.update({'dice6':dice6})
    print("Your roll:")
    print('dice1 = ' + str(stats.get('dice1')))
    print('dice2 = ' + str(stats.get('dice2')))
    print('dice3 = ' + str(stats.get('dice3')))
    print('dice4 = ' + str(stats.get('dice4')))
    print('dice5 = ' + str(stats.get('dice5')))
    print('dice6 = ' + str(stats.get('dice6')))
    return stats

stats = statsRoll()

#STAT ROLL KEEP/REROLL
reroll = 'CHOOSE'
while reroll == 'CHOOSE' or reroll.upper() == 'R':
    reroll = input('Would you like to (K)eep stats or (R)eroll? ')
    if reroll.upper() == 'K':
        print('Stats saved.')
    elif reroll.upper() == 'R':
        stats = statsRoll()
    else:
        reroll.upper() == 'CHOOSE'

# ASSIGN ROLLS TO STATS STRENGTH, DEXTERITY, WISDOM, INTELLIGENCE, CHARISMA, CONSTITUTION
# Need to update to only be able to use each value once...
# Will need to set up some while loops or something to show options left available
# and to limit available choices

sixDice = ['DICE1', 'DICE2', 'DICE3', 'DICE4', 'DICE5', 'DICE6']

# Make a function to do the repetitious process for each stat below:
strength = input('Which dice would you like to assign to Strength? ')
if strength.upper() == 'DICE1' and 'DICE1' in sixDice:
    strength = stats.get('dice1')
    sixDice.remove('DICE1')
elif strength.upper() == 'DICE2' and 'DICE2' in sixDice:
    strength = stats.get('dice2')
    sixDice.remove('DICE2')
elif strength.upper() == 'DICE3' and 'DICE3' in sixDice:
    strength = stats.get('dice3')
    sixDice.remove('DICE3')
elif strength.upper() == 'DICE4' and 'DICE4' in sixDice:
    strength = stats.get('dice4')
    sixDice.remove('DICE4')
elif strength.upper() == 'DICE5' and 'DICE5' in sixDice:
    strength = stats.get('dice5')
    sixDice.remove('DICE5')
elif strength.upper() == 'DICE6' and 'DICE6' in sixDice:
    strength = stats.get('dice6')
    sixDice.remove('DICE6')

dexterity = input('Which dice would you like to assign to Dexterity? ')
if dexterity.upper() == 'DICE1' and 'DICE1' in sixDice:
    dexterity = stats.get('dice1')
    sixDice.remove('DICE1')
elif dexterity.upper() == 'DICE2' and 'DICE2' in sixDice:
    dexterity = stats.get('dice2')
    sixDice.remove('DICE2')
elif dexterity.upper() == 'DICE3' and 'DICE3' in sixDice:
    dexterity = stats.get('dice3')
    sixDice.remove('DICE3')
elif dexterity.upper() == 'DICE4' and 'DICE4' in sixDice:
    dexterity = stats.get('dice4')
    sixDice.remove('DICE4')
elif dexterity.upper() == 'DICE5' and 'DICE5' in sixDice:
    dexterity = stats.get('dice5')
    sixDice.remove('DICE5')
elif dexterity.upper() == 'DICE6' and 'DICE6' in sixDice:
    dexterity = stats.get('dice6')
    sixDice.remove('DICE6')

wisdom = input('Which dice would you like to assign to Wisdom? ')
if wisdom.upper() == 'DICE1' and 'DICE1' in sixDice:
    wisdom = stats.get('dice1')
    sixDice.remove('DICE1')
elif wisdom.upper() == 'DICE2' and 'DICE2' in sixDice:
    wisdom = stats.get('dice2')
    sixDice.remove('DICE2')
elif wisdom.upper() == 'DICE3' and 'DICE3' in sixDice:
    wisdom = stats.get('dice3')
    sixDice.remove('DICE3')
elif wisdom.upper() == 'DICE4' and 'DICE4' in sixDice:
    wisdom = stats.get('dice4')
    sixDice.remove('DICE4')
elif wisdom.upper() == 'DICE5' and 'DICE5' in sixDice:
    wisdom = stats.get('dice5')
    sixDice.remove('DICE5')
elif wisdom.upper() == 'DICE6' and 'DICE6' in sixDice:
    wisdom = stats.get('dice6')
    sixDice.remove('DICE6')

intelligence = input('Which dice would you like to assign to Intelligence? ')
if intelligence.upper() == 'DICE1' and 'DICE1' in sixDice:
    intelligence = stats.get('dice1')
    sixDice.remove('DICE1')
elif intelligence.upper() == 'DICE2' and 'DICE2' in sixDice:
    intelligence = stats.get('dice2')
    sixDice.remove('DICE2')
elif intelligence.upper() == 'DICE3' and 'DICE3' in sixDice:
    intelligence = stats.get('dice3')
    sixDice.remove('DICE3')
elif intelligence.upper() == 'DICE4' and 'DICE4' in sixDice:
    intelligence = stats.get('dice4')
    sixDice.remove('DICE4')
elif intelligence.upper() == 'DICE5' and 'DICE5' in sixDice:
    intelligence = stats.get('dice5')
    sixDice.remove('DICE5')
elif intelligence.upper() == 'DICE6' and 'DICE6' in sixDice:
    intelligence = stats.get('dice6')
    sixDice.remove('DICE6')

charisma = input('Which dice would you like to assign to Charisma? ')
if charisma.upper() == 'DICE1' and 'DICE1' in sixDice:
    charisma = stats.get('dice1')
    sixDice.remove('DICE1')
elif charisma.upper() == 'DICE2' and 'DICE2' in sixDice:
    charisma = stats.get('dice2')
    sixDice.remove('DICE2')
elif charisma.upper() == 'DICE3' and 'DICE3' in sixDice:
    charisma = stats.get('dice3')
    sixDice.remove('DICE3')
elif charisma.upper() == 'DICE4' and 'DICE4' in sixDice:
    charisma = stats.get('dice4')
    sixDice.remove('DICE4')
elif charisma.upper() == 'DICE5' and 'DICE5' in sixDice:
    charisma = stats.get('dice5')
    sixDice.remove('DICE5')
elif charisma.upper() == 'DICE6' and 'DICE6' in sixDice:
    charisma = stats.get('dice6')
    sixDice.remove('DICE6')

constitution = input('Which dice would you like to assign to Constitution? ')
if constitution.upper() == 'DICE1' and 'DICE1' in sixDice:
    constitution = stats.get('dice1')
    sixDice.remove('DICE1')
elif constitution.upper() == 'DICE2' and 'DICE2' in sixDice:
    constitution = stats.get('dice2')
    sixDice.remove('DICE2')
elif constitution.upper() == 'DICE3' and 'DICE3' in sixDice:
    constitution = stats.get('dice3')
    sixDice.remove('DICE3')
elif constitution.upper() == 'DICE4' and 'DICE4' in sixDice:
    constitution = stats.get('dice4')
    sixDice.remove('DICE4')
elif constitution.upper() == 'DICE5' and 'DICE5' in sixDice:
    constitution = stats.get('dice5')
    sixDice.remove('DICE5')
elif constitution.upper() == 'DICE6' and 'DICE6' in sixDice:
    constitution = stats.get('dice6')
    sixDice.remove('DICE6')


# CHOOSE CHARACTER CLASS - ADD STAT REQUIREMENTS TO MAKE CHOICE VALID / INVALID
def getClass():
    classChoice = 'INVALID'
    while classChoice == 'INVALID':
        choice = str(input('Please choose your class:\n(1)Fighter\n(2)Cleric\n(3)Rogue\n(4)Wizard\n(5)Bard\n'))
        if choice == '1':
            classChoice = 'Fighter'
        elif choice == '2':
            classChoice = 'Cleric'
        elif choice == '3':
            classChoice = 'Rogue'
        elif choice == '4':
            classChoice = 'Wizard'
        elif choice == '5':
            classChoice = 'Bard'
        else:
            classChoice = 'INVALID'
            print('Your choice is INVALID. Please choose again.')

    return str(classChoice)


classChoice = getClass()
print('you chose the ' + classChoice + ' class.')


# ROLL HP DEPENDING ON CLASS




# CHOOSE CHARACTER RACE
def getRace():
    raceChoice = 'INVALID'
    while raceChoice == 'INVALID':
        choice = str(input('Please choose your race:\n(1)Human\n(2)Dwarven\n(3)Elven\n(4)Halfling\n(5)Dragonborn\n'))
        if choice == '1':
            raceChoice = 'Human'
        elif choice == '2':
            raceChoice = 'Dwarven'
        elif choice == '3':
            raceChoice = 'Elven'
        elif choice == '4':
            raceChoice = 'Halfling'
        elif choice == '5':
            raceChoice = 'Dragonborn'
        else:
            raceChoice = 'INVALID'
            print('Your choice is INVALID. Please choose again.')

    return str(raceChoice)

raceChoice = getRace()
print('you chose the ' + raceChoice + ' race.')


# CHOOSE YOUR SEX
sex = ""
while sex.upper() != "MALE" and sex.upper() != "FEMALE" and sex.upper() != "M" and sex.upper() != "F":
    sex = input("Male or Female? ")

# NAME YOUR CHARACTER
name = input('What would you like to name your character? ')

exportedCharacter = c.Character(name, strength, dexterity, wisdom, intelligence, charisma, constitution, classChoice, raceChoice, sex)

# saving
with open(exportedCharacter.name + '.dat', 'wb') as f:
    cpickle.dump(exportedCharacter, f, protocol=2)
