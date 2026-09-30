import pandas as pd
import numpy as np
import statsmodels.api as sm
from excluindoColunas import exclui_colunas

covid_sp_alterado = exclui_colunas()

#print(covid_sp_alterado.shape)

#Dividindo a área por 100 para ajustar o tamanho em km2
covid_sp_alterado['area'] = covid_sp_alterado['area']/100 #ou
#covid_sp_alterado.area = covid_sp_alterado.area/100

#print(covid_sp_alterado.head())
#print(covid_sp_alterado.shape)

#Criação de coluna Densidade Demográfica (hsb/km2)
covid_sp_alterado['densidade'] = covid_sp_alterado['pop']/covid_sp_alterado['area']
#print(covid_sp_alterado.head())
#print(covid_sp_alterado.shape)

#Criando uma coluna com índices
lista = list(range(1,374035)) #Arredonda para 374035 para pegar 374034
#print(lista)

#Transforma a lista em um DataFrame
df = pd.DataFrame(lista, columns=['indice'])
#print(df)

#Juntando os dois DataFrames - Incluindo o campo índice da tabela
covid_sp_alterado = pd.concat([covid_sp_alterado,df], axis=1)#axis=1 - Junta pela coluna
#print(covid_sp_alterado.head())

#Colocando o campo índice no começo da tabela
covid_sp_alterado = covid_sp_alterado.reindex(columns=['indice'] + list(covid_sp_alterado.columns[:-1]))
#print(covid_sp_alterado.head())

#Contagem dos registros das variáveis (colunas)
#Contagem de registros de colunas
#print(covid_sp_alterado['semana_epidem'].value_counts())

#Ordenando os registros pelo índice
#print(covid_sp_alterado['semana_epidem'].value_counts().sort_index())

#Outra forma é utilizando a função Counter - A resposta é em formato de dicionário
from collections import Counter
#print(Counter(covid_sp_alterado.semana_epidem))

#Municipios que tiveram novos obitos maior que 50
#Trás quantas vezes registrou obitos novos maior que 50 nos municípios
#Ou seja, mais de 50 pessoas
#print(covid_sp_alterado.query('obitos_novos > 100')['municipio'].value_counts())

#Selecionar variáveis(colunas) por índices
#iloc = 'i' representa o índice
#[:,5:13] - Antes da virgula representa LINHAS.
#[:,5:13] - Após a virgula representa COLUNAS
#x = covid_sp_alterado.iloc[:,5:13]
#print(f"Colunas por índices: \n{x}")

#Quando tem antes da virgula apenas dois-pontos(:), queremos pegar todas as LINHAS
#5 e 13 são os intervalos de colunas - Do 5 até a 13 (seria na verdade a 12º coluna)

#print(type(x))

#Trás somente a coluna da posição 1
#y = covid_sp_alterado.iloc[:,1]
#print(y)

#O y está sendo reconhecido como uma Série
#print(type(y))

#Para que não seja reconhecido como uma Série, inclua .values no final
y = covid_sp_alterado.iloc[:,1].values
#Agora é reconhecido como Arry([])

#print(type(y))

#Transformando um arry([]) em uma lista[]
lista_y = list(y.to_numpy().flatten())
#print(lista_y)

#print(type(lista_y))

#Transforma a lista em um DataFrame
df = pd.DataFrame(lista_y, columns=['municipio'])
print(df)


