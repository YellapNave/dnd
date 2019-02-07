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
        rolls = []
        if len(dice[0]) > 0:
            for roll in dice[0]:
                request = roll.split('d')
                n = int(request[0])
                sides = int(request[1])
                for i in range(n):
                    rolls.append(random.randint(1,sides))
        if len(dice[1]) > 0:
            for roll in dice[1]:
                request = roll.split('d')
                n = int(request[0])
                sides = int(request[1])
                for i in range(n):
                    rolls.append(random.randint(1,sides) * -1)
        return rolls

    # Take a list of dice rolls and the dice that generated those rolls and
    # generate a pretty string
    def parseDice(self, dice, rolls, bonus):
        if bonus == 0:
            op = ''
            strBonus = ''
        elif bonus >= 1:
            op = '+'
            strBonus = str(bonus)
        else:
            op = '-'
            strBonus = str(abs(bonus))
        rollStr = ' '.join(str(i) for i in rolls) + " %s %s" % (op, strBonus)
        posDice = '+'.join(dice[0])
        if len(dice[1]) > 0:
            negDice = "-" + '-'.join(dice[1])
        else:
            negDice = ''
        return(str(sum(rolls) + bonus) + ' (' + posDice + negDice + op + strBonus + '): ' + rollStr)

    # Take multiple dice rolls and return them each as a string in a list, so that
    # '1d10 + 2d6' gives [[1d10, 2d6],[]] and '1d10 + 2d12 - 1d6' gives [[1d10, 2d12],[1d6]]
    def multiples(self, input):
        res = [[],[]] # res[0] = boons, res[1] = banes
        pos = input.split('+')
        for i in pos:
            temp = i.split('-')
            if len(temp) > 1:
                for j in temp:
                    if j == temp[0]:
                        res[0].append(j)
                    else:
                        res[1].append(j)
            else:
                res[0] += temp
        return res


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
            dice = [[],[]]

            if input == 'exit' or input == 'quit':
                go = False
                print("Quitting module.")
                break
            elif input.count('d') > 1:
                dice = self.multiples(input)
                bonus = 0
                verify = True
            elif input.count('+') == 1:
                form = input.split('+')
                if 'd' in form[0]:
                    dice[0].append(form[0])
                    bonus = int(form[1])
                else:
                    dice[0].append(form[1])
                    bonus = int(form[0])
                verify = True
            elif input.count('-') == 1:
                form = input.split('-')
                if 'd' in form[0]:
                    dice[0].append(form[0])
                    bonus = 0 - int(form[1].replace(" ",""))
                else:
                    dice[1].append(form[1])
                    bonus = int(form[0].replace(" ",""))
                verify = True
            else:
                if input.count('-') + input.count('+') > 1:
                    self.multiples(input)
                    verify = True
                    break
                else:
                    verify = True
                    dice[0].append(input)
                    bonus = 0

            rolls = self.rollDice(dice)

            if rolls == []:
                print("Error - format not recognized.")
                verify = False

            if verify:
                result = self.parseDice(dice, rolls, bonus)
                print result
                return result
