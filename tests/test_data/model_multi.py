#!/usr/bin/python3

import moiety_modeling
import jsonpickle


ribose2 = moiety_modeling.Moiety("ribose", {'13C': 5, '18O': 4}, states=['13C_0.18O_0', '13C_5.18O_4'], nickname='r')
glucose2 = moiety_modeling.Moiety("glucose", {'13C': 6, '18O': 5}, states=['13C_0.18O_0', '13C_6.18O_5'], nickname='g')
acetyl2 = moiety_modeling.Moiety("acetyl", {'13C': 2, '18O': 1}, states=['13C_0.18O_0', '13C_2.18O_1'], nickname='a')
uracil2 = moiety_modeling.Moiety("uracil", {'13C': 4, '18O': 2}, states=['13C_0.18O_0', '13C_1.18O_0', '13C_2.18O_1', '13C_2.18O_0', '13C_3.18O_0', '13C_3.18O_1'], nickname='u')

UDP_GlcNAC2 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose2, glucose2, acetyl2, uracil2])

model2 = moiety_modeling.Model('best_model_multi', [ribose2, glucose2, acetyl2, uracil2], [UDP_GlcNAC2])

models = { 'models' : [ model2 ]}

jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
with open('model_multi.json', 'w') as outFile:
    outFile.write(jsonpickle.encode(models))

