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
            Lexer(invalid_string).next_token()

    @parameterized.expand([
        ["0", Lexer.ConstantToken(0)],
        ["1", Lexer.ConstantToken(1)],
        ["1 1", Lexer.ConstantToken(11)],
        ["11", Lexer.ConstantToken(11)],
        ["01", Lexer.ConstantToken(1)],
    ])
    def test_initLexerWithValidConstantString_nextReturnsConstantToken(self, input_string, expected):
        lexer = Lexer(input_string)
        actual = lexer.next_token()
        self.assertEqual(actual, expected)

    @parameterized.expand([
        ["*", Lexer.OperatorToken(Lexer.OperatorToken.Multiply)],
        ["+", Lexer.OperatorToken(Lexer.OperatorToken.Add)],
    ])
    def test_initLexerWithOperator_nextReturnsOperatorToken(self, input_string, expected):
        lexer = Lexer(input_string)
        actual = lexer.next_token()
        self.assertEqual(actual, expected)

    @parameterized.expand([
        ["(", Lexer.BracketToken(Lexer.BracketToken.Open)],
        [")", Lexer.BracketToken(Lexer.BracketToken.Close)],
    ])
    def test_initLexerWithBracket_nextReturnsBracketToken(self, input_string, expected):
        lexer = Lexer(input_string)
        actual = lexer.next_token()
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
