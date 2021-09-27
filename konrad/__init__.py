#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
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

from konrad.abbreviation import ABBREVIATION
from konrad.abbreviation import ABBREVIATION_LOWER
from konrad.lang import Language
from konrad.lang import complexlang
from konrad.lang import iseng
from konrad.lang import simplelang
from konrad.mark import Mark
from konrad.mark import Marks
from konrad.mark import mark2str
from konrad.mark import matches
from konrad.mark import matchesmore
from konrad.mark import remove_marks
from konrad.sign import DOTS
from konrad.sign import HYPHEN_HALF
from konrad.sign import HYPHEN_QUARTER
from konrad.sign import SIGN

GERMAN = Language.GERMAN
ENGLISH = Language.ENGLISH
FRENCH = Language.FRENCH

__version__ = '0.7.1'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
