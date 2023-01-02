import unittest

from calculator.lexer import Lexer


class TestLexing(unittest.TestCase):
    def test_initLexerWithEmptyString_nextReturnsNone(self):
        lexer = Lexer("")
        actual = lexer.next_token()
        expected = None
        self.assertEqual(actual, expected)

    def test_initLexerWithInvalidString_raisesSyntaxError(self):
        with self.assertRaises(Lexer.SyntaxError):
            Lexer("A")


if __name__ == '__main__':
    unittest.main()
