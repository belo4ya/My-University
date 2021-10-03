from __future__ import annotations

from abc import ABC, abstractmethod

from src.utils import to_math, from_math, special_format


class BaseTest(ABC):
    _null_hypothesis = H0 = ''
    _not_null_hypothesis = H1 = ''

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


class FTest(BaseTest):
    r"""
    Проверка гипотезы о значимости линейной регрессии

    Гипотезы:
    \begin{gather}
        H_0: b_1 = ... = b_k = 0, \\
        H_1: b^2_1 + ... + b^2_k > 0.
    \end{gather}

    $ k $ - кол-во факторов в модели

    Формула расчета F-статистики:
    $$ F_{набл} = \frac{\frac{R^2}{k}}{\frac{1 - R^2}{(n - k - 1)}}  $$

    $ R^2 $ - коэффициент детерминации

    Если $ F_{набл} > F_{табл} $, то гипотеза $ H_0 $ отвергается - модель в целом значима
    """
    _null_hypothesis = H0 = 'H_0: {b}_1 = {ellipsis} = {b}_k = 0'
    _not_null_hypothesis = H1 = 'H_1: {b}_1^2 + {ellipsis} + {b}_k^2 > 0'

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
        null_hypothesis = from_math(cls.null_hypothesis(b, details))
        not_null_hypothesis = from_math(cls.not_null_hypothesis(b, details))
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


class TTest(BaseTest):
    r"""
    Проверка гипотез о коэффициенте линейной регрессии

    Гипотезы:
    \begin{gather}
        H_0: b_i = a, \\
        H_1: b_i \neq a.
    \end{gather}

    $ a $ - число, с которым сопоставляют коэффициенты. По умолчанию: $ a = 0 $

    Формула расчета t-статистики:
    $$ t_{набл_{b_i}} = \frac{\hat{b_i} - a}{S_{\hat{b_i}}} $$

    $ \hat{b_i} $ - оценка коэффициента
    $ S_{\hat{b_i} $ - стандартная ошибка оценки коэффициента

    Если $ |t_{набл}| > t_{табл} $, то гипотеза $ H_0 $ отвергается - отличие коэффициента $ b_i $ от $ a $
    является статистически значимым (неслучайным)
    """
    _null_hypothesis = H0 = 'H_0: {b}_i = {a}'
    _not_null_hypothesis = H1 = r'H_1: {b}_i \neq {a}'

    @classmethod
    def null_hypothesis(cls, b: str = 'b', a: float | int = 0, inline: bool = False) -> str:
        return cls._get_hypothesis(cls._null_hypothesis, b, a, inline)

    @classmethod
    def not_null_hypothesis(cls, b: str = 'b', a: float | int = 0, inline: bool = False) -> str:
        return cls._get_hypothesis(cls._not_null_hypothesis, b, a, inline)

    @classmethod
    def hypotheses(cls, b: str = 'b', a: float | int = 0, inline: bool = False) -> str:
        null_hypothesis = from_math(cls.null_hypothesis(b, a))
        not_null_hypothesis = from_math(cls.not_null_hypothesis(b, a))
        expr = rf'{null_hypothesis}, \\ {not_null_hypothesis}.'
        return to_math(expr, inline=inline)

    @staticmethod
    def _get_hypothesis(template: str, b: str, a: float | int, inline: bool) -> str:
        return to_math(template.format(b=b, a=a), inline=inline)
