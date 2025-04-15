import random

print("High Low Game")

rounds = 5  # Changed 'round' to 'rounds' to avoid conflict with Python reserved word.

def main():
    print("Welcome to the High Low Game!")
    print("****************************")

    your_score = 0

    for i in range(rounds):
        print(f"Round {i + 1}")

        computer_number = random.randint(1, 100)
        your_number = random.randint(1, 100)
        print(f"Your number is: {your_number}")

        choice = input("Do you think your number is higher or lower than the computer's number? (Enter 'higher' or 'lower'): ").strip().lower()

        higher_and_correct = choice == "higher" and your_number > computer_number
        lower_and_correct = choice == "lower" and your_number < computer_number

        if higher_and_correct or lower_and_correct:
            print("You guessed correctly!")
            your_score += 1
        else:
            print(f"Sorry, the computer's number was {computer_number}. You guessed wrong.")

        print(f"Your score: {your_score}\n")

    print(f"Game Over! Your final score is {your_score}")

if __name__ == '__main__':
    main()
