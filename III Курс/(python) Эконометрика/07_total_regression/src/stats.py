from __future__ import annotations

import warnings
from functools import cached_property

import numpy as np
import pandas as pd
import scipy
import statsmodels.api as sm


def add_constant(x: pd.Series | pd.DataFrame) -> pd.DataFrame:
    warnings.filterwarnings('ignore')
    x = sm.add_constant(x)
    warnings.resetwarnings()
    return x


class LinearRegression:

    def __init__(self, y: pd.Series, x: pd.Series | pd.DataFrame):
        self._y = y
        self._x = x
        self._model = sm.OLS(self._y, self._x)
        self._results = self._model.fit()

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def results(self) -> sm.regression.linear_model.RegressionResults:
        return self._results

    def summary(self):
        return self._results.summary()

    @property
    def k_constant(self):
        return self._model.k_constant

    @property
    def df_model(self):
        return self._results.df_model

    @property
    def params(self):
        r"""
        $ \hat{b_i} $ - оценки параметров модели

        """
        return self._results.params

    @property
    def bse(self):
        r"""
        $ \hat{S_{b_i}} $ - оценки среднеквадратического отклонения оценок параметров$

        """
        return self._results.bse

    @cached_property
    def rmsd_resid(self):
        """
        $ S_{e_i} $ - оценка среднеквадратического отклонения возмущений

        """
        return np.sqrt(self._results.mse_resid)

    @property
    def rsquared(self):
        """
        $ R^2 $ - коэффициент детерминации

        """
        return self._results.rsquared

    @cached_property
    def mapprxe(self):
        """
        $ A $ - средняя относительная ошибка аппроксимации

        """
        return np.mean(np.abs(self._results.resid / self._y)) * 100

    @property
    def f_value(self):
        """
        $ F_{набл} $ - F-критерий Фишера

        """
        return self._results.fvalue

    def f_critical(self, alpha=0.05):
        """
        $ F_{табл} $ - табличное значение F-критерия Фишера

        :param alpha: уровень значимости
        """
        return scipy.stats.f.ppf(1 - alpha, self._results.nobs, self._results.df_resid)  # noqa

    @property
    def f_pvalue(self):
        """
        $ p{-value}_F $ - p-value для F-критерия Фишера

        """
        return self._results.f_pvalue

    @property
    def t_values(self):
        """
        $ t_{iнабл} $ - значения статистики t-критерия Стьюдента

        """
        return self._results.tvalues

    def t_critical(self, alpha=0.05):
        """
        $ t_{табл} $ - табличное значение статистики t-критерия Стьюдента

        :param alpha: уровень значимости
        """
        return scipy.stats.t.ppf(1 - alpha / 2, self._results.df_resid)  # noqa

    @property
    def t_pvalues(self):
        """
        $ p{-value}_{ti} $ - p-value для t-критерия Стьюдента для оценки значимости параметров модели

        """
        return self._results.pvalues

    def conf_int(self, alpha=0.05, cols=None):
        """
        Доверительные интервалы

        :param alpha: уровень доверительного интервала. По умолчанию 95%
        :param cols:
        """
        return self._results.conf_int(alpha=alpha, cols=cols)

    @cached_property
    def beta(self):
        """
        $ \beta_i $ - бета-коэффициенты

        """
        return (self.params * self._x.std() / self._y.std()).drop('const', errors='ignore')

    @cached_property
    def delta(self):
        r"""
        $ \Delta_i $ - дельта-коэффициенты

        """
        return (self._x.corrwith(self._y) * self.beta / self.rsquared).drop('const', errors='ignore')

    @cached_property
    def elasticity(self):
        """
        $ Э_i $ - коэффициенты эластичности

        """
        return (self.params * self._x.mean() / self._y.mean()).drop('const', errors='ignore')

    @cached_property
    def dw_value(self):
        return sm.stats.durbin_watson(self._results.resid)
