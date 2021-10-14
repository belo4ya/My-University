import numpy as np
import pandas as pd


def gen_data(n) -> pd.DataFrame:
    rng = np.random.default_rng(n * 10)

    cov = [
        [1, 0.8, 0.4, -0.6],
        [0.8, 1, 0.7, -0.4],
        [0.4, 0.7, 1, -0.1],
        [-0.6, -0.4, -0.1, 1]
    ]
    mean = [n * 15, n * n, n + 20, 60 - n]

    data = rng.multivariate_normal(mean, cov, size=300, tol=1e-6)
    return pd.DataFrame(data, columns=['y', 'x1', 'x2', 'x3'])


N = 13  # позиция в списке
DATA_FRAME = gen_data(N)
