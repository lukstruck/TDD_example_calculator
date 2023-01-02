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

    def test_initLexerWith0String_nextReturnsConstantToken(self):
        lexer = Lexer("0")
        actual = lexer.next_token()
        expected = Lexer.ConstantToken(0)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
