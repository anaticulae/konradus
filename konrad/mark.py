# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import enum
import typing

import konrad.lang


class Mark(enum.Enum):
    FULLSTOP = enum.auto()  # .
    COMMA = enum.auto()  # ,
    COLON = enum.auto()  # :
    SEMICOLON = enum.auto()  # ;
    QUESTION_MARK = enum.auto()  #?
    EXCLAMATION_MARK = enum.auto()  # !
    AND = enum.auto()  # &
    APOSTROPHE = enum.auto()  # '
    QUOTATION_MARK_DOUBLE_OPEN = enum.auto()
    QUOTATION_MARK_DOUBLE_CLOSE = enum.auto()
    QUOTATION_MARK_SINGLE_OPEN = enum.auto()
    QUOTATION_MARK_SINGLE_CLOSE = enum.auto()
    HYPHEN = enum.auto()  # - short dash
    DASH = enum.auto()  # -
    DOTS = enum.auto()  # ...
    BRACKET = enum.auto()  # ()
    BRACKET_OPEN = enum.auto()  # (
    BRACKET_CLOSE = enum.auto()  # )
    SQUARE_BRACKET = enum.auto()  # [ ]
    SQUARE_BRACKET_OPEN = enum.auto()  # [
    SQUARE_BRACKET_CLOSE = enum.auto()  #  ]
    QUOTATION_MARK = enum.auto()  # '' ""
    QUOTATION_MARK_SINGLE = enum.auto()  # '' ""

    @classmethod
    def fromstr(cls, item: str):
        """Convert str to `Mark`."""
        return MATCH[item]


Marks = typing.List[Mark]

MATCH = {
    '.': Mark.FULLSTOP,
    ',': Mark.COMMA,
    ':': Mark.COLON,
    ';': Mark.SEMICOLON,
    '?': Mark.QUESTION_MARK,
    '!': Mark.EXCLAMATION_MARK,
    "&": Mark.AND,
    '"': Mark.QUOTATION_MARK,
    "'": Mark.QUOTATION_MARK_SINGLE,
    "„": Mark.QUOTATION_MARK_DOUBLE_OPEN,
    '“': Mark.QUOTATION_MARK_DOUBLE_CLOSE,  # english open
    '”': Mark.QUOTATION_MARK_DOUBLE_CLOSE,
    '‚': Mark.QUOTATION_MARK_SINGLE_OPEN,
    '‘': Mark.QUOTATION_MARK_SINGLE_CLOSE,
    "’": Mark.APOSTROPHE,
    '-': Mark.HYPHEN,
    '–': Mark.DASH,
    '...': Mark.DOTS,
    '()': Mark.BRACKET,
    '(': Mark.BRACKET_OPEN,
    ')': Mark.BRACKET_CLOSE,
    '[': Mark.SQUARE_BRACKET_OPEN,
    ']': Mark.SQUARE_BRACKET_CLOSE,
}


def matches(token: str, lang=None) -> Mark:
    """Convert `token` to `Mark` depending on `lang`. If `lang` is None
    use Language.GERMAN.

    >>> matches(':')
    <Mark.COLON: 3>
    """
    # TODO: MAKE MATCH LANG DEPEDEND
    lang = konrad.lang.Language.GERMAN if lang is None else lang
    return MATCH[token]


def remove_marks(items: list) -> list:
    assert isinstance(items, list), type(items)
    result = [item for item in items if isinstance(item, str)]
    return result


REVERSED = {value: key for key, value in MATCH.items()}


def mark2str(item: Mark, lang=None) -> str:  # pylint:disable=W0613
    """\
    >>> mark2str(konrad.Mark.COMMA)
    ','
    >>> mark2str('Helm')
    'Helm'
    """
    with contextlib.suppress(KeyError):
        item = REVERSED[item]
    return item
