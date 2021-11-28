import pandas as pd


def worker(path) -> pd.DataFrame:
    return pd.read_csv(path, sep=';').groupby('tag')['n_steps'].agg(['sum', 'count'])


def aggregator(results: list[pd.DataFrame]) -> pd.Series:
    res = sum(results)
    return res['sum'] / res['count']
