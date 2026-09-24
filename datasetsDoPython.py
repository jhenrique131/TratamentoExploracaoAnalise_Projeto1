import statsmodels.api as sm

cancer = sm.datasets.cancer.load_pandas().data

print(cancer.head())
