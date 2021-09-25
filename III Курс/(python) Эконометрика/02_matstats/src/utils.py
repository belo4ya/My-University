from __future__ import annotations

from operator import add, sub
from typing import Literal

import pandas as pd


def interval_mode(s: pd.Series, bins) -> float | pd.Series | None:  # почему ты вообще работаешь?
    """
    Формула
    -------
    x + h * (mc - mc_prev) / ((mc - mc_prev) + (mc - mc_next))
    x - левая граница модального интервала
    h - длина модального интервала
    mc - частота модального интервала
    mc_prev - частота предыдущего модального интервала
    mc_next - частота следующего модального интервала

    Особенные случаи
    ----------------
    – если модальный интервал крайний, то m-1 = 0 либо m+1 = 0;
    – если обнаружатся несколько модальных интервалов, которые находятся рядом,
      то рассматриваем модальный интервал (левая граница левого, правая граница правого)
    – если между модальными интервалами есть расстояние,
      то применяем формулу к каждому интервалу,
      получая тем самым 2 или большее количество мод.
    """

    def _interval_mode(_interval: pd.Interval, _freq, _prev_freq=0, _next_freq=0) -> float | None:
        _denominator = (_freq - _prev_freq) + (_freq - _next_freq)
        if _denominator != 0:
            return _interval.left + _interval.length * (_freq - _prev_freq) / _denominator

    intervals = pd.cut(s, bins)
    intervals_freq = intervals.value_counts(sort=False)
    max_freq = intervals_freq.max()
    max_freq_intervals = intervals_freq[intervals_freq == max_freq]

    if len(max_freq_intervals) == 0:
        return None

    elif len(max_freq_intervals) == 1:
        interval = max_freq_intervals.index[0]
        prev_freq = sample[1] if len((sample := intervals_freq[interval:])) > 1 else 0
        next_freq = sample[-2] if len((sample := intervals_freq[:interval])) > 1 else 0
        return pd.Series(_interval_mode(interval, max_freq, prev_freq, next_freq))

    else:

        def _expand_intervals(_intervals: pd.Series) -> list[dict]:
            _expanded = []
            _i = 0
            _prev: pd.Interval = _intervals.index[_i]
            while _i < len(_intervals) - 1:
                _current: pd.Interval = _intervals.index[_i]
                _next: pd.Interval = _intervals.index[_i + 1]

                left = _current.left
                right = _current.right
                freq = _intervals.iloc[_i]
                n_expanded = 0

                if left == _prev.right:
                    left = _prev.left  # расширяем левую границу
                    freq += _intervals[_prev]
                    n_expanded += 1

                if right == _next.left:
                    right = _next.right  # чуть-чуть расширяем правую границу
                    freq += _intervals[_next]
                    n_expanded += 1

                    _offset = 1
                    for _next_next in _intervals.index[_i + 2:]:
                        if _next_next.left == right:
                            right = _next_next.right  # если возможно расширяем ещё
                            freq += _intervals[_next_next]
                            n_expanded += 1
                            _offset += 1
                        else:
                            break

                    _i += _offset

                _expanded.append({
                    'freq': freq,
                    'interval': pd.Interval(left, right),
                    'n': n_expanded,
                })
                _prev = _current
                _i += 1

            if _i < len(_intervals):
                _expanded.append({
                    'freq': _intervals.iloc[-1],
                    'interval': _intervals.index[-1],
                    'n': 0,
                })

            return _expanded

        def _calc_prev_next_freq(_targets: list[dict], _intervals: pd.Series) -> list[dict]:

            def _expand(mode: Literal['left', 'right'], _intervals: pd.Series, _i: int, _n: int) -> int:
                freq = _intervals.iloc[_i]
                _op = sub if mode == 'left' else add
                _j = 0
                while _j < _n and _op(_i, _j) > 0:  # возможно while лишний, но сегодня его день
                    _j += 1
                    freq += _intervals.iloc[_op(_i, _j)]

                return freq

            _prev_next_freq = [
                {
                    'left_freq': _expand('left', _intervals, 0, _targets[0]['n']),
                    'right_freq': _expand('right', _intervals, 0, _targets[0]['n'])
                },
            ]
            _i = 0
            for _target in _targets[1:]:
                left_freq, right_freq = None, 0
                while not (left_freq and right_freq) and _i < len(_intervals):

                    if left_freq is None:
                        if _intervals.index[_i].right > _target['interval'].left:
                            if _i == 0:
                                left_freq = 0
                            else:
                                left_freq = _expand('left', _intervals, _i - 1, _target['n'])
                    else:
                        if _target['interval'].right <= _intervals.index[_i].left:
                            right_freq = _expand('right', _intervals, _i, _target['n'])

                    _i += 1

                _prev_next_freq.append({
                    'left_freq': left_freq,
                    'right_freq': right_freq
                })

            return _prev_next_freq

        expanded_intervals = _expand_intervals(max_freq_intervals)
        prev_next_freq = _calc_prev_next_freq(expanded_intervals, intervals_freq)

        return pd.Series([
            _interval_mode(
                expanded_intervals[i]['interval'],
                expanded_intervals[i]['freq'],
                prev_next_freq[i]['left_freq'],
                prev_next_freq[i]['right_freq'],
            )
            for i in range(len(expanded_intervals))
        ]).dropna().reset_index(drop=True)

# и кто говорил, что у Яндекса плохие собеседования?
