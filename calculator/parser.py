from dataclasses import dataclass
from typing import List

from calculator.lexer import Lexer


class Parser:
    class EmptyTokenListError(Exception):
        pass

    @staticmethod
    def parse(token_list: List[Lexer.Token]):
        if not token_list:
            raise Parser.EmptyTokenListError()

        return Constant(0)


@dataclass
class Constant:
    value: int
