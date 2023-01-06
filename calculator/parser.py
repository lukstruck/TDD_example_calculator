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
        did_something = False
        for token in token_list:
            if token.value == Bracket.Open:
                did_something = False
                bracket_counter += 1
            elif token.value == Bracket.Close:
                if not did_something:
                    raise Parser.SemanticsError(f"Empty brackets! (Missing an instruction inside the brackets)")
                bracket_counter -= 1
            else:
                did_something = True

        if bracket_counter > 0:
            raise Parser.SemanticsError(f"Unclosed brackets! (missing at least {bracket_counter} closing brackets)")
        if bracket_counter < 0:
            raise Parser.SemanticsError(f"Unclosed brackets! (missing at least {-bracket_counter} opening brackets)")
        return Constant(0)


@dataclass
class Constant:
    value: int
