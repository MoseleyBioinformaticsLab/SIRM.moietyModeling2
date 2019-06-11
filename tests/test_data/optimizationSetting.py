#!/usr/bin/python3

import jsonpickle

setting = {}
#
# setting['L-BFGS-B'] = []
# setting['L-BFGS-B'].append({'methodParameters': None, 'optimizationSetting': 'L_BFGS_B'})
# setting['TNC'] = []
# setting['TNC'].append({'methodParameters': None, 'optimizationSetting': 'TNC'})
#
# setting['SLSQP'] = []
# setting['SLSQP'].append({'methodParameters': None, 'optimizationSetting': 'SLSQP'})
#
setting['SAGA'] = []
setting['SAGA'].append({'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 100, 'temperatureStepSize': 100},
        'noPrintAllResults': 1, 'noPrintBestResults': 1, 'optimizationSetting': 'SAGA_100' })

data ={'optimizations': setting}
jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)

with open('SAGA_setting.json', 'w') as outFile:
    outFile.write(jsonpickle.encode(data))



