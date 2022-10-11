### Dice roller Python script! ###
##################################

import sys
import random


# Determines user input, sends input to functions, and prints output of functions
def main():
    usage = """Usage:   python3 dy.py ACTION.. PARAMETER..
Example: python3 dy.py roll 2d8+3

Roll -  dy.py will accept normal Pen and Paper syntax 
        regarding any die rolls from a d1 (why?) to a 
        d100.

        The number after the d(ie) determines the number
        of sides on the die. 
                      
        Multiple dice can be rolled by using a number
        preceeding the 'd'. Leaving this blank defaults
        to 1.

        Modifiers can be placed after the die size, you
        can use - or + to modify the result of the rolls
        to suit your needs."""
    
    try:

        if sys.argv[1] == "shuffle":
            output = "Shuffle, shuffle, shuffle."
        elif sys.argv[1] == "roll":
            output = roll(sys.argv[2])
        else:
            output = usage

    except:
        output = usage

    print(output)

# roll functionality
def roll(s):
    die  = ""
    amt  = 1
    moda = "+"
    modb = 0
    res  = 0
    resl = [0]
    out  = ""
    tmp  = s.split("d", 1)

    # Store modifier in moda, if one exists
    for i in tmp[1]:
        if i == "-":
            moda = "-"
        elif i == "+":
            moda = "+"
        
    # Store amount of rolled die in amt, default 1    
    if len(tmp) == 2 and tmp[0] != '':
        amt = int(tmp[0])
        die = tmp[1]
    else:
        amt = 1
        die = tmp[1]

    # Store modifier value in modb, if one exists
    tmp = die.split(moda)
    die  = tmp[0]
    if len(tmp) == 2:
        modb = tmp[1]

    # Stop from attempting die bigger than d100
    if int(die) > 100:
        out = "Invalid input"
        return out

    # Calculate result and store it in output
    if int(modb) > 0:
        out = f'You rolled {amt} d{die}, with a modifier of {moda}{modb}\n--------\n'
    else:
        out = f'You rolled {amt} d{die}\n---------\n'
    for i in range(0, int(amt)):
        if len(resl) < int(amt):
                resl += [0]
        resl[i] = random.randrange(1, int(die) + 1, 1)
        res    += resl[i]
        out    += f'd{die}: ' 
        if resl[i] < 10:
            out += f'  {str(resl[i])}'
        elif resl[i] < 100:
            out += f' {str(resl[i])}'
        else:
            out += f'{str(resl[i])}'
        if resl[i] == 20 and die == "20":
            out += " Nat 20!\n"
        else:
            out += "\n"
    if moda == "-":
        res -= int(modb)
    else:
        res += int(modb)
    out += "--------\nTotal: " + str(res) 
    return out

# shuffle functionality
def shuffle():
    pass

if __name__ == '__main__':
    main()
