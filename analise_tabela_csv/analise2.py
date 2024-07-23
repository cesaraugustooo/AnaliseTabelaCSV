import pandas as pd
import plotly.express as px

tabela= pd.read_csv("cancelamentos_sample.csv")
display(tabela)
tabela = tabela.drop(columns="CustomerID")
display(tabela)


display(tabela.info())
tabela= tabela.dropna()
display(tabela.info())


display(tabela['cancelou'].value_counts())
display(tabela['cancelou'].value_counts(normalize=True))
graf = px.histogram(tabela, x="cancelou", color="cancelou")
graf.show()

for coluns in tabela:
    graf=px.histogram(tabela,x=coluns,color="cancelou")
    graf.show()
