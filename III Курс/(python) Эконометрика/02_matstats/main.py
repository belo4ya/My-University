import pandas as pd

import utils

# ============================== ЗАГРУЗКА ДАННЫХ ============================== #

input_df = pd.read_csv('resources/csv/data.csv', sep=',', header=2)

# ----------------------------------------------------------------------------- #

# ============================== ВЫБОР ДАННЫХ ============================== #

indicator = 'GDP (constant 2010 US$)'
gdp_series = input_df[input_df['Indicator Name'] == indicator]
gdp_series = gdp_series.loc[:, '1960':'2020'].squeeze().rename('Y')

indicator = 'Final consumption expenditure (% of GDP)'
fce_series = input_df[input_df['Indicator Name'] == indicator]
fce_series = fce_series.loc[:, '1960':'2020'].squeeze()
fce_series = (fce_series / 100 * gdp_series).rename('C')

indicator = 'Net investment in nonfinancial assets (% of GDP)'
investment_series = input_df[input_df['Indicator Name'] == indicator]
investment_series = investment_series.loc[:, '1960':'2020'].squeeze()
investment_series = (investment_series / 100 * gdp_series).rename('I')

indicator = 'General government final consumption expenditure (constant 2010 US$)'
gfce_series = input_df[input_df['Indicator Name'] == indicator]
gfce_series = gfce_series.loc[:, '1960':'2020'].squeeze().rename('G')

# -------------------------------------------------------------------------- #

# ============================== - ============================== #

data_df = pd.concat([gdp_series, fce_series, investment_series, gfce_series], axis=1)
utils.print_df(data_df)
