from renomeandoColunas import renomeando_colunas

covid_sp = renomeando_colunas()

#Visualização dos registros
print(covid_sp.shape)

def exclui_colunas():
    #Excluir por nome
    covid_sp_alterado = covid_sp.drop(columns=['cod_ra'])
    #print(covid_sp.head())

    print(covid_sp_alterado.shape)

    #Excluir por número
    covid_sp_alterado = covid_sp_alterado.drop(covid_sp_alterado.columns[[1]], axis=1)#axis=1 - Coluna, 
                                                                          #axis=0 - Linha

    print(covid_sp_alterado.shape)

    #Excluir mais de uma coluna
    covid_sp_alterado.drop(columns=['rotulo_mapa','codigo_mapa','cod_drs'], inplace=True)
    print(covid_sp_alterado.shape)

    #Excluir mais de uma variável por números
    #covid_sp_alterado.drop(covid_sp_alterado.columns[[13,14,18,19]], axis=1, inplace=True)
    #print(covid_sp_alterado.shape)

    return covid_sp_alterado

