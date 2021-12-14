import pandas as pd
from IPython.display import Markdown

from src._components import (
    to_math,
    CONF_INT,
    PrettyModel,
    FTest,
    TTest,
    RMSD_RESID,
    RSQUARED,
    MAPPRXE,
    BETA,
    DELTA,
    ELASTICITY,
    DurbinWatsonTest, BreuschGodfreyTest
)
from src.stats import LinearRegression

SEP = '<br>\n'


def general(model: LinearRegression, precision: int = 3) -> Markdown:
    pretty_model = PrettyModel(model, precision=precision)
    return Markdown((SEP + SEP).join([
        pretty_model.specification(inline=True),
        pretty_model.true_form(inline=True),
        pretty_model.parameterized(inline=True),
        SEP.join(pretty_model.bse(inline=True))
    ]))


def general_assessment(model: LinearRegression, precision: int = 3) -> Markdown:
    return Markdown((SEP + SEP + SEP).join([
        _rmsd_resid(model, precision=precision),
        _rsquared(model, precision=precision),
        _mapprxe(model, precision=precision),
    ]))


def _rmsd_resid(model: LinearRegression, precision: int = 3) -> str:
    title = '### Оценка среднеквадратического отклонения возмущений.'
    assessments = [
        (pd.Interval(0, 2), '<b>10/10</b>'),
        (pd.Interval(2, 5), '<b>8/10</b>'),
        (pd.Interval(5, 10), '<b>7.5/10</b>'),
        (pd.Interval(10, 15), '<b>3.5/10</b>'),
        (pd.Interval(15, 30), '<b>0.8/10</b>'),
        (None, '<b>0/10</b>')
    ]
    percent = model.rmsd_resid * 100
    percent_pretty = rf'{percent:.2f}_{{S_{{ei}}}} \%'
    expr = (to_math(rf'{assessments[-2][0].right} \% < {percent_pretty} \rightarrow', inline=True) +
            f' оценка: {assessments[-1][1]}.')
    for interval, assessment in assessments[:-1]:
        if percent in interval:
            expr = (to_math(rf'{interval.left} \% < {percent_pretty} < {interval.right} \% \rightarrow', inline=True) +
                    f' оценка: {assessment}.')
            break

    pretty_model = PrettyModel(model, precision=precision)
    expr = SEP.join([
        title + SEP,
        to_math(RMSD_RESID, inline=True) + SEP,
        pretty_model.rmsd_resid(inline=True),
        expr
    ])

    return expr


def _rsquared(model: LinearRegression, precision: int = 3) -> str:
    title = '### Коэффициент детерминации.'
    assessments = [
        (pd.Interval(0.9, 1), '<b>10/10</b>'),
        (pd.Interval(0.8, 0.9), '<b>8/10</b>'),
        (pd.Interval(0.7, 0.8), '<b>7/10</b>'),
        (pd.Interval(0.5, 0.7), '<b>3/10</b>'),
        (None, '<b>0/10</b>')
    ]

    rsquared_ = model.rsquared
    rsquared_pretty = f'{rsquared_:.{precision}f}'
    expr = (to_math(rf'{assessments[-2][0].left} > {rsquared_pretty} \rightarrow', inline=True) +
            f' оценка: {assessments[-1][1]}.')
    for interval, assessment in assessments[:-1]:
        if rsquared_ in interval:
            expr = (to_math(rf'{interval.left} < {rsquared_pretty} < {interval.right} \rightarrow', inline=True) +
                    f' оценка: {assessment}.')
            break

    pretty_model = PrettyModel(model, precision=precision)
    expr = SEP.join([
        title + SEP,
        to_math(RSQUARED, inline=True) + SEP,
        pretty_model.rsquared(inline=True),
        expr
    ])

    return expr


def _mapprxe(model: LinearRegression, precision: int = 3) -> str:
    title = '### Средняя относительная ошибка аппроксимации.'
    assessments = [
        (pd.Interval(0, 2), '<b>10/10</b>'),
        (pd.Interval(2, 5), '<b>8/10</b>'),
        (pd.Interval(5, 10), '<b>6/10</b>'),
        (pd.Interval(10, 15), '<b>2/10</b>'),
        (None, '<b>0/10</b>')
    ]

    mapprxe_ = model.mapprxe
    mapprxe_pretty = f'{mapprxe_:.{precision}f}'
    expr = (to_math(rf'{assessments[-2][0].right} \% < {mapprxe_pretty} \rightarrow', inline=True) +
            f' оценка: {assessments[-1][1]}.')
    for interval, assessment in assessments[:-1]:
        if mapprxe_ in interval:
            expr = (to_math(rf'{interval.left} \% < {mapprxe_pretty} < {interval.right} \% \rightarrow', inline=True) +
                    f' оценка: {assessment}.')
            break

    pretty_model = PrettyModel(model, precision=precision)
    expr = SEP.join([
        title + SEP,
        to_math(MAPPRXE, inline=True) + SEP,
        pretty_model.mapprxe(inline=True),
        expr
    ])

    return expr


def f_test(model: LinearRegression, precision: int = 3, alpha: float = 0.05) -> Markdown:
    return Markdown(FTest(model, precision=precision).report(alpha=alpha))


def t_test(model: LinearRegression, precision: int = 3, alpha: float = 0.05) -> Markdown:
    return Markdown(TTest(model, precision=precision).report(alpha=alpha))


def conf_int(model: LinearRegression, precision: int = 3, alpha: float = 0.05) -> Markdown:
    pretty_model = PrettyModel(model, precision=precision)
    conf_int = pretty_model.conf_int(alpha=alpha, inline=True)
    return Markdown((SEP + SEP).join([
        to_math(CONF_INT, inline=True),
        to_math(rf'\alpha = {alpha}', inline=True),
        SEP.join(conf_int)
    ]))


def other(model: LinearRegression, precision: int = 3) -> Markdown:
    pretty_model = PrettyModel(model, precision=precision)
    beta = (
            '### Бета-коэффициенты.' + SEP + SEP +
            to_math(BETA, inline=True) + SEP + SEP +
            SEP.join(pretty_model.beta(inline=True))
    )
    delta = (
            '### Дельта-коэффициенты.' + SEP + SEP +
            to_math(DELTA, inline=True) + SEP + SEP +
            SEP.join(pretty_model.delta(inline=True))
    )
    elasticity = (
            '### Коэффициенты эластичности.' + SEP + SEP +
            to_math(ELASTICITY, inline=True) + SEP + SEP +
            SEP.join(pretty_model.elasticity(inline=True))
    )
    return Markdown((SEP + SEP).join([beta, delta, elasticity]))


def dw_test(model: LinearRegression, precision: int = 3) -> Markdown:
    return Markdown(DurbinWatsonTest(model, precision=precision).report())


def bg_test(model: LinearRegression, precision: int = 3) -> Markdown:
    return Markdown(BreuschGodfreyTest(model, precision=precision).report())
