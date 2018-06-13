# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
q= "yes"
y=1
import random
random_num = random.randint(1, 10)
input = int(raw_input("Pick a number between 1 and 9 or type 00 to end the game"))
#start
while input != 00 and int(y) <= 7 and q != "No":
    if input > random_num:
        print "That number is too high!"
    else:
        print "That number is too low!"
    y = y + 1
    input = int(raw_input("Guess again, or type 00 to end/stop."))
    if input == random_num:
        print "That number is correct!"
        q = raw_input("Do you want to play again?")
        q = q[0].upper() + q[1:].lower()
        if q == "Yes":
            "okay"
            y=(y-y)+1
        else:
            print "Good Bye."

