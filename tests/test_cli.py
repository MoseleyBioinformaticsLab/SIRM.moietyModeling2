import os
import pytest


@pytest.mark.parametrize("settingFile", [

    ("tests/test_data/SLSQP_setting.json"),
    ("tests/test_data/SAGA_setting.json"),
    ("tests/test_data/L-BFGS-B_setting.json")
])
def test_modeling(settingFile):
    # single-tracer testing
    command1 = "python3 -m moiety_modeling modeling --models={0} --datasets={1} --optimizations={2} --repetition=100 --split --multiprocess --energyFunction=logDifference" \
        .format("tests/test_data/model_single.json", "tests/test_data/UDP_single_simulate_48.json", settingFile)

    assert os.system(command1) == 0

    command2 = "python3 -m moiety_modeling modeling --models={0} --datasets={1} --optimizations={2} --repetition=100 --multiprocess --energyFunction=logDifference" \
        .format("tests/test_data/model_single.json", "tests/test_data/UDP_single_simulate_48.json", settingFile)

    assert os.system(command2) == 0

    command3 = "python3 -m moiety_modeling modeling --models={0} --datasets={1} --optimizations={2} --repetition=100 --split --energyFunction=logDifference" \
        .format("tests/test_data/model_single.json", "tests/test_data/UDP_single_simulate_48.json", settingFile)

    assert os.system(command3) == 0

    command4 = "python3 -m moiety_modeling modeling --models={0} --datasets={1} --optimizations={2} --repetition=100 --split --energyFunction=absDifference" \
        .format("tests/test_data/model_single.json", "tests/test_data/UDP_single_simulate_48.json", settingFile)

    assert os.system(command4) == 0

    command5 = "python3 -m moiety_modeling modeling --models={0} --datasets={1} --optimizations={2} --repetition=100 --split --energyFunction=absDifference" \
        .format("tests/test_data/model_single.json", "tests/test_data/UDP_data_48_72.json", settingFile)

    assert os.system(command5) == 0

    # multi-tracer testing
    command6 = "python3 -m moiety_modeling modeling --models={0} --datasets={1} --optimizations={2} --repetition=100 --split --multiprocess --energyFunction=absDifference" \
        .format("tests/test_data/model_multi.json", "tests/test_data/UDP_multi_simulate_48.json", settingFile)

    assert os.system(command6) == 0


@pytest.mark.parametrize("optimizationPaths_txtfile", [

    ("tests/analysis_results/all_single_models_UDP_data_48_72_optimization_setting_T_100_S_M_logDifference/TNC_logDifference.txt"),
    ("tests/analysis_results/all_single_models_UDP_data_48_72_optimization_setting_T_100_S_M_logDifference/SLSQP_logDifference.txt"),
    ("tests/analysis_results/all_single_models_UDP_data_48_72_optimization_setting_T_100_S_M_logDifference/SAGA_1000_logDifference.txt"),
    ("tests/analysis_results/all_single_models_UDP_data_48_72_optimization_setting_T_100_S_M_logDifference/L_BFGS_B_logDifference.txt")
])
def test_analysis_a(optimizationPaths_txtfile):

    base = os.path.basename(optimizationPaths_txtfile)
    baseName = os.path.splitext(base)[0]
    command = "python3 -m moiety_modeling analyze optimizations --a {} --working=tests/{}/ ".format(optimizationPaths_txtfile, baseName)

    assert os.system(command) == 0


@pytest.mark.parametrize("optimizationResults_jsonfile", [

    ("tests/analysis_results/all_single_models_UDP_data_48_72_optimization_setting_T_100_S_M_logDifference/SAGA_1000/best_model_48h_72h_SAGA_1000.json"),
    ("tests/analysis_results/all_single_models_UDP_data_48_72_optimization_setting_T_100_S_M_logDifference/SLSQP/best_model_48h_72h_SLSQP.json"),
    ("tests/analysis_results/all_single_models_UDP_data_48_72_optimization_setting_T_100_S_M_logDifference/TNC/best_model_48h_72h_TNC.json"),
    ("tests/analysis_results/all_single_models_UDP_data_48_72_optimization_setting_T_100_S_M_logDifference/L_BFGS_B/best_model_48h_72h_L_BFGS_B.json")
])
def test_analysis_s(optimizationResults_jsonfile):

    command = "python3 -m moiety_modeling analyze optimizations --s {}".format(optimizationResults_jsonfile)

    assert os.system(command) == 0


@pytest.mark.parametrize("analysisPaths_txtfile", [

    ("tests/analysis_results/all_single_models_UDP_data_48_72_optimization_setting_T_100_S_M_logDifference/SAGA_1000_logDifference_analysis/SAGA_1000_logDifference_analysis.txt"),
    ("tests/analysis_results/all_single_models_UDP_data_48_72_optimization_setting_T_100_S_M_logDifference/TNC_logDifference_analysis/TNC_logDifference_analysis.txt"),
    ("tests/analysis_results/all_single_models_UDP_data_48_72_optimization_setting_T_100_S_M_logDifference/SLSQP_logDifference_analysis/SLSQP_logDifference_analysis.txt"),
    ("tests/analysis_results/all_single_models_UDP_data_48_72_optimization_setting_T_100_S_M_logDifference/L_BFGS_B_logDifference_analysis/L_BFGS_B_logDifference_analysis.txt")
])
def test_rank(analysisPaths_txtfile):

    base = os.path.basename(analysisPaths_txtfile)
    baseName = os.path.splitext(base)[0]
    command = "python3 -m moiety_modeling analyze rank {} --working=tests/{}/ --rankCriteria=AICc".format(analysisPaths_txtfile, baseName)

    assert os.system(command) == 0


@pytest.mark.parametrize("analysisResults_jsonfile", [

    ("tests/analysis_results/all_single_models_UDP_data_48_72_optimization_setting_T_100_S_M_logDifference/SAGA_1000_logDifference_analysis/best_model_48h_72h_SAGA_1000_States.json"),
    ("tests/analysis_results/all_single_models_UDP_data_48_72_optimization_setting_T_100_S_M_logDifference/TNC_logDifference_analysis/best_model_48h_72h_TNC_States.json"),
    ("tests/analysis_results/all_single_models_UDP_data_48_72_optimization_setting_T_100_S_M_logDifference/SLSQP_logDifference_analysis/best_model_48h_72h_SLSQP_States.json"),
    ("tests/analysis_results/all_single_models_UDP_data_48_72_optimization_setting_T_100_S_M_logDifference/L_BFGS_B_logDifference_analysis/best_model_48h_72h_L_BFGS_B_States.json")
])
def test_plot(analysisResults_jsonfile):

    command = "python3 -m moiety_modeling plot moiety {}".format(analysisResults_jsonfile)

    assert os.system(command) == 0

    command1 = "python3 -m moiety_modeling plot isotopologue {}".format(analysisResults_jsonfile)

    assert os.system(command1) == 0




