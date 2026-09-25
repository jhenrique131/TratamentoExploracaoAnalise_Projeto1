#Importa a função do arquivo importaçãoDados.py
from importacaoDados import carrega_dados_covid_sp

#Chama a função carrega_dados_covid_sp()
covid_sp = carrega_dados_covid_sp()

print("Visualizando as primeira linhas do DataFrame")

#Visualização dos registros
#print(covid_sp.head())

def renomeando_colunas():
    #Alterando o nome da coluna e sobreescrevendo a tabela
    covid_sp.rename(columns={'nome_munic':'municipio'}, inplace=True)#Inplace=True faz a troca permanente

    #Alterando a coluna de datahora para data
    covid_sp.rename(columns={'datahora':'data'}, inplace=True)

    #print(covid_sp.head())

    #Renomeando várias colunas ao mesmo tempo
    covid_sp.rename(columns={'map_leg':'rotulo_mapa', 'map_leg_s':'codigo_mapa'}, inplace=True)

    #print(covid_sp.head())

    return covid_sp
