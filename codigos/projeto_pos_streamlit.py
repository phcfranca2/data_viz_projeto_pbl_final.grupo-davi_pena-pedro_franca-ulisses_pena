import streamlit as st
import plotly.express as px
import os
import sys
import polars as pl
import altair as alt

st.set_page_config(
    layout="wide",
    page_title="Entrega Final - PBL",
    page_icon="📊",
)

@st.cache_data
def carregar_bases():
    kanban = pl.read_parquet('../parquets/kanban.parquet')
    
    kanban_groupby = kanban.group_by(
        pl.col('grupo'),
        pl.col('sprint')
    ).agg(
        pl.len().alias('quantidade cards')
    ).with_columns(
        pl.coalesce(pl.col('sprint'),pl.lit('Sprint Não Informado')).alias('sprint')
    )
    
    commits = pl.read_csv(f'../bases/commits.csv').with_columns(
        pl.col('commitado_em').str.slice(0,10).str.strptime( dtype=pl.Datetime, format="%Y-%m-%d")
    )
    
    return kanban,kanban_groupby,commits

var = carregar_bases()
kanban,kanban_groupby,commits = var[0],var[1],var[2]

st.title('Entrega Final - PBL')
st.subheader('''
Integrantes:

- Ulisses Pena
- Davi Pena
- Pedro França
             ''')

st.markdown('---')



col1, col2 = st.columns(2)

with col1:
    st.subheader("Analítico Cards")
    grupo_fiter = st.selectbox('Grupo: ', kanban.select(pl.col('grupo')).unique().sort('grupo').to_series().to_list())
    
    filtros = pl.col('grupo') == grupo_fiter
    
    col1_, col2_ = st.columns(2)

    with col1_:
        card_fiter = st.selectbox('Card: ', kanban.select(pl.col('cartao_numero')).unique().sort('cartao_numero').to_series().to_list(), index=None)
        
        if card_fiter:
            filtros &= pl.col('cartao_numero') == card_fiter
    
    with col2_:
            sprint_fiter = st.selectbox('Sprint: ', kanban.select(pl.col('sprint')).unique().sort('sprint').to_series().to_list(), index=None)
            
            if sprint_fiter:
                filtros &= pl.col('sprint') == sprint_fiter
        
        
    st.dataframe(kanban.filter(filtros).select(
        pl.col('grupo').alias('Grupo'),
        pl.concat_str(pl.col('cartao_numero'),pl.lit(' - '),pl.col('sprint')).alias('Card Por Sprint'),
        pl.col('titulo').alias('Título'),
        pl.col('descricao').alias('Descrição'),
        pl.col('situacao').alias('Situação Card'),
        pl.col('rotulos').alias('Rotulo Card'),
        pl.col('pessoa_id').alias('Pessoa'),
        pl.col('acao').alias('Ação'),
        pl.col('ocorrido_em').alias('Data De Acontecimento Card'),
    ))
    
    st.markdown('\n\n')
    
    st.subheader(f"Variação Linhas Commits Por Grupo - {grupo_fiter}")
    st.bar_chart(
        commits.with_columns(pl.col("commitado_em").dt.strftime("%m/%Y")).filter(pl.col('grupo') == grupo_fiter).group_by(pl.col("commitado_em")).agg(
            pl.col("linhas_adicionadas").sum(),pl.col("linhas_removidas").sum(),pl.col("linhas_total").sum()
        ),
        x="commitado_em",
        y=["linhas_adicionadas","linhas_removidas","linhas_total"],
        color=["#0000FF","#FF0000", "#00FF00"],
        stack=False,
    )

# ------------------- #

with col2:
    st.subheader("Quantidade de Cards por Sprints separados por Grupos")
    st.bar_chart(
        kanban_groupby,
        x="grupo",
        y="quantidade cards",
        color='sprint',
        stack=False,
        horizontal=True
        
    )

   