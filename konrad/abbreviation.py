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

import konrad.utils

ABBREVIATION = konrad.utils.parse_table("""\
a.a.O.                                         am angeführten Ort
Abb.                                           Abbildung
al.
Aufl.                                          Auflage
Bd.                                            Band
bspw.                                          beispielsweise
bzw.                                           beziehungsweise
ca.                                            circa
Co.                                            ???
Diss.                                          Dissertation
Dok.                                           Dokument
et.
et. al.                                        et alii
etc.                                           et cetera
evtl.                                          eventuell
f.                                             (die) folgende
ff.
Fig.                                           Figure
Forts.                                         Fortsetzung
ggf.                                           gegebenenfalls
H.                                             Heft
Hrsg.                                          Herausgeber
Jg.                                            Jahrgang
lat.                                           latein
mind.                                          mindestens
o.A.                                           ohne Autor
o.J.                                           ohne Jahrgangsangabe
o.V.                                           ohne Verfasser
o.Ä.                                           ohne Änderung?
S.                                             Seite
Sp.                                            Spalte
s.                                             siehe
Tab.                                           Tabelle
u.a.                                           unter anderem
usw.                                           und so weiter
vgl.                                           vergleiche
vs.                                            versus
Verf.                                          Verfasser
Verl.                                          Verlag
Vol.                                           Volume
z.B.                                           zum Beispiel
""")

for key, value in list(ABBREVIATION.items()):
    # insert spaces into abbreviation keys
    key = '. '.join(key.split('.')).strip()  # pylint:disable=C0103
    ABBREVIATION[key] = value

ABBREVIATION_LOWER = {item.lower() for item in ABBREVIATION}
