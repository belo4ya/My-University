import pandas as pd


def print_df(df: pd.DataFrame, title: str = None) -> None:
    options = [
        *('display.max_rows', None),
        *('display.max_columns', None),
        *('display.width', None),
        *('display.max_colwidth', None),
        *('display.precision', 2)
    ]
    with pd.option_context(*options):
        if title:
            title = '  ' + title.upper() + '  '
            print(f'\n{title:*^120}')
            print('=' * 120)
        print(df)
        print('\n')
