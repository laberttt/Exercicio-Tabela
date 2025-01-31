#José Victor Justino de Oliveira - 20240010840
#Labert Paixão Ribeiro - 20240011365

#Biblioteca apenas para visualizar a tabela no terminal (pip install pandas)
import pandas as pd

#Primeiro Requesito
def criarTabela():
    print("\n-=CRIANDO TABELA=-\n")   
    tabela = {}
    nColunas = int(input("Número de colunas: "))

    for i in range (nColunas):
        nomeColuna = input(f"Nome da coluna {i}: ")
        
        linha = input(f"Digite as linhas da coluna {i} separados por (;): ").split(';')

        tabela[nomeColuna] = linha

    return tabela

#Segundo Requesito
def addLinha(tabela):
    print("\n-=ADICIONANDO NOVA LINHA=-\n")  
    for key, valor in tabela.items():
        novo_item = input(f"Digite o novo item da coluna | {key}: ").capitalize()
        
        while True:
            if novo_item!="":
                break
            else:
                print("Inválido. Tente Novamente! ")
                novo_item = input(f"Digite o novo item da coluna | {key}: ")

        valor.append(novo_item)
        
    return exibir_tabela(tabela)

#Terceiro Requesito
def delLinha(tabela):
    print("\n-=DELETANDO LINHA=-\n")  
    indice = int(input("Digite o indice que quer remover: "))
    cont_linha = list(tabela.values())

    while (indice >= len(cont_linha[0]) or indice < 0):
        print("Erro, tamanho errado!!")
        indice = int(input("Digite o indice que quer remover: "))

    for j in tabela.values():
        j.pop(indice)
    print("Removido com Sucesso!")

    return exibir_tabela(tabela)
                
#Quarto Requesito
def addColuna(tabela):
    print("\n-=ADICIONANDO COLUNA=-\n")  
    coluna = input("Digite o nome da nova coluna: ").capitalize()

    adicionar_coluna = input("Digite as linhas separados por (;): ").split(';')
    
    cont_linha  = list(tabela.values())

    while len(adicionar_coluna) != len(cont_linha[0]):
        print(f"Você esta adicionando mais linhas do que colunas, temos {len(cont_linha[0])}")
        adicionar_coluna = input("Digite as linhas separados por (;): ").split(';')

    tabela [coluna] = adicionar_coluna
    
    return exibir_tabela(tabela)
        

#Quinto Requesito
def delColuna(tabela):
    print("\n-=REMOVENDO COLUNA=-\n")
    print(f"Colunas Válidas: {[x for x in tabela.keys()]}")
    coluna_remove = input ("Digite o nome da coluna para remover: ").capitalize()
    print("\n")

    while coluna_remove not in tabela.keys():
        print ("Nome de Coluna Inválido! Tente Novamente")
        print(f"Colunas Válidas: {[x for x in tabela.keys()]}")
        coluna_remove = input ("Digite o nome da coluna para remover: ")

    tabela.pop(coluna_remove)

    return exibir_tabela(tabela)
        
#Sexto Requesito
def sumTable(tabela):
    print("\n-=SOMANDO OS ITENS DA TABELA=-\n")  
    soma = 0

    for i in tabela.values():
        for j in i:
            if j.isdigit():
                soma+=int(j)
            else:
                pass
    if soma==0:
        return "Não possui Inteiros\n"
    else:
        return soma

#Sétimo Requesito
def mediaTable(tabela):
    print("\n-=MÉDIA DOS ITEMS DA TABELA=-\n")  
    soma = 0
    cont = 0

    for i in tabela.values():
        for j in i:
            if j.isdigit():
                soma += int(j)
                cont += 1
            else:
                pass
    if cont == 0:
        return 'Não possui Inteiros\n'
    else:
        return (soma/cont)

#Oitavo Requesito
def exibir_tabela(tabela):
    print("\n-=EXIBINDO A TABELA=-\n")  
    print(pd.DataFrame(tabela))

