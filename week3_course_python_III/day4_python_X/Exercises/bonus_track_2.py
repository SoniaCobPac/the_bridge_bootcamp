"""
Make a program using while that generates a deck of cards of 4 different suits. The deck must have 40 cards.

Develop the program in a .py file that will be run through the terminal.

Then, import the module to this notebook and show the deck you've generated below.
"""

cards = 1
while cards <= 1:
    tipos = ["picas", "corazones", "rombos", "treboles"]
    for i in list(range(1,11)):
        output = (list(map(lambda x: f"{i} de {x}", tipos)))
        print(output)
    cards +=1