from optopsy.backtest import run
from optopsy.option_strategies import long_iron_condor, short_iron_condor
from optopsy.data import get
from datetime import datetime
import os
import pytest

CURRENT_FILE = os.path.abspath(os.path.dirname(__file__))
TEST_FILE_PATH_FULL = os.path.join(
    CURRENT_FILE, "../test_data/test_options_data_full.csv"
)


def test_long_iron_condor_integration(hod_struct):
    data = get(TEST_FILE_PATH_FULL, hod_struct, prompt=False)

    filters = {
        "leg1_delta": (0.05, 0.10, 0.15),
        "leg2_delta": (0.25, 0.30, 0.45),
        "leg3_delta": (0.25, 0.30, 0.45),
        "leg4_delta": (0.05, 0.10, 0.15),
        "entry_dte": 31,
        "exit_dte": 7,
    }

    start = datetime(2018, 1, 1)
    end = datetime(2018, 2, 28)

    trades = long_iron_condor(data, start, end, filters)
    backtest = run(data, trades, filters)
    print(backtest[1])
    assert backtest[0] == 53225
    assert (
        backtest[1].iat[0, 5] == 1
        and backtest[1].iat[0, 9] == -0.10
        and backtest[1].iat[0, 8] == 2580
        and backtest[1].iat[0, 16] == 4550.0
    )
    assert (
        backtest[1].iat[1, 5] == -1
        and backtest[1].iat[1, 9] == -0.30
        and backtest[1].iat[1, 8] == 2665
        and backtest[1].iat[1, 16] == -12550.0
    )
    assert (
        backtest[1].iat[2, 5] == -1
        and backtest[1].iat[2, 9] == 0.31
        and backtest[1].iat[2, 8] == 2720
        and backtest[1].iat[2, 16] == 110550.0
    )
    assert (
        backtest[1].iat[3, 5] == 1
        and backtest[1].iat[3, 9] == 0.10
        and backtest[1].iat[3, 8] == 2750
        and backtest[1].iat[3, 16] == -87925.0
    )
    assert (
        backtest[1].iat[4, 5] == 1
        and backtest[1].iat[4, 9] == -0.10
        and backtest[1].iat[4, 8] == 2675
        and backtest[1].iat[4, 16] == -10500.0
    )
    assert (
        backtest[1].iat[5, 5] == -1
        and backtest[1].iat[5, 9] == -0.30
        and backtest[1].iat[5, 8] == 2775
        and backtest[1].iat[5, 16] == 60200.0
    )
    assert (
        backtest[1].iat[6, 5] == -1
        and backtest[1].iat[6, 9] == 0.30
        and backtest[1].iat[6, 8] == 2865
        and backtest[1].iat[6, 16] == -14250.0
    )
    assert (
        backtest[1].iat[7, 5] == 1
        and backtest[1].iat[7, 9] == 0.10
        and backtest[1].iat[7, 8] == 2920
        and backtest[1].iat[7, 16] == 3150.0
    )


def test_long_iron_condor_market_integration(hod_struct):
    data = get(TEST_FILE_PATH_FULL, hod_struct, prompt=False)

    filters = {
        "leg1_delta": (0.05, 0.10, 0.15),
        "leg2_delta": (0.25, 0.30, 0.45),
        "leg3_delta": (0.25, 0.30, 0.45),
        "leg4_delta": (0.05, 0.10, 0.15),
        "entry_dte": 31,
        "exit_dte": 7,
    }

    start = datetime(2018, 1, 1)
    end = datetime(2018, 2, 28)

    trades = long_iron_condor(data, start, end, filters)
    backtest = run(data, trades, filters, mode="market")
    print(backtest[1])
    assert backtest[0] == 61350.0
    assert (
        backtest[1].iat[0, 5] == 1
        and backtest[1].iat[0, 9] == -0.10
        and backtest[1].iat[0, 8] == 2580
        and backtest[1].iat[0, 16] == 4700.0
    )
    assert (
        backtest[1].iat[1, 5] == -1
        and backtest[1].iat[1, 9] == -0.30
        and backtest[1].iat[1, 8] == 2665
        and backtest[1].iat[1, 16] == -12300.0
    )
    assert (
        backtest[1].iat[2, 5] == -1
        and backtest[1].iat[2, 9] == 0.31
        and backtest[1].iat[2, 8] == 2720
        and backtest[1].iat[2, 16] == 113300.0
    )
    assert (
        backtest[1].iat[3, 5] == 1
        and backtest[1].iat[3, 9] == 0.10
        and backtest[1].iat[3, 8] == 2750
        and backtest[1].iat[3, 16] == -86650.0
    )
    assert (
        backtest[1].iat[4, 5] == 1
        and backtest[1].iat[4, 9] == -0.10
        and backtest[1].iat[4, 8] == 2675
        and backtest[1].iat[4, 16] == -9900.0
    )
    assert (
        backtest[1].iat[5, 5] == -1
        and backtest[1].iat[5, 9] == -0.30
        and backtest[1].iat[5, 8] == 2775
        and backtest[1].iat[5, 16] == 62900.0
    )
    assert (
        backtest[1].iat[6, 5] == -1
        and backtest[1].iat[6, 9] == 0.30
        and backtest[1].iat[6, 8] == 2865
        and backtest[1].iat[6, 16] == -14000.0
    )
    assert (
        backtest[1].iat[7, 5] == 1
        and backtest[1].iat[7, 9] == 0.10
        and backtest[1].iat[7, 8] == 2920
        and backtest[1].iat[7, 16] == 3300.0
    )


def test_long_iron_condor_butterfly_integration(hod_struct):
    data = get(TEST_FILE_PATH_FULL, hod_struct, prompt=False)

    filters = {
        "leg1_delta": (0.25, 0.30, 0.45),
        "leg2_delta": (0.45, 0.50, 0.55),
        "leg3_delta": (0.45, 0.50, 0.55),
        "leg4_delta": (0.25, 0.30, 0.45),
        "entry_dte": (18, 18, 18),
        "exit_dte": 7,
    }

    start = datetime(2018, 1, 1)
    end = datetime(2018, 2, 28)

    trades = long_iron_condor(data, start, end, filters)
    backtest = run(data, trades, filters)
    print(backtest[1])
    assert backtest[1].empty


def test_short_iron_condor_integration(hod_struct):
    data = get(TEST_FILE_PATH_FULL, hod_struct, prompt=False)

    filters = {
        "leg1_delta": (0.05, 0.10, 0.15),
        "leg2_delta": (0.25, 0.30, 0.45),
        "leg3_delta": (0.25, 0.30, 0.45),
        "leg4_delta": (0.05, 0.10, 0.15),
        "entry_dte": 31,
        "exit_dte": 7,
    }

    start = datetime(2018, 1, 1)
    end = datetime(2018, 2, 28)

    trades = short_iron_condor(data, start, end, filters)
    backtest = run(data, trades, filters)
    print(backtest[1])
    assert backtest[0] == -53225
    assert (
        backtest[1].iat[0, 5] == -1
        and backtest[1].iat[0, 9] == -0.10
        and backtest[1].iat[0, 8] == 2580
        and backtest[1].iat[0, 16] == -4550.0
    )
    assert (
        backtest[1].iat[1, 5] == 1
        and backtest[1].iat[1, 9] == -0.30
        and backtest[1].iat[1, 8] == 2665
        and backtest[1].iat[1, 16] == 12550.0
    )
    assert (
        backtest[1].iat[2, 5] == 1
        and backtest[1].iat[2, 9] == 0.31
        and backtest[1].iat[2, 8] == 2720
        and backtest[1].iat[2, 16] == -110550.0
    )
    assert (
        backtest[1].iat[3, 5] == -1
        and backtest[1].iat[3, 9] == 0.10
        and backtest[1].iat[3, 8] == 2750
        and backtest[1].iat[3, 16] == 87925.0
    )
    assert (
        backtest[1].iat[4, 5] == -1
        and backtest[1].iat[4, 9] == -0.10
        and backtest[1].iat[4, 8] == 2675
        and backtest[1].iat[4, 16] == 10500.0
    )
    assert (
        backtest[1].iat[5, 5] == 1
        and backtest[1].iat[5, 9] == -0.30
        and backtest[1].iat[5, 8] == 2775
        and backtest[1].iat[5, 16] == -60200.0
    )
    assert (
        backtest[1].iat[6, 5] == 1
        and backtest[1].iat[6, 9] == 0.30
        and backtest[1].iat[6, 8] == 2865
        and backtest[1].iat[6, 16] == 14250.0
    )
    assert (
        backtest[1].iat[7, 5] == -1
        and backtest[1].iat[7, 9] == 0.10
        and backtest[1].iat[7, 8] == 2920
        and backtest[1].iat[7, 16] == -3150.0
    )
