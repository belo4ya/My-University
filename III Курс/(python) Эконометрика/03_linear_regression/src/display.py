from __future__ import annotations

from functools import cached_property

import pandas as pd
from pylatex import Math

from src.stats import add_constant

OLS = r'\[% \sum_{i}^{n}{(y_i - \hat{y_i})^2} \rightarrow \min_{n} %\]'


class ModelView:
    dependent = 'y_i'
    factor = 'x_{{i{}}}'
    param = 'b_{{{}}}'
    noise = 'e_i'

    def __init__(self, x: pd.Series | pd.DataFrame, y: pd.Series):
        self._x = x
        self._y = y

        self._factors = []
        self._params = []
        self._const = ''

        if isinstance(self._x, pd.Series):
            n = 1
        else:
            n = self._x.shape[1]
            if 'const' in self._x.columns:
                self._const = self.param.format(0)
                n -= 1

        for i in range(1, n + 1):
            self._factors.append(self.factor.format(i))
            self._params.append(self.param.format(i))

        self._template = '{y} = {a} + {bx}' if self._const else '{y} = {bx}'

    @property
    def p_spec(self):
        return self._params[:]

    @property
    def p_true(self):
        return [rf'\hat{{{param}}}' if param else '' for param in self._params]

    @cached_property
    def specification(self):
        template = self._template + ' + {e}'

        bx_template = '{bx}'
        print()
        print(self._params)
        print(self._factors)
        print()
        kwargs = {
            'y': self.dependent,
            'a': self._const,
            'bx': bx_template,
            'e': self.noise
        }

        return template.format(**kwargs)

    @cached_property
    def true_form(self):
        return self._template

    def parameterized(self, params):
        pass


if __name__ == '__main__':
    y = pd.Series([15, 18, 11, 300, 800, 22])

    x = pd.DataFrame([[2, 3],
                      [2, 3],
                      [1, 4],
                      [6, 7]])
    x_with_const = add_constant(x)

    print(ModelView(x, y).specification)
    print(ModelView(x_with_const, y).specification)

    print(ModelView(x, y).true_form)
    print(ModelView(x_with_const, y).true_form)
