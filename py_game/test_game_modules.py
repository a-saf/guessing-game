import Game_Mock
import io
from unittest import TestCase
from unittest.mock import patch


class TestGameModules(TestCase):
    test_game = Game_Mock.GameMock()

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
    @patch('builtins.input', side_effect=[4, 14, 44])
    def test_numbers_module_correct_level_one(self, _, input):
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

    # def test_colours_module(self):
    #     self.fail()
    #
    # def test_animals_module(self):
    #     self.fail()
