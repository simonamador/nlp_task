from transformers import pipeline
import pandas as pd

# Codigo por @simonamador
# El proposito de este codigo es emplear metodos de NLP
# Para clasificar descripciones a categorias y lenguajes.

# Se inicializa el clasificador de MoritzLaurer, obtenido de HuggingFace
# Se elige este clasificador de texto ya que tiene compatibilidad con el
# idioma español.

classifier = pipeline("zero-shot-classification", model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")

# Definimos las etiquetas que queremos extraer de las descripciones.
# Queremos saber si es de uso personal, juegos, negocios
labels1 = ['personal', 'videojuegos', 'negocios']
labels2 = ['técnico', 'natural']

# Se abre el csv con los datos obtenidos
df = pd.read_csv('desc_data.csv')

# Se procede a clasificar las descripciones
df['Lenguaje'] = df['Desc'].map(lambda x: classifier(x, labels2, multi_label=False)['labels'][0])
df['PuntajeL']= df['Desc'].map(lambda x: classifier(x, labels2, multi_label=False)['scores'][0])
df['Categoria'] = df['Desc'].map(lambda x: classifier(x, labels1, multi_label=False)['labels'][0])
df['PuntajeC']= df['Desc'].map(lambda x: classifier(x, labels1, multi_label=False)['scores'][0])

df.to_csv('proc_data.csv')