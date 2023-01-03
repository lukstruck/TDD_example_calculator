import unittest

from parameterized import parameterized

from calculator.lexer import Lexer


class TestLexing(unittest.TestCase):
    def test_initLexerWithEmptyString_nextReturnsNone(self):
        lexer = Lexer("")
        actual = lexer.next_token()
        expected = None
        self.assertEqual(expected, actual)

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
        self.assertEqual(expected, actual)

    @parameterized.expand([
        ["*", Lexer.OperatorToken(Lexer.OperatorToken.Multiply)],
        ["+", Lexer.OperatorToken(Lexer.OperatorToken.Add)],
    ])
    def test_initLexerWithOperator_nextReturnsOperatorToken(self, input_string, expected):
        lexer = Lexer(input_string)
        actual = lexer.next_token()
        self.assertEqual(expected, actual)

    @parameterized.expand([
        ["(", Lexer.BracketToken(Lexer.BracketToken.Open)],
        [")", Lexer.BracketToken(Lexer.BracketToken.Close)],
    ])
    def test_initLexerWithBracket_nextReturnsBracketToken(self, input_string, expected):
        lexer = Lexer(input_string)
        actual = lexer.next_token()
        self.assertEqual(expected, actual)

    def test_initLexerWithValidCombination_nextReturnsValidTokens(self):
        input_string = "+*(1 23)5)))84+3"
        expected_tokens = [
            Lexer.OperatorToken(Lexer.OperatorToken.Add),
            Lexer.OperatorToken(Lexer.OperatorToken.Multiply),
            Lexer.BracketToken(Lexer.BracketToken.Open),
            Lexer.ConstantToken(123),
            Lexer.BracketToken(Lexer.BracketToken.Close),
            Lexer.ConstantToken(5),
            Lexer.BracketToken(Lexer.BracketToken.Close),
            Lexer.BracketToken(Lexer.BracketToken.Close),
            Lexer.BracketToken(Lexer.BracketToken.Close),
            Lexer.ConstantToken(84),
            Lexer.OperatorToken(Lexer.OperatorToken.Add),
            Lexer.ConstantToken(3),
            None
        ]
        lexer = Lexer(input_string)
        for expected_token in expected_tokens:
            actual = lexer.next_token()
            self.assertEqual(expected_token, actual)


if __name__ == '__main__':
    unittest.main()
