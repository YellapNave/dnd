import random
import roller

# Loop for picking the module
while True:

    module = raw_input("Select module:\n1. Dice roller\n")
    module = roller.cleanse(module)

    if module == '1':
        print("Dice roller selected.")
        roller = roller.Roller()
        roller.module()

    # Every while loop should have an exit condition
    elif module == 'exit' or module == 'quit' :
        print("Goodbye.")
        break

    else: print("Sorry, module not found.")
