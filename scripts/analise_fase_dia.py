from carregar_dados import acidentes_total
import matplotlib.pyplot as plt

# Contagem por fase do dia
fase_dia = acidentes_total['fase_dia'].value_counts()

# Criar gráfico
plt.figure(figsize=(10,6))
barras = plt.bar(fase_dia.index, fase_dia.values)

# Título e eixos
plt.title('Acidentes por fase do dia')
plt.xlabel('Fase do dia')
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

plt.xticks(rotation=10)

plt.show()