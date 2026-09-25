import statsmodels.api as sm
import sklearn
from sklearn import datasets

cancer = sm.datasets.cancer.load_pandas().data

print(cancer.head())
print(cancer.shape)
print(type(cancer))

iris = datasets.load_iris()
#print(iris)
#Fornce apenas os dados da tabela iris
print(iris.data)

#Classifica os dados. Mostra o código da descrição
print(iris.target)

#Descrição referente aos códigos
print(iris.target_names)


