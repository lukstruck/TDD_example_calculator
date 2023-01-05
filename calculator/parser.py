from dataclasses import dataclass
from typing import List

from calculator.lexer import Lexer, Bracket


class Parser:
    class SemanticsError(Exception):
        pass

    class EmptyTokenListError(Exception):
        pass

    @staticmethod
    def parse(token_list: List[Lexer.Token]):
        if not token_list:
            raise Parser.EmptyTokenListError()

        bracket_counter = 0
        for token in token_list:
            if token.value == Bracket.Open:
                bracket_counter += 1
            if token.value == Bracket.Close:
                bracket_counter -= 1

        if bracket_counter > 0:
            raise Parser.SemanticsError(f"Unclosed brackets! (missing at least {bracket_counter} closing brackets)")
        if bracket_counter < 0:
            raise Parser.SemanticsError(f"Unclosed brackets! (missing at least {-bracket_counter} opening brackets)")
        return Constant(0)


@dataclass
class Constant:
    value: int
