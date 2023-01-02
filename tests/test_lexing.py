import unittest

from calculator.lexer import Lexer


class TestLexing(unittest.TestCase):
    def test_initLexer(self):
        lexer = Lexer()


if __name__ == '__main__':
    unittest.main()
