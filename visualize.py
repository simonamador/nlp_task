import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Codigo por @simonamador
# El proposito de este codigo es visualizar los resultados obtenidos.

# Se extrae la data procesada
df = pd.read_csv('proc_data.csv')

# Se establece un estilo de seaborn
sns.set_style("dark")

# Se generan los datos a visualizar removiendo datos faltantes y empleando group_by
n_df = df.copy()
n_df['Desc'] = n_df['Desc'].apply(lambda x: x!='0')
a = pd.DataFrame({'count': n_df.groupby('Categoria')['Desc'].sum()}).reset_index()
b = pd.DataFrame({'count' : n_df.groupby(['Laptop','Categoria'])['Desc'].sum()}).reset_index()
c = pd.DataFrame({'count': n_df.groupby('Lenguaje')['Desc'].sum()}).reset_index()
d = pd.DataFrame({'count' : n_df.groupby(['Laptop','Lenguaje'])['Desc'].sum()}).reset_index()

# Se visualizan productos con descripcion vs sin descripcion
sum_all = sum(n_df.groupby('Categoria')['Desc'].count().agg(list))
na = (sum_all-sum(n_df.groupby('Categoria')['Desc'].sum().agg(list)))

ax1 = sns.barplot(x = ['sin descripción', 'descripción'], y = [round(na/sum_all*100),round((sum_all-na)/sum_all*100)])
for i in ax1.containers:
    ax1.bar_label(i,)
ax1.set(yticklabels=[])
ax1.set(ylabel=None)
ax1.figure.savefig("results/desc.png")
plt.clf()

# Se visualizan la distribucion total acorde a categoria
ax2 = sns.barplot(x = 'Categoria', y = 'count', data = a, palette='deep')
for i in ax2.containers:
    ax2.bar_label(i,)
ax2.set(yticklabels=[])
ax2.set(ylabel=None)
ax2.set(xlabel=None)
ax2.set(title='Categoria descrita')
ax2.figure.savefig("results/cat1.png") 
plt.clf()


# Se visualiza la distribucion de categorias acorde a la marca de laptop
ax3 = sns.barplot(data=b, x="Laptop", y="count", hue="Categoria")
plt.legend(loc='upper left')
ax3.set(ylabel=None)
ax3.figure.savefig("results/cat2.png") 
plt.clf()

# Se visualizan la distribucion total acorde a lenguaje
ax4 = sns.barplot(x = 'Lenguaje', y = 'count', data = c, palette='deep')
for i in ax4.containers:
    ax4.bar_label(i,)
ax4.set(yticklabels=[])
ax4.set(ylabel=None)
ax4.set(xlabel=None)
ax4.set(title='Lenguaje usado')
ax4.figure.savefig("results/len1.png") 
plt.clf()

# Se visualiza la distribucion de lenguaje acorde a la marca de laptop
ax5 = sns.barplot(data=d, x="Laptop", y="count", hue="Lenguaje")
plt.legend(loc='upper left')
ax5.set(ylabel=None)
ax5.figure.savefig("results/len2.png") 
plt.clf()