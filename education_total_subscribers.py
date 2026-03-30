import pandas as pd
import plotly.express as px


df_education = pd.read_csv("samples/MICRODADOS_CADASTRO_CURSOS_2024.CSV", 
                           sep=';', encoding='iso-8859-1', low_memory=False)

total_inscritos = df_education['QT_INSCRITO_TOTAL'].sum()

grafico = px.bar(x=["Total de Inscritos "], 
             y=[total_inscritos],
             title="Inscritos Totais - Censo 2024",
             labels={'y': 'Quantidade de Pessoas', 'x': '2024'},
             text_auto=',.0f')

grafico.update_traces(marker_color='darkviolet', width=0.1) 
grafico.show()