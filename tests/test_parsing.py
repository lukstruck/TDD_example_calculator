import unittest

from parameterized import parameterized

from calculator.lexer import Lexer
from calculator.parser import Parser, Constant


class TestParsing(unittest.TestCase):
    def test_constantToken_returnsConstant(self):
        actual = Parser.parse([Lexer.ConstantToken(0)])
        expected = Constant(0)
        self.assertEqual(expected, actual)

    def test_emptyList_raisesError(self):
        with self.assertRaises(Parser.EmptyTokenListError):
            Parser.parse([])

    @parameterized.expand([
        [[Lexer.BracketToken(Lexer.BracketToken.Open)]],
        [[Lexer.BracketToken(Lexer.BracketToken.Close)]],
    ])
    def test_invalidList_raisesError(self, token_list):
        with self.assertRaises(Parser.SemanticsError):
            Parser.parse(token_list)


if __name__ == '__main__':
    unittest.main()
