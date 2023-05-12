import pandas as pd
import plotly.express as px

tabela = pd.read_csv("clientes.csv", encoding="latin", sep=";")

tabela = tabela.drop("Unnamed: 8", axis=1)
tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce") 

tabela = tabela.dropna()

print(tabela)
print(tabela.info())
print(tabela.describe())

for coluna in tabela.columns:
    grafic = px.histogram(tabela, x=coluna, y="Nota (1-100)", histfunc="avg", text_auto=True)
    grafic.show()
    
print("Conclusões: Conclusões: - Acima de 15 anos (não existe grande diferença entre faixas etárias a partir deste ponto) - Faixa salarial não possui grandes influências na nota - Áreas de trabalho: Entretenimento e Artista (evitar construção) - Possui entre 10 e 15 anos de experiência - Com famílias médias (até no máximo 7 pessoas)")

#Análise de dados pode ser melhor visualizada através de um notebook jupyter
#por isso criei uma versão do código utilizando um para melhor visualização