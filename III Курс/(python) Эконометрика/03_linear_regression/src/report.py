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
