import os
import pytest


# def test_modeling():
#
#     command1 = "python3 -m moiety_modeling modeling --models={0} --datasets={1} --optimizations={2} --repetition=100 --split --multiprocess --energyFunction=logDifference" \
#         .format("tests/test_data/test_models.json", "tests/test_data/UDP_data_24_48_72.json",
#                 "tests/test_data/optimizationSetting.json")
#
#     assert os.system(command1) == 0
#
#     command2 = "python3 -m moiety_modeling modeling --models={0} --datasets={1} --optimizations={2} --repetition=100 --multiprocess --energyFunction=logDifference" \
#         .format("tests/test_data/test_models.json", "tests/test_data/UDP_data_24_48_72.json",
#                 "tests/test_data/optimizationSetting.json")
#
#     assert os.system(command2) == 0
#
#     command3 = "python3 -m moiety_modeling modeling --models={0} --datasets={1} --optimizations={2} --repetition=100 --split --energyFunction=logDifference" \
#         .format("tests/test_data/test_models.json", "tests/test_data/UDP_data_24_48_72.json",
#                 "tests/test_data/optimizationSetting.json")
#
#     assert os.system(command3) == 0
#
#     command4 = "python3 -m moiety_modeling modeling --models={0} --datasets={1} --optimizations={2} --repetition=100 --energyFunction=logDifference" \
#         .format("tests/test_data/test_models.json", "tests/test_data/UDP_data_24_48_72.json",
#                 "tests/test_data/optimizationSetting.json")
#
#     assert os.system(command4) == 0


@pytest.mark.parametrize("optimizationPaths_txtfile", [

    ("tests/analysis_results/models_UDP_data_24_48_72_optimizationSetting_T_100_S_M_logDifference/TNC_logDifference.txt"),
    ("tests/analysis_results/models_UDP_data_24_48_72_optimizationSetting_T_100_S_M_logDifference/SLSQP_logDifference.txt"),
    ("tests/analysis_results/models_UDP_data_24_48_72_optimizationSetting_T_100_S_M_logDifference/SAGA_1000_logDifference.txt"),
    ("tests/analysis_results/models_UDP_data_24_48_72_optimizationSetting_T_100_S_M_logDifference/L_BFGS_B_logDifference.txt")
])
def test_analysis_a(optimizationPaths_txtfile):

    command = "python3 -m moiety_modeling analyze optimizations --a {}".format(optimizationPaths_txtfile)

    assert os.system(command) == 0


@pytest.mark.parametrize("optimizationResults_jsonfile", [

    ("tests/analysis_results/models_UDP_data_24_48_72_optimizationSetting_T_100_S_M_logDifference/SAGA_1000/best_model_SAGA_1000.json"),
    ("tests/analysis_results/models_UDP_data_24_48_72_optimizationSetting_T_100_S_M_logDifference/SLSQP/best_model_SLSQP.json"),
    ("tests/analysis_results/models_UDP_data_24_48_72_optimizationSetting_T_100_S_M_logDifference/TNC/best_model_TNC.json"),
    ("tests/analysis_results/models_UDP_data_24_48_72_optimizationSetting_T_100_S_M_logDifference/L_BFGS_B/best_model_L_BFGS_B.json")
])
def test_analysis_s(optimizationResults_jsonfile):

    command = "python3 -m moiety_modeling analyze optimizations --s {}".format(optimizationResults_jsonfile)

    assert os.system(command) == 0


@pytest.mark.parametrize("analysisPaths_txtfile", [

    ("tests/analysis_results/models_UDP_data_24_48_72_optimizationSetting_T_100_S_M_logDifference/SAGA_1000_logDifference_analysis/SAGA_1000_logDifference_analysis.txt"),
    ("tests/analysis_results/models_UDP_data_24_48_72_optimizationSetting_T_100_S_M_logDifference/TNC_logDifference_analysis/TNC_logDifference_analysis.txt"),
    ("tests/analysis_results/models_UDP_data_24_48_72_optimizationSetting_T_100_S_M_logDifference/SLSQP_logDifference_analysis/SLSQP_logDifference_analysis.txt"),
    ("tests/analysis_results/models_UDP_data_24_48_72_optimizationSetting_T_100_S_M_logDifference/L_BFGS_B_logDifference_analysis/L_BFGS_B_logDifference_analysis.txt")
])
def test_rank(analysisPaths_txtfile):

    command = "python3 -m moiety_modeling analyze rank {} --rankCriteria=AICc".format(analysisPaths_txtfile)

    assert os.system(command) == 0


@pytest.mark.parametrize("analysisResults_jsonfile", [

    ("/tests/analysis_results/models_UDP_data_24_48_72_optimizationSetting_T_100_S_M_logDifference/SAGA_1000_logDifference_analysis/best_model_SAGA_1000_logDifference_Stats.json"),
    ("tests/analysis_results/models_UDP_data_24_48_72_optimizationSetting_T_100_S_M_logDifference/TNC_logDifference_analysis/best_model_TNC_logDifference_Stats.json"),
    ("tests/analysis_results/models_UDP_data_24_48_72_optimizationSetting_T_100_S_M_logDifference/SLSQP_logDifference_analysis/best_model_SLSQP_logDifference_Stats.json"),
    ("tests/analysis_results/models_UDP_data_24_48_72_optimizationSetting_T_100_S_M_logDifference/L_BFGS_B_logDifference_analysis/best_model_L_BFGS_B_logDifference_Stats.json")
])
def test_plot(analysisResults_jsonfile):

    command = "python3 -m moiety_modeling plot moiety {}".format(analysisResults_jsonfile)

    assert os.system(command) == 0

    command1 = "python3 -m moiety_modeling plot isotopologue {}".format(analysisResults_jsonfile)

    assert os.system(command1) == 0




