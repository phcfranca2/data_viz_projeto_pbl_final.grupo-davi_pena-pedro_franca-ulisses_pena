# 📊 Entrega Final — PBL

Dashboard interativo desenvolvido em **Python com Streamlit** para análise de cards de Kanban e métricas de commits, permitindo acompanhar a distribuição de tarefas por grupo e sprint, consultar informações detalhadas dos cards e analisar a variação de linhas de código ao longo do tempo.

## 🎯 Objetivo do Projeto

Disponibilizar uma interface analítica para explorar os dados de gerenciamento de tarefas e desenvolvimento de software, facilitando o acompanhamento das atividades e a visualização de indicadores relevantes do projeto.

## 🚀 Funcionalidades

### 1. Analítico de Cards

Permite consultar e filtrar os cards do Kanban por:

- **Grupo:** seleção do grupo que será analisado.
- **Card:** filtro por número do card.
- **Sprint:** filtro por sprint associada ao card.

A tabela apresenta informações detalhadas, incluindo grupo, número do card, sprint, título, descrição, situação, rótulos, pessoa responsável, ação e data de acontecimento.

### 2. Variação de Linhas de Código por Grupo

Apresenta um gráfico de barras com a variação das linhas de código dos commits associados ao grupo selecionado.

O gráfico contempla três indicadores:

- Linhas adicionadas.
- Linhas removidas.
- Total de linhas.

Os dados são agrupados por mês e ano, permitindo acompanhar a evolução das alterações no código ao longo do tempo.

### 3. Quantidade de Cards por Sprint e Grupo

Exibe um gráfico de barras horizontais com a quantidade de cards distribuídos entre os grupos e suas respectivas sprints.

Essa visualização permite comparar o volume de cards por grupo e sprint, facilitando a análise da distribuição das atividades.

## 🛠️ Tecnologias Utilizadas

- **Python:** linguagem principal do projeto.
- **Streamlit:** criação e disponibilização do dashboard interativo.
- **Polars:** leitura, transformação, filtragem e agregação dos dados.
- **Plotly Express:** biblioteca disponível no projeto para visualizações de dados.
- **Altair:** biblioteca disponível no projeto para visualizações declarativas.

## 📁 Estrutura de Diretórios

O projeto espera que os arquivos estejam organizados conforme a estrutura abaixo:

```text
projeto/
├── codigos
    └── projeto_pos_streamlit.py
    └── notebook-testes-etl.ipynb
├── bases/
│   └── *.csv
└── parquets/
│   └── kanban.parquet
├── README.md
```

**Importante:** os caminhos utilizados no código são relativos ao diretório de execução. Execute o comando a partir da pasta que contém o arquivo `projeto_pos_streamlit.py`, mantendo as pastas `bases` e `parquets` nos locais esperados.

## ⚙️ Como Executar o Dashboard

### 1. Pré-requisitos

Certifique-se de ter o Python instalado e os arquivos de dados necessários disponíveis no projeto.

### 2. Instalar as dependências

Abra o terminal na pasta do projeto e execute:

```bash
pip install streamlit polars plotly altair
```

### 3. Executar o Streamlit

No terminal, dentro da pasta onde está localizado o arquivo `projeto_pos_streamlit.py`, execute:

```bash
streamlit run projeto_pos_streamlit.py
```

O Streamlit iniciará um servidor local e disponibilizará o endereço de acesso ao dashboard no terminal. Normalmente, o endereço padrão é:

```text
http://localhost:8501
```

Abra esse endereço no navegador para visualizar e interagir com o dashboard.

### 4. Encerrar a execução

Para interromper o servidor, retorne ao terminal em que o Streamlit está sendo executado e pressione `Ctrl + C`.

## 📂 Fontes de Dados

O dashboard utiliza duas fontes principais:

| Arquivo | Formato | Finalidade |
|---|---|---|
| `kanban.parquet` | Parquet | Informações dos cards, grupos, sprints e demais atributos do Kanban. |
| `commits.csv` | CSV | Informações dos commits, incluindo datas e quantidades de linhas adicionadas, removidas e totais. |

Os dados são carregados por meio da função `carregar_bases()`, que utiliza o mecanismo de cache do Streamlit para reduzir leituras repetidas durante a navegação.

## 👥 Integrantes

- Ulisses Pena
- Davi Pena
- Pedro França

---

*Projeto desenvolvido como entrega final do PBL.*