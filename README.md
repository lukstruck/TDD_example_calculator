# TDD_example_calculator

A calculator implemented using TDD.

# Specification

The calculator takes in mathematically correct terms as strings with the following grammar:

```
TERM           : ( ACTION ) | CONSTANT
ACTION         : ADDITION | MULTIPLICATION
ADDITION       : + TERM TERM
MULTIPLICATION : * TERM TERM
CONSTANT       : CONSTANT CONSTANT | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```

And outputs the calculated value of the term. The output is always an integer.

# Requirements Analysis

## Lexing

### Constants

- [x] "" -> Nothing
- [x] "0" -> ConstantToken(0)
- [x] "11" -> ConstantToken(11)
- [x] "1 1" -> ConstantToken(11)
- [x] "A" -> Syntax Error, unknown symbol

### + * ( )

- [x] \+ -> OperatorToken(Add)
- [x] \* -> OperatorToken(Multiply)
- [x] ( -> BracketToken(Open)
- [x] ) -> BracketToken(Close)

### Combinations

- [x] \+*(1 23)5)))84+3

## Parsing

- [ ] "" -> 0
- [ ] "0" -> 0
- [ ] "1" -> 1
- [ ] "1 1" -> 11
- [ ] "A" -> Syntax Error, unknown symbol
- [ ] "(", ")" -> Semantics Error, unclosed bracket
- [ ] "()" -> Semantics Error, missing operator
- [ ] "(4)" -> Semantics Error, unknown operator
- [ ] "4 +" -> Semantics Error, operator not first instruction in brackets

### Constants

### Additions

### Multiplications
