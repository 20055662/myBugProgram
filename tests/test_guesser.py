import guesser
import unittest

class TestGuesser(unittest.TestCase):
    def test_output_message(self):
        message = guesser.play_game()
        self.assertEqual(message, "You got it!")



if __name__ == '__main__':
    unittest.main()