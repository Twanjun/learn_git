# -*-coding:UTF-8 -*-

from sys import exit

def forest_room():
    print "you are coming in the forest_room with some animals,can you know them, look, what's that are eating the banana?"
    print "Is that lion? tiger? or monkey?"
	
    next = raw_input(">")
	
    if "monkey" in next:
        print "you are right,you are win three games, so, you win."
        exit()
    else:
        dead("false, you fail.")

def dead(why):
    print why,"good job!"

def fire_room():
    print "you are coming in the fire_room,please choose a tool to put up the fire and help yourself."
    print "do you want a pool of water or a fire extinguisher"
	
    next = raw_input(">")
	
    if "fire extinguisher" in next:
        exit("you help yourself, you are win three games, so, you go through it.")
    else:
        print "choose a pool of water is foolish,you can't help yourself!"
        print "but a good man help you, so, you are live."
        print "go on."
        forest_room()

def skating_room():
    print "you are coming a funny room.let's play a staking game, choose a rival."
    print "a monkey? a canadian? or a chiness?"

    next = raw_input(">")
    
    if "monkey" in next:
        print "you are smart,you win the monkey. you go thtrough it."
        fire_room()
    elif "canadian" in next:
        exit("your rival is wonderful,so, you fail!")
    else:
        print "oh, grudge match,let's play again."
        skating_room()

def dragon_room():
    print "welcome to the adventure game, if you go through three games ,you win!"
    print "this is dragon_room,i want you theft the dragon egg for me."
    print "but that is dangeragu, please choose the time you do it,that decide your life."
    print "morning? afternoon? or evening?"

    next = raw_input(">")

    if "morning" in next:
        print "congratulation, you get a egg, you go through it."
        skating_room()
    else:
        dead("you are discoveried by the mother of dragon, you are die!")

dragon_room()