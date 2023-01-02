import unittest

from parameterized import parameterized

from calculator.lexer import Lexer


class TestLexing(unittest.TestCase):
    def test_initLexerWithEmptyString_nextReturnsNone(self):
        lexer = Lexer("")
        actual = lexer.next_token()
        expected = None
        self.assertEqual(actual, expected)

    @parameterized.expand([
        ["a"],
        ["A"],
        ["."],
    ])
    def test_initLexerWithInvalidString_raisesSyntaxError(self, invalid_string):
        with self.assertRaises(Lexer.SyntaxError):
            Lexer(invalid_string)


if __name__ == '__main__':
    unittest.main()
