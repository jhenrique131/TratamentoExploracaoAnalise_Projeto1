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
#lista = list(range(1,374035)) #Arredonda para 374035 para pegar 374034
#print(lista)
