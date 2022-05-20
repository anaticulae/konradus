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
ders.                                          derselbe
dies.                                          dieselbe
d.h.                                           das heißt
Diss.                                          Dissertation
Dok.                                           Dokument
ebd.                                           ebenda
et.
et.al.                                         et alii (und andere)
etc.                                           et cetera
evtl.                                          eventuell
f.                                             (die) folgende
ff.                                            fortfolgende Seiten
Fig.                                           Figure
Forts.                                         Fortsetzung
ggf.                                           gegebenenfalls
H.                                             Heft
Habil.                                         Habilitationsschrift
Hrsg.                                          Herausgeber
hrsg.v.                                        herausgegeben von
ibd.                                           ibidem
Jg.                                            Jahrgang
Kap.                                           Kapitel
lat.                                           latein
loc.cit.                                       loco citato (am aufgeführten Ort)
mind.                                          mindestens
Nachdr.                                        Nachdruck
N.N.                                           nomen nominandum
Nr.                                            Nummer
No.                                            Number
o.A.                                           ohne Autor
o.O                                            ohne Ort
o.J.                                           ohne Jahrgangsangabe
o.S.                                           ohne Seitenangabe
o.V.                                           ohne Verfasser
o.Ä.                                           ohne Änderung?
pass.                                          passim (da und dort/verstreut)
S.                                             Seite(n)
s.                                             siehe
Sp.                                            Spalte(n)
Tab.                                           Tabelle
überarb.                                       überarbeitet
u.a.                                           unter anderem??/und andere
usw.                                           und so weiter
Verf.                                          Verfasser
Verl.                                          Verlag
vgl.                                           vergleiche
Vol.                                           Volume (Band)
vs.                                            versus
z.B.                                           zum Beispiel
zit.n.                                         zitiert nach
zit.nach                                       zitiert nach
""")

for key, value in list(ABBREVIATION.items()):
    # insert spaces into abbreviation keys
    key = '. '.join(key.split('.')).strip()  # pylint:disable=C0103
    ABBREVIATION[key] = value

ABBREVIATION_LOWER = {item.lower() for item in ABBREVIATION}
