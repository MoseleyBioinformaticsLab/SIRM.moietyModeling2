#!/usr/bin/python3

import moiety_modeling
import jsonpickle

dataset2 = moiety_modeling.Dataset("48h", {'UDP_GlcNAC': [{'labelingIsotopes': '13C_0', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_1', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_2', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_3', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_4', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_5', 'height': 0.013, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_6', 'height': 0.026, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_7', 'height': 0.05, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_8', 'height': 0.049, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_9', 'height': 0.026, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_10', 'height': 0.016, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_11', 'height': 0.117, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_12', 'height': 0.115, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_13', 'height': 0.335, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_14', 'height': 0.106, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_15', 'height': 0.123, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_16', 'height': 0.024, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_17', 'height': 0, 'heightSE': 0}]})




dataset = { 'datasets' : [ dataset2 ]}
jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
with open('UDP_single_simulate_48.json', 'w') as outFile:
    outFile.write(jsonpickle.encode(dataset))

