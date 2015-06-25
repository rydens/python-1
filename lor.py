"""This is my Lord of the Rings Quiz. I happen to be listening to music from it as I write this."""

import colors as c
from utils import ask

intro = c.green + '''
Welcome to Ryan's Lord of the Rings Quiz.
There are many questions on many things.
Note: All answers should have a cap at the beggining of each word, 
exept for things like: "the", "of" unless they are at the beggining
of the answer.
Other Note: LOTR stands for "Lord of the Rings".
Good Luck!''' + c.reset

def q1():
    author = ask('Who wrote the Lord of the Rings Books?')
    if author == 'J. R. R. Tolkein':
        return True
    return False

def q2():
    mc = ask('Who was the main character?')
    if mc == 'Frodo Baggins':
        return True
    return False

def q3():
    prebook = ask('What is the name of the prequel book(before the LOTR series)?')
    if prebook == 'The Hobbit':
        return True
    return False

def q4():
    book1 = ask('What is the name of the first book of the LOTR series?')
    if book1 == 'The Fellowship of the Ring':
        return True
    return False

def q5():
    book2 = ask('What is the name of the second book of the LOTR series?')
    if book2 == 'The Two Towers':
        return True
    return False

def q6():
    book3 = ask('What is the name of the third book of the LOTR series?')
    if book3 == 'The Return of the King':
        return True
    return False
