#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================
"""Konrad DUDEN
============

The central approach of this package is store information which are
located in DUDEN and are basic rules for the german language

Difference to `german`
----------------------

The `german` package is a wrapper for external tooling which have some
`magic` inside to determine the type of a word or split a sentence in
valid chunks.

"""

import os

from konradus.abbr import ABBREVIATION
from konradus.abbr import ABBREVIATION_LOWER
from konradus.lang import Language
from konradus.lang import complexlang
from konradus.lang import iseng
from konradus.lang import simplelang
from konradus.mark import HIGHNOTE
from konradus.mark import Mark
from konradus.mark import Marks
from konradus.mark import isspecial
from konradus.mark import mark2str
from konradus.mark import matches
from konradus.mark import matchesmore
from konradus.mark import remove_special
from konradus.sentence import SentenceType
from konradus.sentence import is_formula
from konradus.sentence import is_list
from konradus.sentence import is_listitem
from konradus.sentence import is_listsepa
from konradus.sentence import is_quote
from konradus.sentence import list_split
from konradus.sentence import nosentence
from konradus.sentence import sentence_type
from konradus.sign import DOTS
from konradus.sign import HYPHEN_HALF
from konradus.sign import HYPHEN_QUARTER
from konradus.sign import SIGN

GERMAN = Language.GERMAN
ENGLISH = Language.ENGLISH
FRENCH = Language.FRENCH

__version__ = '0.10.3'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# TODO: REMOVE LATER
remove_marks = remove_special
