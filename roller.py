import random
import re

# Take an input and remove all the spaces, then convert it entirely to
# lowercase. Then, make sure that the last char of the string is a number or
# letter.
def cleanse(input):
    input = (input.replace(" ","")).lower()
    if re.match('[0-9a-zA-Z]', input[len(input)-1]):
        return input
    else:
        return input[:-1]

# Take a basic dice format, such as 2d4, and output an array of integers equal
# to the rolls that result. 
def rollDice(dice):
    request = dice.split('d')
    n = int(request[0])
    sides = int(request[1])
    rolls = []
    for i in range(n):
        rolls.append(random.randint(1,sides))
    return rolls
    
# Take a list of dice rolls and the dice that generated those rolls and generate
# a pretty string
def parseDice(dice, rolls, bonus):
    rollStr = ' '.join((str(i) for i in rolls
    return ((str(sum(rolls)) + ' (' + dice + ')' + ': ' + rollStr))

def splitDice(unit):
    dice = re.search('[0-9]*d[0-9]*', unit)
    if dice:
        new = unit.split(dice.group())
        return new + [dice.group()]
    else:
        return []

def roller():
    go = True

    # Loop for rolling dice
    while go:
        input = raw_input("Roll condition: ")
        input = cleanse(input)

        if input == 'exit' or input == 'quit':
            go = False
            print("Quitting module.")
            break
        elif input.count('+') == 1:
            form = input.split('+')
            dice = form[0]
            bonus = int(cleanse(form[1]))
            verify = True
        elif input.count('-') == 1:
            form = input.split('-')
            dice = form[0]
            bonus = 0 - int(form[1].replace(" ",""))
            verify = True
        else:
            if input.count('-') > 1 or input.count('+') > 1:
                print("Error - format not recognized.")
                verify = False
                break
            else:
                verify = True
                dice = input
                bonus = 0

        rolls = rollDice(dice)
        if rolls == []:
            print("Error - format not recognized.")
            verify = False

        if verify:
            if bonus < 0:
                operator = " - "
            else:
                operator = " + "
            result = parseDice(dice, rolls)
            if bonus != 0:
                print result + operator + str(abs(bonus))
            else:
                print result
