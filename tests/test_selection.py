import pytest
from moiety_modeling import analysis
import jsonpickle
import math

@pytest.mark.parametrize("optimization_file, analysis_file", [

    ("tests/analysis_results/all_single_models_UDP_data_48_72_optimization_setting_T_100_S_M_logDifference/SAGA_1000/best_model_48h_72h_SAGA_1000.json",
     "tests/analysis_results/all_single_models_UDP_data_48_72_optimization_setting_T_100_S_M_logDifference/SAGA_1000_logDifference_analysis/best_model_48h_72h_SAGA_1000_States.json"),
    ("tests/analysis_results/all_single_models_UDP_data_48_72_optimization_setting_T_100_S_M_logDifference/SLSQP/best_model_48h_72h_SLSQP.json",
     "tests/analysis_results/all_single_models_UDP_data_48_72_optimization_setting_T_100_S_M_logDifference/SLSQP_logDifference_analysis/best_model_48h_72h_SLSQP_logDifference_Stats.json"),
    ("tests/analysis_results/all_single_models_UDP_data_48_72_optimization_setting_T_100_S_M_logDifference/TNC/best_model_48h_72h_TNC.json",
     "tests/analysis_results/all_single_models_UDP_data_48_72_optimization_setting_T_100_S_M_logDifference/TNC_logDifference_analysis/best_model_48h_72h_TNC_logDifference_Stats.json"),
    ("tests/analysis_results/all_single_models_UDP_data_48_72_optimization_setting_T_100_S_M_logDifference/L_BFGS_B/best_model_48h_72h_L_BFGS_B.json",
     "tests/analysis_results/all_single_models_UDP_data_48_72_optimization_setting_T_100_S_M_logDifference/L_BFGS_B_logDifference_analysis/best_model_48h_72h_L_BFGS_B_logDifference_Stats.json")
])
def test_analysis(optimization_file, analysis_file):

    analysisInstance = analysis.ResultsAnalysis(optimization_file)
    analysisResults = analysisInstance.analyze()
    with open(analysis_file) as file:
        standardResults = jsonpickle.decode(file.read())
    anaMolecules = analysisResults['calculatedMolecules']
    standMolecules = standardResults['calculatedMolecules']

    for molecule in anaMolecules:
        for isotopologue in anaMolecules[molecule]:
            assert abs(anaMolecules[molecule][isotopologue]['mean'] - standMolecules[molecule][isotopologue]['mean']) < math.pow(10, -6)
            assert abs(anaMolecules[molecule][isotopologue]['max'] - standMolecules[molecule][isotopologue]['max']) < math.pow(10, -6)
            assert abs(anaMolecules[molecule][isotopologue]['std'] - standMolecules[molecule][isotopologue]['std']) < math.pow(10, -6)




