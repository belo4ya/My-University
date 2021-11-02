
from typing import Mapping
from multiprocessing import Queue
import pandas as pd


def worker(path) -> pd.Series:
    return pd.read_csv(path, sep=';').groupby('tag')['n_steps'].mean()


def aggregator(results: list[pd.Series]) -> Mapping[str, int]:
    return (sum(results) / len(results)).to_dict()


def run(paths_queue: Queue, results_queue: Queue):
    while not paths_queue.empty():
        results_queue.put(worker(paths_queue.get()))

