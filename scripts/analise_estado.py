from carregar_dados import acidentes_total
import matplotlib.pyplot as plt

acidentes_por_estado = acidentes_total['uf'].value_counts().head(10)

acidentes_por_estado.plot(kind='bar')

plt.title('Top 10 estados com mais acidentes')
plt.xlabel('Estado')
plt.ylabel('Quantidade de acidentes')

for i, v in enumerate(acidentes_por_estado):
    plt.text(i, v, str(v), ha='center', va='bottom')

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()