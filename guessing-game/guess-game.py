#Guessing Game v0.0
#Simple guessing game using Python.

#Learning Python programming through accelerated learning
#principles. This is one of the projects I chose to do.
#Will eventually look to upgrade.
#Please note, there will be alot of commentaries - for myself.

import random
import sys
#loading "random" module (aka library)
#loading "sys" module

hidden = random.randrange(1,6)
print(hidden)
#a line for debugging purposes, delete hash
#hidden is a variable
#random.randrange is a function

guess = int(input("Guess the number from 1 -6? "))
#guess is a variable
#int is a function that converts an integer to a string

if guess == hidden:
	print("You got me!")
	sys.exit()
elif guess < hidden:
	print("A little higher....")

else:
	print("A little lower.....")
