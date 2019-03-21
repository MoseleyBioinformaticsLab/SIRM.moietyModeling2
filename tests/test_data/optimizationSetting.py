#!/usr/bin/python3

import jsonpickle

setting = {}

setting['L-BFGS-B'] = {'methodParameters': None, 'optimizationSetting': 'L_BFGS_B'}

setting['TNC'] = {'methodParameters': None, 'optimizationSetting': 'TNC'}

setting['SLSQP'] = {'methodParameters': None, 'optimizationSetting': 'SLSQP'}

setting['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 10000, 'temperatureStepSize': 100},
        'noPrintAllResults': 1, 'noPrintBestResults': 1, 'optimizationSetting': 'SAGA_10000' }

data ={'optimizations': setting}
jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)

with open('optimizationSetting.json', 'w') as outFile:
    outFile.write(jsonpickle.encode(data))



