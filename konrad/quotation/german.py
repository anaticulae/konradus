# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import konrad.mark

DOUBLE_OPEN = konrad.mark.Mark.QUOTATION_MARK_DOUBLE_OPEN
DOUBLE_CLOSE = konrad.mark.Mark.QUOTATION_MARK_DOUBLE_CLOSE
SINGLE_OPEN = konrad.mark.Mark.QUOTATION_MARK_SINGLE_OPEN
SINGLE_CLOSE = konrad.mark.Mark.QUOTATION_MARK_SINGLE_CLOSE


def double_quotation_closed(token: list) -> bool:
    open_close = [item for item in token if item in (DOUBLE_OPEN, DOUBLE_CLOSE)]
    if not open_close:
        return True
    double_open = [item for item in open_close if item == DOUBLE_OPEN]
    double_close = [item for item in open_close if item == DOUBLE_CLOSE]
    return len(double_open) == len(double_close)


def no_double_quotes_inside_double(token: list) -> bool:
    """Check if single quotation are used in citation."""
    open_close = [item for item in token if item in (DOUBLE_OPEN, DOUBLE_CLOSE)]
    # ensure alernating
    if not open_close:
        return True
    for current, after in zip(open_close[0:-1], open_close[1:]):
        if current == after:
            # require single marks inside
            # wrong: „zu diesem „etwas“ kontrollieren kann“.
            return False
    return True


def valid_single_marks_count(token: list) -> bool:
    assert isinstance(token, list), type(token)
    single_open = [item for item in token if item == SINGLE_OPEN]
    single_close = [item for item in token if item == SINGLE_CLOSE]

    valid = len(single_open) == len(single_close)
    return valid
