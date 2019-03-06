#!/usr/bin/python3

import jsonpickle

# setting1 = {}
# setting1['defaultMethod'] = 'SLSQP'
# setting1['SLSQP'] = {'methodParameters': {'maxiter': 100, 'ftol': math.exp(-5)}, 'split': 1, 'times': 100, 'suffix': 'SLSQP_100_test', 'multiProcess':1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/test_maims/SLSQP_test_results/'}
#
#
# setting2 = {}
# setting2['defaultMethod'] = 'L-BFGS-B'
# setting2['L-BFGS-B'] = {'methodParameters': {'maxiter': 15000, 'maxfun': 15000, 'gtol': math.exp(-5), 'ftol': math.exp(-9)} , 'split': 1, 'times': 100, 'suffix': 'L_BFGS_B_100_test', 'multiProcess':1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/test_maims/L_BFGS_B_test_results/'}

# setting3 = {}
# setting3['defaultMethod'] = 'SAGA'
# setting3['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 15000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'noPrintAllResults': 1, 'suffix': 'SAGA_15000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/10_5_test/SAGA_15000_split_results/'}
#
# setting4 = {}
# setting4['defaultMethod'] = 'SAGA'
# setting4['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 20000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'noPrintAllResults': 1, 'suffix': 'SAGA_20000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/10_5_test/SAGA_20000_split_results/'}
#

# setting5 = {}
# setting5['defaultMethod'] = 'SAGA'
# setting5['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 500, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'square', 'noPrintAllResults': 1, 'suffix': 'SAGA_500_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_square/SAGA_500_split_results/'}
#
#
# setting6 = {}
# setting6['defaultMethod'] = 'SAGA'
# setting6['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 1000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'square', 'noPrintAllResults': 1, 'suffix': 'SAGA_1000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_square/SAGA_1000_split_results/'}
#
#
#
# setting7 = {}
# setting7['defaultMethod'] = 'SAGA'
# setting7['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 2000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'square', 'noPrintAllResults': 1, 'suffix': 'SAGA_2000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_square/SAGA_2000_split_results/'}
#
#
#
# setting8 = {}
# setting8['defaultMethod'] = 'SAGA'
# setting8['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 5000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'square', 'noPrintAllResults': 1, 'suffix': 'SAGA_5000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_square/SAGA_5000_split_results/'}
#
#
# setting9 = {}
# setting9['defaultMethod'] = 'SAGA'
# setting9['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 10000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'square', 'noPrintAllResults': 1, 'suffix': 'SAGA_10000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_square/SAGA_10000_split_results/'}
#
#
# setting10 = {}
# setting10['defaultMethod'] = 'SAGA'
# setting10['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 25000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'square', 'noPrintAllResults': 1, 'suffix': 'SAGA_25000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_square/SAGA_25000_split_results/'}
#
# setting11 = {}
# setting11['defaultMethod'] = 'SAGA'
# setting11['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 50000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'square', 'noPrintAllResults': 1, 'suffix': 'SAGA_50000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_square/SAGA_50000_split_results/'}
#
# setting12 = {}
# setting12['defaultMethod'] = 'SAGA'
# setting12['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 15000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'square', 'noPrintAllResults': 1, 'suffix': 'SAGA_15000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_square/SAGA_15000_split_results/'}
#
#


# setting13 = {}
# setting13['defaultMethod'] = 'SAGA'
# setting13['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 500, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'log', 'noPrintAllResults': 1, 'suffix': 'SAGA_500_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_log/SAGA_500_split_results/'}
#
#
# setting14 = {}
# setting14['defaultMethod'] = 'SAGA'
# setting14['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 1000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'log', 'noPrintAllResults': 1, 'suffix': 'SAGA_1000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_log/SAGA_1000_split_results/'}
#
#
#
# setting15 = {}
# setting15['defaultMethod'] = 'SAGA'
# setting15['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 2000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'log', 'noPrintAllResults': 1, 'suffix': 'SAGA_2000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_log/SAGA_2000_split_results/'}
#
#
#
# setting16 = {}
# setting16['defaultMethod'] = 'SAGA'
# setting16['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 5000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'log', 'noPrintAllResults': 1, 'suffix': 'SAGA_5000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_log/SAGA_5000_split_results/'}
#
#
# setting17 = {}
# setting17['defaultMethod'] = 'SAGA'
# setting17['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 10000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'log', 'noPrintAllResults': 1, 'suffix': 'SAGA_10000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_log/SAGA_10000_split_results/'}
#
#
# setting18 = {}
# setting18['defaultMethod'] = 'SAGA'
# setting18['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 25000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'log', 'noPrintAllResults': 1, 'suffix': 'SAGA_25000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_log/SAGA_25000_split_results/'}
#
# setting19 = {}
# setting19['defaultMethod'] = 'SAGA'
# setting19['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 50000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'log', 'noPrintAllResults': 1, 'suffix': 'SAGA_50000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_log/SAGA_50000_split_results/'}
#
# setting20 = {}
# setting20['defaultMethod'] = 'SAGA'
# setting20['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 15000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'log', 'noPrintAllResults': 1, 'suffix': 'SAGA_15000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_log/SAGA_15000_split_results/'}


# setting21 = {}
# setting21['defaultMethod'] = 'SAGA'
# setting21['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 500, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'log_sum', 'noPrintAllResults': 1, 'suffix': 'SAGA_500_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_log_sum/SAGA_500_split_results/'}
#
# setting22 = {}
# setting22['defaultMethod'] = 'SAGA'
# setting22['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 1000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'log_sum', 'noPrintAllResults': 1, 'suffix': 'SAGA_1000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_log_sum/SAGA_1000_split_results/'}
#
#
#
# setting23 = {}
# setting23['defaultMethod'] = 'SAGA'
# setting23['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 2000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'log_sum', 'noPrintAllResults': 1, 'suffix': 'SAGA_2000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_log_sum/SAGA_2000_split_results/'}
#
#
#
# setting24 = {}
# setting24['defaultMethod'] = 'SAGA'
# setting24['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 5000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'log_sum', 'noPrintAllResults': 1, 'suffix': 'SAGA_5000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_log_sum/SAGA_5000_split_results/'}
#
#
# setting25 = {}
# setting25['defaultMethod'] = 'SAGA'
# setting25['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 10000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'log_sum', 'noPrintAllResults': 1, 'suffix': 'SAGA_10000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_log_sum/SAGA_10000_split_results/'}
#
#
# setting26 = {}
# setting26['defaultMethod'] = 'SAGA'
# setting26['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 25000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'log_sum', 'noPrintAllResults': 1, 'suffix': 'SAGA_25000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_log_sum/SAGA_25000_split_results/'}
#
# setting27 = {}
# setting27['defaultMethod'] = 'SAGA'
# setting27['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 50000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'log_sum', 'noPrintAllResults': 1, 'suffix': 'SAGA_50000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_log_sum/SAGA_50000_split_results/'}
#
# setting28 = {}
# setting28['defaultMethod'] = 'SAGA'
# setting28['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 15000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'log_sum', 'noPrintAllResults': 1, 'suffix': 'SAGA_15000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_log_sum/SAGA_15000_split_results/'}
#
#



# setting29 = {}
# setting29['defaultMethod'] = 'SLSQP'
# setting29['SLSQP'] = {'methodParameters': None, 'split': 1, 'times': 100, 'energyFunction': 'log_sum', 'suffix': 'SLSQP', 'multiProcess':1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_log_sum/SLSQP_split_results/'}
#
#
# setting30 = {}
# setting30['defaultMethod'] = 'L-BFGS-B'
# setting30['L-BFGS-B'] = {'methodParameters': None, 'split': 1, 'times': 100, 'energyFunction': 'log_sum', 'suffix': 'L_BFGS_B', 'multiProcess':1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_log_sum/L_BFGS_B_split_results/'}
#



# setting31 = {}
# setting31['defaultMethod'] = 'SAGA'
# setting31['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 100000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'log_sum', 'noPrintAllResults': 1, 'suffix': 'SAGA_100000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_log_sum/SAGA_100000_split_results/'}
#
# setting32 = {}
# setting32['defaultMethod'] = 'SAGA'
# setting32['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 150000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'log_sum', 'noPrintAllResults': 1, 'suffix': 'SAGA_150000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_log_sum/SAGA_150000_split_results/'}
#
#

# setting33 = {}
# setting33['defaultMethod'] = 'TNC'
# setting33['TNC'] = {'methodParameters': None, 'split': 1, 'times': 100, 'energyFunction': 'log_sum', 'suffix': 'TNC', 'multiProcess':1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_log_sum/TNC_split_results/'}
#



# setting34 = {}
# setting34['defaultMethod'] = 'SAGA'
# setting34['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 500, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'proportionalDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_500_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_proportional/SAGA_500_split_results/'}
#
# setting35 = {}
# setting35['defaultMethod'] = 'SAGA'
# setting35['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 1000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'proportionalDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_1000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_proportional/SAGA_1000_split_results/'}
#
#
#
# setting36 = {}
# setting36['defaultMethod'] = 'SAGA'
# setting36['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 2000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'proportionalDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_2000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_proportional/SAGA_2000_split_results/'}
#
#
#
# setting37 = {}
# setting37['defaultMethod'] = 'SAGA'
# setting37['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 5000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'proportionalDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_5000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_proportional/SAGA_5000_split_results/'}
#
#
# setting38 = {}
# setting38['defaultMethod'] = 'SAGA'
# setting38['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 10000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'proportionalDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_10000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_proportional/SAGA_10000_split_results/'}
#
#
# setting39 = {}
# setting39['defaultMethod'] = 'SAGA'
# setting39['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 25000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'proportionalDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_25000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_proportional/SAGA_25000_split_results/'}
#
# setting40 = {}
# setting40['defaultMethod'] = 'SAGA'
# setting40['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 50000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'proportionalDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_50000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_proportional/SAGA_50000_split_results/'}
#
# setting41 = {}
# setting41['defaultMethod'] = 'SAGA'
# setting41['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 15000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'proportionalDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_15000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_proportional/SAGA_15000_split_results/'}
#
#
# setting42 = {}
# setting42['defaultMethod'] = 'SAGA'
# setting42['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 100000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'proportionalDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_100000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/energy_proportional/SAGA_100000_split_results/'}
#



# setting43 = {}
# setting43['defaultMethod'] = 'SAGA'
# setting43['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 500, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_500_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_log_sum/SAGA_500_split_results/'}
#
# setting44 = {}
# setting44['defaultMethod'] = 'SAGA'
# setting44['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 1000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_1000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_log_sum/SAGA_1000_split_results/'}
#
#
#
# setting45 = {}
# setting45['defaultMethod'] = 'SAGA'
# setting45['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 2000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_2000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_log_sum/SAGA_2000_split_results/'}
#
#
#
# setting46 = {}
# setting46['defaultMethod'] = 'SAGA'
# setting46['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 5000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_5000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_log_sum/SAGA_5000_split_results/'}
#
#
# setting47 = {}
# setting47['defaultMethod'] = 'SAGA'
# setting47['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 10000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_10000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_log_sum/SAGA_10000_split_results/'}
#
#
# setting48 = {}
# setting48['defaultMethod'] = 'SAGA'
# setting48['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 25000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_25000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_log_sum/SAGA_25000_split_results/'}
#
# setting49 = {}
# setting49['defaultMethod'] = 'SAGA'
# setting49['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 50000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_50000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_log_sum/SAGA_50000_split_results/'}
#
# setting50 = {}
# setting50['defaultMethod'] = 'SAGA'
# setting50['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 15000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_15000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_log_sum/SAGA_15000_split_results/'}
#
#
# setting51 = {}
# setting51['defaultMethod'] = 'SAGA'
# setting51['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 100000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_100000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_log_sum/SAGA_100000_split_results/'}


# setting52 = {}
# setting52['defaultMethod'] = 'SAGA'
# setting52['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 500, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_500_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_log_sum/SAGA_500_split_results/'}
#
# setting53 = {}
# setting53['defaultMethod'] = 'SAGA'
# setting53['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 1000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_1000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_log_sum/SAGA_1000_split_results/'}
#
#
#
# setting54 = {}
# setting54['defaultMethod'] = 'SAGA'
# setting54['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 2000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_2000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_log_sum/SAGA_2000_split_results/'}
#
#
#
# setting55 = {}
# setting55['defaultMethod'] = 'SAGA'
# setting55['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 5000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_5000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_log_sum/SAGA_5000_split_results/'}
#
#
# setting56 = {}
# setting56['defaultMethod'] = 'SAGA'
# setting56['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 10000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_10000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_log_sum/SAGA_10000_split_results/'}
#
#
# setting57 = {}
# setting57['defaultMethod'] = 'SAGA'
# setting57['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 25000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_25000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_log_sum/SAGA_25000_split_results/'}
#
# setting58 = {}
# setting58['defaultMethod'] = 'SAGA'
# setting58['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 50000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_50000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_log_sum/SAGA_50000_split_results/'}
#
# setting59 = {}
# setting59['defaultMethod'] = 'SAGA'
# setting59['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 15000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_15000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_log_sum/SAGA_15000_split_results/'}
#
#
# setting60 = {}
# setting60['defaultMethod'] = 'SAGA'
# setting60['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 100000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_100000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_log_sum/SAGA_100000_split_results/'}
#



# setting61 = {}
# setting61['defaultMethod'] = 'SAGA'
# setting61['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 500, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'absDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_500_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_absDiff/SAGA_500_split_results/'}
#
# setting62 = {}
# setting62['defaultMethod'] = 'SAGA'
# setting62['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 1000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'absDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_1000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_absDiff/SAGA_1000_split_results/'}
#
#
#
# setting63 = {}
# setting63['defaultMethod'] = 'SAGA'
# setting63['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 2000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'absDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_2000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_absDiff/SAGA_2000_split_results/'}
#
#
#
# setting64 = {}
# setting64['defaultMethod'] = 'SAGA'
# setting64['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 5000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'absDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_5000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_absDiff/SAGA_5000_split_results/'}
#
#
# setting65 = {}
# setting65['defaultMethod'] = 'SAGA'
# setting65['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 10000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'absDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_10000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_absDiff/SAGA_10000_split_results/'}
#
#


# setting66 = {}
# setting66['defaultMethod'] = 'SAGA'
# setting66['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 25000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'absDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_25000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_absDiff/SAGA_25000_split_results/'}
#
# setting67 = {}
# setting67['defaultMethod'] = 'SAGA'
# setting67['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 50000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'absDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_50000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_absDiff/SAGA_50000_split_results/'}
#
# setting68 = {}
# setting68['defaultMethod'] = 'SAGA'
# setting68['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 15000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'absDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_15000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_absDiff/SAGA_15000_split_results/'}
#
#
# setting69 = {}
# setting69['defaultMethod'] = 'SAGA'
# setting69['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 100000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'absDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_100000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_absDiff/SAGA_100000_split_results/'}




# setting70 = {}
# setting70['defaultMethod'] = 'SAGA'
# setting70['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 500, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_500_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_0_6_logDiff/SAGA_500_split_results/'}
#
# setting71 = {}
# setting71['defaultMethod'] = 'SAGA'
# setting71['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 1000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_1000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_0_6_logDiff/SAGA_1000_split_results/'}
#
#
#
# setting72 = {}
# setting72['defaultMethod'] = 'SAGA'
# setting72['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 2000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_2000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_0_6_logDiff/SAGA_2000_split_results/'}
#
#
#
# setting73 = {}
# setting73['defaultMethod'] = 'SAGA'
# setting73['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 5000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_5000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_0_6_logDiff/SAGA_5000_split_results/'}
#
#
# setting74 = {}
# setting74['defaultMethod'] = 'SAGA'
# setting74['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 10000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_10000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_0_6_logDiff/SAGA_10000_split_results/'}
#
#
# setting75 = {}
# setting75['defaultMethod'] = 'SAGA'
# setting75['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 25000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_25000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_0_6_logDiff/SAGA_25000_split_results/'}
#
# setting76 = {}
# setting76['defaultMethod'] = 'SAGA'
# setting76['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 50000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_50000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_0_6_logDiff/SAGA_50000_split_results/'}
#
# setting77 = {}
# setting77['defaultMethod'] = 'SAGA'
# setting77['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 15000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_15000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_0_6_logDiff/SAGA_15000_split_results/'}
#
#
# setting78 = {}
# setting78['defaultMethod'] = 'SAGA'
# setting78['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 100000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_100000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_0_6_logDiff/SAGA_100000_split_results/'}





# setting70 = {}
# setting70['defaultMethod'] = 'SAGA'
# setting70['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 500, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_500_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_0_logDiff/SAGA_500_split_results/'}
#
# setting71 = {}
# setting71['defaultMethod'] = 'SAGA'
# setting71['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 1000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_1000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_0_logDiff/SAGA_1000_split_results/'}
#
#
#
# setting72 = {}
# setting72['defaultMethod'] = 'SAGA'
# setting72['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 2000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_2000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_0_logDiff/SAGA_2000_split_results/'}
#
#
#
# setting73 = {}
# setting73['defaultMethod'] = 'SAGA'
# setting73['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 5000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_5000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_0_logDiff/SAGA_5000_split_results/'}
#
#
# setting74 = {}
# setting74['defaultMethod'] = 'SAGA'
# setting74['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 10000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_10000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_0_logDiff/SAGA_10000_split_results/'}
#
#
# setting75 = {}
# setting75['defaultMethod'] = 'SAGA'
# setting75['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 25000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_25000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_0_logDiff/SAGA_25000_split_results/'}
#
# setting76 = {}
# setting76['defaultMethod'] = 'SAGA'
# setting76['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 50000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_50000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_0_logDiff/SAGA_50000_split_results/'}
#
# setting77 = {}
# setting77['defaultMethod'] = 'SAGA'
# setting77['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 15000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_15000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_0_logDiff/SAGA_15000_split_results/'}
#
#
# setting78 = {}
# setting78['defaultMethod'] = 'SAGA'
# setting78['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 100000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_100000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data2_0_logDiff/SAGA_100000_split_results/'}


#










# setting70 = {}
# setting70['defaultMethod'] = 'SAGA'
# setting70['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 500, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_500_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_0_6_logDiff/SAGA_500_split_results/'}
#
# setting71 = {}
# setting71['defaultMethod'] = 'SAGA'
# setting71['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 1000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_1000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_0_6_logDiff/SAGA_1000_split_results/'}
#
#
#
# setting72 = {}
# setting72['defaultMethod'] = 'SAGA'
# setting72['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 2000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_2000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_0_6_logDiff/SAGA_2000_split_results/'}
#
#
#
# setting73 = {}
# setting73['defaultMethod'] = 'SAGA'
# setting73['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 5000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_5000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_0_6_logDiff/SAGA_5000_split_results/'}
#
#
# setting74 = {}
# setting74['defaultMethod'] = 'SAGA'
# setting74['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 10000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_10000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_0_6_logDiff/SAGA_10000_split_results/'}
#
#
# setting75 = {}
# setting75['defaultMethod'] = 'SAGA'
# setting75['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 25000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_25000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_0_6_logDiff/SAGA_25000_split_results/'}
#
# setting76 = {}
# setting76['defaultMethod'] = 'SAGA'
# setting76['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 50000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_50000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_0_6_logDiff/SAGA_50000_split_results/'}
#
# setting77 = {}
# setting77['defaultMethod'] = 'SAGA'
# setting77['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 15000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_15000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_0_6_logDiff/SAGA_15000_split_results/'}
#
#
# setting78 = {}
# setting78['defaultMethod'] = 'SAGA'
# setting78['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 100000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_100000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_0_6_logDiff/SAGA_100000_split_results/'}
#

# setting70 = {}
# setting70['defaultMethod'] = 'SAGA'
# setting70['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 500, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_500_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_0_logDiff/SAGA_500_split_results/'}
#
# setting71 = {}
# setting71['defaultMethod'] = 'SAGA'
# setting71['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 1000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_1000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_0_logDiff/SAGA_1000_split_results/'}
#
#
#
# setting72 = {}
# setting72['defaultMethod'] = 'SAGA'
# setting72['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 2000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_2000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_0_logDiff/SAGA_2000_split_results/'}
#
#
#
# setting73 = {}
# setting73['defaultMethod'] = 'SAGA'
# setting73['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 5000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_5000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_0_logDiff/SAGA_5000_split_results/'}
#
#
# setting74 = {}
# setting74['defaultMethod'] = 'SAGA'
# setting74['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 10000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_10000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_0_logDiff/SAGA_10000_split_results/'}
#
#
# setting75 = {}
# setting75['defaultMethod'] = 'SAGA'
# setting75['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 25000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_25000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_0_logDiff/SAGA_25000_split_results/'}
#
# setting76 = {}
# setting76['defaultMethod'] = 'SAGA'
# setting76['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 50000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_50000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_0_logDiff/SAGA_50000_split_results/'}
#
# setting77 = {}
# setting77['defaultMethod'] = 'SAGA'
# setting77['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 15000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_15000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_0_logDiff/SAGA_15000_split_results/'}
#
#
# setting78 = {}
# setting78['defaultMethod'] = 'SAGA'
# setting78['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 100000, 'temperatureStepSize': 100},
#         'split': 1, 'times': 100, 'energyFunction': 'logDifference', 'noPrintAllResults': 1, 'suffix': 'SAGA_100000_split', 'multiProcess': 1, 'path': '/mlab/data/hji236/projects/SIRM.moietyModeling2/old/maims_data1_0_logDiff/SAGA_100000_split_results/'}











# setting70 = {}
# setting70['defaultMethod'] = 'SAGA'
# setting70['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 500, 'temperatureStepSize': 100},
#         'noPrintAllResults': 1, 'noPrintBestResults': 1, 'suffix': 'SAGA_500_split' }
#
# setting71 = {}
# setting71['defaultMethod'] = 'SAGA'
# setting71['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 1000, 'temperatureStepSize': 100},
#         'noPrintAllResults': 1, 'noPrintBestResults': 1, 'suffix': 'SAGA_1000_split'}
#
#
#
# setting72 = {}
# setting72['defaultMethod'] = 'SAGA'
# setting72['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 2000, 'temperatureStepSize': 100},
#         'noPrintAllResults': 1, 'noPrintBestResults': 1, 'suffix': 'SAGA_2000_split'}
#
#
#
# setting73 = {}
# setting73['defaultMethod'] = 'SAGA'
# setting73['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 5000, 'temperatureStepSize': 100},
#          'noPrintAllResults': 1, 'noPrintBestResults': 1, 'suffix': 'SAGA_5000_split'}
#
#
# setting74 = {}
# setting74['defaultMethod'] = 'SAGA'
# setting74['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 10000, 'temperatureStepSize': 100},
#         'noPrintAllResults': 1, 'noPrintBestResults': 1, 'suffix': 'SAGA_10000_split' }
#
#
# setting75 = {}
# setting75['defaultMethod'] = 'SAGA'
# setting75['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 25000, 'temperatureStepSize': 100},
#         'noPrintAllResults': 1, 'noPrintBestResults': 1, 'suffix': 'SAGA_25000_split'}
#
# setting76 = {}
# setting76['defaultMethod'] = 'SAGA'
# setting76['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 50000, 'temperatureStepSize': 100},
#          'noPrintAllResults': 1, 'noPrintBestResults': 1, 'suffix': 'SAGA_50000_split'}
#
# setting77 = {}
# setting77['defaultMethod'] = 'SAGA'
# setting77['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 15000, 'temperatureStepSize': 100},
#         'noPrintAllResults': 1, 'noPrintBestResults': 1, 'suffix': 'SAGA_15000_split'}
#
#
# setting78 = {}
# setting78['defaultMethod'] = 'SAGA'
# setting78['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 100000, 'temperatureStepSize': 100},
#          'noPrintAllResults': 1, 'noPrintBestResults': 1, 'suffix': 'SAGA_100000_split'}





# setting78['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 100000, 'temperatureStepSize': 100},
#          'noPrintAllResults': 1, 'noPrintBestResults': 1, 'suffix': 'SAGA_100000_split'}



# setting70 = {}
# setting70['defaultMethod'] = 'SAGA'
# setting70['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 500, 'temperatureStepSize': 100},
#         'noPrintAllResults': 1, 'noPrintBestResults': 1, 'suffix': 'SAGA_500' }
#
# setting71 = {}
# setting71['defaultMethod'] = 'SAGA'
# setting71['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 1000, 'temperatureStepSize': 100},
#         'noPrintAllResults': 1, 'noPrintBestResults': 1, 'suffix': 'SAGA_1000'}
#
#
#
# setting72 = {}
# setting72['defaultMethod'] = 'SAGA'
# setting72['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 2000, 'temperatureStepSize': 100},
#         'noPrintAllResults': 1, 'noPrintBestResults': 1, 'suffix': 'SAGA_2000'}
#
#
#
# setting73 = {}
# setting73['defaultMethod'] = 'SAGA'
# setting73['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 5000, 'temperatureStepSize': 100},
#          'noPrintAllResults': 1, 'noPrintBestResults': 1, 'suffix': 'SAGA_5000'}
#
#
# setting74 = {}
# setting74['defaultMethod'] = 'SAGA'
# setting74['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 10000, 'temperatureStepSize': 100},
#         'noPrintAllResults': 1, 'noPrintBestResults': 1, 'suffix': 'SAGA_10000' }
#
#
# setting75 = {}
# setting75['defaultMethod'] = 'SAGA'
# setting75['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 15000, 'temperatureStepSize': 100},
#         'noPrintAllResults': 1, 'noPrintBestResults': 1, 'suffix': 'SAGA_15000'}
#
# setting76 = {}
# setting76['defaultMethod'] = 'SAGA'
# setting76['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 25000, 'temperatureStepSize': 100},
#         'noPrintAllResults': 1, 'noPrintBestResults': 1, 'suffix': 'SAGA_25000'}
#
#



# setting76 = {}
# setting76['defaultMethod'] = 'SAGA'
# setting76['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 50000, 'temperatureStepSize': 100},
#          'noPrintAllResults': 1, 'noPrintBestResults': 1, 'suffix': 'SAGA_50000_split'}
#
# setting78 = {}
# setting78['defaultMethod'] = 'SAGA'
# setting78['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 100000, 'temperatureStepSize': 100},
#          'noPrintAllResults': 1, 'noPrintBestResults': 1, 'suffix': 'SAGA_100000_split'}
#
#
# setting79 = {}
# setting79['defaultMethod'] = 'SAGA'
# setting79['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 150000, 'temperatureStepSize': 100},
#          'noPrintAllResults': 1, 'noPrintBestResults': 1, 'suffix': 'SAGA_150000_split'}
#
#
# setting80 = {}
# setting80['defaultMethod'] = 'SAGA'
# setting80['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 200000, 'temperatureStepSize': 100},
#          'noPrintAllResults': 1, 'noPrintBestResults': 1, 'suffix': 'SAGA_200000_split'}
#


# setting79 = {}
# setting79['defaultMethod'] = 'SAGA'
# setting79['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 250000, 'temperatureStepSize': 100},
#          'noPrintAllResults': 1, 'noPrintBestResults': 1, 'suffix': 'SAGA_250000'}
#
#
# setting80 = {}
# setting80['defaultMethod'] = 'SAGA'
# setting80['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 300000, 'temperatureStepSize': 100},
#          'noPrintAllResults': 1, 'noPrintBestResults': 1, 'suffix': 'SAGA_300000'}

# setting2 = {}
# setting2['defaultMethod'] = 'L-BFGS-B'
# setting2['L-BFGS-B'] = {'methodParameters': {'maxiter': 15000, 'maxfun': 15000, 'gtol': math.exp(-5), 'ftol': math.exp(-8)} , 'suffix': 'L_BFGS_B_8'}
#
#
#
# setting3 = {}
# setting3['defaultMethod'] = 'L-BFGS-B'
# setting3['L-BFGS-B'] = {'methodParameters': {'maxiter': 15000, 'maxfun': 15000, 'gtol': math.exp(-5), 'ftol': math.exp(-9)} , 'suffix': 'L_BFGS_B_9'}

# setting2 = {}
# setting2['defaultMethod'] = 'L-BFGS-B'
# setting2['L-BFGS-B'] = {'methodParameters': None, 'suffix': 'L_BFGS_B'}


# setting2 = {}
# setting2['defaultMethod'] = 'TNC'
# setting2['TNC'] = {'methodParameters': None, 'suffix': 'TNC'}
#
#
# setting3 = {}
# setting3['defaultMethod'] = 'L-BFGS-B'
# setting3['L-BFGS-B'] = {'methodParameters': None, 'suffix': 'L_BFGS_B'}
#
#
# setting4 = {}
# setting4['defaultMethod'] = 'SLSQP'
# setting4['SLSQP'] = {'methodParameters': None, 'suffix': 'SLSQP'}

setting70 = {}
setting70['SAGA'] = {'methodParameters': {'alpha': 1, 'crossoverRate': 0.05, 'mutationRate': 3, 'populationSize': 20, 'startTemperature': 0.5, 'stepNumber': 500, 'temperatureStepSize': 100},
        'noPrintAllResults': 1, 'noPrintBestResults': 0, 'optimizationSetting': 'SAGA_500' }

# setting70['L-BFGS-B'] = {'methodParameters': None, 'optimizationSetting': 'L_BFGS_B'}

data ={'optimizations': setting70}
jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)

with open('SAGA_500_setting.json', 'w') as outFile:
    outFile.write(jsonpickle.encode(data))



