import pytest
from moiety_modeling import analysis
import jsonpickle
import math

@pytest.mark.parametrize("optimization_file, analysis_file", [

    ("tests/analysis_results/models_UDP_data_24_48_72_optimizationSetting_T_100_S_M_logDifference/SAGA_1000/best_model_SAGA_1000.json",
     "tests/analysis_results/models_UDP_data_24_48_72_optimizationSetting_T_100_S_M_logDifference/SAGA_1000_logDifference_analysis/best_model_SAGA_1000_logDifference_Stats.json"),
    ("tests/analysis_results/models_UDP_data_24_48_72_optimizationSetting_T_100_S_M_logDifference/SLSQP/best_model_SLSQP.json",
     "tests/analysis_results/models_UDP_data_24_48_72_optimizationSetting_T_100_S_M_logDifference/SLSQP_logDifference_analysis/best_model_SLSQP_logDifference_Stats.json"),
    ("tests/analysis_results/models_UDP_data_24_48_72_optimizationSetting_T_100_S_M_logDifference/TNC/best_model_TNC.json",
     "tests/analysis_results/models_UDP_data_24_48_72_optimizationSetting_T_100_S_M_logDifference/TNC_logDifference_analysis/best_model_TNC_logDifference_Stats.json"),
    ("tests/analysis_results/models_UDP_data_24_48_72_optimizationSetting_T_100_S_M_logDifference/L_BFGS_B/best_model_L_BFGS_B.json",
     "tests/analysis_results/models_UDP_data_24_48_72_optimizationSetting_T_100_S_M_logDifference/L_BFGS_B_logDifference_analysis/best_model_L_BFGS_B_logDifference_Stats.json")
])
def test_analysis(optimization_file, analysis_file):

    analysisInstance = analysis.ResultsAnalysis(optimization_file)
    analysisResults = analysisInstance.analyze()
    with open(analysis_file) as file:
        standardResults = jsonpickle.decode(file.read())
    anaMolecules = analysisResults['calculatedMolecules']
    standMolecules = standardResults['calculatedMolecules']
    print("anaMolecules", anaMolecules)
    print("standMolecules", standMolecules)

    for molecule in anaMolecules:
        for isotopologue in anaMolecules[molecule]:
            assert abs(isotopologue['mean'] - standMolecules[molecule][isotopologue]['mean']) < math.pow(10, -6)
            assert abs(isotopologue['max'] - standMolecules[molecule][isotopologue]['max']) < math.pow(10, -6)
            assert abs(isotopologue['std'] - standMolecules[molecule][isotopologue]['std']) < math.pow(10, -6)




