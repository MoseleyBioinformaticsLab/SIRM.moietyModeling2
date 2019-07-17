#!/usr/bin/python3

import moiety_modeling
import jsonpickle


ribose1 = moiety_modeling.Moiety("ribose", {'13C': 5}, isotopeStates={'13C': [0, 5]}, nickname='r')
glucose1 = moiety_modeling.Moiety("glucose", {'13C': 6}, isotopeStates={'13C': [0, 6]}, nickname='g')
acetyl1 = moiety_modeling.Moiety("acetyl", {'13C': 2}, isotopeStates={'13C': [0, 2]}, nickname='a')
uracil1 = moiety_modeling.Moiety("uracil", {'13C': 4}, isotopeStates={'13C': [0, 1, 2, 3]}, nickname='u')

UDP_GlcNAC1 = moiety_modeling.Molecule('UDP_GlcNAC', [ribose1, glucose1, acetyl1, uracil1])

model1 = moiety_modeling.Model('best_model_single', [ribose1, glucose1, acetyl1, uracil1], [UDP_GlcNAC1])

models = { 'models' : [ model1]}

jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
with open('model_single.json', 'w') as outFile:
    outFile.write(jsonpickle.encode(models))

