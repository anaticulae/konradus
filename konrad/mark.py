# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import enum
import typing

import konrad


class Mark(enum.Enum):
    AND = enum.auto()  # &
    APOSTROPHE = enum.auto()  # '
    BACKSLASH = enum.auto()  # \
    BRACKET = enum.auto()  # ()
    BRACKET_CLOSE = enum.auto()  # )
    BRACKET_ELEPHANT_CLOSE = enum.auto()  # }
    BRACKET_ELEPHANT_OPEN = enum.auto()  # {
    BRACKET_GREATHER = enum.auto()  # >
    BRACKET_OPEN = enum.auto()  # (
    BRACKET_SMALLER = enum.auto()  # <
    COLON = enum.auto()  # :
    COMMA = enum.auto()  # ,
    DASH = enum.auto()  # -
    DOT = enum.auto()  # . in Fig. or Abb. - but not a FULLSTOP
    DOTS = enum.auto()  # ...
    ELLIPSIS = enum.auto()  # '…'
    EN_QUOTATION_MARK_DOUBLE_CLOSE = enum.auto()
    EN_QUOTATION_MARK_DOUBLE_OPEN = enum.auto()
    EN_QUOTATION_MARK_SINGLE_CLOSE = enum.auto()
    EN_QUOTATION_MARK_SINGLE_OPEN = enum.auto()
    EXCLAMATION_MARK = enum.auto()  # !
    FULLSTOP = enum.auto()  # .
    HYPHEN = enum.auto()  # - short dash
    QUESTION_MARK = enum.auto()  #?
    QUOTATION_GUILLEMENTS_DOUBLE_CLOSE = enum.auto()  # «
    QUOTATION_GUILLEMENTS_DOUBLE_OPEN = enum.auto()  # »
    QUOTATION_GUILLEMENTS_SINGLE_CLOSE = enum.auto()  # ‹
    QUOTATION_GUILLEMENTS_SINGLE_OPEN = enum.auto()  # ›
    QUOTATION_MARK = enum.auto()  # '' ""
    QUOTATION_MARK_DOUBLE_CLOSE = enum.auto()
    QUOTATION_MARK_DOUBLE_OPEN = enum.auto()
    QUOTATION_MARK_SINGLE = enum.auto()  # '' ""
    QUOTATION_MARK_SINGLE_CLOSE = enum.auto()
    QUOTATION_MARK_SINGLE_OPEN = enum.auto()
    SEMICOLON = enum.auto()  # ;
    SLASH = enum.auto()  # /
    SQUARE_BRACKET = enum.auto()  # [ ]
    SQUARE_BRACKET_CLOSE = enum.auto()  #  ]
    SQUARE_BRACKET_OPEN = enum.auto()  # [

    def __str__(self):
        """\
        >>> str(Mark.DASH)
        '–'
        >>> str(Mark.EN_QUOTATION_MARK_DOUBLE_CLOSE)
        '”'
        """
        lang = konrad.ENGLISH if str(self.name).startswith('EN_') else None
        return mark2str(self, lang=lang)


Marks = typing.List[Mark]

MATCH = {
    '.': Mark.FULLSTOP,
    ',': Mark.COMMA,
    ':': Mark.COLON,
    ';': Mark.SEMICOLON,
    '?': Mark.QUESTION_MARK,
    '!': Mark.EXCLAMATION_MARK,
    "&": Mark.AND,
    '…': Mark.ELLIPSIS,
    '"': Mark.QUOTATION_MARK,
    "'": Mark.QUOTATION_MARK_SINGLE,
    "„": Mark.QUOTATION_MARK_DOUBLE_OPEN,
    '“': Mark.QUOTATION_MARK_DOUBLE_CLOSE,
    '”': Mark.QUOTATION_MARK_DOUBLE_CLOSE,
    '‚': Mark.QUOTATION_MARK_SINGLE_OPEN,
    '‘': Mark.QUOTATION_MARK_SINGLE_CLOSE,
    '»': Mark.QUOTATION_GUILLEMENTS_DOUBLE_OPEN,
    '«': Mark.QUOTATION_GUILLEMENTS_DOUBLE_CLOSE,
    '›': Mark.QUOTATION_GUILLEMENTS_SINGLE_OPEN,
    '‹': Mark.QUOTATION_GUILLEMENTS_SINGLE_CLOSE,
    '>': Mark.BRACKET_GREATHER,
    '<': Mark.BRACKET_SMALLER,
    "’": Mark.APOSTROPHE,
    '-': Mark.HYPHEN,
    '–': Mark.DASH,
    '...': Mark.DOTS,
    '()': Mark.BRACKET,
    '{': Mark.BRACKET_ELEPHANT_OPEN,
    '}': Mark.BRACKET_ELEPHANT_CLOSE,
    '(': Mark.BRACKET_OPEN,
    ')': Mark.BRACKET_CLOSE,
    '[': Mark.SQUARE_BRACKET_OPEN,
    ']': Mark.SQUARE_BRACKET_CLOSE,
    '/': Mark.SLASH,
    '\\': Mark.BACKSLASH,
}
MATCH_ENG = {
    '“': Mark.EN_QUOTATION_MARK_DOUBLE_OPEN,
    '”': Mark.EN_QUOTATION_MARK_DOUBLE_CLOSE,
    '‘': Mark.EN_QUOTATION_MARK_SINGLE_OPEN,
    "’": Mark.EN_QUOTATION_MARK_SINGLE_CLOSE,
}


def matches(token: str, lang=None) -> Mark:
    """Convert `token` to `Mark` depending on `lang`.

    If `lang` is None, use Language.GERMAN.

    >>> matches(':')
    <Mark.COLON:...>
    >>> matches('”', lang=konrad.ENGLISH)
    <Mark.EN_QUOTATION_MARK_DOUBLE_CLOSE:...>
    """
    if konrad.iseng(lang):
        with contextlib.suppress(KeyError):
            return MATCH_ENG[token]
    return MATCH[token]


def matchesmore(token: str, lang=None) -> Mark:
    with contextlib.suppress(KeyError):
        return matches(token, lang=lang)
    return token


def remove_marks(items: list) -> list:
    assert isinstance(items, list), type(items)
    result = [item for item in items if isinstance(item, str)]
    return result


REVERSED = {value: key for key, value in MATCH.items()}
REVERSED_ENG = {value: key for key, value in MATCH_ENG.items()}


def mark2str(item: Mark, lang=None) -> str:  # pylint:disable=W0613
    """\
    >>> mark2str(konrad.Mark.COMMA)
    ','
    >>> mark2str('Helm')
    'Helm'
    >>> mark2str(konrad.Mark.EN_QUOTATION_MARK_DOUBLE_OPEN, lang=konrad.ENGLISH)
    '“'
    """
    if konrad.iseng(lang):
        with contextlib.suppress(KeyError):
            return REVERSED_ENG[item]
    with contextlib.suppress(KeyError):
        return REVERSED[item]
    return item
