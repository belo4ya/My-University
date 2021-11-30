from functools import reduce
from multiprocessing import Queue, Process

import pandas as pd


class Worker(Process):

    def __init__(self, tasks_queue: Queue, results_queue: Queue):
        self._tasks_queue = tasks_queue
        self._results_queue = results_queue
        super(Worker, self).__init__()

    def run(self) -> None:
        while not self._tasks_queue.empty():
            task = self._tasks_queue.get()
            self._results_queue.put(task())


class Task:

    def __init__(self, path):
        self._path = path

    def __call__(self) -> pd.DataFrame:
        return pd.read_csv(self._path, sep=';').groupby('tag')['n_steps'].agg(['sum', 'count'])


def aggregate(results_queue: Queue, qsize: int) -> dict[str, float]:
    initial = results_queue.get()
    res = reduce(lambda a, b: a + b, lazy_queue_get(results_queue, qsize - 1), initial)
    return (res['sum'] / res['count']).to_dict()


def lazy_queue_get(queue: Queue, qsize: int):
    for i in range(qsize):
        yield queue.get()
