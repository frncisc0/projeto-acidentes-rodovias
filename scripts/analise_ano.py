from carregar_dados import acidentes_total
import pandas as pd
import matplotlib.pyplot as plt

# Converter coluna para data
acidentes_total['data_inversa'] = pd.to_datetime(acidentes_total['data_inversa'], errors='coerce')

# Criar coluna de ano
acidentes_total['ano'] = acidentes_total['data_inversa'].dt.year

# Agrupar por ano
acidentes_por_ano = acidentes_total.groupby('ano').size()

# Plotar gráfico
acidentes_por_ano.plot(kind='bar')

plt.title('Quantidade de acidentes por ano (2021-2025)')
plt.xlabel('Ano')
plt.ylabel('Quantidade de acidentes')

for i, v in enumerate(acidentes_por_ano):
    plt.text(i, v, str(v), ha='center', va='bottom')
    
plt.xticks(rotation=0)
plt.tight_layout()   #evita cote de texto no gráfico

plt.show()