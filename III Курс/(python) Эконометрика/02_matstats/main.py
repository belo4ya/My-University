import pandas as pd

import utils

# ============================== ЗАГРУЗКА ДАННЫХ ============================== #

data_df = pd.read_csv('data/csv/data.csv', sep=',', header=2)

# ----------------------------------------------------------------------------- #


# ============================== ИССЛЕДУЕМЫЕ ДАННЫЕ ============================== #

data_router = {
    'Y': {
        'indicator': 'GDP (constant 2010 US$)',
        'ru': 'Объем ВВП, $'
    },
    'C': {
        'indicator': 'Final consumption expenditure (% of GDP)',
        'ru': 'Уровень потребления, $'
    },
    'I': {
        'indicator': 'Net investment in nonfinancial assets (% of GDP)',
        'ru': 'Объем инвестиций, $'
    },
    'G': {
        'indicator': 'General government final consumption expenditure (constant 2010 US$)',
        'ru': 'Величина государственных расходов, $'
    },
}

# ----------------------------------------------------------------------------- #

# ============================== ВВП ============================== #

indicator = data_router['Y']['indicator']
gdp_series = data_df[data_df['Indicator Name'] == indicator]
gdp_series = gdp_series.loc[:, '1960':'2020'].squeeze()

# ----------------------------------------------------------------- #


# ============================== УРОВЕНЬ ПОТРЕБЛЕНИЯ ============================== #

indicator = data_router['C']['indicator']
fce_series = data_df[data_df['Indicator Name'] == indicator]
fce_series = fce_series.loc[:, '1960':'2020'].squeeze()
fce_series = fce_series * gdp_series / 100

# --------------------------------------------------------------------------------- #


# ============================== ИНВЕСТИЦИИ ============================== #

indicator = data_router['I']['indicator']
investment_series = data_df[data_df['Indicator Name'] == indicator]
investment_series = investment_series.loc[:, '1960':'2020'].squeeze()
investment_series = investment_series * gdp_series / 100

# -------------------------------------------------------------------------- #


# ============================== ГОС РАСХОДЫ ============================== #

indicator = data_router['G']['indicator']
gfce_series = data_df[data_df['Indicator Name'] == indicator]
gfce_series = gfce_series.loc[:, '1960':'2020'].squeeze()

# --------------------------------------------------------------------------- #

# ============================== - ============================== #

df = pd.concat(
    [
        gdp_series.rename('Y'),
        fce_series.rename('C'),
        investment_series.rename('I'),
        gfce_series.rename('G')
    ],
    axis=1
)
df.index = pd.to_datetime(df.index.values)

# -------------------------------------------------------------------------- #


# ============================== ДИАГРАММЫ РАССЕИВАНИЯ ============================== #

df['Y_t-1'] = df['Y'].shift(1)
df['Y_t-2'] = df['Y'].shift(2)
df['G_t-1'] = df['G'].shift(1)

utils.print_df(df)

df.plot.scatter(x='', y='')

# ----------------------------------------------------------------------------------- #


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

# ------------------------------------------------------------------------------------- #

# ============================== ДИАГРАММЫ РАССЕИВАНИЯ ============================== #

# fig = make_subplots(rows=2, cols=2)
#
# fig.add_trace(px.scatter(df, x='Y', y='C').data[0], row=1, col=1)
# fig.add_trace(px.scatter(df, x='C', y='I').data[0], row=1, col=2)
# fig.add_trace(px.scatter(df, x='I', y='G').data[0], row=2, col=1)
# fig.add_trace(px.scatter(df, x='G', y='Y').data[0], row=2, col=2)
#
# fig.update_xaxes(title_text='Y', row=1, col=1)
# fig.update_xaxes(title_text='C', row=1, col=2)
# fig.update_xaxes(title_text='I', row=2, col=1)
# fig.update_xaxes(title_text='G', row=2, col=2)
#
# fig.update_yaxes(title_text='C', row=1, col=1)
# fig.update_yaxes(title_text='I', row=1, col=2)
# fig.update_yaxes(title_text='G', row=2, col=1)
# fig.update_yaxes(title_text='Y', row=2, col=2)
#
# fig.show()
#
# # ----------------------------------------------------------------------------------- #
#
# # ============================== ГИСТОГРАМЫ РАСПРЕДЕЛЕНИЙ ============================== #
#
# fig_ = make_subplots(rows=2, cols=2)
#
# fig_.add_trace(px.histogram(df, x='Y').data[0], row=1, col=1)
# fig_.add_trace(px.histogram(df, x='C').data[0], row=1, col=2)
# fig_.add_trace(px.histogram(df, x='I').data[0], row=2, col=1)
# fig_.add_trace(px.histogram(df, x='G').data[0], row=2, col=2)
#
# fig_.show()
#
# # -------------------------------------------------------------------------------------- #
