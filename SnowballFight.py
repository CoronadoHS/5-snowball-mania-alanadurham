''' 
    Name: Snowball-Mania
    Author: Alana Durham
    Date: 12-3-24
    Class: AP Computer Science Principles
    Python: 3.11.5
'''

import random
import time

def main():
    # the main runner of the game
	# welcome the player, gather names, and run the snowball fight!
    print("Welcome to Snowball Mania!")
    name = input("State your name. ")
    opposition = input("Your presence is a pleasure, " + name + "! Who will you fight? ")
    print(name + " vs. " + opposition)
    
    # number of kills per player
    killcount = []
    killcount.append(0)
    killcount.append(0)
    
    players = []
    players.append(name)
    players.append(opposition)
    
    nextPlayer = ""

    while (nextPlayer != "DONE"):
        nextPlayer = input("Is that all the players? Type one at a time, or DONE if not. Then, press 'Enter'. ")
        players.append(nextPlayer)
        killcount.append(0)
    players.remove("DONE")
    del killcount[0]
    

    choice = input("Will you choose who gets hit, or let us decide for you? Type 'yes' or 'no'. ")
    print(killcount)
    gameplay(name, players, killcount, choice)



def gameplay(name, players, killcount, manual):
    # randomly choose one person to throw the snowball
    while (len(players) > 1):
        thrower = random.choice(players)
        if (thrower == name):
            if (manual == "yes"):   # manual mode
                target = input("Your turn, who will you hit? ")
            else:       # auto mode
                #print(thrower)
                target = random.choice(players)
                while (target == thrower):
                    target = random.choice(players)
        else:       # thrower is not the user, picking randomly
                #print(thrower)
                target = random.choice(players)
                while (target == thrower):
                    target = random.choice(players)
        #print(target)
        print(thrower + " threw the snowball at " + target + "!")
        time.sleep(1)
        # generate a random number to use as hitNum
        hitNum = random.randint(1, 5)
        success = hitResult(hitNum)
        if (success == True):
            print("It hits " + target + ", they're down!")
            # +1 elimination
            score = players.index(thrower)
            loser = players.index(target)
            killcount[score] += 1
            del killcount[loser]
            players.remove(target)
        else:
            print("It misses " + target + ", they live another day...")
        time.sleep(1)
    if (killcount[0] > 1):
        print(players[0] + " wins the battle with " + str(killcount[0]) + " wins!")
    else:
        print(players[0] + " wins the battle with " + str(killcount[0]) + " win!")



def hitResult(hitNum):
    # based on the number that is passed in, return True or False 
    # indicating if this was a hit or a miss
    if (hitNum == 3): #1 in 5 chance, 3 magic number
        return True
    return False

main()
