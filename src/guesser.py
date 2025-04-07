import random

def play_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    print ("Guess  a number between 1 and 10")

    while True:
        guess = int(input("your guess: "))
        attempts += 1

        if guess == secret_number:
            print (f"Correct! it took you {attempts} attempts")
            break
        elif guess < secret_number:
                print ("Too high")
        else:
                print ("Too low!")

play_game()