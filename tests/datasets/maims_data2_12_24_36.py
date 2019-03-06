#!/usr/bin/python3

import moiety_modeling
import jsonpickle



dataset1 = moiety_modeling.Dataset("12h", {'UDP_GlcNAC': [{'labelingIsotopes': '13C0', 'height':  0.0206527976, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C1', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C2', 'height': 9.29E-05, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C3', 'height': 0.0003583153, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C4', 'height': 0.0020703059, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C5', 'height': 0.0919107237, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C6', 'height': 0.0715747914, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C7', 'height': 0.0201321486, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C8', 'height': 0.0582958468, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C9', 'height': 0.0038209994, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C10', 'height': 0.0312405595, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C11', 'height': 0.3086614901, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C12', 'height': 0.049523904, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C13', 'height': 0.2952708988, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C14', 'height': 0.024567609, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C15', 'height': 0.0218266848, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C16', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C17', 'height': 0, 'heightSE': 0}]})
                                                        
dataset2 = moiety_modeling.Dataset("24h", {'UDP_GlcNAC': [{'labelingIsotopes': '13C0', 'height': 0.0054112001, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C1', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C2', 'height': 0.0002443601, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C3', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C4', 'height': 0.0006771256, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C5', 'height': 0.0601364562, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C6', 'height': 0.0505878726, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C7', 'height': 0.0257101541, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C8', 'height': 0.0558144077, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C9', 'height': 0.0078118293, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C10', 'height':  0.0238954121, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C11', 'height':  0.2451402014, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C12', 'height':  0.0650931207, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C13', 'height':  0.3471455508, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C14', 'height':  0.0524199207, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C15', 'height': 0.0546107206, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C16', 'height':  0.0053016678, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C17', 'height': 0, 'heightSE': 0}]})


dataset3 = moiety_modeling.Dataset("36h", {'UDP_GlcNAC': [{'labelingIsotopes': '13C0', 'height': 0.0013563833, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C1', 'height': 0, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C2', 'height': 0.000470185, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C3', 'height': 0.0002145004, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C4', 'height': 0.0008907347, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C5', 'height': 0.0470947611, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C6', 'height': 0.0371916408, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C7', 'height': 0.0219394801, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C8', 'height':  0.0486243453, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C9', 'height': 0.0056235016, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C10', 'height':  0.0243139349, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C11', 'height':  0.2437263469, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C12', 'height':  0.0664551468, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C13', 'height':  0.3776013587, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C14', 'height': 0.0617711234, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C15', 'height': 0.0555852048, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C16', 'height':  0.0071413523, 'heightSE': 0},
                                                        {'labelingIsotopes': '13C17', 'height': 0, 'heightSE': 0}]})




dataset = { 'datasets' : [ dataset1, dataset2, dataset3 ]}
jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
with open('maims_data2_12_24_36.json', 'w') as outFile:
    outFile.write(jsonpickle.encode(dataset))

