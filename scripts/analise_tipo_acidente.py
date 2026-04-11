from carregar_dados import acidentes_total
import matplotlib.pyplot as plt

# Contagem dos tipos
tipos = acidentes_total['tipo_acidente'].value_counts().head(10)

# Quebrar texto em linhas
tipos.index = [t.replace(' ', '\n') for t in tipos.index]

plt.figure(figsize=(12,6))

# Criar gráfico
ax = tipos.plot(kind='bar') 

plt.title('Tipos de acidentes mais frequentes')
plt.xlabel('Tipo de acidente')
plt.ylabel('Quantidade')

# Adicionar valores nas barras
for i, v in enumerate(tipos):
    ax.text(i, v, f'{v}', ha='center', va='bottom')

plt.xticks(rotation=0)
plt.tight_layout()

plt.show()