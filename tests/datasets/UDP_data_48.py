#!/usr/bin/python3

import moiety_modeling
import jsonpickle




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




dataset = { 'datasets' : [ dataset2 ]}
jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
with open('UDP_data_48.json', 'w') as outFile:
    outFile.write(jsonpickle.encode(dataset))

