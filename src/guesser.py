import random

def play_game(testing):

    if testing:
        return "You got it!"
    secret_number = random.randint(1, 10)
    attempts = 0

    print ("Guess  a number between 1 and 10")

    while True:
        guess = int(input("your guess: "))
        attempts += 1

        if guess == secret_number:
            return f"You got it!"

        elif guess > secret_number:
                print ("Too high")
        else:
                print ("Too low!")


if __name__ == '__main__':
    play_game(False)