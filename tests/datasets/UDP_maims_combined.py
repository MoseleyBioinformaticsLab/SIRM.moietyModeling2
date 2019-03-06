#!/usr/bin/python3

import moiety_modeling
import jsonpickle


dataset1 = moiety_modeling.Dataset("24h", {'UDP_GlcNAC': [{'labelingIsotopes': '13C0', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C1', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C2', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C3', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C4', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C5', 'height': 0.029666287, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C6', 'height': 0.02772308, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C7', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C8', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C9', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C10', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C11', 'height': 0.11405327, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C12', 'height': 0.04114416, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C13', 'height': 0.691677894, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C14', 'height': 0.048813349, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C15', 'height': 0.046921961, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C16', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C17', 'height': 0, 'heightSE': 0}]})

dataset2 = moiety_modeling.Dataset("48h", {'UDP_GlcNAC': [{'labelingIsotopes': '13C0', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C1', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C2', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C3', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C4', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C5', 'height': 0.017323401, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C6', 'height': 0.005577785, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C7', 'height': 0.010122988, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C8', 'height': 0.0385743, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C9', 'height': 0.0021297, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C10', 'height': 0.01521214, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C11', 'height': 0.132576107, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C12', 'height': 0.112099644, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C13', 'height': 0.390518688, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C14', 'height': 0.144054358, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C15', 'height': 0.115603046, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C16', 'height': 0.016207844, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C17', 'height': 0, 'heightSE': 0}]})

dataset3 = moiety_modeling.Dataset("72h", {'UDP_GlcNAC': [{'labelingIsotopes': '13C0', 'height': 0.0050033, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C1', 'height': 0.00094257, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C2', 'height': 0.00099737, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C3', 'height': 0.00065213, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C4', 'height': 0.0037484, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C5', 'height': 0.041111, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C6', 'height': 0.029762, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C7', 'height': 0.036908, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C8', 'height': 0.046745, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C9', 'height': 0.017722, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C10', 'height': 0.033593, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C11', 'height': 0.11357, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C12', 'height': 0.099003, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C13', 'height': 0.29721, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C14', 'height': 0.12134, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C15', 'height': 0.10877, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C16', 'height': 0.043753, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C17', 'height': 0.00056993, 'heightSE': 0}]})

dataset4 = moiety_modeling.Dataset("maims_12h", {
    'UDP_GlcNAC': [{'labelingIsotopes': '13C0', 'height': 0.0175442549, 'heightSE': 0},
                   {'labelingIsotopes': '13C1', 'height': 0, 'heightSE': 0},
                   {'labelingIsotopes': '13C2', 'height': 0.0007113347, 'heightSE': 0},
                   {'labelingIsotopes': '13C3', 'height': 0.0002990498, 'heightSE': 0},
                   {'labelingIsotopes': '13C4', 'height': 0.0012322448, 'heightSE': 0},
                   {'labelingIsotopes': '13C5', 'height': 0.0962990868, 'heightSE': 0},
                   {'labelingIsotopes': '13C6', 'height': 0.0737941503, 'heightSE': 0},
                   {'labelingIsotopes': '13C7', 'height': 0.0194440036, 'heightSE': 0},
                   {'labelingIsotopes': '13C8', 'height': 0.063026207, 'heightSE': 0},
                   {'labelingIsotopes': '13C9', 'height': 0.0058731399, 'heightSE': 0},
                   {'labelingIsotopes': '13C10', 'height': 0.0312896069, 'heightSE': 0},
                   {'labelingIsotopes': '13C11', 'height': 0.3124695022, 'heightSE': 0},
                   {'labelingIsotopes': '13C12', 'height': 0.0573898846, 'heightSE': 0},
                   {'labelingIsotopes': '13C13', 'height': 0.277122791, 'heightSE': 0},
                   {'labelingIsotopes': '13C14', 'height': 0.0234859781, 'heightSE': 0},
                   {'labelingIsotopes': '13C15', 'height': 0.0200187655, 'heightSE': 0},
                   {'labelingIsotopes': '13C16', 'height': 0, 'heightSE': 0},
                   {'labelingIsotopes': '13C17', 'height': 0, 'heightSE': 0}]})

dataset5 = moiety_modeling.Dataset("maims_24h",
                                      {'UDP_GlcNAC': [{'labelingIsotopes': '13C0', 'height': 0.00697626, 'heightSE': 0},
                                                      {'labelingIsotopes': '13C1', 'height': 0, 'heightSE': 0},
                                                      {'labelingIsotopes': '13C2', 'height': 0.0008426934,
                                                       'heightSE': 0},
                                                      {'labelingIsotopes': '13C3', 'height': 0.0007070956,
                                                       'heightSE': 0},
                                                      {'labelingIsotopes': '13C4', 'height': 0.0006206594,
                                                       'heightSE': 0},
                                                      {'labelingIsotopes': '13C5', 'height': 0.068147345,
                                                       'heightSE': 0},
                                                      {'labelingIsotopes': '13C6', 'height': 0.0499393097,
                                                       'heightSE': 0},
                                                      {'labelingIsotopes': '13C7', 'height': 0.023993641,
                                                       'heightSE': 0},
                                                      {'labelingIsotopes': '13C8', 'height': 0.062901247,
                                                       'heightSE': 0},
                                                      {'labelingIsotopes': '13C9', 'height': 0.0056603032,
                                                       'heightSE': 0},
                                                      {'labelingIsotopes': '13C10', 'height': 0.0281210238,
                                                       'heightSE': 0},
                                                      {'labelingIsotopes': '13C11', 'height': 0.2482899264,
                                                       'heightSE': 0},
                                                      {'labelingIsotopes': '13C12', 'height': 0.0613088541,
                                                       'heightSE': 0},
                                                      {'labelingIsotopes': '13C13', 'height': 0.3325253653,
                                                       'heightSE': 0},
                                                      {'labelingIsotopes': '13C14', 'height': 0.0499904271,
                                                       'heightSE': 0},
                                                      {'labelingIsotopes': '13C15', 'height': 0.0537153908,
                                                       'heightSE': 0},
                                                      {'labelingIsotopes': '13C16', 'height': 0.0062604583,
                                                       'heightSE': 0},
                                                      {'labelingIsotopes': '13C17', 'height': 0, 'heightSE': 0}]})

dataset6 = moiety_modeling.Dataset("maims_36h", {
    'UDP_GlcNAC': [{'labelingIsotopes': '13C0', 'height': 0.0009166044, 'heightSE': 0},
                   {'labelingIsotopes': '13C1', 'height': 0, 'heightSE': 0},
                   {'labelingIsotopes': '13C2', 'height': 0, 'heightSE': 0},
                   {'labelingIsotopes': '13C3', 'height': 4.62586843804159E-06, 'heightSE': 0},
                   {'labelingIsotopes': '13C4', 'height': 0.0003291166, 'heightSE': 0},
                   {'labelingIsotopes': '13C5', 'height': 0.0461930963, 'heightSE': 0},
                   {'labelingIsotopes': '13C6', 'height': 0.0411700819, 'heightSE': 0},
                   {'labelingIsotopes': '13C7', 'height': 0.0173512837, 'heightSE': 0},
                   {'labelingIsotopes': '13C8', 'height': 0.0516141159, 'heightSE': 0},
                   {'labelingIsotopes': '13C9', 'height': 0.0027135558, 'heightSE': 0},
                   {'labelingIsotopes': '13C10', 'height': 0.0224157713, 'heightSE': 0},
                   {'labelingIsotopes': '13C11', 'height': 0.2514380699, 'heightSE': 0},
                   {'labelingIsotopes': '13C12', 'height': 0.0718100061, 'heightSE': 0},
                   {'labelingIsotopes': '13C13', 'height': 0.3662556844, 'heightSE': 0},
                   {'labelingIsotopes': '13C14', 'height': 0.0597315432, 'heightSE': 0},
                   {'labelingIsotopes': '13C15', 'height': 0.0579801179, 'heightSE': 0},
                   {'labelingIsotopes': '13C16', 'height': 0.0100763266, 'heightSE': 0},
                   {'labelingIsotopes': '13C17', 'height': 0, 'heightSE': 0}]})

dataset = { 'datasets' : [ dataset1, dataset2, dataset3, dataset4, dataset5, dataset6 ]}
jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
with open('UDP_maims_combined.json', 'w') as outFile:
    outFile.write(jsonpickle.encode(dataset))

