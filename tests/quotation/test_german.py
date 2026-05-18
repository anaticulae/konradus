# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

# import german

import konradus.quotation.german as german_quotes
from konradus.mark import Mark

DOUBLE_QUOTE = [
    Mark.QUOTATION_MARK_DOUBLE_OPEN,
    'Manfred',
    Mark.QUOTATION_MARK_DOUBLE_CLOSE,
]


def test_double_quotation_closed():
    assert german_quotes.double_quotation_closed(DOUBLE_QUOTE)


def test_no_double_quotation_inside_double():
    assert german_quotes.no_double_quotes_inside_double(DOUBLE_QUOTE)


STANDARD = """„Protest“, so schreibt Sigrid Baringhorst, „ist
kommunikatives Handeln“ (1998: 327). Will man das Phänomen ‚Protest‘
angemessen erfassen, so gilt es zu untersuchen, wie er kommuniziert
wird."""

# def test_german_double_quote():
#     first = german.word_tokenize(german.sentence_tokenize(STANDARD)[0])
#     assert german_quotes.double_quotation_closed(first)
#     assert german_quotes.no_double_quotes_inside_double(first)

REQUIRE_SINGLE_INSIDE = """\
Bevor die Konzepte der Privatheit und Öffentlichkeit \
systemtheoretisch näher betrachtet werden, soll vorab kurz umrissen \
werden, was darunter verstanden wird. Rössler beschreibt etwas \
Privates folgendermaßen: „‚privat‘ nennen wir einerseits Handlungs- \
und Verhaltensweisen, zum Zweiten ein bestimmtes Wissen und drittens \
Räume“ und weiter: „als privat gilt etwas dann, wenn man selbst \
den Zugang zu diesem „etwas“ kontrollieren kann“. Privatheit \
beinhaltet also den Aspekt der Zugangskontrolle seitens des \
Individuums.
"""

# def test_german_double_quote_inside_double():
#     splitted = german.sentence_tokenize(REQUIRE_SINGLE_INSIDE)
#     assert len(splitted) == 5
#     no_double = german.word_tokenize(splitted[1])
#     assert german_quotes.no_double_quotes_inside_double(no_double)
#     double_inside = german.word_tokenize(splitted[3])
#     assert not german_quotes.no_double_quotes_inside_double(double_inside)
