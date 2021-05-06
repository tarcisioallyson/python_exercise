""" Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

The keypad has the following layout:

┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.

He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.

* possible in sense of: the observed PIN itself and all variations considering the adjacent digits

Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list in Java and C#) of all variations for an observed PIN with a length of 1 to 8 digits. We could name the function getPINs (get_pins in python, GetPINs in C#). But please note that all PINs, the observed one and also the results, must be strings, because of potentially leading '0's. We already prepared some test cases for you.

Detective, we are counting on you!

For C# user: Do not use Mono. Mono is too slower when run your code. """

def get_pins(observed):    
    
    keypad = {
        '0': ['0','8'],
        '1': ['1','2','4'],
        '2': ['1','2','3','5'],
        '3': ['2','3','6'],
        '4': ['1','4','5','7'],
        '5': ['2','4','5','6','8'],
        '6': ['3','5','6','9'],
        '7': ['4','7','8'],
        '8': ['0','5','7','8','9'],
        '9': ['6','8','9']
    }
    
    pin = []
    
    if len(observed) == 1:
        return keypad[observed]
   
    elif len(observed) == 2:
        for digit_one in keypad[observed[0]]:
            for digit_two in keypad[observed[1]]:
                pin.append(digit_one+digit_two)
    
    elif len(observed) == 3:
        for digit_one in keypad[observed[0]]:
            for digit_two in keypad[observed[1]]:
                for digit_three in keypad[observed[2]]:
                    pin.append(digit_one+digit_two+digit_three)
    
    elif len(observed) == 4:
        for digit_one in keypad[observed[0]]:
            for digit_two in keypad[observed[1]]:
                for digit_three in keypad[observed[2]]:
                    for digit_four in keypad[observed[3]]:
                        pin.append(digit_one+digit_two+digit_three+digit_four)
    
    elif len(observed) == 5:
        for digit_one in keypad[observed[0]]:
            for digit_two in keypad[observed[1]]:
                for digit_three in keypad[observed[2]]:
                    for digit_four in keypad[observed[3]]:
                        for digit_five in keypad[observed[4]]:
                            pin.append(digit_one+digit_two+digit_three+digit_four+digit_five)
    
    elif len(observed) == 6:
        for digit_one in keypad[observed[0]]:
            for digit_two in keypad[observed[1]]:
                for digit_three in keypad[observed[2]]:
                    for digit_four in keypad[observed[3]]:
                        for digit_five in keypad[observed[4]]:
                            for digit_six in keypad[observed[5]]:
                                pin.append(digit_one+digit_two+digit_three+digit_four+digit_five+digit_six)
    
    elif len(observed) == 7:
        for digit_one in keypad[observed[0]]:
            for digit_two in keypad[observed[1]]:
                for digit_three in keypad[observed[2]]:
                    for digit_four in keypad[observed[3]]:
                        for digit_five in keypad[observed[4]]:
                            for digit_six in keypad[observed[5]]:
                                for digit_seven in keypad[observed[6]]:
                                    pin.append(digit_one+digit_two+digit_three+digit_four+digit_five+digit_six+digit_seven)
    
    elif len(observed) == 8:
        for digit_one in keypad[observed[0]]:
            for digit_two in keypad[observed[1]]:
                for digit_three in keypad[observed[2]]:
                    for digit_four in keypad[observed[3]]:
                        for digit_five in keypad[observed[4]]:
                            for digit_six in keypad[observed[5]]:
                                for digit_seven in keypad[observed[6]]:
                                    for digit_eight in keypad[observed[7]]:
                                        pin.append(digit_one+digit_two+digit_three+digit_four+digit_five+digit_six+digit_seven+digit_eight)
            
    return pin

print(get_pins('11'))