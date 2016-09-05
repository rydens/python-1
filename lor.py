"""This is my Lord of the Rings Quiz. I happen to be listening to music from it as I write this."""

import colors as c
from utils import ask

def right():
    print(c.magenta + 'You are correct! :D' + c.reset)

def wrong():
    print(c.blue + 'Nope, sorry. :(' + c.reset)

intro = c.green + '''
Welcome to Ryan's Lord of the Rings Quiz.
There are many questions on many things. Sort of.''' + c.red + '''
Note: All answers should have a cap at the begining of each word, 
exept for things like: "the", "of" unless they are at the begining
of the answer.
Other Note: LOTR stands for "Lord of the Rings". Also, you can 
type 'exit' at any time to cleanly exit the program.''' + c.green + '''
Good Luck!
''' + c.reset

score = 0
def add1(x):
    return x + 1

def q1():
    author = ask('Who wrote the Lord of the Rings Books?')
    if author == 'J. R. R. Tolkein':
        right()
        global score
        score = add1(score)
        return True
    elif author == 'exit':
        exit()
    else:
        wrong()
        return False

def q2():
    mc = ask('Who was the main character?')
    if mc == 'Frodo Baggins':
        right()
        global score
        score = add1(score)
        return True
    elif mc == 'exit':
        exit()
    else:
        wrong()
        return False

def q3():
    prebook = ask('What is the name of the prequel book(before the LOTR series)?')
    if prebook == 'The Hobbit':
        right()
        global score
        score = add1(score)
        return True
    elif prebook == 'exit':
        exit()
    else:
        wrong()
        return False

def q4():
    book1 = ask('What is the name of the first book of the LOTR series?')
    if book1 == 'The Fellowship of the Ring':
        right()
        global score
        score = add1(score)
        return True
    elif book1 == 'exit':
        exit()
    else:
        wrong()
        return False

def q5():
    book2 = ask('What is the name of the second book of the LOTR series?')
    if book2 == 'The Two Towers':
        right()
        global score
        score = add1(score)
        return True
    elif book2 == 'exit':
        exit()
    else:
        wrong()
        return False

def q6():
    book3 = ask('What is the name of the third book of the LOTR series?')
    if book3 == 'The Return of the King':
        right()
        global score
        score = add1(score)
        return True
    elif book3 == 'exit':
        exit()
    else:
        wrong()
        return False

questions = [q1,q2,q3,q4,q5,q6]
