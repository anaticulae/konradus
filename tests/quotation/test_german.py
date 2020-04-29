# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import konrad.quotation.german as german
from konrad.mark import Mark

DOUBLE_QUOTE = [
    Mark.QUOTATION_MARK_DOUBLE_OPEN,
    'Manfred',
    Mark.QUOTATION_MARK_DOUBLE_CLOSE,
]


def test_double_quotation_closed():
    assert german.double_quotation_closed(DOUBLE_QUOTE)


def test_no_double_quotation_inside_double():
    assert german.no_double_quotes_inside_double(DOUBLE_QUOTE)
