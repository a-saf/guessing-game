import random


def greet_name():
    name = input("What's your name? \n")
    print(name + ", welcome to the Guessing Game!")
    return name


def display_level(level):
    print("You are at level " + str(level))


def choose_module():
    print("Which game would you like to play?")
    print("1 - Guess the number")
    print("2 - Guess the colour")
    print("3 - Guess the animal")
    print("4 - Quit")
    return int(input("Choice number: \n"))


def display_rules():
    print("You have three tries to guess correctly.\n"
          "If you guess it right, you win the round and move to next level.\n"
          "If you guess wrong, you lose the game and move down a level.\n"
          "Good luck, " + player_name)


def run_numbers_module():
    game_over = False
    level = 1
    numbers_list = []
    range_list = {1: "between 1 and 10.", 2: "between 1 and 20.", 3: "between 1 and 50."}

    while not game_over:
        tries = 1
        if level == 1:
            correct = random.randint(1, 10)
            for i in range(1, 11):
                numbers_list.append(i)
        elif level == 2:
            correct = random.randint(1, 20)
            for i in range(1, 21):
                numbers_list.append(i)
        elif level == 3:
            correct = random.randint(1, 50)
            for i in range(1, 51):
                numbers_list.append(i)
        else:
            print("You won the guessing game!")
            break
        print("Level " + str(level) + ". Guess the number " + range_list.get(level))

        while tries <= 3:
            print("Try #" + str(tries))
            guess = int(input("Enter your guess: \n"))
            if guess not in numbers_list:
                print("Invalid option. Try again.")
                break
            if guess > correct:
                print("You've guessed too high.")
            elif guess < correct:
                print("You've guessed too low.")
            else:
                print("Congratulations! Your guess is right.")
                level += 1
                if level <= 3:
                    print("Next level: " + str(level))
                break
            tries += 1
            print("Guess again...")
        if tries == 4:
            if level > 1:
                print("You guessed wrong three times, move down one level.")
                level -= 1
            else:
                print("You guessed incorrectly. Game over!")
                game_over = True


def print_list(some_list, key):
    print("Guess item from the following list:")
    print(some_list.get(key))


def run_colours_module():
    game_over = False
    level = 1
    colours_list = {1: ["red", "orange", "yellow", "green", "blue", "purple"],
                    2: ["red", "orange", "yellow", "green", "blue", "purple", "pink", "white", "black", "magenta"],
                    3: ["red", "orange", "yellow", "green", "blue", "purple", "pink", "white", "black", "magenta",
                        "grey", "teal", "beige", "cyan", "aquamarine"]}
    while not game_over:
        tries = 1
        if level == 1:
            correct = random.choice(colours_list.get(level))
            print_list(colours_list, level)
        elif level == 2:
            correct = random.choice(colours_list.get(level))
            print_list(colours_list, level)
        elif level == 3:
            correct = random.choice(colours_list.get(level))
            print_list(colours_list, level)
        else:
            print("You won the guessing game!")
            break
        print("Level " + str(level) + ". Guess the colour!")

        while tries <= 3:
            print("Try #" + str(tries))
            guess = input("Enter your guess: \n")
            if guess not in colours_list.get(level):
                print("Invalid option. Try again.")
                break
            if guess != correct:
                print("You've guessed incorrectly.")
                if tries < 3:
                    print("Guess again...")
            else:
                print("Congratulations! Your guess is right.")
                level += 1
                if level <= 3:
                    print("Next level: " + str(level))
                break
            tries += 1
        if tries == 4:
            if level > 1:
                print("You guessed wrong three times, move down one level.")
                level -= 1
            else:
                print("You guessed incorrectly. Game over!")
                game_over = True


def run_animals_module():
    game_over = False
    level = 1
    animals_list = {1: ["cat", "dog", "hamster", "parrot", "gold fish", "rabbit"],
                    2: ["horse", "chicken", "cow", "goat", "sheep", "pig", "turkey"],
                    3: ["lion", "cheetah", "elephant", "monkey", "giraffe", "hippo", "antelope", "crocodile"]}

    while not game_over:
        tries = 1
        if level == 1:
            correct = random.choice(animals_list.get(level))
            print_list(animals_list, level)
        elif level == 2:
            correct = random.choice(animals_list.get(level))
            print_list(animals_list, level)
        elif level == 3:
            correct = random.choice(animals_list.get(level))
            print_list(animals_list, level)
        else:
            print("You won the guessing game!")
            break
        print("Level " + str(level) + ". Guess the colour!")

        while tries <= 3:
            print("Try #" + str(tries))
            guess = input("Enter your guess: \n")
            if guess not in animals_list.get(level):
                print("Invalid option. Try again.")
                break
            if guess != correct:
                print("You've guessed incorrectly.")
                if tries < 3:
                    print("Guess again...")
            else:
                print("Congratulations! Your guess is right.")
                level += 1
                if level <= 3:
                    print("Next level: " + str(level))
                break
            tries += 1
        if tries == 4:
            if level > 1:
                print("You guessed wrong three times, move down one level.")
                level -= 1
            else:
                print("You guessed incorrectly. Game over!")
                game_over = True


player_name = greet_name()

while True:
    choice = choose_module()

    if choice == 1:
        display_rules()
        run_numbers_module()
    elif choice == 2:
        display_rules()
        run_colours_module()
    elif choice == 3:
        display_rules()
        run_animals_module()
    elif choice == 4:
        print("Thanks for playing. Goodbye!")
        exit()
    else:
        print("Invalid module choice. Please try again")