from ogre import Ogre
from Fighter import fighter
from archer import archer
from mage import mage
from Champion import champion
from goblin1 import Goblin1
from goblin2 import Goblin2
from potion import Potion
from dragon import Dragon
from color import color
def select1():
    character_selection = input()
    name = input('\nwhat would you like to name your character? ')
    if character_selection == "1":
    # Player chose Fighter
        my_hero = fighter(name)
        print("You have chosen the class Fighter! Good luck on your adventure!")
    elif character_selection == "2":
    # player chose Mage.
        my_hero = mage(name)
        print("You have chosen the class Mage! Good luck on your adventure wizard!")
    elif character_selection == "3":
    # player chose Archer
        my_hero = archer(name)
        print("you have chosen the class Archer! Good luck on your adventure!")
    return my_hero
def decision1():
    decision1 = input()
    decision1 = decision1.upper()
    if decision1 == "YES":
            print("\nYou go towards the scream full sprint trying to see where the sound came from.")
            print("\n\nas you continue down the path you run across three goblins, one has a princess!")
            print('\n the goblin with the princess runs off and the other two goblins turn to fight you.. Prepare for a fight!')
    elif decision1 == "NO":
        print("\nyou're a coward and as you try the go the other way you feel a magical urge push you the way towards the scream.")

        print("\n\nas you continue down the path you run across three goblins, one has a princess!")
        print('\n the goblin with the princess runs off and the other two goblins turn to fight you.. Prepare for a fight!')
def fight1(goblin1, goblin2, my_hero, inventory):
    while goblin1.is_alive() or goblin2.is_alive() and my_hero.is_alive():
        my_hero.print_status()
        goblin1.print_status()
        goblin2.print_status()
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            my_hero.attack(goblin1)
            if goblin1.health > 0:
            # Goblin attacks hero
                goblin1.attack(my_hero)
        elif user_input == '2':
            #Hero attacks second goblin.
            my_hero.attack(goblin2)
            if goblin2.health > 0:
            #second goblin hit hero
                goblin2.attack(my_hero)
        elif user_input == "3":
            #hero uses a health potion.
            if inventory['potions']["health potions"] > 0:
                Potion.heals(my_hero)
                inventory["potions"]["health potions"] -=1
            print(inventory['potions'])
        elif user_input == "4":
            #hero does nothing besides take damage.
            pass
        elif user_input == "5":
            #run away little girl, run away.
            break
def fight2(ogre, my_hero, inventory):
    while ogre.is_alive() and my_hero.is_alive():
    
        my_hero.print_status()
        ogre.print_status()

        print()
        print(color.PURPLE + "What do you want to do?" + color.END)
        print("1." + color.RED + "attack Ogre" + color.END)
        print('2.' + color.GREEN + 'Drink a health potion' + color.END)
        print('3.' + color.BLUE + 'Run past the Ogre' + color.END)
        print('4.' + color.YELLOW +  'Run away little girl...Run away.' + color.END)

        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            my_hero.attack(ogre)
            if ogre.health > 0:
            # orge attacks hero
                ogre.attack(my_hero)
        elif user_input == '2':
        #hero uses a health potion.
            if inventory['potions']["health potions"] > 0:
                Potion.heals(my_hero)
                inventory["potions"]["health potions"] -=1
            print(inventory['potions'])
        elif user_input == '3':
            #hero tries to run past ogre to get inside
            if ogre.health > 0:
                # ogre attacks hero
                    ogre.attack(my_hero)
                    print("Ouch that hurt, lets not try that again.")
        elif user_input == '4':
            #hero Flees
            break
        print(ogre.health)
        if ogre.health <= 0:
            print("\n\nAfter your fierce fight with the Ogre you take the keys from his belt and free the princess")
            print("She goes to give you a reward All of the sudden the ground starts to shake and you see spikes emerge from the outskirts of the city.")
            print("You feel as the spikes are pulling you down and start to look around as you see Hell all around " + my_hero.name + "...What will happen next?")
            print((color.BOLD  + color.RED + '\n\nTO BE CONTINUED' + color.END))
def fight3(dragon, my_hero, inventory):
    while dragon.is_alive() and my_hero.is_alive():
                    my_hero.print_status()
                    dragon.print_status()
                    print()
                    print("What do you want to do?")
                    print("1." + color.RED + "attack dragon" + color.END)
                    print("2." + color.GREEN + 'Drink a health potion' + color.END)
                    print('4.' + color.YELLOW + 'Run away little girl...Run away.' + color.END)
                    user_input = input()
                    if user_input == "1":
                                # Hero attacks goblin
                                my_hero.attack(dragon)
                                if dragon.health > 0:
                                # orge attacks hero
                                    dragon.attack(my_hero)
                    elif user_input == '2':
                                    #hero uses a health potion.
                                        if inventory['potions']["health potions"] > 0:
                                            Potion.heals(my_hero)
                                            inventory["potions"]["health potions"] -=1
                                            print(inventory['potions'])
                    elif user_input == '3':
                                #hero tries to run past dragon to get inside
                                if dragon.health > 0:
                                    # dragon attacks hero
                                        dragon.attack(my_hero)
                                        print("Ouch that hurt, lets not try that again.")
                    elif user_input == '4':
                                #hero Flees
                                break
            
                    if dragon.health <= 0:
                        print("\n\nYou slay the dragon and save the princess....All of the sudden the ground starts to shake and you see spikes emerge from the outskirts of the city.")
                        print("You feel as the spikes are pulling you down and start to look around as you see Hell all around " + my_hero.name + " ... What will you do next?")
                        print((color.BOLD  + color.RED + '\n\nTO BE CONTINUED' + color.END))
def help1(my_hero, name,dragon,inventory,ogre): 
     Help1 = input()
     Help1 = Help1.upper()
     if Help1 == "YES":
        print("\nYou help the lady to her feet and help her up the road")
        print("\nupon getting to the end of the road,you feel stronger and more alive.")
        print(" Are level up's real??")
        my_hero.level_up()
        my_hero.print_status()
        fight2(ogre, my_hero, inventory)
        #added fight2 function and who they fight.
     elif Help1 == "NO":
        print("\nYou ignore the old lady because thats not your problem and continue on your way.")
        print("\nas you continue up the road you notice the clouds above turn black and turn around and the old lady is gone.")
        my_hero.level_up()
        my_hero.print_status()
        print("\nAs " + name  + " reaches the top of the road he see's a tower and the goblin throwing the princess in the tower and locking her inside.")
        print("As you get closer the goblin notices you and starts to laugh.. he seems to glow red and starts growing in size.")
        print("The Goblin now has turned into an Ogre!! ")
        fight3(dragon, my_hero, inventory)
        # added fight 3 function and who they do fight ^
def main():
    goblin1 = Goblin1()
    goblin2 = Goblin2()
    potion = Potion()
    ogre = Ogre()
    dragon = Dragon()
    inventory = {
        "weapons": ['Staff of magic', 'Holy Great Sword', 'Magic Long bow'],
        "potions": {"health potions": 3},
        "Currency": ['4 gold', '20 silver'] 
    }

    print("This is a simple a game, choose your character and go on an adventure!")

    list1 = ["Character 1: Fighter:" "25 health, 8 Power," "Character 2: Mage 17 Health, 10 power Character 3: Archer 17 Health, 10 Power "]
    print(list1)

    my_hero = select1()

    print("press I to access inventory now")
    bag = input()
    bag = bag.upper()
    print(inventory['weapons'])
    print(inventory['potions'])
    print(inventory['Currency'])

    print("\n\n\nNow " + my_hero.name +  " sets out on their adventure..  " + my_hero.name +  " walks until the see a fork in the road")
    print("..while pondering their decision " + my_hero.name + " hears a woman scream out in the distance!")

    print("\n Go towards the scream or go to opposite way? Yes or No. ")

    decision1()
    print()
    print(color.PURPLE + "What do you want to do?" + color.END)
    print("1." + color.RED + "attack first goblin" + color.END)
    print("2." + color.RED + "attack second goblin" + color.END)
    print("3." + color.GREEN + "Use a potion" + color.END)
    print("4." + color.BLUE+ "Do nothing" + color.END)
    print("5." + color.YELLOW + "Flee" + color.END)
    fight1(goblin1,goblin2,my_hero,inventory)

    print("\n\nYou destoy the two goblins with ease and look around for the third goblin.")
    print("\nYou continue up the road searching around and come across and old lady who seems to be struggling")
    print("\nDo you help the old lady? Yes or No?")
    help1(my_hero, my_hero.name, dragon,inventory,ogre)
    help1(my_hero, my_hero.name, dragon,inventory,ogre)
main()