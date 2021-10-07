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
    assessment = {
        pd.Interval(0, 2): '10/10',
        pd.Interval(2, 5): '8/10',
        pd.Interval(5, 10): '7.5/10',
        pd.Interval(10, 15): '3.5/10',
        pd.Interval(15, 30): '0.8/10',
        None: '0/10'
    }
    percent = model.rmsd_resid / model.y.mean() * 100
    for k, v in assessment.items():
        if k is None:
            print(percent, k)
        elif percent in k:
            print(percent, k)
            break


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
