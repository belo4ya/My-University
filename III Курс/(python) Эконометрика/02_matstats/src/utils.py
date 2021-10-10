from __future__ import annotations

import pandas as pd


# и кто говорил, что у Яндекса плохие собеседования?

def interval_mode(s: pd.Series, bins) -> float | pd.Series | None:
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

    intervals = pd.cut(s, bins).value_counts(sort=False)  # частотные интервалы
    max_freq = intervals.max()
    commons = intervals[intervals == max_freq]

    if len(commons) == 0:
        return None

    elif len(commons) == 1:
        interval = commons.index[0]
        prev_freq = sample[1] if len((sample := commons[interval:])) > 1 else 0
        next_freq = sample[-2] if len((sample := commons[:interval])) > 1 else 0
        return pd.Series(_interval_mode(interval, max_freq, prev_freq, next_freq))

    # else ========================== else #

    def _foo(_commons: pd.Series, _intervals: pd.Series) -> list[dict]:
        _objects = []
        prev_const = prev_temp = _commons.index[0]
        freq = _commons[prev_temp]
        left = prev_temp.left
        n = 0
        for i in range(1, len(_commons)):
            current = _commons.index[i]

            if prev_temp.right == current.left:
                n += 1
                freq += _commons[current]
            else:

                # ============================================================
                before = _intervals[:prev_const].iloc[-2 - (n + 1):-2]
                before_freq = before.sum() if len(before) else 0

                after = _intervals[prev_temp:].iloc[1:1 + (n + 1)]
                after_freq = after.sum() if len(after) else 0
                # ============================================================

                _objects.append({
                    'target': pd.Series(freq, [pd.Interval(left, prev_temp.right)]),
                    'before_freq': before_freq,
                    'after_freq': after_freq,
                })

                freq = _commons[current]
                left = current.left
                n = 0
                prev_const = current

            prev_temp = current

        # ============================================================
        before = _intervals[:prev_const].iloc[-2 - (n + 1):-2]
        before_freq = before.sum() if len(before) else 0

        after = _intervals[prev_temp:].iloc[1:1 + (n + 1)]
        after_freq = after.sum() if len(after) else 0
        # ============================================================

        _objects.append({
            'target': pd.Series(freq, [pd.Interval(left, prev_temp.right)]),
            'before_freq': before_freq,
            'after_freq': after_freq,
        })

        return _objects

    return pd.Series([
        _interval_mode(
            i['target'].index,
            i['target'].iloc[0],
            i['before_freq'],
            i['after_freq']
        )
        for i in _foo(commons, intervals)
    ]).dropna().reset_index(drop=True)
