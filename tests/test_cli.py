import os
import pytest




def test_modeling():

    command1 = "python3 -m moiety_modeling modeling --models={0} --datasets={1} --optimizations={2} --repetition=100 --split --multiprocess --energyFunction=logDifference" \
        .format("tests/test_data/test_models.json", "tests/test_data/UDP_data_24_48_72.json",
                "tests/test_data/optimizationSetting.json")

    assert os.system(command1) == 0

    command2 = "python3 -m moiety_modeling modeling --models={0} --datasets={1} --optimizations={2} --repetition=100 --multiprocess --energyFunction=logDifference" \
        .format("tests/test_data/test_models.json", "tests/test_data/UDP_data_24_48_72.json",
                "tests/test_data/optimizationSetting.json")

    assert os.system(command2) == 0

    command3 = "python3 -m moiety_modeling modeling --models={0} --datasets={1} --optimizations={2} --repetition=100 --split --energyFunction=logDifference" \
        .format("tests/test_data/test_models.json", "tests/test_data/UDP_data_24_48_72.json",
                "tests/test_data/optimizationSetting.json")

    assert os.system(command3) == 0

    command4 = "python3 -m moiety_modeling modeling --models={0} --datasets={1} --optimizations={2} --repetition=100 --energyFunction=logDifference" \
        .format("tests/test_data/test_models.json", "tests/test_data/UDP_data_24_48_72.json",
                "tests/test_data/optimizationSetting.json")

    assert os.system(command4) == 0




@pytest.mark.parametrize("optimizationPaths_txtfile", [




])

def test_analysis_a(optimizationPaths_txtfile):

    command = "python3 -m moiety_modeling analyze optimizations --a {}".format(optimizationPaths_txtfile)

    assert os.system(command) == 0




@pytest.mark.parametrize("optimizationResults_jsonfile", [



])

def test_analysis_s(optimizationResults_jsonfile):

    command = "python3 -m moiety_modeling analyze optimizations --s {}".format(optimizationResults_jsonfile)

    assert os.system(command) == 0




@pytest.mark.parametrize("analysisPaths_txtfile", [



])

def test_rank(analysisPaths_txtfile):

    command = "python3 -m moiety_modeling analyze rank {} --rankCriteria=AICc".format(analysisPaths_txtfile)

    assert os.system(command) == 0




def test_table():


def test_plot():



