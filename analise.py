import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_excel("vendas_farmavida.xlsx")

# Converter data
df["data"] = pd.to_datetime(df["data"])

# Criar coluna de mês
df["mes"] = df["data"].dt.to_period("M")

# Agrupar vendas por mês
vendas_mes = df.groupby("mes")["valor"].sum()

# Mostrar no terminal
print(vendas_mes)

# Criar gráfico
vendas_mes.plot(kind="line", title="Vendas por mês")

# Mostrar gráfico
plt.savefig("grafico_vendas.png")
plt.show()