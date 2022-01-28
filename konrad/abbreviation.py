# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""Abbreviation
============

Collection of common valid DUDEN abbreviations.

>>> assert 'u.a.' in ABBREVIATION_LOWER

Ensure that abbreviations with/ and without spaces are available.

>>> assert 'a. a. o.' in ABBREVIATION_LOWER

>>> assert ABBREVIATION['a.a.O.'] == ABBREVIATION['a. a. O.']
"""

ABBREVIATION = {
    'Abb.': 'Abbildung',
    'Aufl.': 'Auflage',
    'Bd.': 'Band',
    'Co.': '???',
    'Diss.': 'Dissertation',
    'Dok.': 'Dokument',  # ?
    'Fig.': 'Figure',
    'Forts.': 'Fortsetzung',
    'H.': 'Heft',
    'Hrsg.': 'Herausgeber',
    'Jg.': 'Jahrgang',
    'S.': 'Seite',
    'Sp.': 'Spalte',
    'Tab.': 'Tabelle',
    'Verf.': 'Verfasser',
    'Verl.': 'Verlag',
    'Vol.': 'Volume',
    'a.a.O.': 'am angeführten Ort',
    'al.': '',
    'bspw.': 'beispielsweise',
    'bzw.': 'beziehungsweise',
    'ca.': 'circa',
    'et. al.': 'et alii',  # TODO: CHECK DOTS
    'et.': '',
    'etc.': 'et cetera',
    'evtl.': 'eventuell',
    'f.': '(die) folgende',
    'ff.': '',
    'ggf.': 'gegebenenfalls',
    'lat.': 'latein',
    'mind.': 'mindestens',
    'o.J.': 'ohne Jahrgangsangabe',
    'o.V.': 'ohne Verfasser',
    'o.Ä.': 'ohne Änderung?',
    's.': 'siehe',
    'u.a.': 'unter anderem',
    'usw.': 'und so weiter',
    'vgl.': 'vergleiche',
    'vs.': 'versus',
    'z.B.': 'zum Beispiel',
}

for key, value in list(ABBREVIATION.items()):
    # insert spaces into abbreviation keys
    key = '. '.join(key.split('.')).strip()  # pylint:disable=C0103
    ABBREVIATION[key] = value

ABBREVIATION_LOWER = {item.lower() for item in ABBREVIATION}
