import random

# Take an input and remove all the spaces, then convert it entirely to lowercase.
def cleanse(input):
    return (input.replace(" ","")).lower()

# Take a basic dice format, such as 2d4, and output an array of integers equal
# to the rolls that result. If the input contains more than one 'd', or there is
# a single d with something other than numbers on either side of it, an empty
# list is returned.
def parseDice(form):
    if form.count('+') == 0 and form.count('-') == 0:
        if form.count('d') >= 2:
            return []
        else:
            request = form.split('d')

        for i in request[0]:
            if i.isdigit() == False:
                return []
        for i in request[1]:
            if i.isdigit() == False:
                return []

        n = int(request[0])
        sides = int(request[1])
        rolls = []
        for i in range(n):
            rolls.append(random.randint(1,sides))
        return (rolls)

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
            request = form[0].split('d')
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

        rolls = parseDice(dice)
        if rolls == []:
            print("Error - format not recognized.")
            verify = False

        if verify:
            if bonus < 0:
                operator = " - "
            else:
                operator = " + "
            result = str(sum(rolls) + bonus) + ': ' + ' '.join((str(i) for i in rolls))
            if bonus != 0:
                print result + operator + str(abs(bonus))
            else:
                print result
