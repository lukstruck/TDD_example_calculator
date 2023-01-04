from dataclasses import dataclass
from enum import Enum
from typing import TypeVar, Generic

T = TypeVar("T")


class Operator(Enum):
    Multiply = "*"
    Add = "+"


class Bracket(Enum):
    Open = "("
    Close = ")"


class Lexer:
    class SyntaxError(Exception):
        pass

    class Token(Generic[T]):
        value: T

        @staticmethod
        def matches(token_string: str):
            raise NotImplementedError()

    def __init__(self, input_string: str):
        cleaned_string = input_string.replace(" ", "")
        self.input_string = cleaned_string

    def next_token(self):
        if self.input_string == "":
            return None

        return self._get_next_token()

    def _get_next_token(self):
        current_token_str = ""
        current_token_type = self._get_token_type(self.input_string[0])

        while self._input_string_not_empty() and self._token_type_still_same(current_token_type, current_token_str):
            current_token_str += self._pop_input_string()

        return current_token_type(current_token_str)

    def _token_type_still_same(self, current_token_type, current_token_str):
        return current_token_type.matches(current_token_str + self.input_string[0])

    def _input_string_not_empty(self):
        return self.input_string != ""

    def _pop_input_string(self):
        head = self.input_string[0]
        self.input_string = self.input_string[1:]
        return head

    def _get_token_type(self, token_str):
        for token_type in self.token_types:
            if token_type.matches(token_str):
                return token_type

        raise Lexer.SyntaxError(f"Input string contains illegal characters: {self.input_string[0]}")

    @dataclass
    class ConstantToken(Token[int]):
        def __init__(self, token_string):
            self.value = int(token_string)

        @staticmethod
        def matches(token_string: str):
            return token_string[-1] in "0123456789"

    @dataclass
    class OperatorToken(Token[Operator]):
        def __init__(self, token_string):
            self.value = Operator(token_string)

        @staticmethod
        def matches(token_string: str):
            return len(token_string) == 1 and token_string in "+*"

        Multiply = Operator.Multiply
        Add = Operator.Add

    @dataclass
    class BracketToken(Token[Bracket]):
        def __init__(self, token_string):
            self.value = Bracket(token_string)

        @staticmethod
        def matches(token_string: str):
            return len(token_string) == 1 and token_string in "()"

        Open = Bracket.Open
        Close = Bracket.Close

    token_types = [ConstantToken, OperatorToken, BracketToken]
