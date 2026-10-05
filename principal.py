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
#from collections import Counter
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
#y = covid_sp_alterado.iloc[:,1].values
#Agora é reconhecido como Arry([])

#print(type(y))

#Transformando um arry([]) em uma lista[]
#lista_y = list(y.to_numpy().flatten())
#print(lista_y)

#print(type(lista_y))

#Transforma a lista em um DataFrame
#df = pd.DataFrame(lista_y, columns=['municipio'])
#print(df)

#Excluinda, Filtrando e Substituindo registros (Linhas)
#Excluindo linhas por índices (Valores Absolutos)
covid_sp_alterado2 = covid_sp_alterado.drop(covid_sp_alterado.index[[1,3]])
#print(f"Valores excluído por índices - Valores absolutos: \n{covid_sp_alterado2}")
#Linhas 1 e 3 foram excluídas


#Excluindo lindas por índices (Intervalos de valores)
covid_sp_alterado2 = covid_sp_alterado2.drop(covid_sp_alterado.index[4:7])
#print(f"Excluindo linas por índices - Intervalo de valores: \n{covid_sp_alterado2}")


#Reordenação dos índices após exclusão - Reset no índice
covid_sp_alterado2 = covid_sp_alterado2.reset_index(drop=True)
#print(f"Índice reordenado: \n{covid_sp_alterado2}")

#Excluindo as linhas onde estão os registros 'ignorado'
#Econtrando os registros
ignorado = covid_sp_alterado2.loc[covid_sp_alterado2['municipio'] == 'Ignorado']
#print(f"Excluindo registros 'ignorado': \n{ignorado}")

#print(ignorado.shape)

#Pega os registros diferentes de 'Ignorado' - Exclui os registros 'Ignorado'
covid_sp_alterado2 = covid_sp_alterado2.loc[covid_sp_alterado2['municipio'] != 'Ignorado']
#print(f"Registros 'Ignorado' do campo municipio excluídos: \n{covid_sp_alterado2}")

#Análise de apenas um município
guarulhos = covid_sp_alterado2.loc[covid_sp_alterado2['municipio'] == 'Guarulhos']
#print(f"Análise do município Guarulhos: \n{guarulhos}")

#Excluindo colunas
guarulhos.drop(columns=['data','municipio'], inplace=True)
#print(f"Colunas data e municipio excluídas: \n{guarulhos.head()}")

#Substituir código por descrição - Dicionário{}
guarulhos['semana_epidem'] = guarulhos['semana_epidem'].replace({9:'nove', 10:'dez'})
#print(f"Substituição de código por descrição - Dicionario{}: \n{guarulhos.head()}")

#Substituir código por descrição - lista[]
guarulhos['semana_epidem'] = guarulhos['semana_epidem'].replace([11,12,13], ['onze','doze','treze'])
#print(f"Substituição de código por descrição - Lista[]: \n{guarulhos.head()}")

#Substituir virgula por ponto utilizando lambda
guarulhos['casos_pc'] = guarulhos['casos_pc'].apply(lambda x: x.replace(',','.'))
#print(f"Substituindo virgula por ponto utilizando lambda: \n{guarulhos.head(30)}")

#Criando colunas com datas
import datetime

#Cria uma data específica
data = np.array('2020-02-25', dtype=np.datetime64())
#print(f"Criando uma data específica: \n{data}")

#Agora estende para todas as outras 579 linhas
data = data + np.arange(579)
#print(f"Data estendida para todas as outras 579 linhas: \n{data}")

#Transforma em um DataFrame
data = pd.DataFrame(data)
#print(f"Transformação em um DataFrame: \n{data}")


#Renomendo a coluna 0 para Data
data.columns = ['data']
#print(f"Coluna 0 renomeada para data: \n{data}")

#Concatenando a data com a tabela guarulhos
guarulhos2 = pd.concat([data,guarulhos], axis=1)
print(f"Data e tabela guarulhos concatenadas: \n{guarulhos2}")

#Os outros registros ficaram nulos devido os índices da tabela anterior
#Os índices devem ser resetado para que a nova tabela não fique com os valores nulos

#Reordenando os índices para coincidir a tabela 'data' com a tabela 'guarulhos'
guarulhos = guarulhos.reset_index(drop=True)
#print(f"Reordenação dos íncides da tabela: \n{guarulhos}")

#Após reordenação dos índices, fazemos a concatenação das duas tabelas, 'data' e 'guarulhos'
#Concatenando a data com a tabela guarulhos
guarulhos2 = pd.concat([data, guarulhos], axis=1)
#print(f"Concatenação da data com a tabela guarulhos: \n{guarulhos2}")










