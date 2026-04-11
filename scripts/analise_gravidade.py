from carregar_dados import acidentes_total
import matplotlib.pyplot as plt

gravidade = {
    'Mortos': acidentes_total['mortos'].sum(),
    'Feridos graves': acidentes_total['feridos_graves'].sum(),
    'Feridos leves': acidentes_total['feridos_leves'].sum(),
    'Ilesos': acidentes_total['ilesos'].sum()           # Somar os valores
}

categorias = list(gravidade.keys())
valores = list(gravidade.values())      # Criar listas

plt.bar(categorias, valores)     # Plotar gráfico

plt.title('Gravidade dos acidentes (2021-2025)')
plt.xlabel('Categoria')
plt.ylabel('Quantidade de pessoas')

for i, v in enumerate(valores):
    plt.text(i, v, str(v), ha='center', va='bottom')       # Mostrar valores nas barras

plt.tight_layout()
plt.show()