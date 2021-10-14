from __future__ import annotations

from abc import ABC, abstractmethod

import numpy as np
import pandas as pd

from src._components.formula import F_VALUE, T_VALUE, DW_VALUE
from src._components.pretty import PrettyModel
from src._components.utils import to_math, from_math, special_format
from src.stats import LinearRegression


class BaseTest(ABC):
    _null_hypothesis = ''
    _not_null_hypothesis = ''
    _formula = ''

    def __init__(self, model: LinearRegression, precision: int = 3):
        self._model = model
        self._precision = precision
        self._pretty_model = PrettyModel(model, precision=precision)

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
    def critical_test(self, **kwargs) -> bool:
        pass

    @abstractmethod
    def pvalue_test(self, alpha: float) -> bool:
        pass

    @abstractmethod
    def test_report(self, **kwargs) -> str:
        pass

    @abstractmethod
    def report(self) -> str:
        pass


class FTest(BaseTest):
    r"""
    F-тест.
    Проверка гипотезы о значимости линейной регрессии.

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

    def test_report(self, alpha: float = 0.05) -> str:
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
        f_value, f_pvalue = self._model.f_value, self._model.f_pvalue

        calc_assign = self._pretty_model.f_value(inline=True) + '<br>\n' + self._pretty_model.f_pvalue(inline=True)
        present_assign = (to_math(rf'\alpha = {alpha}', inline=True) + '<br>\n' +
                          self._pretty_model.f_critical(alpha=alpha, inline=True))

        null_hypothesis = self.pvalue_test(alpha=alpha)
        if null_hypothesis:
            sign = '>'
        else:
            sign = '<'

        parameterized = to_math(f'{f_pvalue:.{self._precision}g} {sign} {alpha}', inline=True) + '<br>\n'
        literal = to_math(rf'p\text{{-}}value {sign} \alpha \rightarrow', inline=True)

        premise = '\n<br><br>\n'.join([calc_assign, present_assign, parameterized + literal])
        implication = self._implication.format(**self._verdicts[null_hypothesis])

        return premise + ' ' + implication

    def report(self, alpha: float = 0.05) -> str:
        return '\n<br><br>\n'.join([
            self._title,
            self.hypotheses(inline=True),
            self.formula(),
            self.test_report(alpha=alpha)
        ])


class TTest(BaseTest):
    r"""
    T-тест.
    Проверка гипотез о коэффициенте линейной регрессии.

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
    _implication = 'гипотеза $ H_0 $ {verdict} - параметр {expertise}.'

    _verdicts = {
        True: {'verdict': '<b>принимается</b>', 'expertise': '<b>незначим</b>'},
        False: {'verdict': '<b>отвергается</b>', 'expertise': '<b>значим</b>'}
    }
    _formula = T_VALUE
    _title = '### t-критерий Стьюдета для оценки значимости параметров модели.'

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

    @classmethod
    def formula(cls, inline: bool = False) -> str:
        return to_math(cls._formula, inline=inline)

    def critical_test(self, alpha: float = 0.05) -> pd.Series:
        return np.abs(self._model.t_values) < self._model.t_critical(alpha=alpha)  # noqa

    def pvalue_test(self, alpha: float = 0.05) -> pd.Series:
        return self._model.t_pvalues > alpha

    def test_report(self, alpha: float = 0.05) -> str:
        r"""
        Пример:
        -------

        """
        lines = []
        for res, t_value, t_pvalue in zip(
                self.pvalue_test(alpha=alpha),
                self._pretty_model.t_values(inline=True),
                self._pretty_model.t_pvalues(inline=True)
        ):
            sign = '>' if res else '<'
            literal = to_math(rf'p\text{{-}}value {sign} \alpha \rightarrow', inline=True)
            lines.append(', '.join([t_value, t_pvalue, literal]) +
                         self._implication.format(**self._verdicts[res]))

        preamble = '\n<br>\n'.join([
            to_math(rf'\alpha = {alpha}', inline=True),
            self._pretty_model.t_critical(alpha=alpha, inline=True),
            '\n<br>\n' + '<br>'.join(lines)
        ])

        return preamble

    def report(self, alpha: float = 0.05) -> str:
        return '\n<br><br>\n'.join([
            self._title,
            self.hypotheses(inline=True),
            self.formula(),
            self.test_report(alpha=alpha)
        ])


class DurbinWatsonTest(BaseTest):
    r"""
    Тест Дарбина-Уотсона.

    Проверка гипотез о наличие/отсутствии автокорреляции первого порядка.
    DW-критерий - статистический критерий, используемый для тестирования
    автокорреляции первого порядка элементов исследуемой последовательности.

    Гипотезы:
    ---------
        \begin{gather}
            H_0: \rho_1 = 0, \\
            H_1: \rho_1 \neq 0.
        \end{gather}

    Формула расчета DW-критерия:
    ----------------------------
        $$ DW = \frac{\sum_{i=2}^{n}{(e_i - e_{i-1})^2}}{\sum_{i=1}^{n}{e_i^2}} \approx 2(1-\rho_1) $$

        $ \rho_1 $ - коэффициент автокорреляции первого порядка

    Если $ DW \approx 2 $ - принимается гипотеза $ H_0 $ - автокорреляция отсутствует.
    Если $ 1.5 < DW < 2.5 $ - принимается гипотеза $ H_0 $ - автокорреляция незначительна.
    Иначе - гипотеза $ H_0 $ отвергается - автокорреляция значительна.
    """

    _null_hypothesis = r'H_0: \rho_1 = 0'
    _not_null_hypothesis = r'H_1: \rho_1 \neq 0'
    _implication = 'гипотеза $ H_0 $ {verdict} - автокорреляция {expertise}.'

    _verdicts = {
        True: {'verdict': '<b>принимается</b>', 'expertise': '<b>незначительна или отсутствует</b>'},
        False: {'verdict': '<b>отвергается</b>', 'expertise': '<b>значительна</b>'}
    }
    _formula = DW_VALUE
    _title = '### Критерий Дарбина-Уотсона для тестирования автокорреляции первого порядка.'
    _left, _right = 1.5, 2.5

    @classmethod
    def null_hypothesis(cls, inline: bool = False) -> str:
        return to_math(cls._null_hypothesis, inline=inline)

    @classmethod
    def not_null_hypothesis(cls, inline: bool = False) -> str:
        return to_math(cls._not_null_hypothesis, inline=inline)

    @classmethod
    def hypotheses(cls, b: str = 'b', a: float | int = 0, inline: bool = False) -> str:
        return to_math(rf'{cls._null_hypothesis}, \\ {cls._not_null_hypothesis}.', inline=inline)

    H0 = null_hypothesis
    H1 = not_null_hypothesis
    H = hypotheses

    @classmethod
    def formula(cls, inline: bool = False) -> str:
        return to_math(cls._formula, inline=inline)

    def critical_test(self) -> bool:
        return self._left < self._model.dw_value < self._right

    def pvalue_test(self, alpha: float) -> bool:
        raise NotImplementedError

    def test_report(self) -> str:
        dw_value = self._model.dw_value

        null_hypothesis = self.critical_test()
        if null_hypothesis:
            literal = f'{self._left} < {dw_value:.{self._precision}g} < {self._right}'
        elif dw_value < self._left:
            literal = f'{dw_value:.{self._precision}g} < {self._left}'
        else:
            literal = f'{dw_value:.{self._precision}g} > {self._right}'

        premise = '\n<br><br>\n'.join([
            self._pretty_model.dw_value(inline=True),
            to_math(literal + r' \rightarrow', inline=True)
        ])
        implication = self._implication.format(**self._verdicts[null_hypothesis])

        return premise + ' ' + implication

    def report(self) -> str:
        return '\n<br><br>\n'.join([
            self._title,
            self.hypotheses(inline=True),
            self.formula(),
            self.test_report()
        ])


class BreuschGodfreyTest(BaseTest):
    r"""
    Тест Бреуша-Годфри.

    Проверка гипотез о наличие/отсутствии автокорреляции.

    Гипотезы:
    ---------

    """
    pass


class GoldfeldQuandtTest(BaseTest):
    r"""
    Теста Голдфельда-Квандта.

    Обнаружение гетероскедастичности.

    Гипотезы:
    ---------

    """
    pass


class BreuschPaganTest(BaseTest):
    r"""
    Теста Бреуша-Пагана.

    Обнаружение гетероскедастичности.

    Гипотезы:
    ---------

    """
    pass
