from .tokens import tokens

single_char_tokens = {
    '(': tokens.LEFT_PAREN,
    ')': tokens.RIGHT_PAREN,
    '{': tokens.LEFT_BRACE,
    '}': tokens.RIGHT_BRACE,
    ',': tokens.COMMA,
    '.': tokens.DOT,
    '-': tokens.MINUS,
    '+': tokens.PLUS,
    ';': tokens.SEMICOLON,
    '*': tokens.STAR,
}

two_char_tokens = {
    '!': '=',
    '=': '=',
    '<': '=',
    '>': '=',
    '|': '|',
    '&': '&',
}

optional_to_token = {
    '!=': tokens.BANG_EQUAL,
    '==': tokens.EQUAL_EQUAL,
    '<=': tokens.LESS_EQUAL,
    '>=': tokens.GREATER_EQUAL,
    '=': tokens.EQUAL,
    '<': tokens.LESS,
    '>': tokens.GREATER,
    '!': tokens.BANG,
    '||': tokens.OR,
    '&&': tokens.AND,
}


word_to_keyword = {
    'and': tokens.AND,
    'class': tokens.CLASS,
    'else': tokens.ELSE,
    'false': tokens.FALSE,
    'for': tokens.FOR,
    'if': tokens.IF,
    'null': tokens.NULL,
    'or': tokens.OR,
    'print': tokens.PRINT,
    'return': tokens.RETURN,
    'super': tokens.SUPER,
    'this': tokens.THIS,
    'true': tokens.TRUE,
    'let': tokens.LET,
    'while': tokens.WHILE,
    'byte': tokens.BYTE,	
    'short': tokens.SHORT,
    'int': tokens.INT,
    'long': tokens.LONG,
}