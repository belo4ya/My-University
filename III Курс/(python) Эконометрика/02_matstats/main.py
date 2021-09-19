import pandas as pd

import utils

# ============================== ЗАГРУЗКА ДАННЫХ ============================== #

data_df = pd.read_csv('resources/csv/data.csv', sep=',', header=2)

# ----------------------------------------------------------------------------- #

# ============================== ВЫБОР ДАННЫХ ============================== #

indicator = 'GDP (constant 2010 US$)'
gdp_series = data_df[data_df['Indicator Name'] == indicator]
gdp_series = gdp_series.loc[:, '1960':'2020'].squeeze().rename('Y')

indicator = 'Final consumption expenditure (% of GDP)'
fce_series = data_df[data_df['Indicator Name'] == indicator]
fce_series = fce_series.loc[:, '1960':'2020'].squeeze()
fce_series = (fce_series / 100 * gdp_series).rename('C')

indicator = 'Net investment in nonfinancial assets (% of GDP)'
investment_series = data_df[data_df['Indicator Name'] == indicator]
investment_series = investment_series.loc[:, '1960':'2020'].squeeze()
investment_series = (investment_series / 100 * gdp_series).rename('I')

indicator = 'General government final consumption expenditure (constant 2010 US$)'
gfce_series = data_df[data_df['Indicator Name'] == indicator]
gfce_series = gfce_series.loc[:, '1960':'2020'].squeeze().rename('G')

# -------------------------------------------------------------------------- #

# ============================== - ============================== #

df = pd.concat([gdp_series, fce_series, investment_series, gfce_series], axis=1)
utils.print_df(df)

# -------------------------------------------------------------------------- #

# ============================== ОПИСАТЕЛЬНАЯ СТАТИСТИКА ============================== #

utils.print_df(df.var(), title='ДИСПЕРСИЯ')
utils.print_df(df.std(), title='СТАНДАТНОЕ ОТКЛОНЕНИЕ')
utils.print_df(df.mean(), title='СРЕДНЕЕ')
utils.print_df(df.median(), title='МЕДИАНА')

# FIXME: мода для интервального ряда
# utils.print_df(df.mode(), title='МОДА')
# print(pd.interval_range(df.min()['C'], df.max()['C'], periods=10))

utils.print_df(df.kurtosis(), title='ЭКСЦЕСС')
utils.print_df(df.skew(), title='АСИММЕТРИЯ')

utils.print_df(df.corr(), title='ПАРНАЯ КОРРЕЛЯЦИЯ')

# -------------------------------------------------------------------------- #
