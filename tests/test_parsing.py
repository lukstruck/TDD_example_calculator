import unittest

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


if __name__ == '__main__':
    unittest.main()
