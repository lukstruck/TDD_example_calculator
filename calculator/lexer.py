from dataclasses import dataclass
from enum import Enum


class Lexer:
    class SyntaxError(Exception):
        pass

    def __init__(self, input_string: str):
        cleaned_string = input_string.replace(" ", "")
        self.input_string = cleaned_string
        self.token_types = [Lexer.ConstantToken, Lexer.OperatorToken, Lexer.BracketToken]

    def next_token(self):
        if self.input_string == "":
            return None

        return self._get_next_token()

    def _get_next_token(self):
        current_token_str = ""
        current_token_type = self._get_token_type(self.input_string[0])

        while self._input_string_not_empty() and self._token_type_still_same(current_token_type):
            current_token_str += self._pop_input_string()

        return current_token_type(current_token_str)

    def _token_type_still_same(self, current_token_type):
        return current_token_type.matches(self.input_string[0])

    def _input_string_not_empty(self):
        return self.input_string != ""

    def _pop_input_string(self):
        head = self.input_string[0]
        self.input_string = self.input_string[1:]
        return head

    def _get_token_type(self, token_str):
        current_token_type = None
        for token_type in self.token_types:
            if token_type.matches(token_str):
                current_token_type = token_type
                break

        if current_token_type is None:
            raise Lexer.SyntaxError(f"Input string contains illegal characters: {self.input_string[0]}")

        return current_token_type

    @dataclass
    class ConstantToken:
        value: int

        def __init__(self, token_string):
            self.value = int(token_string)

        @staticmethod
        def matches(character: str):
            return character in "0123456789"

    @dataclass
    class OperatorToken:
        class Operator(Enum):
            Multiply = "*"
            Add = "+"

        value: Operator

        def __init__(self, token_string):
            self.value = Lexer.OperatorToken.Operator(token_string)

        @staticmethod
        def matches(character: str):
            return character in "+*"

        Multiply = Operator.Multiply
        Add = Operator.Add

    @dataclass
    class BracketToken:
        class Bracket(Enum):
            Open = "("
            Close = ")"

        value: Bracket

        def __init__(self, token_string):
            self.value = Lexer.BracketToken.Bracket(token_string)

        @staticmethod
        def matches(character: str):
            return character in "()"

        Open = Bracket.Open
        Close = Bracket.Close
