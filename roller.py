import random
import re

# Take an input and remove all the spaces, then convert it entirely to
# lowercase. Then, make sure that the last char of the string is a number or
# letter.

def cleanse(input):
    input = (input.replace(" ","")).lower()
    if re.match('[0-9a-zA-Z]', input[len(input)-1]):
        return input

class Roller(object):
    # Take a basic dice format, such as 2d4, and output an array of integers equal
    # to the rolls that result.
    def rollDice(self, dice):
        request = dice.split('d')
        n = int(request[0])
        sides = int(request[1])
        rolls = []
        for i in range(n):
            rolls.append(random.randint(1,sides))
        return rolls

    # Take a list of dice rolls and the dice that generated those rolls and generate
    # a pretty string
    def parseDice(self, dice, rolls, bonus):
        rollStr = ' '.join(str(i) for i in rolls)
        return(str(sum(rolls) + bonus) + ' (' + dice + '+' + str(bonus) + '): ' + rollStr)


    def splitDice(self, unit):
        dice = re.search('[0-9]*d[0-9]*', unit)
        if dice:
            new = unit.split(dice.group())
            return new + [dice.group()]
        else:
            return []

    def module(self):
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
                if 'd' in form[0]:
                    dice = form[0]
                    bonus = int(form[1])
                else:
                    dice = form[1]
                    bonus = int(form[0])
                verify = True
            elif input.count('-') == 1:
                form = input.split('-')
                if 'd' in form[0]:
                    dice = form[0]
                    bonus = 0 - int(form[1].replace(" ",""))
                else:
                    dice = form[1]
                    bonus = 0 - int(form[0].replace(" ",""))
                verify = True
            else:
                if input.count('-') + input.count('+') > 1:
                    print("Error - format not recognized.")
                    verify = False
                    break
                else:
                    verify = True
                    dice = input
                    bonus = 0

            rolls = self.rollDice(dice)
            if rolls == []:
                print("Error - format not recognized.")
                verify = False

            if verify:
                if bonus < 0:
                    operator = " - "
                else:
                    operator = " + "
                result = self.parseDice(dice, rolls, bonus)
                if bonus != 0:
                    print result + operator + str(abs(bonus))
                else:
                    print result
