"""
Dice Rolling Terms
Poshun Lin
A dice simulator that rolls two dice, prints the total,
and displays specific condition statements
No starter code
02/14/2026
"""
import random

game = ""

print(f"Dice simulator")
game = input("Press Enter to roll")

while game != "stop": 
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)

    total = (dice_1 + dice_2)
    if total == 2:
        print (dice_1, ",", dice_2)
        print(f"The total is {total} Snake Eyes")
        
    elif total == 3:
        print (dice_1, ",", dice_2)
        print(f"The total is {total} Ace Caught a Deuce")

    
    elif total == 4:
        print (dice_1, ",", dice_2)
        if dice_1 == 2 and dice_2 == 2:
            print(f"The total is {total} Little Joe from Kokomo")
        else:
            print(f"The total is {total}")
    
    elif total == 5:
        print (dice_1, ",", dice_2)
        print(f"The total is {total} Little Phoebe")
   
    elif total == 6:
        print (dice_1, ",", dice_2)
        if dice_1 == 3 and dice_2 == 3:
            print(f"The total is {total} Jimmy Hicks from the Sticks")
        else:
            print(f"The total is {total}")
    
    elif total == 7:
        print (dice_1, ",", dice_2)
        if dice_1 == 1 and dice_2 == 6 or dice_1 == 6 and dice_2 == 1:
            print(f"The total is {total} Six Ace")
        else:
            print(f"The total is {total}")
    
    elif total == 8:
        print (dice_1, ",", dice_2)
        if dice_1 == 4 and dice_2 ==4:
            print(f"The total is {total} Eighter from Decatur")
        else:
            print(f"The total is {total}")
    
    elif total == 9:
        print (dice_1, ",", dice_2)
        print(f"The total is {total} Nina from Pasadena")
    
    elif total == 10:
        print (dice_1, ",", dice_2)
        if dice_1 == 5 and dice_2 ==5:
            print(f"The total is {total} Puppy Paws")
        else:
            print(f"The total is {total}")
    
    elif total == 11:
        print (dice_1, ",", dice_2)
        print(f"The total is {total} Six Five no Jive")
    
    elif total == 12:
        print (dice_1, ",", dice_2)
        print(f"The total is {total} Boxcars")
    
    game = input("Press Enter to roll again or type 'stop': ")
print(f"Thank you for youre playing")


