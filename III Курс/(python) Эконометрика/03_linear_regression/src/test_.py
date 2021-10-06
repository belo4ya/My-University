from __future__ import annotations

from abc import ABC, abstractmethod

import numpy as np
import pandas as pd

from src.display import ModelView
from src.formula import F_VALUE, T_VALUE
from src.stats import LinearRegression
from src.utils import to_math, from_math, special_format


class BaseTest(ABC):
    _null_hypothesis = ''
    _not_null_hypothesis = ''
    _formula = ''

    def __init__(self, model: LinearRegression):
        self._model = model

    @classmethod
    @abstractmethod
    def null_hypothesis(cls, *args, **kwargs) -> str:
        pass

    @classmethod
    @abstractmethod
    def not_null_hypothesis(cls, *args, **kwargs) -> str:
        pass

    @classmethod
    @abstractmethod
    def hypotheses(cls, *args, **kwargs) -> str:
        pass

    H0 = null_hypothesis
    H1 = not_null_hypothesis
    H = hypotheses

    @classmethod
    @abstractmethod
    def formula(cls, inline: bool = False) -> str:
        pass

    @abstractmethod
    def critical_test(self, alpha: float) -> bool:
        pass

    @abstractmethod
    def pvalue_test(self, alpha: float) -> bool:
        pass

    @abstractmethod
    def test_report(self, alpha: float, precision: int) -> str:
        pass

    @abstractmethod
    def report(self) -> str:
        pass


class FTest(BaseTest):
    r"""
    Проверка гипотезы о значимости линейной регрессии

    Гипотезы:
    ---------
        \begin{gather}
            H_0: b_1 = ... = b_k = 0, \\
            H_1: b^2_1 + ... + b^2_k > 0.
        \end{gather}

        $ k $ - кол-во факторов в модели

    Формула расчета F-статистики:
    -----------------------------
        $$ F_{набл} = \frac{\frac{R^2}{k}}{\frac{1 - R^2}{(n - k - 1)}}  $$

        $ R^2 $ - коэффициент детерминации

    Если $ F_{набл} > F_{табл} $, то гипотеза $ H_0 $ отвергается - модель в целом значима
    """

    _null_hypothesis = 'H_0: {b}_1 = {ellipsis} = {b}_k = 0'
    _not_null_hypothesis = 'H_1: {b}_1^2 + {ellipsis} + {b}_k^2 > 0'
    _implication = 'гипотеза $ H_0 $ {verdict} - модель в целом {expertise}.'

    _verdicts = {
        True: {'verdict': '<b>принимается</b>', 'expertise': '<b>незначима</b>'},
        False: {'verdict': '<b>отвергается</b>', 'expertise': '<b>значима</b>'}
    }
    _formula = F_VALUE
    _title = '### F-критерий Фишера.'

    @classmethod
    def null_hypothesis(cls, b: str = 'b', details: int = 0, inline: bool = False) -> str:
        ellipsis_ = special_format(cls._get_ellipsis(b, details), sign='=', apply='')
        return cls._get_hypothesis(cls._null_hypothesis, b, ellipsis_, inline)

    @classmethod
    def not_null_hypothesis(cls, b: str = 'b', details: int = 0, inline: bool = False) -> str:
        ellipsis_ = special_format(cls._get_ellipsis(b, details), sign='+', apply='^2')
        return cls._get_hypothesis(cls._not_null_hypothesis, b, ellipsis_, inline)

    @classmethod
    def hypotheses(cls, b: str = 'b', details: int = 0, inline: bool = False) -> str:
        null_hypothesis = from_math(cls.null_hypothesis(b=b, details=details))
        not_null_hypothesis = from_math(cls.not_null_hypothesis(b=b, details=details))
        expr = rf'{null_hypothesis}, \\ {not_null_hypothesis}.'
        return to_math(expr, inline=inline)

    @staticmethod
    def _get_hypothesis(template: str, b: str, ellipsis_: str, inline: bool) -> str:
        return to_math(template.format(b=b, ellipsis=ellipsis_), inline=inline)

    @staticmethod
    def _get_ellipsis(b: str, details: int) -> str:
        if details:
            return ' {sign} '.join([*[f'{b}_{{{i}}}{{apply}}' for i in range(2, details + 2)], '...'])
        return '...'

    H0 = null_hypothesis
    H1 = not_null_hypothesis
    H = hypotheses

    @classmethod
    def formula(cls, inline: bool = False) -> str:
        return to_math(cls._formula, inline=inline)

    def critical_test(self, alpha: float = 0.05) -> bool:
        return self._model.f_value < self._model.f_critical(alpha=alpha)

    def pvalue_test(self, alpha: float = 0.05) -> bool:
        return self._model.f_pvalue > alpha

    def test_report(self, alpha: float = 0.05, precision: int = 3) -> str:
        r"""
        Пример:
        -------
            $ F_{набл} = 17.7 $<br>
            $ p\text{-}value = 6.83e−06$
            <br><br>
            $ \alpha = 0.05 $<br>
            $ F_{табл_{0.05}} = 2.21 $
            <br><br>
            $ 6.83e−06 < 0.05 $<br>
            $ p\text{-}value < \alpha \rightarrow $ - гипотеза $ H_0 $ отвергается - модель в целом значима.
        """
        model_view = ModelView(self._model, precision=precision)
        f_value, f_pvalue = self._model.f_value, self._model.f_pvalue

        calc_assign = model_view.f_value(inline=True) + '<br>\n' + model_view.f_pvalue(inline=True)
        present_assign = (to_math(rf'\alpha = {alpha}', inline=True) + '<br>\n' +
                          model_view.f_critical(alpha=alpha, inline=True))

        null_hypothesis = self.pvalue_test(alpha=alpha)
        if null_hypothesis:
            sign = '>'
        else:
            sign = '<'

        parameterized = to_math(f'{f_pvalue:.{precision}g} {sign} {alpha}', inline=True) + '<br>\n'
        literal = to_math(rf'p\text{{-}}value {sign} \alpha \rightarrow', inline=True)

        premise = '\n<br><br>\n'.join([calc_assign, present_assign, parameterized + literal])
        implication = self._implication.format(**self._verdicts[null_hypothesis])

        return premise + ' ' + implication

    def report(self, alpha: float = 0.05, precision: int = 3) -> str:
        return '\n<br><br>\n'.join([
            self._title + '\n<br>\n',
            self.hypotheses(inline=True),
            self.formula(),
            self.test_report(alpha=alpha, precision=precision)
        ])


class TTest(BaseTest):
    r"""
    Проверка гипотез о коэффициенте линейной регрессии

    Гипотезы:
    ---------
        \begin{gather}
            H_0: b_i = 0, \\
            H_1: b_i \neq 0.
        \end{gather}

    Формула расчета t-статистики:
    -----------------------------
        $$ t_{набл_{b_i}} = \frac{\hat{b_i}}{S_{\hat{b_i}}} $$

        $ \hat{b_i} $ - оценка коэффициента
        $ S_{\hat{b_i} $ - стандартная ошибка оценки коэффициента

    Если $ |t_{набл}| > t_{табл} $, то гипотеза $ H_0 $ отвергается - отличие
    параметра $ b_i $ от $ 0 $ является статистически значимым (неслучайным)
    """

    _null_hypothesis = 'H_0: {b}_i = {a}'
    _not_null_hypothesis = r'H_1: {b}_i \neq {a}'
    _implication = 'гипотеза $ H_0 $ {verdict} - параметр {b} {expertise}.'

    _verdicts = {
        True: {'verdict': 'принимается', 'expertise': 'незначим'},
        False: {'verdict': 'отвергается', 'expertise': 'значим'}
    }
    _formula = T_VALUE
    _title = '### t-критерий Стьюдента.'

    @classmethod
    def null_hypothesis(cls, b: str = 'b', a: float | int = 0, inline: bool = False) -> str:
        return cls._get_hypothesis(cls._null_hypothesis, b, a, inline)

    @classmethod
    def not_null_hypothesis(cls, b: str = 'b', a: float | int = 0, inline: bool = False) -> str:
        return cls._get_hypothesis(cls._not_null_hypothesis, b, a, inline)

    @classmethod
    def hypotheses(cls, b: str = 'b', a: float | int = 0, inline: bool = False) -> str:
        null_hypothesis = from_math(cls.null_hypothesis(b=b, a=a))
        not_null_hypothesis = from_math(cls.not_null_hypothesis(b=b, a=a))
        expr = rf'{null_hypothesis}, \\ {not_null_hypothesis}.'
        return to_math(expr, inline=inline)

    @staticmethod
    def _get_hypothesis(template: str, b: str, a: float | int, inline: bool) -> str:
        return to_math(template.format(b=b, a=a), inline=inline)

    H0 = null_hypothesis
    H1 = not_null_hypothesis
    H = hypotheses

    def formula(self, inline: bool = False) -> str:
        return to_math(self._formula, inline=inline)

    def critical_test(self, alpha: float = 0.05) -> pd.Series:
        return np.abs(self._model.t_values) < self._model.t_critical(alpha=alpha)  # noqa

    def pvalue_test(self, alpha: float = 0.05) -> pd.Series:
        return self._model.t_pvalues > alpha

    def test_report(self, alpha: float = 0.05, precision: int = 3) -> str:
        r"""
        Пример:
        -------
            $ \alpha = 0.05 $<br>
            <br>
            $ t_{b_i} = 1 $,
            $ p\text{-}value = 0.828 $,
            $ p\text{-}value > \alpha \rightarrow $ - гипотеза $ H_0 $ принимается - параметр $ b_i $ незначим.
        """
        model_view = ModelView(self._model, precision=precision)

        null_hypothesis = self.pvalue_test(alpha=alpha)
        for param, res in null_hypothesis.items():
            print(param, res)
            if res:
                pass
            else:
                pass

            premise = ''

            implication = ''

            for premise, implication in zip(premise, implication):
                pass

        preamble = '\n<br>\n'.join([
            to_math(rf'\alpha = {alpha}', inline=True),
            model_view.t_critical(alpha=alpha, inline=True)
        ])
        return preamble

    def report(self, alpha: float = 0.05, precision: int = 3) -> str:
        return '\n<br><br>\n'.join([
            self._title + '\n<br>\n',
            self.hypotheses(inline=True),
            self.formula(),
            self.test_report(alpha=alpha, precision=precision)
        ])
