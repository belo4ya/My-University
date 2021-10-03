from __future__ import annotations

import scipy
import statsmodels.api as sm
import numpy as np
import pandas as pd
import warnings


def add_constant(x: pd.Series | pd.DataFrame) -> pd.DataFrame:
    warnings.filterwarnings('ignore')
    x = sm.add_constant(x)
    warnings.resetwarnings()
    return x


sm.regression.linear_model.RegressionResults