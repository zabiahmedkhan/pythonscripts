import random

def intornot(x):
    #print type(x)
    if type(x) is int:
        #print type(x)
        guess_no()
    else:
        print "enter a valid integer"

def guess_no():
    rand=random.randint(1,100)
    print rand
    if user_in==rand:
        print "you guessed it right"
    else:
        if user_in > rand:
            print "you guessed it high"
        else:
            print "you guess it less"

user_in=input("guess a number from 1 to 100")
intornot(user_in)
