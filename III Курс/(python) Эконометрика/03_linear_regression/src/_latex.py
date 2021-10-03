from pylatex import Command, Math, NoEscape

rightarrow = r'\rightarrow'
min_ = r'\min'


def subscript(s, i) -> str:
    return f'{s}_{{{i}}}'


def superscript(s, i) -> str:
    return f'{s}^{{{i}}}'


def frac(a, b) -> str:
    return command('frac', [a, b])


def hat(s, noescape=None) -> str:
    if noescape:
        s = NoEscape(s)
    return command('hat', s)


def sum_(s, i=None, n=None):
    limits = subscript('', f'{i=}' if i else 'i') + superscript('', f'{n=}' if n else 'n')
    return command('sum' + NoEscape(r'\limits' + limits), s)


def command(_command=None, arguments=None, options=None, *, extra_arguments=None, packages=None) -> str:
    return Command(
        command=_command,
        arguments=arguments,
        options=options,
        extra_arguments=extra_arguments,
        packages=packages
    ).dumps()


def math(*, inline=False, data=None, escape=None) -> str:
    return Math(inline=inline, data=data, escape=escape).dumps()
