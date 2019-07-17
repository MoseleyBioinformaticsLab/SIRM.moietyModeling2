#!/usr/bin/python3

import moiety_modeling
import jsonpickle


ribose1 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 2, 3, 5]}, nickname='r')
glucose1 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 3, 6]}, nickname='g')
acetyl1 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 2]}, nickname='a')
uracil1 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

relationship1_1 = moiety_modeling.Relationship(glucose1, '13C3', ribose1, '13C2', '*', 2)
relationship1_2 = moiety_modeling.Relationship(ribose1, '13C3', ribose1, '13C2')
relationship1_3 = moiety_modeling.Relationship(glucose1, '13C0', ribose1, '13C0')
relationship1_4 = moiety_modeling.Relationship(glucose1, '13C6', ribose1, '13C5')

UDP_GlcNAC1 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose1, glucose1, acetyl1, uracil1])

model1 = moiety_modeling.Model('6_G0R2A1U3_g3r2r3_g6r5', [ribose1, glucose1, acetyl1, uracil1], [UDP_GlcNAC1], [relationship1_1, relationship1_2, relationship1_3, relationship1_4])


ribose2 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 5]}, nickname='r')
glucose2 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 6]}, nickname='g')
acetyl2 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 1]}, nickname='a')
uracil2 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC2 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose2, glucose2, acetyl2, uracil2])

model2 = moiety_modeling.Model('6_G1R1A1U3_a1', [ribose2, glucose2, acetyl2, uracil2], [UDP_GlcNAC2])


ribose3 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 5]}, nickname='r')
glucose3 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 5]}, nickname='g')
acetyl3 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 2]}, nickname='a')
uracil3 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC3 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose3, glucose3, acetyl3, uracil3])

model3 = moiety_modeling.Model('6_G1R1A1U3_g5', [ribose3, glucose3, acetyl3, uracil3], [UDP_GlcNAC3])


ribose4 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 4]}, nickname='r')
glucose4 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 6]}, nickname='g')
acetyl4 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 2]}, nickname='a')
uracil4 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC4 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose4, glucose4, acetyl4, uracil4])

model4 = moiety_modeling.Model('6_G1R1A1U3_r4', [ribose4, glucose4, acetyl4, uracil4], [UDP_GlcNAC4])


ribose5 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 5]}, nickname='r')
glucose5 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 6]}, nickname='g')
acetyl5 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 2]}, nickname='a')
uracil5 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 4]}, nickname='u')

UDP_GlcNAC5 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose5, glucose5, acetyl5, uracil5])

model5 = moiety_modeling.Model('6_G1R1A1U3', [ribose5, glucose5, acetyl5, uracil5], [UDP_GlcNAC5])


ribose6 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 2, 3, 5]}, nickname='r')
glucose6 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 3, 6]}, nickname='g')
acetyl6 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 1, 2]}, nickname='a')
uracil6 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

relationship6_1 = moiety_modeling.Relationship(glucose6, '13C3', ribose6, '13C2', '*', 2)
relationship6_2 = moiety_modeling.Relationship(ribose6, '13C3', ribose6, '13C2')
relationship6_3 = moiety_modeling.Relationship(glucose6, '13C0', ribose6, '13C0')
relationship6_4 = moiety_modeling.Relationship(glucose6, '13C6', ribose6, '13C5')

UDP_GlcNAC6 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose6, glucose6, acetyl6, uracil6])

model6 = moiety_modeling.Model('7_G0R2A2U3_g3r2r3_g6r5', [ribose6, glucose6, acetyl6, uracil6], [UDP_GlcNAC6], [relationship6_1, relationship6_2, relationship6_3, relationship6_4])


ribose7 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 2, 3, 4, 5]}, nickname='r')
glucose7 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 3, 5, 6]}, nickname='g')
acetyl7 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 2]}, nickname='a')
uracil7 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

relationship7_1 = moiety_modeling.Relationship(glucose7, '13C3', ribose7, '13C2', '*', 2)
relationship7_2 = moiety_modeling.Relationship(ribose7, '13C3', ribose7, '13C2')
relationship7_3 = moiety_modeling.Relationship(glucose7, '13C0', ribose7, '13C0')
relationship7_4 = moiety_modeling.Relationship(glucose7, '13C6', ribose7, '13C5')
relationship7_5 = moiety_modeling.Relationship(glucose7, '13C5', ribose7, '13C4')

UDP_GlcNAC7 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose7, glucose7, acetyl7, uracil7])

model7 = moiety_modeling.Model('7_G0R3A1U3_g3r2r3_g6r5_g5r4', [ribose7, glucose7, acetyl7, uracil7], [UDP_GlcNAC7], [relationship7_1, relationship7_2, relationship7_3, relationship7_4, relationship7_5])


ribose8 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 2, 3, 4, 5]}, nickname='r')
glucose8 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 3, 6]}, nickname='g')
acetyl8 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 2]}, nickname='a')
uracil8 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

relationship8_1 = moiety_modeling.Relationship(glucose8, '13C3', ribose8, '13C2', '*', 2)
relationship8_2 = moiety_modeling.Relationship(ribose8, '13C3', ribose8, '13C2')
relationship8_3 = moiety_modeling.Relationship(glucose8, '13C0', ribose8, '13C0')
relationship8_4 = moiety_modeling.Relationship(glucose8, '13C6', ribose8, '13C5')

UDP_GlcNAC8 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose8, glucose8, acetyl8, uracil8])

model8 = moiety_modeling.Model('7_G0R3A1U3_g3r2r3_g6r5_r4', [ribose8, glucose8, acetyl8, uracil8], [UDP_GlcNAC8], [relationship8_1, relationship8_2, relationship8_3, relationship8_4])


ribose9 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 5]}, nickname='r')
glucose9 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 6]}, nickname='g')
acetyl9 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 2]}, nickname='a')
uracil9 = moiety_modeling.Moiety("uracil", {'13C': 3}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')
CO29 = moiety_modeling.Moiety("CO2", {'13C': 1}, isotopeStates={'13C': [0, 1]}, nickname='c')

UDP_GlcNAC9 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose9, glucose9, acetyl9, uracil9, CO29])

model9 = moiety_modeling.Model('7_G1R1A1U3C1', [ribose9, glucose9, acetyl9, uracil9, CO29], [UDP_GlcNAC9])


ribose10 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 5]}, nickname='r')
glucose10 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 6]}, nickname='g')
acetyl10 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 2]}, nickname='a')
uracil10 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3, 4]}, nickname='u')

UDP_GlcNAC10 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose10, glucose10, acetyl10, uracil10])

model10 = moiety_modeling.Model('7_G1R1A1U4', [ribose10, glucose10, acetyl10, uracil10], [UDP_GlcNAC10])


ribose11 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 5]}, nickname='r')
glucose11 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 6]}, nickname='g')
acetyl11 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 1, 2]}, nickname='a')
uracil11 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC11 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose11, glucose11, acetyl11, uracil11])

model11 = moiety_modeling.Model('7_G1R1A2U3', [ribose11, glucose11, acetyl11, uracil11], [UDP_GlcNAC11])


ribose12 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 2, 3, 5]}, nickname='r')
glucose12 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 3, 6]}, nickname='g')
acetyl12 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 2]}, nickname='a')
uracil12 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

relationship12_1 = moiety_modeling.Relationship(glucose12, '13C3', ribose12, '13C2', '*', 2)
relationship12_2 = moiety_modeling.Relationship(ribose12, '13C3', ribose12, '13C2')

UDP_GlcNAC12 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose12, glucose12, acetyl12, uracil12])

model12 = moiety_modeling.Model('7_G1R2A1U3_g3r2r3', [ribose12, glucose12, acetyl12, uracil12], [UDP_GlcNAC12], [relationship12_1, relationship12_2])


ribose13 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 1, 5]}, nickname='r')
glucose13 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 6]}, nickname='g')
acetyl13 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 2]}, nickname='a')
uracil13 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC13 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose13, glucose13, acetyl13, uracil13])

model13 = moiety_modeling.Model('7_G1R2A1U3_r1', [ribose13, glucose13, acetyl13, uracil13], [UDP_GlcNAC13])


ribose14 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 2, 5]}, nickname='r')
glucose14 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 6]}, nickname='g')
acetyl14 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 2]}, nickname='a')
uracil14 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC14 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose14, glucose14, acetyl14, uracil14])

model14 = moiety_modeling.Model('7_G1R2A1U3_r2', [ribose14, glucose14, acetyl14, uracil14], [UDP_GlcNAC14])


ribose15 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 3, 5]}, nickname='r')
glucose15 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 6]}, nickname='g')
acetyl15 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 2]}, nickname='a')
uracil15 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC15 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose15, glucose15, acetyl15, uracil15])

model15 = moiety_modeling.Model('7_G1R2A1U3_r3', [ribose15, glucose15, acetyl15, uracil15], [UDP_GlcNAC15])


ribose16 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 4, 5]}, nickname='r')
glucose16 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 6]}, nickname='g')
acetyl16 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 2]}, nickname='a')
uracil16 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC16 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose16, glucose16, acetyl16, uracil16])

model16 = moiety_modeling.Model('7_G1R2A1U3_r4', [ribose16, glucose16, acetyl16, uracil16], [UDP_GlcNAC16])


ribose17 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 5]}, nickname='r')
glucose17 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 1, 6]}, nickname='g')
acetyl17 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 2]}, nickname='a')
uracil17 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC17 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose17, glucose17, acetyl17, uracil17])

model17 = moiety_modeling.Model('7_G2R1A1U3_g1', [ribose17, glucose17, acetyl17, uracil17], [UDP_GlcNAC17])


ribose18 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 5]}, nickname='r')
glucose18 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 2, 6]}, nickname='g')
acetyl18 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 2]}, nickname='a')
uracil18 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC18 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose18, glucose18, acetyl18, uracil18])

model18 = moiety_modeling.Model('7_G2R1A1U3_g2', [ribose18, glucose18, acetyl18, uracil18], [UDP_GlcNAC18])


ribose19 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 5]}, nickname='r')
glucose19 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 3, 6]}, nickname='g')
acetyl19 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 2]}, nickname='a')
uracil19 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC19 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose19, glucose19, acetyl19, uracil19])

model19 = moiety_modeling.Model('7_G2R1A1U3_g3', [ribose19, glucose19, acetyl19, uracil19], [UDP_GlcNAC19])


ribose20 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 5]}, nickname='r')
glucose20 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 4, 6]}, nickname='g')
acetyl20 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 2]}, nickname='a')
uracil20 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC20 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose20, glucose20, acetyl20, uracil20])

model20 = moiety_modeling.Model('7_G2R1A1U3_g4', [ribose20, glucose20, acetyl20, uracil20], [UDP_GlcNAC20])


ribose21 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 5]}, nickname='r')
glucose21 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 5, 6]}, nickname='g')
acetyl21 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 2]}, nickname='a')
uracil21 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC21 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose21, glucose21, acetyl21, uracil21])

model21 = moiety_modeling.Model('7_G2R1A1U3_g5', [ribose21, glucose21, acetyl21, uracil21], [UDP_GlcNAC21])


ribose22 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 5]}, nickname='r')
glucose22 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 6]}, nickname='g')
acetyl22 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 1, 2]}, nickname='a')
uracil22 = moiety_modeling.Moiety("uracil", {'13C': 3}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')
CO222 = moiety_modeling.Moiety("CO2", {'13C': 1}, isotopeStates={'13C': [0, 1]}, nickname='c')

UDP_GlcNAC22 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose22, glucose22, acetyl22, uracil22, CO222])

model22 = moiety_modeling.Model('8_G1R1A2U3C1', [ribose22, glucose22, acetyl22, uracil22, CO222], [UDP_GlcNAC22])


ribose23 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 2, 3, 5]}, nickname='r')
glucose23 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 3, 6]}, nickname='g')
acetyl23 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 1, 2]}, nickname='a')
uracil23 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

relationship23_1 = moiety_modeling.Relationship(glucose23, '13C3', ribose23, '13C2', '*', 2)
relationship23_2 = moiety_modeling.Relationship(ribose23, '13C3', ribose23, '13C2')

UDP_GlcNAC23 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose23, glucose23, acetyl23, uracil23])

model23 = moiety_modeling.Model('8_G1R2A2U3_g3r2r3', [ribose23, glucose23, acetyl23, uracil23], [UDP_GlcNAC23], [relationship23_1, relationship23_2])


ribose24 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 2, 3, 5]}, nickname='r')
glucose24 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 3, 5, 6]}, nickname='g')
acetyl24 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 1, 2]}, nickname='a')
uracil24 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

relationship24_2 = moiety_modeling.Relationship(glucose24, '13C6', ribose24, '13C5')
relationship24_1 = moiety_modeling.Relationship(ribose24, '13C3', ribose24, '13C2')
relationship24_3 = moiety_modeling.Relationship(glucose24, '13C3', ribose24, '13C2', '*', 2)

UDP_GlcNAC24 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose24, glucose24, acetyl24, uracil24])

model24 = moiety_modeling.Model('8_G1R2A2U3_g3r2r3_g6r5_g5', [ribose24, glucose24, acetyl24, uracil24], [UDP_GlcNAC24], [relationship24_1, relationship24_2, relationship24_3])


ribose25 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 1, 5]}, nickname='r')
glucose25 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 6]}, nickname='g')
acetyl25 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 1, 2]}, nickname='a')
uracil25 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC25 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose25, glucose25, acetyl25, uracil25])

model25 = moiety_modeling.Model('8_G1R2A2U3_r1', [ribose25, glucose25, acetyl25, uracil25], [UDP_GlcNAC25])


ribose26 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 2, 5]}, nickname='r')
glucose26 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 6]}, nickname='g')
acetyl26 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 1, 2]}, nickname='a')
uracil26 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC26 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose26, glucose26, acetyl26, uracil26])

model26 = moiety_modeling.Model('8_G1R2A2U3_r2', [ribose26, glucose26, acetyl26, uracil26], [UDP_GlcNAC26])


ribose27 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 2, 3, 5]}, nickname='r')
glucose27 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 6]}, nickname='g')
acetyl27 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 1, 2]}, nickname='a')
uracil27 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC27 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose27, glucose27, acetyl27, uracil27])

relationship27_1 = moiety_modeling.Relationship(ribose27, '13C3', ribose27, '13C2')

model27 = moiety_modeling.Model('8_G1R2A2U3_r2r3', [ribose27, glucose27, acetyl27, uracil27], [UDP_GlcNAC27], [relationship27_1])


ribose28 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 3, 5]}, nickname='r')
glucose28 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 6]}, nickname='g')
acetyl28 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 1, 2]}, nickname='a')
uracil28 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC28 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose28, glucose28, acetyl28, uracil28])

model28 = moiety_modeling.Model('8_G1R2A2U3_r3', [ribose28, glucose28, acetyl28, uracil28], [UDP_GlcNAC28])


ribose29 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 4, 5]}, nickname='r')
glucose29 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 6]}, nickname='g')
acetyl29 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 1, 2]}, nickname='a')
uracil29 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC29 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose29, glucose29, acetyl29, uracil29])

model29 = moiety_modeling.Model('8_G1R2A2U3_r4', [ribose29, glucose29, acetyl29, uracil29], [UDP_GlcNAC29])


ribose30 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 5]}, nickname='r')
glucose30 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 1, 6]}, nickname='g')
acetyl30 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 1, 2]}, nickname='a')
uracil30 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC30 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose30, glucose30, acetyl30, uracil30])

model30 = moiety_modeling.Model('8_G2R1A2U3_g1', [ribose30, glucose30, acetyl30, uracil30], [UDP_GlcNAC30])


ribose31 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 5]}, nickname='r')
glucose31 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 2, 6]}, nickname='g')
acetyl31 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 1, 2]}, nickname='a')
uracil31 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC31 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose31, glucose31, acetyl31, uracil31])

model31 = moiety_modeling.Model('8_G2R1A2U3_g2', [ribose31, glucose31, acetyl31, uracil31], [UDP_GlcNAC31])


ribose32 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 5]}, nickname='r')
glucose32 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 3, 6]}, nickname='g')
acetyl32 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 1, 2]}, nickname='a')
uracil32 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC32 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose32, glucose32, acetyl32, uracil32])

model32 = moiety_modeling.Model('8_G2R1A2U3_g3', [ribose32, glucose32, acetyl32, uracil32], [UDP_GlcNAC32])


ribose33 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 5]}, nickname='r')
glucose33 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 4, 6]}, nickname='g')
acetyl33 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 1, 2]}, nickname='a')
uracil33 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC33 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose33, glucose33, acetyl33, uracil33])

model33 = moiety_modeling.Model('8_G2R1A2U3_g4', [ribose33, glucose33, acetyl33, uracil33], [UDP_GlcNAC33])


ribose34 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 5]}, nickname='r')
glucose34 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 5, 6]}, nickname='g')
acetyl34 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 1, 2]}, nickname='a')
uracil34 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC34 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose34, glucose34, acetyl34, uracil34])

model34 = moiety_modeling.Model('8_G2R1A2U3_g5', [ribose34, glucose34, acetyl34, uracil34], [UDP_GlcNAC34])


ribose35 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 2, 3, 5]}, nickname='r')
glucose35 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 1, 6]}, nickname='g')
acetyl35 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 1, 2]}, nickname='a')
uracil35 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC35 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose35, glucose35, acetyl35, uracil35])

relationship35_1 = moiety_modeling.Relationship(ribose35, '13C3', ribose35, '13C2')

model35 = moiety_modeling.Model('9_G2R2A2U3_r2r3_g1', [ribose35, glucose35, acetyl35, uracil35], [UDP_GlcNAC35], [relationship35_1])


ribose36 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 2, 3, 5]}, nickname='r')
glucose36 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 2, 6]}, nickname='g')
acetyl36 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 1, 2]}, nickname='a')
uracil36 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC36 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose36, glucose36, acetyl36, uracil36])

relationship36_1 = moiety_modeling.Relationship(ribose36, '13C3', ribose36, '13C2')

model36 = moiety_modeling.Model('9_G2R2A2U3_r2r3_g2', [ribose36, glucose36, acetyl36, uracil36], [UDP_GlcNAC36], [relationship36_1])


ribose37 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 2, 3, 5]}, nickname='r')
glucose37 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 3, 6]}, nickname='g')
acetyl37 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 1, 2]}, nickname='a')
uracil37 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC37 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose37, glucose37, acetyl37, uracil37])

relationship37_1 = moiety_modeling.Relationship(ribose37, '13C3', ribose37, '13C2')

model37 = moiety_modeling.Model('9_G2R2A2U3_r2r3_g3', [ribose37, glucose37, acetyl37, uracil37], [UDP_GlcNAC37], [relationship37_1])


ribose38 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 2, 3, 5]}, nickname='r')
glucose38 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 4, 6]}, nickname='g')
acetyl38 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 1, 2]}, nickname='a')
uracil38 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC38 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose38, glucose38, acetyl38, uracil38])

relationship38_1 = moiety_modeling.Relationship(ribose38, '13C3', ribose38, '13C2')

model38 = moiety_modeling.Model('9_G2R2A2U3_r2r3_g4', [ribose38, glucose38, acetyl38, uracil38], [UDP_GlcNAC38], [relationship38_1])


ribose39 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 2, 3, 5]}, nickname='r')
glucose39 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 5, 6]}, nickname='g')
acetyl39 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 1, 2]}, nickname='a')
uracil39 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC39 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose39, glucose39, acetyl39, uracil39])

relationship39_1 = moiety_modeling.Relationship(ribose39, '13C3', ribose39, '13C2')

model39 = moiety_modeling.Model('9_G2R2A2U3_r2r3_g5', [ribose39, glucose39, acetyl39, uracil39], [UDP_GlcNAC39], [relationship39_1])


ribose40 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 2, 3, 5]}, nickname='r')
glucose40 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 3, 5, 6]}, nickname='g')
acetyl40 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 1, 2]}, nickname='a')
uracil40 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

relationship40_2 = moiety_modeling.Relationship(glucose40, '13C6', ribose40, '13C5')
relationship40_1 = moiety_modeling.Relationship(ribose40, '13C3', ribose40, '13C2')

UDP_GlcNAC40 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose40, glucose40, acetyl40, uracil40])

model40 = moiety_modeling.Model('9_G2R2A2U3_r2r3_g6r5_g3_g5', [ribose40, glucose40, acetyl40, uracil40], [UDP_GlcNAC40], [relationship40_1, relationship40_2])


ribose41 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 5]}, nickname='r')
glucose41 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 6]}, nickname='g')
acetyl41 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 2]}, nickname='a')
uracil41 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC41 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose41, glucose41, acetyl41, uracil41])

model41 = moiety_modeling.Model('best_model', [ribose41, glucose41, acetyl41, uracil41], [UDP_GlcNAC41])

models = { 'models' : [ model1, model2, model3, model4, model5, model6, model7, model8, model9, model10, model11, model12, model13, model14, model15, model16, model17, model18, model19, model20, model21, model22, model23,
 model24, model25, model26, model27, model28, model29, model30, model31, model32, model33, model34, model35, model36, model37, model38, model39, model40, model41]}


jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
with open('all_single_models.json', 'w') as outFile:
    outFile.write(jsonpickle.encode(models))
