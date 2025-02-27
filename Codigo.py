import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("vendas.csv")
print(df.head())

df['Total_Venda'] = df['Quantidade'] * df['Preço Unitário (R$)']

media_preço = df['Preço Unitário (R$)'].mean()
total_vendas = df['Total_Venda'].sum()
maior_vendas = df['Total_Venda'].max()
menor_venda = df['Total_Venda'].min()

print(media_preço, total_vendas, maior_vendas, menor_venda)

vendas_categoria = df.groupby('Categoria')['Total_Venda'].sum()
vendas_categoria.plot(kind='bar', color=['blue', 'green', 'red'])
plt.title('Total de vendas por categoria')
plt.xlabel('categoria')
plt.ylabel('valor em R$')
plt.show()