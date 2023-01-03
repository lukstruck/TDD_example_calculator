from dataclasses import dataclass
from enum import Enum


class Lexer:
    class SyntaxError(Exception):
        pass

    def __init__(self, input_string: str):
        cleaned_string = input_string.replace(" ", "")
        self.input_string = cleaned_string
        self.token_types = [Lexer.ConstantToken, Lexer.OperatorToken]

    def next_token(self):
        if self.input_string == "":
            return None
        current_token = ""
        last_token_type = None
        for token_type in self.token_types:
            if token_type.matches(self.input_string[0]):
                last_token_type = token_type
                break
        if last_token_type is None:
            raise Lexer.SyntaxError(f"Input string contains illegal characters: {self.input_string[0]}")

        while self.input_string != "" and last_token_type.matches(self.input_string[0]):
            current_token += self.input_string[0]
            self.input_string = self.input_string[1:]

        return last_token_type(current_token)

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
