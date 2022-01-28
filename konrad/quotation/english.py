# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import konrad.mark

DOUBLE_OPEN = konrad.mark.Mark.QUOTATION_MARK_DOUBLE_OPEN


def valid_double_marks_count_english(token: list):
    # TODO: DOUBLE_OPEN IS CURRENTLY GERMAN OPEN
    german_open = [item for item in token if item == DOUBLE_OPEN]
    if any(german_open):
        return False
    return True
