"""Theese ees muy ameezing queez meedule"""

import colors as c
import time as t
from utils import ask

intro = c.magenta + '''
Welcome to the Pink Fluffy Unicorns Quiz!
♫ Pink Fluffy Unicorns ancing on rainbows... ♫
Let's test your knowledge to see what you've learned so far.
''' + c.reset
t.sleep(2)


def q1():
    color = ask("What color are the unicorns?")
    if color == 'pink':
        return True
    return False

def q2():
    place = ask("Where are they dancing?")
    if 'rainbows' in place:
        return True
    return False

def q3():
    word = ask("Please use one word to describe the texture of their meegical fur.")
    if word == 'smiles':
        return True
    return False

questions = [q1,q2,q3]


    
