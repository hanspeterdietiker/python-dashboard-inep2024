import pandas as pd
import plotly.express as px

df_education = pd.read_csv("samples/MICRODADOS_CADASTRO_CURSOS_2024.CSV", 
                           sep=';', encoding='iso-8859-1', low_memory=False)


px.histogram(x= df_education['NO_CINE_ROTULO'])
