#!/usr/bin/python3

import moiety_modeling
import jsonpickle


dataset2 = moiety_modeling.Dataset("48h", {'UDP_GlcNAC': [{'labelingIsotopes': '13C_0', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_1', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_2', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_3', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_4', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_5', 'height': 0.017323401, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_6', 'height': 0.005577785, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_7', 'height': 0.010122988, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_8', 'height': 0.0385743, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_9', 'height': 0.0021297, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_10', 'height': 0.01521214, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_11', 'height': 0.132576107, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_12', 'height': 0.112099644, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_13', 'height': 0.390518688, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_14', 'height': 0.144054358, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_15', 'height': 0.115603046, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_16', 'height': 0.016207844, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_17', 'height': 0, 'heightSE': 0}]})

dataset3 = moiety_modeling.Dataset("72h", {'UDP_GlcNAC': [{'labelingIsotopes': '13C_0', 'height': 0.0050033, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_1', 'height': 0.00094257, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_2', 'height': 0.00099737, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_3', 'height': 0.00065213, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_4', 'height': 0.0037484, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_5', 'height': 0.041111, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_6', 'height': 0.029762, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_7', 'height': 0.036908, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_8', 'height': 0.046745, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_9', 'height': 0.017722, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_10', 'height': 0.033593, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_11', 'height': 0.11357, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_12', 'height': 0.099003, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_13', 'height': 0.29721, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_14', 'height': 0.12134, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_15', 'height': 0.10877, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_16', 'height': 0.043753, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C_17', 'height': 0.00056993, 'heightSE': 0}]})


dataset = { 'datasets' : [ dataset2, dataset3 ]}
jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
with open('UDP_data_48_72.json', 'w') as outFile:
    outFile.write(jsonpickle.encode(dataset))

