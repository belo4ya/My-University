from __future__ import annotations

import pandas as pd

from src.stats import add_constant, LinearRegression
from src.utils import to_math


class ModelView:
    dependent = 'y_i'
    factor = 'x_{{i{}}}'
    param = 'b_{{{}}}'
    const = 'a_{{{}}}'
    noise = 'e_i'

    def __init__(self, model: LinearRegression, precision: int = 3):
        self._model = model
        self._round = f'.{precision}g'

        self._has_const = self._model.k_constant
        self._n_factors = int(self._model.df_model)

        self._template = '{y} = {a} + {bx}' if self._has_const else '{y} = {bx}'
        self._template = self._template.format(
            y='{y}',
            a='{a}',
            bx=' + '.join([f'{{bx_{i}}}' for i in range(1, self._n_factors + 1)])
        )

    def specification(self, inline: bool = False) -> str:
        template = self._template + ' + {e}'
        bxs = {f'bx_{i}': f'{self.param.format(i)} {self.factor.format(i)}'
               for i in range(1, self._n_factors + 1)}
        expr = template.format(
            y=self.dependent,
            a=self.const.format(0),
            e=self.noise,
            **bxs
        )

        return to_math(expr, inline=inline)

    def true_form(self, inline: bool = False) -> str:
        bxs = {f'bx_{i}': fr'\hat{{{self.param.format(i)}}} {self.factor.format(i)}'
               for i in range(1, self._n_factors + 1)}
        expr = self._template.format(
            y=fr'\hat{{{self.dependent}}}',
            a=fr'\hat{{{self.const.format(0)}}}',
            **bxs
        )

        return to_math(expr, inline=inline)

    def parameterized(self, inline: bool = False) -> str:
        params = self._model.params

        if self._has_const:
            a = f'{params["const"]:{self._round}}'
        else:
            a = ''

        bxs = {f'bx_{i}': f'{params.loc[i - 1]:{self._round}} {self.factor.format(i)}'
               for i in range(1, self._n_factors + 1)}

        expr = self._template.format(
            y=fr'\hat{{{self.dependent}}}',
            a=a,
            **bxs
        )

        return to_math(expr, inline=inline)

    def bse(self, inline: bool = False) -> list[str]:
        bse = self._model.bse

        bse_list = []
        if self._has_const:
            const_bse_tex = rf'S_\hat{{a}} = {bse["const"]:{self._round}}'
            bse_list.append(const_bse_tex)

        for i in range(self._n_factors):
            bse_tex = rf'S_{{\hat{{{self.param.format(i + 1)}}}}} = {bse.loc[i]:{self._round}}'
            bse_list.append(bse_tex)

        return to_math(bse_list, as_list=True, inline=inline)

    def rmsd_resid(self, inline: bool = False) -> str:
        expr = f'S_{{{self.noise}}} = {self._model.rmsd_resid:{self._round}}'
        return to_math(expr, inline=inline)

    def rsquared(self, inline: bool = False) -> str:
        expr = f'R^2 = {self._model.rsquared:{self._round}}'
        return to_math(expr, inline=inline)

    def mapprxe(self, inline: bool = False) -> str:
        expr = f'A = {self._model.mapprxe:{self._round}}'
        return to_math(expr, inline=inline)

    def f_value(self, inline: bool = False) -> str:
        expr = f'F_{{набл}} = {self._model.f_value:{self._round}}'
        return to_math(expr, inline=inline)

    def f_critical(self, alpha=0.05, inline: bool = False) -> str:
        expr = f'F_{{табл_{{{alpha}}}}} = {self._model.f_critical(alpha):{self._round}}'
        return to_math(expr, inline=inline)

    def f_pvalue(self, inline: bool = False) -> str:
        expr = rf'p\text{{-}}value_F = {self._model.f_pvalue:{self._round}}'
        return to_math(expr, inline=inline)


if __name__ == '__main__':
    y = pd.Series(
        [15, 18, 11, 300, 15, 18, 11, 300, 15, 18, 11, 300,
         15, 18, 11, 300, 15, 18, 11, 300, 15, 18, 11, 300]
    )

    x = pd.DataFrame([[2, 3], [2, 3], [1, 4], [6, 7], [2, 3], [2, 3], [1, 4], [6, 7],
                      [2, 3], [2, 3], [1, 4], [6, 7], [2, 3], [2, 3], [1, 4], [6, 7],
                      [2, 3], [2, 3], [1, 4], [6, 7], [2, 3], [2, 3], [1, 4], [6, 7]])

    model_0 = LinearRegression(y, x)
    model_1 = LinearRegression(y, add_constant(x))

    print(ModelView(model_0).specification())
    print(ModelView(model_1).specification())

    print(ModelView(model_0).true_form())
    print(ModelView(model_1).true_form())

    print(ModelView(model_0).parameterized())
    print(ModelView(model_1).parameterized())

    print(ModelView(model_0).bse(inline=True))
    print(ModelView(model_1).bse(inline=True))

    print(ModelView(model_0).rmsd_resid(inline=True))
    print(ModelView(model_1).rmsd_resid(inline=True))

    print(ModelView(model_0).rsquared(inline=True))
    print(ModelView(model_1).rsquared(inline=True))
