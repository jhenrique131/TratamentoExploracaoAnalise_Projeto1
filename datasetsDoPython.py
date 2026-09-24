import statsmodels.api as sm
import sklearn
from sklearn import datasets

cancer = sm.datasets.cancer.load_pandas().data

print(cancer.head())
print(cancer.shape)
print(type(cancer))

