import random

def roll_dice():
    print random.randint(1,6)
    #print random.randint(1,6)
    counter=2
    while (counter > 0):
        x=raw_input("do you want to roll the dice again? say 'y' or 'n'")
        if x=='y':
            print random.randint(1,6)
        else:
            print "goodbye"
            break
        counter=counter-1


print "FYI I can roll the dice only 3 times"
print "let's roll the dice"
roll_dice()
