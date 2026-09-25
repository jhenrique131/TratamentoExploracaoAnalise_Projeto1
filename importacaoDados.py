#Projeto Análise de dados da COVID19 no estado de São Paulo
#Este projeto analisa os dados dos casos de covid 19 no
#estado de São Paulo no período de fevereiro de 2020 a setembro de 2021.
import numpy as np
import pandas as pd

def carrega_dados_covid_sp():
    arquivo_csv = "E:/0 - Portifolio/python/TratamentoExploracaoAnalise_Projeto1/dados/dados_covid_sp.csv"
    covid_sp = pd.read_csv(arquivo_csv, sep=';', encoding='utf-8')

    print(covid_sp.head())
    print(covid_sp.shape)

    return covid_sp 





