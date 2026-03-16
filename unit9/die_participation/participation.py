from die import Die


def main() -> None:
    """Run the die rolling program."""
    sides = int(input("Enter the number of sides for the die: "))

    die = Die(sides)

    print(f"\nRolling a {sides}-sided die 10 times:")
    for _ in range(10):
        die.roll_die()


if __name__ == "__main__":
    main()