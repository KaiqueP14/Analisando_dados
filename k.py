import pandas as pd

#Visulaizar tabela
tabela = pd.read_csv("cancelamentos_sample.csv")
tabela = tabela.drop("CustomerID", axis=1)
print(tabela)

#identificando e removendo valores vazios
print(tabela.info())

#Excluindo os valores vazios 
tabela = tabela.dropna()
print(tabela.info())

#Quantas pessoas cancelaram e não cancelaram
print(tabela["cancelou"].value_counts())

#Calculando em porcentagem
print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

print(tabela["duracao_contrato"].value_counts(normalize=True))
print(tabela["duracao_contrato"].value_counts())

#Analisando o contrato mensal
print(tabela.groupby("duracao_contrato").mean(numeric_only=True))
#Podemos ver que a média de cancelamentos é 1, ou seja, todos contratos mensais foram cancelados

#Podemos deduzir que contrato mensal é ruim, vamos tirar ele e continuar analisando
tabela = tabela[tabela["duracao_contrato"]!="Monthly"]
print(tabela)
print(tabela["cancelou"].value_counts())
print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

#Chegamos em menos da metade de pessoas cancelando, vamos continuar analisando
print(tabela["assinatura"].value_counts(normalize=True))
print(tabela.groupby("assinatura").mean(numeric_only=True))
#Os cancelamentos são na média bem parecidos, então fica difícil tirar alguma conclusão da média, vamos precisar ir mais a fundo

import plotly.express as px

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou")
    grafico.show()

    #Com os graficos a gente consegue descobrir muita coisa:
#Dias atraso acima de 20 dias, 100% de cancelamento
#Clientes com 5 ou mais ligações sempre cancelam

tabela = tabela[tabela["ligacoes_callcenter"]<5]
tabela = tabela[tabela["dias_atraso"]<=20]
print(tabela)
print(tabela["cancelou"].value_counts())
print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

#Se resolvermos isso, já caímos para 18% de cancelamento
#As três principais causas são:
# - Forma de contrato mensal
# - Necessidade de ligações no call center
# - Atraso no pagamento