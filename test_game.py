import io
from unittest import TestCase
from unittest.mock import patch
import Game


class TestGame(TestCase):
    test_game = Game.Game()

    @patch('builtins.input', side_effect=['Josephine'])
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
