import pytest
import moiety_modeling
import jsonpickle
import math

@pytest.mark.parameterize("optimization_file, analysis_file", [

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

    analysis = moiety_modeling.ResultsAnalysis(optimization_file)
    analysisResults = analysis.analyze()
    with open(analysis_file) as file:
        standardResults = jsonpickle.decode(file.read())
    anaMolecules = analysisResults['calculatedMolecules']
    standMoleculs = standardResults['calculatedMolecules']
    for molecule in anaMolecules:
        for isotopologue in anaMolecules[molecule]:
            assert abs(isotopologue['mean'] - standMoleculs[molecule][isotopologue]['mean']) < math.pow(10, -6)
            assert abs(isotopologue['max'] - standMoleculs[molecule][isotopologue]['max']) < math.pow(10, -6)
            assert abs(isotopologue['std'] - standMoleculs[molecule][isotopologue]['std']) < math.pow(10, -6)




