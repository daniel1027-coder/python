
import random


class Die:
    def __init__(self, sides: int = 6) -> None:
        """
        Initialize the die with a default of 6 sides.
        
        Additionally, you can specify the number of sides when creating an instance of Die.
        
        Args: sides (int): The number of sides on the die. Default is 6.
        
        """
        self.sides = sides

    def roll_die(self) -> None:
        """
        Roll the die and print the result.
        
        This method generates a random number between 1 and the number of sides on the die,
        and prints the result to the console.

        """
        result = random.randint(1, self.sides)
        print(result)