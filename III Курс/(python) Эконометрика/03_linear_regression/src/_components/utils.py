from __future__ import annotations

MATH_TEMPLATE = '$$ {} $$'
INLINE_MATH_TEMPLATE = '$ {} $'


def to_math(expr: str | list[str], as_list: bool = False, inline: bool = False) -> str | list[str]:
    if as_list:
        if inline:
            return [INLINE_MATH_TEMPLATE.format(_) for _ in expr]
        return [MATH_TEMPLATE.format(_) for _ in expr]

    if inline:
        return INLINE_MATH_TEMPLATE.format(expr)
    return MATH_TEMPLATE.format(expr)


def from_math(expr: str | list[str], as_list: bool = False) -> str | list[str]:
    if as_list:
        return [_.replace('$', '').strip() for _ in expr]
    return expr.replace('$', '').strip()


def special_format(s: str, **kwargs) -> str:
    for k, v in kwargs.items():
        s = s.replace('{' + k + '}', v)
    return s
