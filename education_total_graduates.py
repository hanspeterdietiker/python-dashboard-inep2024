import pandas as pd
import plotly.express as px

#Total de Concluintes
df_education = pd.read_csv("/content/samples/MICRODADOS_CADASTRO_CURSOS_2024.CSV",
                           sep=';', encoding='iso-8859-1', low_memory=False)


total_concluintes = df_education['QT_CONC'].sum()

total_concluintes = {'Ano':['2024'], 'Total': [total_concluintes]}


grafico = px.bar(total_concluintes,
                 x ='Ano',
                 y='Total',
                 title="Concluintes - Censo 2024",
                 labels={'y': 'Quantidade de Pessoas', 'x': 'Censo'},
                 text_auto=',.0f')


grafico.update_traces(marker_color='CornflowerBlue', width=0.1)
grafico.update_layout(yaxis_tickformat=',.0f')

grafico.show()