"""This is my awesome utility kitchen sink. Don't judge me."""

import colors as c

def ask(question,color=c.green):
    print(color + question + c.reset)
    answer = input(c.yellow + "> " + c.cyan)
    print(c.reset)
    return answer

if __name__ == '__main__':
    print(c.clear)
    name = ask("What is your name?")
    color = ask("What is your name in color?",c.random_color())
