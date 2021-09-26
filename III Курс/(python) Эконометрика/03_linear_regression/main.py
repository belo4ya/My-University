import statsmodels.api as sm

x = []
y = []

X = sm.add_constant(x)

model = sm.OLS(y, X).fit()

predictions = model.predict()

model.summary()
