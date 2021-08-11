TT_INT = "INT"
TT_FLOAT = "FLOAT"
TT_STRING = "STRING"
TT_IDENTIFIER = "IDENTIFIER"
TT_KEYWORD = "KEYWORD"
TT_PLUS = "PLUS"
TT_MINUS = "MINUS"
TT_MUL = "MUL"
TT_DIV = "DIV"
TT_POW = "POW"
TT_EQ = "EQ"
TT_LPAREN = "LPAREN"
TT_RPAREN = "RPAREN"
TT_LSQUARE = "LSQUARE"
TT_RSQUARE = "RSQUARE"
TT_EE = "EE"
TT_NE = "NE"
TT_LT = "LT"
TT_GT = "GT"
TT_LTE = "LTE"
TT_GTE = "GTE"
TT_COMMA = "COMMA"
TT_ARROW = "ARROW"
TT_NEWLINE = "NEWLINE"
TT_EOF = "EOF"

KEYWORDS = [
    # Lang 1
    "VAR",
    "AND",
    "OR",
    "NOT",
    "IF",
    "ELIF",
    "ELSE",
    "FOR",
    "TO",
    "STEP",
    "WHILE",
    "FUN",
    "THEN",
    "END",
    "RETURN",
    "CONTINUE",
    "BREAK",
    # Lang 2
    "VAR_TWO",
    "AND_TWO",
    "OR_TWO",
    "NOT_TWO",
    "IF_TWO",
    "ELIF_TWO",
    "ELSE_TWO",
    "FOR_TWO",
    "TO_TWO",
    "STEP_TWO",
    "WHILE_TWO",
    "FUN_TWO",
    "THEN_TWO",
    "END_TWO",
    "RETURN_TWO",
    "CONTINUE_TWO",
    "BREAK_TWO",
]

LANGUAGE_KEYWORD = {
    "en": {
        "VAR": "VAR",
        "AND": "AND",
        "OR": "OR",
        "NOT": "NOT",
        "IF": "IF",
        "ELIF": "ELIF",
        "ELSE": "ELSE",
        "FOR": "FOR",
        "TO": "TO",
        "STEP": "STEP",
        "WHILE": "WHILE",
        "FUN": "FUN",
        "THEN": "THEN",
        "END": "END",
        "RETURN": "RETURN",
        "CONTINUE": "CONTINUE",
        "BREAK": "BREAK",
    },
    "two": { 
        "VAR": "VAR_TWO",
        "AND": "AND_TWO",
        "OR": "OR_TWO",
        "NOT": "NOT_TWO",
        "IF": "IF_TWO",
        "ELIF": "ELIF_TWO",
        "ELSE": "ELSE_TWO",
        "FOR": "FOR_TWO",
        "TO": "TO_TWO",
        "STEP": "STEP_TWO",
        "WHILE": "WHILE_TWO",
        "FUN": "FUN_TWO",
        "THEN": "THEN_TWO",
        "END": "END_TWO",
        "RETURN": "RETURN_TWO",
        "CONTINUE": "CONTINUE_TWO",
        "BREAK": "BREAK_TWO",
    },
}


class Token:
    def __init__(self, type_, value=None, pos_start=None, pos_end=None, lang=None):
        self.type = type_
        self.value = value

        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()

        if pos_end:
            self.pos_end = pos_end.copy()

        self.lang = lang

    def matches(self, type_, value):
        if self.lang is not None and self.lang in LANGUAGE_KEYWORD:
            return self.type == type_ and self.value == LANGUAGE_KEYWORD[self.lang][value]
        return self.type == type_ and self.value == value

    def __repr__(self):
        if self.value:
            return f"{self.type}:{self.value}"
        return f"{self.type}"
