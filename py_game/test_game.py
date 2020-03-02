import io
import unittest
from unittest import TestCase
from mock import patch
import Game


class TestGame(TestCase):
    test_game = Game.GameMock()

    @patch('builtins.input', side_effect=["Josephine"])
    def test_greet_name(self, _):
        self.assertEqual(self.test_game.greet_name(), "Josephine")

    @patch('builtins.input', side_effect=[2])
    def test_choose_module(self, _):
        self.assertEqual(self.test_game.choose_module(), 2)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_rules(self, _):
        expected_out = "You have three tries to guess correctly.\n" \
                       "If you guess it right, you win the round and move to next level.\n" \
                       "If you guess wrong, you lose the game and move down a level.\n" \
                       "Good luck, Josephine\n"
        self.test_game.player_name = "Josephine"
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.test_game.display_rules()
            self.assertEqual(fake_out.getvalue(), expected_out)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_list(self, _):
        expected_out = "Guess item from the following list:\n" + \
                       str(["red", "orange", "yellow", "green", "blue", "purple", "pink", "white", "black", "magenta",
                            "grey", "teal", "beige", "cyan", "aquamarine"]) + "\n"
        colours_list = {1: ["red", "orange", "yellow", "green", "blue", "purple"],
                        2: ["red", "orange", "yellow", "green", "blue", "purple", "pink", "white", "black", "magenta"],
                        3: ["red", "orange", "yellow", "green", "blue", "purple", "pink", "white", "black", "magenta",
                            "grey", "teal", "beige", "cyan", "aquamarine"]}
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.test_game.print_list(colours_list, 3)
            self.assertEqual(fake_out.getvalue(), expected_out)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[1, 2, 5])
    def test_numbers_module_incorrect_level_one(self, _, input):
        expected_out = "Level 1. Guess the number between 1 and 10.\n" \
                       "Try #1\n" \
                       "You've guessed too low.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed too low.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "You've guessed too high.\n" \
                       "You guessed incorrectly. Game over!\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.test_game.run_numbers_module()
            self.assertEqual(fake_out.getvalue(), expected_out)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[1, 2, 4, 12, 13, 18, 1, 1, 3])
    def test_numbers_module_incorrect_level_two(self, _, input):
        expected_out = "Level 1. Guess the number between 1 and 10.\n" \
                       "Try #1\n" \
                       "You've guessed too low.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed too low.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "Congratulations! Your guess is right.\n" \
                       "Next level: 2\n" \
                       "Level 2. Guess the number between 1 and 20.\n" \
                       "Try #1\n" \
                       "You've guessed too low.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed too low.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "You've guessed too high.\n" \
                       "You guessed wrong three times, move down one level.\n" \
                       "Level 1. Guess the number between 1 and 10.\n" \
                       "Try #1\n" \
                       "You've guessed too low.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed too low.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "You've guessed too low.\n" \
                       "You guessed incorrectly. Game over!\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.test_game.run_numbers_module()
            self.assertEqual(fake_out.getvalue(), expected_out)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[4, 14, 1, 1, 5, 23, 3, 7, 3, 8, 9])
    def test_numbers_module_incorrect_level_three(self, _, input):
        expected_out = "Level 1. Guess the number between 1 and 10.\n" \
                       "Try #1\n" \
                       "Congratulations! Your guess is right.\n" \
                       "Next level: 2\n" \
                       "Level 2. Guess the number between 1 and 20.\n" \
                       "Try #1\n" \
                       "Congratulations! Your guess is right.\n" \
                       "Next level: 3\n" \
                       "Level 3. Guess the number between 1 and 50.\n" \
                       "Try #1\n" \
                       "You've guessed too low.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed too low.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "You've guessed too low.\n" \
                       "You guessed wrong three times, move down one level.\n" \
                       "Level 2. Guess the number between 1 and 20.\n" \
                       "Try #1\n" \
                       "You've guessed too high.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed too low.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "You've guessed too low.\n" \
                       "You guessed wrong three times, move down one level.\n" \
                       "Level 1. Guess the number between 1 and 10.\n" \
                       "Try #1\n" \
                       "You've guessed too low.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed too high.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "You've guessed too high.\n" \
                       "You guessed incorrectly. Game over!\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.test_game.run_numbers_module()
            self.assertEqual(fake_out.getvalue(), expected_out)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[4, 14, 44])
    def test_numbers_module_correct(self, _, input):
        expected_out = "Level 1. Guess the number between 1 and 10.\n" \
                       "Try #1\n" \
                       "Congratulations! Your guess is right.\n" \
                       "Next level: 2\n" \
                       "Level 2. Guess the number between 1 and 20.\n" \
                       "Try #1\n" \
                       "Congratulations! Your guess is right.\n" \
                       "Next level: 3\n" \
                       "Level 3. Guess the number between 1 and 50.\n" \
                       "Try #1\n" \
                       "Congratulations! Your guess is right.\n" \
                       "You won the guessing game!\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.test_game.run_numbers_module()
            self.assertEqual(fake_out.getvalue(), expected_out)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[25, 4, 14, 44])
    def test_numbers_module_correct_and_invalid_input(self, _, input):
        expected_out = "Level 1. Guess the number between 1 and 10.\n" \
                       "Try #1\n" \
                       "Invalid option. Try again.\n" \
                       "Level 1. Guess the number between 1 and 10.\n" \
                       "Try #1\n" \
                       "Congratulations! Your guess is right.\n" \
                       "Next level: 2\n" \
                       "Level 2. Guess the number between 1 and 20.\n" \
                       "Try #1\n" \
                       "Congratulations! Your guess is right.\n" \
                       "Next level: 3\n" \
                       "Level 3. Guess the number between 1 and 50.\n" \
                       "Try #1\n" \
                       "Congratulations! Your guess is right.\n" \
                       "You won the guessing game!\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.test_game.run_numbers_module()
            self.assertEqual(fake_out.getvalue(), expected_out)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["red", "pink", "aquamarine"])
    def test_colours_module_correct(self, _, input):
        expected_out = "Guess item from the following list:\n" \
                       "['red', 'orange', 'yellow', 'green', 'blue', 'purple']\n" \
                       "Level 1. Guess the colour!\n" \
                       "Try #1\n" \
                       "Congratulations! Your guess is right.\n" \
                       "Next level: 2\n" \
                       "Guess item from the following list:\n" \
                       "['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'white', 'black', 'magenta']\n" \
                       "Level 2. Guess the colour!\n" \
                       "Try #1\n" \
                       "Congratulations! Your guess is right.\n" \
                       "Next level: 3\n" \
                       "Guess item from the following list:\n" \
                       "['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'white', 'black', " \
                       "'magenta', 'grey', 'teal', 'beige', 'cyan', 'aquamarine']\n" \
                       "Level 3. Guess the colour!\n" \
                       "Try #1\n" \
                       "Congratulations! Your guess is right.\n" \
                       "You won the guessing game!\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.test_game.run_colours_module()
            self.assertEqual(fake_out.getvalue(), expected_out)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["orange", "green", "blue"])
    def test_colours_module_incorrect_level_one(self, _, input):
        expected_out = "Guess item from the following list:\n" \
                       "['red', 'orange', 'yellow', 'green', 'blue', 'purple']\n" \
                       "Level 1. Guess the colour!\n" \
                       "Try #1\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "You've guessed incorrectly.\n" \
                       "You guessed incorrectly. Game over!\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.test_game.run_colours_module()
            self.assertEqual(fake_out.getvalue(), expected_out)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["orange", "green", "red", "red", "white", "magenta", "purple", "yellow",
                                          "green"])
    def test_colours_module_incorrect_level_two(self, _, input):
        expected_out = "Guess item from the following list:\n" \
                       "['red', 'orange', 'yellow', 'green', 'blue', 'purple']\n" \
                       "Level 1. Guess the colour!\n" \
                       "Try #1\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "Congratulations! Your guess is right.\n" \
                       "Next level: 2\n" \
                       "Guess item from the following list:\n" \
                       "['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'white', 'black', 'magenta']\n" \
                       "Level 2. Guess the colour!\n" \
                       "Try #1\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "You've guessed incorrectly.\n" \
                       "You guessed wrong three times, move down one level.\n" \
                       "Guess item from the following list:\n" \
                       "['red', 'orange', 'yellow', 'green', 'blue', 'purple']\n" \
                       "Level 1. Guess the colour!\n" \
                       "Try #1\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "You've guessed incorrectly.\n" \
                       "You guessed incorrectly. Game over!\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.test_game.run_colours_module()
            self.assertEqual(fake_out.getvalue(), expected_out)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["orange", "green", "red", "red", "white", "pink", "purple", "yellow",
                                          "green", "white", "black", "magenta", "blue", "orange", "purple"])
    def test_colours_module_incorrect_level_three(self, _, input):
        expected_out = "Guess item from the following list:\n" \
                       "['red', 'orange', 'yellow', 'green', 'blue', 'purple']\n" \
                       "Level 1. Guess the colour!\n" \
                       "Try #1\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "Congratulations! Your guess is right.\n" \
                       "Next level: 2\n" \
                       "Guess item from the following list:\n" \
                       "['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'white', 'black', 'magenta']\n" \
                       "Level 2. Guess the colour!\n" \
                       "Try #1\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "Congratulations! Your guess is right.\n" \
                       "Next level: 3\n" \
                       "Guess item from the following list:\n" \
                       "['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'white', 'black', 'magenta', " \
                       "'grey', 'teal', 'beige', 'cyan', 'aquamarine']\n" \
                       "Level 3. Guess the colour!\n" \
                       "Try #1\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "You've guessed incorrectly.\n" \
                       "You guessed wrong three times, move down one level.\n" \
                       "Guess item from the following list:\n" \
                       "['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'white', 'black', 'magenta']\n" \
                       "Level 2. Guess the colour!\n" \
                       "Try #1\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "You've guessed incorrectly.\n" \
                       "You guessed wrong three times, move down one level.\n" \
                       "Guess item from the following list:\n" \
                       "['red', 'orange', 'yellow', 'green', 'blue', 'purple']\n" \
                       "Level 1. Guess the colour!\n" \
                       "Try #1\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "You've guessed incorrectly.\n" \
                       "You guessed incorrectly. Game over!\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.test_game.run_colours_module()
            self.assertEqual(fake_out.getvalue(), expected_out)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["aquamarine", "blue", "yellow", "green"])
    def test_colours_module_invalid_input(self, _, input):
        expected_out = "Guess item from the following list:\n" \
                       "['red', 'orange', 'yellow', 'green', 'blue', 'purple']\n" \
                       "Level 1. Guess the colour!\n" \
                       "Try #1\n" \
                       "Invalid option. Try again.\n" \
                       "Guess item from the following list:\n" \
                       "['red', 'orange', 'yellow', 'green', 'blue', 'purple']\n" \
                       "Level 1. Guess the colour!\n" \
                       "Try #1\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "You've guessed incorrectly.\n" \
                       "You guessed incorrectly. Game over!\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.test_game.run_colours_module()
            self.assertEqual(fake_out.getvalue(), expected_out)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["cat", "chicken", "hippo"])
    def test_animals_module_correct(self, _, input):
        expected_out = "Guess item from the following list:\n" \
                       "['cat', 'dog', 'hamster', 'parrot', 'gold fish', 'rabbit']\n" \
                       "Level 1. Guess the colour!\n" \
                       "Try #1\n" \
                       "Congratulations! Your guess is right.\n" \
                       "Next level: 2\n" \
                       "Guess item from the following list:\n" \
                       "['horse', 'chicken', 'cow', 'goat', 'sheep', 'pig', 'turkey']\n" \
                       "Level 2. Guess the colour!\n" \
                       "Try #1\n" \
                       "Congratulations! Your guess is right.\n" \
                       "Next level: 3\n" \
                       "Guess item from the following list:\n" \
                       "['lion', 'cheetah', 'elephant', 'monkey', 'giraffe', 'hippo', 'antelope', 'crocodile']\n" \
                       "Level 3. Guess the colour!\n" \
                       "Try #1\n" \
                       "Congratulations! Your guess is right.\n" \
                       "You won the guessing game!\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.test_game.run_animals_module()
            self.assertEqual(fake_out.getvalue(), expected_out)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["dog", "parrot", "rabbit"])
    def test_animals_module_incorrect_level_one(self, _, input):
        expected_out = "Guess item from the following list:\n" \
                       "['cat', 'dog', 'hamster', 'parrot', 'gold fish', 'rabbit']\n" \
                       "Level 1. Guess the colour!\n" \
                       "Try #1\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "You've guessed incorrectly.\n" \
                       "You guessed incorrectly. Game over!\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.test_game.run_animals_module()
            self.assertEqual(fake_out.getvalue(), expected_out)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["dog", "parrot", "cat", "turkey", "horse", "pig", "gold fish", "hamster",
                                          "rabbit"])
    def test_animals_module_incorrect_level_two(self, _, input):
        expected_out = "Guess item from the following list:\n" \
                       "['cat', 'dog', 'hamster', 'parrot', 'gold fish', 'rabbit']\n" \
                       "Level 1. Guess the colour!\n" \
                       "Try #1\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "Congratulations! Your guess is right.\n" \
                       "Next level: 2\n" \
                       "Guess item from the following list:\n" \
                       "['horse', 'chicken', 'cow', 'goat', 'sheep', 'pig', 'turkey']\n" \
                       "Level 2. Guess the colour!\n" \
                       "Try #1\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "You've guessed incorrectly.\n" \
                       "You guessed wrong three times, move down one level.\n" \
                       "Guess item from the following list:\n" \
                       "['cat', 'dog', 'hamster', 'parrot', 'gold fish', 'rabbit']\n" \
                       "Level 1. Guess the colour!\n" \
                       "Try #1\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "You've guessed incorrectly.\n" \
                       "You guessed incorrectly. Game over!\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.test_game.run_animals_module()
            self.assertEqual(fake_out.getvalue(), expected_out)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["dog", "parrot", "cat", "horse", "cow", "chicken", "lion", "cheetah",
                                          "monkey", "cow", "turkey", "goat", "dog", "hamster", "parrot"])
    def test_animals_module_incorrect_level_three(self, _, input):
        expected_out = "Guess item from the following list:\n" \
                       "['cat', 'dog', 'hamster', 'parrot', 'gold fish', 'rabbit']\n" \
                       "Level 1. Guess the colour!\n" \
                       "Try #1\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "Congratulations! Your guess is right.\n" \
                       "Next level: 2\n" \
                       "Guess item from the following list:\n" \
                       "['horse', 'chicken', 'cow', 'goat', 'sheep', 'pig', 'turkey']\n" \
                       "Level 2. Guess the colour!\n" \
                       "Try #1\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "Congratulations! Your guess is right.\n" \
                       "Next level: 3\n" \
                       "Guess item from the following list:\n" \
                       "['lion', 'cheetah', 'elephant', 'monkey', 'giraffe', 'hippo', 'antelope', 'crocodile']\n" \
                       "Level 3. Guess the colour!\n" \
                       "Try #1\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "You've guessed incorrectly.\n" \
                       "You guessed wrong three times, move down one level.\n" \
                       "Guess item from the following list:\n" \
                       "['horse', 'chicken', 'cow', 'goat', 'sheep', 'pig', 'turkey']\n" \
                       "Level 2. Guess the colour!\n" \
                       "Try #1\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "You've guessed incorrectly.\n" \
                       "You guessed wrong three times, move down one level.\n" \
                       "Guess item from the following list:\n" \
                       "['cat', 'dog', 'hamster', 'parrot', 'gold fish', 'rabbit']\n" \
                       "Level 1. Guess the colour!\n" \
                       "Try #1\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "You've guessed incorrectly.\n" \
                       "You guessed incorrectly. Game over!\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.test_game.run_animals_module()
            self.assertEqual(fake_out.getvalue(), expected_out)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["antelope", "dog", "parrot", "hamster"])
    def test_animals_module_invalid_input(self, _, input):
        expected_out = "Guess item from the following list:\n" \
                       "['cat', 'dog', 'hamster', 'parrot', 'gold fish', 'rabbit']\n" \
                       "Level 1. Guess the colour!\n" \
                       "Try #1\n" \
                       "Invalid option. Try again.\n" \
                       "Guess item from the following list:\n" \
                       "['cat', 'dog', 'hamster', 'parrot', 'gold fish', 'rabbit']\n" \
                       "Level 1. Guess the colour!\n" \
                       "Try #1\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #2\n" \
                       "You've guessed incorrectly.\n" \
                       "Guess again...\n" \
                       "Try #3\n" \
                       "You've guessed incorrectly.\n" \
                       "You guessed incorrectly. Game over!\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.test_game.run_animals_module()
            self.assertEqual(fake_out.getvalue(), expected_out)


if __name__ == '__main__':
    log_file = 'results.txt'
    with open(log_file, "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
