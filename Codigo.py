import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("vendas.csv")
print(df.head())  

df['Total_Venda'] = df['Quantidade'] * df['Preço Unitário (R$)']

media_preço = df['Preço Unitário (R$)'].mean()
total_vendas = df['Total_Venda'].sum()
maior_vendas = df['Total_Venda'].max()
menor_venda = df['Total_Venda'].min()

print("Média de preço:", media_preço)
print("Total de vendas:", total_vendas)
print("Maior venda:", maior_vendas)
print("Menor venda:", menor_venda)

vendas_categoria = df.groupby('Categoria')['Total_Venda'].sum()

plt.style.use('ggplot')  
fig, ax = plt.subplots(figsize=(8, 5))  
cores = ['#1f77b4', '#2ca02c', '#d62728']  

vendas_categoria.plot(kind='bar', color=cores, ax=ax)

for index, value in enumerate(vendas_categoria):
    ax.text(index, value + (value * 0.02), f'R${value:,.2f}', ha='center', fontsize=10)

plt.title('Total de Vendas por Categoria', fontsize=14, fontweight='bold')
plt.xlabel('Categoria', fontsize=12)
plt.ylabel('Valor em R$', fontsize=12)
plt.xticks(rotation=360)  

plt.grid(axis='y', linestyle='--', alpha=0.7)  
plt.tight_layout()  

plt.show()
