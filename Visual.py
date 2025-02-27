import matplotlib.pyplot as plt

vendas_categoria = df.groupby('Categoria')['Total_Venda'].sum()
vendas_categoria.plot(kind='bar', color=['blue', 'green', 'red'])
plt.title('Total de vendas por categoria')
plt.xlabel('categoria')
plt.ylabel('vlor em R$')
plt.show()