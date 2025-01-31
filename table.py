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
