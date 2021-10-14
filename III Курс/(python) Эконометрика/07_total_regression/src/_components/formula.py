# МНК
OLS = r'\sum_{i}^{n}{(y_i - \hat{y_i})^2} \rightarrow \min_{n}'
OLS_M = 'B = (X^T X)^{-1} X^T Y'

# F-критерий Фишера
F_VALUE = r'F = \frac{\frac{R^2}{k}}{\frac{1 - R^2}{(n - k - 1)}}'

# t-критерий Стьдента
T_VALUE = r't_{b_i} = \frac{\hat{b_i}}{S_{\hat{b_i}}}'

# Доверительные интервалы
CONF_INT = r'\hat{b_i} - \hat{\sigma} \cdot t_{табл} \leq b_i \leq \hat{b_i} + \hat{\sigma} \cdot t_{табл}'

# S_e
RMSD_RESID = r'\sqrt{\frac{1}{n - k - 1} \sum_{i=1}^{n}{(y_i - \hat{y_i}})^2}'

# R^2
RSQUARED = (r'R^2 = '
            r'1 - \frac{\sum_{i=1}^{n}{(y_i - \hat{y_i})^2}}{\sum_{i=1}^{n}{(y_i - \bar{y})^2}}  = '
            r'\frac{\sum_{i=1}^{n}{(\hat{y_i} - \bar{y})^2}}{\sum_{i=1}^{n}{(y_i - \bar{y})^2}}  = '
            r'1 - \frac{RSS}{TSS} = \frac{ESS}{TSS}')

# A
MAPPRXE = r'A = \frac{1}{n} \sum_{i=1}^{n}{|\frac{y_i - \hat{y_i}}{y_i}|} \cdot 100 \%'

# beta
BETA = r'\beta_j = \hat{b_j} \cdot \frac{S_{x_{ij}}}{S_{y_i}}'

# delta
DELTA = r'\Delta_j = r_{y_i x_{ij}} \cdot \frac{\hat{b_j}}{R^2}'

# elasticity
ELASTICITY = r'Э_{j} = \hat{b_j} \cdot \frac{\bar{x_{ij}}}{\bar{y_i}}'

# DW-критерий (Дарбина-Уотсона)
DW_VALUE = r'DW = \frac{\sum_{i=2}^{n}{(e_i - e_{i-1})^2}}{\sum_{i=1}^{n}{e_i^2}} \approx 2(1-\rho_1)'

# BG
BG_VALUE = r'BG = nR^2_{aux}'
