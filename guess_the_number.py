import random


def guess_num(number):
    random_num = random.randint(1, number)

    guess = 0

    while guess != random_num:
        guess = int(input(f"Enter a number between 1 and {number}: "))

        if guess < random_num:
            print("You have to guess again, number is too low")

        elif guess > random_num:
            print("Too high, please guess again")

    print(f"Yay! You Guessed the number {number} right, Welldone")


guess_num(10)
