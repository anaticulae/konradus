# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import re

import utila


def parse_table(raw: str) -> dict:
    # TODO: MOVE TO UTILA
    result = dict()
    for line in raw.strip().splitlines():
        splitted = re.split(r'\s{10,}', line)
        key = splitted[0]
        if len(splitted) == 1:
            result[key] = 'NO VALUE'
            utila.debug(f'EMPTY VALUE: {line}')
        else:
            value = splitted[1]
            result[key] = value
    return result
