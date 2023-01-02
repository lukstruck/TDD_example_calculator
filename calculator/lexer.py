from dataclasses import dataclass


class Lexer:
    class SyntaxError(Exception):
        pass

    def __init__(self, input_string: str):
        cleaned_string = input_string.replace(" ", "")
        if not (cleaned_string.isnumeric() or cleaned_string == ""):
            raise Lexer.SyntaxError(f"Input string contains illegal characters: {input_string}")
        self.input_string = cleaned_string

    def next_token(self):
        if self.input_string == "":
            return None
        return Lexer.ConstantToken(int(self.input_string))

    @dataclass
    class ConstantToken:
        value: int
