from pygments import style
from pygments import token


ALMOST_BLACK = '#1c1c1c'
DARKER_GREY = '#262626'
DARK_GREY = '#303030'
GREY = '#444444'
MEDIUM_GREY = '#585858'
LIGHT_GREY = '#6c6c6c'
LIGHTER_GREY = '#bcbcbc'
WHITE = '#ffffff'
PURPLE = '#5f5f87'
LIGHT_PURPLE = '#8787af'
GREEN = '#5f875f'
LIGHT_GREEN = '#87af87'
AQUA = '#5f8787'
LIGHT_AQUA = '#5fafaf'
BLUE = '#5f87af'
LIGHT_BLUE = '#8fafd7'
RED = '#af5f5f'
ORANGE = '#ff8700'
OCRE = '#87875f'
YELLOW = '#ffffaf'


class ApprenticeStyle(style.Style):
    background = DARKER_GREY
    default_style = ''

    styles = {
        token.Text: LIGHTER_GREY,
        token.Comment: MEDIUM_GREY,
        token.Keyword: LIGHT_BLUE,
        token.Keyword.Constant: ORANGE,
        token.Keyword.Psuedo: BLUE,
        token.Keyword.Namespace: AQUA,

        token.Name.Builtin: LIGHT_BLUE,
        token.Name.Pseudo: BLUE,
        token.Name.Class: LIGHT_PURPLE,
        token.Name.Function: YELLOW,
        token.Name.Decorator: YELLOW,

        token.Number: ORANGE,

        token.String: LIGHT_GREEN,
        token.String.Escape: GREEN,
        token.String.Interpol: GREEN,
        token.String.Symbol: GREEN,

        token.Operator: LIGHT_BLUE,

        token.Generic.Prompt: GREEN,
    }
