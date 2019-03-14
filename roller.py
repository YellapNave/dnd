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
    def __init__(self):
        self.bonus = 0

    # Take list of dice in the form [[positive][negative]] and output an array
    # of integers equal to the rolls that result.
    def rollDice(self, dice):
        rolls = []
        if len(dice[0]) > 0:
            for roll in dice[0]:
                if 'd' not in roll:
                    self.bonus += int(roll)
                    continue
                request = roll.split('d')
                n = int(request[0])
                sides = int(request[1])
                for i in range(n):
                    rolls.append(random.randint(1,sides))
        if len(dice[1]) > 0:
            for roll in dice[1]:
                if 'd' not in roll:
                    self.bonus -= int(roll)
                    continue
                request = roll.split('d')
                n = int(request[0])
                sides = int(request[1])
                for i in range(n):
                    rolls.append(random.randint(1,sides) * -1)
        return rolls

    # Take a list of dice rolls and the dice that generated those rolls and
    # generate a pretty string
    def parseDice(self, dice, rolls):
        if self.bonus == 0:
            op = ''
            strBonus = ''
        elif self.bonus >= 1:
            op = '+'
            strBonus = str(self.bonus)
        else:
            op = '-'
            strBonus = str(abs(self.bonus))
        rollStr = ' '.join(str(i) for i in rolls) + " %s %s" % (op, strBonus)

        posList = [] # list of positive dice
        posNums = ''
        for n in dice[0]:
            if 'd' in n:
                posList.append(n)
                dice[0].remove(n)
        posDice = '+'.join(posList)
        if len(dice[0]) > 0:
            posNums = "+" + '+'.join(dice[0])

        negList = [] # list of 'negative dice'
        negNums = ''
        if len(dice[1]) > 0:
            for n in dice[1]:
                if 'd' in n:
                    negList.append(n)
                    dice[1].remove(n)
            negDice = "-" + '-'.join(negList)
            if len(dice[1]) > 0:
                negNums = "-" + '-'.join(dice[1])
        else:
            negDice = ''
        return(str(sum(rolls) + self.bonus) + ' (' + posDice + negDice + posNums + negNums + '): ' + rollStr)

    # Take multiple dice rolls and return them each as a string in a list, so that
    # '1d10 + 2d6' gives [[1d10, 2d6],[]] and '1d10 + 2d12 - 1d6' gives [[1d10, 2d12],[1d6]]
    def multiples(self, input):
        res = [[],[]] # res[0] = boons, res[1] = banes
        pos = input.split('+')
        for i in pos:
            temp = i.split('-')
            if len(temp) > 1:
                res[0].append(temp[0])
                res[1] += temp[1:]
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
        verify = True

        # Loop for rolling dice
        while go:
            input = raw_input("Roll condition: ")
            input = cleanse(input)
            dice = [[],[]]

            if input == 'exit' or input == 'quit':
                go = False
                print("Quitting module.")
                break
            elif input.count('d') > 0:
                dice = self.multiples(input)
            else:
                dice[0].append(input)

            rolls = self.rollDice(dice)

            if rolls == []:
                print("Error - format not recognized.")
                verify = False

            if verify:
                result = self.parseDice(dice, rolls)
                self.bonus = 0
                print result
