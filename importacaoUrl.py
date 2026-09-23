import numpy as np
import pandas as pd

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

colnames = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'Class']

iris = pd.read_csv(url, names=colnames)

print(iris.head())
print(iris.shape)
print(f"Tipo de dados da variável iris:  {type(iris)}")