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

