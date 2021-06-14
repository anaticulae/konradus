# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import enum


class Language(enum.Enum):
    GERMAN = enum.auto()
    ENGLISH = enum.auto()
    FRENCH = enum.auto()
    UNKNOWN = enum.auto()


LANGUAGE = {
    Language.GERMAN: 'ger',
    Language.ENGLISH: 'eng',
    Language.FRENCH: 'fre',
    Language.UNKNOWN: 'none',
}


def simplelang(lang: Language):
    return LANGUAGE[lang]


ENGLISH = {'eng', 'english', Language.ENGLISH}


def iseng(lang: Language) -> bool:
    """\
    >>> iseng(Language.ENGLISH)
    True
    """
    if lang is None:
        return False
    return lang in ENGLISH
