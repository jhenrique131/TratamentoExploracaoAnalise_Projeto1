from importacaoDados import carrega_dados_covid_sp

df = carrega_dados_covid_sp()

print("Visualizando as primeira linhas do DataFrame")

print(df.head())