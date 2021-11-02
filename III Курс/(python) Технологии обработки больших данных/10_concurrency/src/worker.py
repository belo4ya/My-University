
import pandas as pd


def worker(path) -> pd.Series:
    return pd.read_csv(path, sep=';').groupby('tag')['n_steps'].mean()

