class Lexer:
    class SyntaxError(Exception):
        pass

    def __init__(self, input_string: str):
        if not (input_string.isnumeric() or input_string == ""):
            raise Lexer.SyntaxError(f"Input string contains illegal characters: {input_string}")
        self.input_string = input_string

    def next_token(self):
        pass
