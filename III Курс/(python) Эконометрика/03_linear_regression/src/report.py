import pandas as pd
from IPython.display import Markdown

from src._components import to_math, CONF_INT, PrettyModel, FTest, TTest
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
    pretty_model = PrettyModel(model, precision=precision)
    return Markdown((SEP + SEP).join([
        pretty_model.rmsd_resid(inline=True),
        pretty_model.rsquared(inline=True),
        pretty_model.mapprxe(inline=True)
    ]))


def rmsd_resid(model: LinearRegression, precision: int = 3) -> Markdown:
    title = '### Оценка среднеквадратического отклонения возмущений.'
    assessments = [
        (pd.Interval(0, 2), '<b>10/10</b>'),
        (pd.Interval(2, 5), '<b>8/10</b>'),
        (pd.Interval(5, 10), '<b>7.5/10</b>'),
        (pd.Interval(10, 15), '<b>3.5/10</b>'),
        (pd.Interval(15, 30), '<b>0.8/10</b>'),
        (None, '<b>0/10</b>')
    ]
    percent = model.rmsd_resid / model.y.mean() * 100
    percent_pretty = rf'{percent:.2f}_{{S_{{ei}}}}\%'
    expr = (to_math(rf'{assessments[-2][0].right}\% < {percent_pretty} \rightarrow', inline=True) +
            f' оценка: {assessments[-1][1]}.')
    for interval, assessment in assessments[:-1]:
        if percent in interval:
            expr = (to_math(rf'{interval.left}\% < {percent_pretty} < {interval.right}\% \rightarrow', inline=True) +
                    f' оценка: {assessment}.')
            break

    pretty_model = PrettyModel(model, precision=precision)
    expr = SEP.join([
        title + SEP,
        pretty_model.rmsd_resid(inline=True),
        expr
    ])

    return Markdown(expr)


def rsquared(model: LinearRegression, precision: int = 3) -> Markdown:
    pass


def mapprxe(model: LinearRegression, precision: int = 3) -> Markdown:
    pass


def f_test(model: LinearRegression, precision: int = 3, alpha: float = 0.05) -> Markdown:
    return Markdown(FTest(model).report(alpha=alpha, precision=precision))


def t_test(model: LinearRegression, precision: int = 3, alpha: float = 0.05) -> Markdown:
    return Markdown(TTest(model).report(alpha=alpha, precision=precision))


def conf_int(model: LinearRegression, precision: int = 3, alpha: float = 0.05) -> Markdown:
    pretty_model = PrettyModel(model, precision=precision)
    conf_int = pretty_model.conf_int(alpha=alpha, inline=True)
    return Markdown((SEP + SEP).join([
        to_math(CONF_INT, inline=True),
        to_math(rf'\alpha = {alpha}', inline=True),
        SEP.join(conf_int)
    ]))
