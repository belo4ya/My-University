from __future__ import annotations

from src.stats import LinearRegression
from src._components.utils import to_math


class PrettyModel:
    dependent = 'y_i'
    factor = 'x_{{i{}}}'
    param = 'b_{{{}}}'
    const = 'a'
    noise = 'e'

    def __init__(self, model: LinearRegression, precision: int = 3):
        self._model = model
        self._round = f'.{precision}f'

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
            a=self.const,
            e=self.noise + '_i',
            **bxs
        )

        return to_math(expr, inline=inline)

    def true_form(self, inline: bool = False) -> str:
        bxs = {f'bx_{i}': fr'\hat{{{self.param.format(i)}}} {self.factor.format(i)}'
               for i in range(1, self._n_factors + 1)}
        expr = self._template.format(
            y=fr'\hat{{{self.dependent}}}',
            a=fr'\hat{{{self.const}}}',
            **bxs
        )

        return to_math(expr, inline=inline)

    def parameterized(self, inline: bool = False) -> str:
        if self._has_const:
            a = f'{self._model.params["const"]:{self._round}}'
        else:
            a = ''

        params = self._model.params.drop('const', errors='ignore')
        bxs = {f'bx_{i}': f'{params.iloc[i - 1]:{self._round}} {self.factor.format(i)}'
               for i in range(1, self._n_factors + 1)}

        expr = self._template.format(
            y=fr'\hat{{{self.dependent}}}',
            a=a,
            **bxs
        )

        return to_math(expr, inline=inline)

    def bse(self, inline: bool = False) -> list[str]:
        bse_list = []
        if self._has_const:
            expr = rf'S_\hat{{a}} = {self._model.bse["const"]:{self._round}}'
            bse_list.append(expr)

        bse = self._model.bse.drop('const', errors='ignore')
        for i in range(1, self._n_factors + 1):
            expr = rf'S_{{\hat{{{self.param.format(i)}}}}} = {bse.iloc[i - 1]:{self._round}}'
            bse_list.append(expr)

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

    def f_critical(self, alpha: float = 0.05, inline: bool = False) -> str:
        expr = f'F_{{табл_{{{alpha}}}}} = {self._model.f_critical(alpha):{self._round}}'
        return to_math(expr, inline=inline)

    def f_pvalue(self, inline: bool = False) -> str:
        expr = rf'p\text{{-}}value_F = {self._model.f_pvalue:{self._round}}'
        return to_math(expr, inline=inline)

    def t_values(self, inline: bool = False) -> list[str]:
        t_values_list = []

        if self._has_const:
            expr = rf't_{{a}} = {self._model.t_values["const"]:{self._round}}'
            t_values_list.append(expr)

        t_values = self._model.t_values.drop('const', errors='ignore')
        for i in range(1, self._n_factors + 1):
            expr = rf't_{{{self.param.format(i)}}} = {t_values.iloc[i - 1]:{self._round}}'
            t_values_list.append(expr)

        return to_math(t_values_list, as_list=True, inline=inline)

    def t_critical(self, alpha: float = 0.05, inline: bool = False) -> str:
        expr = f't_{{табл_{{{alpha}}}}} = {self._model.t_critical(alpha):{self._round}}'
        return to_math(expr, inline=inline)

    def t_pvalues(self, inline: bool = False) -> list[str]:
        t_pvalues_list = []
        t_pvalues = self._model.t_pvalues

        if self._has_const:
            expr = rf'p\text{{-}}value_{{t_{{a}}}} = {t_pvalues["const"]:{self._round}}'
            t_pvalues_list.append(expr)

        t_pvalues = t_pvalues.drop('const', errors='ignore')
        for i in range(1, self._n_factors + 1):
            expr = rf'p\text{{-}}value_{{t_{{{self.param.format(i)}}}}} = {t_pvalues.iloc[i - 1]:{self._round}}'
            t_pvalues_list.append(expr)

        return to_math(t_pvalues_list, as_list=True, inline=inline)

    def conf_int(self, alpha: float = 0.05, inline: bool = False) -> list[str]:
        conf_int_list = []
        conf_int = self._model.conf_int(alpha=alpha)

        if self._has_const:
            interval = conf_int.loc["const"]
            expr = rf'{self.const} : ({interval[0]:{self._round}}; {interval[1]:{self._round}})'
            conf_int_list.append(expr)

        conf_int = conf_int.drop('const', errors='ignore')
        for i in range(1, self._n_factors + 1):
            interval = conf_int.iloc[i - 1]
            expr = rf'{self.param.format(i)} : ({interval[0]:{self._round}}; {interval[1]:{self._round}})'
            conf_int_list.append(expr)

        return to_math(conf_int_list, as_list=True, inline=inline)

    def beta(self, inline: bool = False) -> list[str]:
        beta_list = []
        beta = self._model.beta

        for i in range(1, self._n_factors + 1):
            expr = rf'\beta_{{{i}}} = {beta.iloc[i - 1]:{self._round}}'
            beta_list.append(expr)

        return to_math(beta_list, as_list=True, inline=inline)

    def delta(self, inline: bool = False) -> list[str]:
        delta_list = []
        delta = self._model.delta

        for i in range(1, self._n_factors + 1):
            expr = rf'\Delta_{{{i}}} = {delta.iloc[i - 1]:{self._round}}'
            delta_list.append(expr)

        return to_math(delta_list, as_list=True, inline=inline)

    def elasticity(self, inline: bool = False) -> list[str]:
        elasticity_list = []
        elasticity = self._model.elasticity

        for i in range(1, self._n_factors + 1):
            expr = rf'Э_{{{i}}} = {elasticity.iloc[i - 1]:{self._round}}'
            elasticity_list.append(expr)

        return to_math(elasticity_list, as_list=True, inline=inline)
