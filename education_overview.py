import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
##Total de Cursos
df_education = pd.read_csv("samples/MICRODADOS_CADASTRO_CURSOS_2024.CSV", 
                           sep=';', encoding='iso-8859-1', low_memory=False)

total_cursos = df_education['NO_CINE_ROTULO'].count()


fig_total = go.Figure(go.Indicator(
    mode = "number",
    value = total_cursos,
    number = {'valueformat': ',.0f'}, 
    title = {"text": "Total de Cursos Cadastrados (Brasil)"}
))
fig_total.show()

df_contagem = df_education['NO_CINE_ROTULO'].value_counts().reset_index().head(30)
df_contagem.columns = ['Curso', 'Quantidade']


grafico = px.bar(df_contagem, 
             y='Curso', 
             x='Quantidade',
             orientation='h', 
             title='Top 20 Cursos por Quantidade',
             text_auto=True, 
             color='Quantidade',
             color_continuous_scale='Blues')


grafico.update_layout(yaxis={'categoryorder':'total ascending'}, height=900)

grafico.show()