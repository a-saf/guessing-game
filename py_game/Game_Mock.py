import random


class GameMock:

    player_name = None
    level = 1

    def __init__(self):
        pass

    def greet_name(self):
        self.player_name = input("What's your name? \n")
        print(self.player_name + ", welcome to the Guessing Game!")
        return self.player_name

    def choose_module(self):
        print("Which game would you like to play?")
        print("1 - Guess the number")
        print("2 - Guess the colour")
        print("3 - Guess the animal")
        print("4 - Quit")
        return int(input("Choice number: \n"))

    def display_rules(self):
        print("You have three tries to guess correctly.\n"
              "If you guess it right, you win the round and move to next level.\n"
              "If you guess wrong, you lose the game and move down a level.\n"
              "Good luck, " + self.player_name)

    def run_numbers_module(self):
        self.level = 1
        game_over = False
        numbers_list = []
        range_list = {1: "between 1 and 10.",
                      2: "between 1 and 20.",
                      3: "between 1 and 50."}

        while not game_over:
            tries = 1
            if self.level == 1:
                correct = 4
                for i in range(1, 11):
                    numbers_list.append(i)
            elif self.level == 2:
                correct = 14
                for i in range(1, 21):
                    numbers_list.append(i)
            elif self.level == 3:
                correct = 44
                for i in range(1, 51):
                    numbers_list.append(i)
            else:
                print("You won the guessing game!")
                break
            print("Level " + str(self.level) + ". Guess the number " + range_list.get(self.level))

            while tries <= 3:
                print("Try #" + str(tries))
                guess = int(input("Enter your guess: \n"))
                if guess not in numbers_list:
                    print("Invalid option. Try again.")
                    break
                if guess > correct:
                    print("You've guessed too high.")
                    if tries < 3:
                        print("Guess again...")
                elif guess < correct:
                    print("You've guessed too low.")
                    if tries < 3:
                        print("Guess again...")
                else:
                    print("Congratulations! Your guess is right.")
                    self.level += 1
                    if self.level <= 3:
                        print("Next level: " + str(self.level))
                    break
                tries += 1
            if tries == 4:
                if self.level > 1:
                    print("You guessed wrong three times, move down one level.")
                    self.level -= 1
                else:
                    print("You guessed incorrectly. Game over!")
                    game_over = True

    def print_list(self, some_list, key):
        print("Guess item from the following list:")
        print(some_list.get(key))

    def run_colours_module(self):
        self.level = 1
        game_over = False
        colours_list = {1: ["red", "orange", "yellow", "green", "blue", "purple"],
                        2: ["red", "orange", "yellow", "green", "blue", "purple", "pink", "white", "black", "magenta"],
                        3: ["red", "orange", "yellow", "green", "blue", "purple", "pink", "white", "black", "magenta",
                            "grey", "teal", "beige", "cyan", "aquamarine"]}
        while not game_over:
            tries = 1
            if self.level == 1:
                correct = "red"
                self.print_list(colours_list, self.level)
            elif self.level == 2:
                correct = "pink"
                self.print_list(colours_list, self.level)
            elif self.level == 3:
                correct = "aquamarine"
                self.print_list(colours_list, self.level)
            else:
                print("You won the guessing game!")
                break
            print("Level " + str(self.level) + ". Guess the colour!")

            while tries <= 3:
                print("Try #" + str(tries))
                guess = input("Enter your guess: \n")
                if guess not in colours_list.get(self.level):
                    print("Invalid option. Try again.")
                    break
                if guess != correct:
                    print("You've guessed incorrectly.")
                    if tries < 3:
                        print("Guess again...")
                else:
                    print("Congratulations! Your guess is right.")
                    self.level += 1
                    if self.level <= 3:
                        print("Next level: " + str(self.level))
                    break
                tries += 1
            if tries == 4:
                if self.level > 1:
                    print("You guessed wrong three times, move down one level.")
                    self.level -= 1
                else:
                    print("You guessed incorrectly. Game over!")
                    game_over = True

    def run_animals_module(self):
        self.level = 1
        game_over = False
        self.level = 1
        animals_list = {1: ["cat", "dog", "hamster", "parrot", "gold fish", "rabbit"],
                        2: ["horse", "chicken", "cow", "goat", "sheep", "pig", "turkey"],
                        3: ["lion", "cheetah", "elephant", "monkey", "giraffe", "hippo", "antelope", "crocodile"]}

        while not game_over:
            tries = 1
            if self.level == 1:
                correct = "cat"
                self.print_list(animals_list, self.level)
            elif self.level == 2:
                correct = "chicken"
                self.print_list(animals_list, self.level)
            elif self.level == 3:
                correct = "hippo"
                self.print_list(animals_list, self.level)
            else:
                print("You won the guessing game!")
                break
            print("Level " + str(self.level) + ". Guess the colour!")

            while tries <= 3:
                print("Try #" + str(tries))
                guess = input("Enter your guess: \n")
                if guess not in animals_list.get(self.level):
                    print("Invalid option. Try again.")
                    break
                if guess != correct:
                    print("You've guessed incorrectly.")
                    if tries < 3:
                        print("Guess again...")
                else:
                    print("Congratulations! Your guess is right.")
                    self.level += 1
                    if self.level <= 3:
                        print("Next level: " + str(self.level))
                    break
                tries += 1
            if tries == 4:
                if self.level > 1:
                    print("You guessed wrong three times, move down one level.")
                    self.level -= 1
                else:
                    print("You guessed incorrectly. Game over!")
                    game_over = True
