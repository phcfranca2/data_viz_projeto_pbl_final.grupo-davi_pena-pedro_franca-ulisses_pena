import streamlit as st
import plotly.express as px

import polars as pl

kanban = pl.read_parquet('/Users/PedroFranca/Desktop/Projeto dashboard Apartamento/pasta-git-projeto-data-viz/data_viz_projeto_pbl_final.grupo-davi_pena-pedro_franca-ulisses_pena/parquets/kanban.parquet')
kanban_groupby = kanban.group_by(
    pl.col('grupo'),
    pl.col('sprint')
).agg(
    pl.len().alias('quantidade cards')
).with_columns(
    pl.coalesce(pl.col('sprint'),pl.lit('Sprint Não Informado')).alias('sprint')
)

st.title('Entrega Final - PBL')
st.subheader('''
Integrantes:

- Ulisses Pena
- Davi Pena
- Pedro França
             ''')

st.markdown('---')

col1, col2 = st.columns([1,2])

with col1:
    st.dataframe(kanban)

# ------------------- #

with col2:
    fig = px.bar(
        kanban_groupby,
        x="grupo",
        y="quantidade cards",
        color="sprint",
        barmode="group",
        text="quantidade cards",
        title="Quantidade de Kanbans por Grupo e Sprint"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        xaxis_title="Grupo",
        yaxis_title="Quantidade de Kanbans",
        legend_title="Sprint"
    )

    st.plotly_chart(fig, use_container_width=True)