import pandas as pd
import plotly.express as px

#Total de Inscritos
df_education = pd.read_csv("/content/samples/MICRODADOS_CADASTRO_CURSOS_2024.CSV", 
                           sep=';', encoding='iso-8859-1', low_memory=False)


total_inscritos = df_education['QT_INSCRITO_TOTAL'].sum()

total_inscritos = {'Ano':['2024'], 'Total': [total_inscritos]}


grafico = px.bar(total_inscritos, 
                 x ='Ano', 
                 y='Total',
                 title="Inscritos Totais - Censo 2024",
                 labels={'y': 'Quantidade de Pessoas', 'x': 'Censo'},
                 text_auto=',.0f') 


grafico.update_traces(marker_color='CornflowerBlue', width=0.1) 
grafico.update_layout(yaxis_tickformat=',.0f')

grafico.show()