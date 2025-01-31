#José Victor Justino de Oliveira - 20240010840
#Labert Paixão Ribeiro - 20240011365

from table import *

tabela = criarTabela()
exibir_tabela(tabela)
addLinha(tabela)
delLinha(tabela)
addColuna(tabela)
delColuna(tabela)
print(f"Soma: {sumTable(tabela)}")
print(f"Média: {mediaTable(tabela)}")
