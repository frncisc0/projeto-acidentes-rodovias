from carregar_dados import acidentes_total
import matplotlib.pyplot as plt

# Contagem por condição meteorológica
clima = acidentes_total['condicao_metereologica'].value_counts()

# Selecionar os 5 mais frequentes
top_clima = clima.head(5)

# Criar gráfico
plt.figure(figsize=(10,6))
barras = plt.bar(top_clima.index, top_clima.values)

# Título e eixos
plt.title('Acidentes por condição meteorológica')
plt.xlabel('Condição meteorológica')
plt.ylabel('Quantidade')

# Adicionar números acima das barras
for barra in barras:
    altura = barra.get_height()
    plt.text(
        barra.get_x() + barra.get_width()/2,
        altura,
        f'{int(altura)}',
        ha='center',
        va='bottom'
    )

plt.xticks(rotation=15)

plt.show()