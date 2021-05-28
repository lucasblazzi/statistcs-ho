import streamlit as st
import pandas as pd
import plotly.figure_factory as ff

from utils.fetch import get_data
from utils.plot import get_scatter
from utils.plot import get_bar
from utils.plot import get_multi_bar

from utils.text import question_mapping

st.set_page_config(layout='wide')
pd.set_option('display.max_colwidth', None)

side_bar = st.sidebar


def _amostra(visualizations, raw_data):
    st.subheader("Amostra")
    cols = st.beta_columns(2)
    amostras = ("Tipo de trabalho", "Categoria")
    for i, amostra in enumerate(amostras):
        count_amostra = visualizations[amostra].value_counts()
        amostra_bar = get_bar(count_amostra, x=amostra, y=count_amostra.index,
                              title=amostra)
        cols[i].plotly_chart(amostra_bar)

    count_raw = raw_data["Curso"].value_counts()
    raw_bar = get_bar(count_raw, x=count_raw.index, y="Curso",
                          title="Distribuição por curso", width=1000, height=500)
    cols[0].plotly_chart(raw_bar)


def _comparison(visualizations):
    compare = ("Performance", "Carga Horária", "Impacto nos estudos")
    for comp in compare:
        fig = get_multi_bar(visualizations, comp)
        st.plotly_chart(fig)


def _base_scatter(home_office):
    x = "Qual é seu nível de satisfação com o trabalho remoto?"
    y = "Horas trabalhadas"
    f = get_scatter(home_office, x, y)
    st.plotly_chart(f)


def _set_title(title):
    st.markdown("____")
    st.header(title)
    st.markdown("<br><br>", unsafe_allow_html=True)


def main():
    raw_data = get_data("raw_mat013_forms")
    home_office = get_data("home_office")
    not_home_office = get_data("not_home_office")
    on_office = get_data("on_office")
    unemployed = get_data("unemployed")
    visualizations = get_data("visualizations")

    sets = {
        "Dados Brutos": raw_data,
        "Empregado - Home Office": home_office,
        "Empregado - Presencial": on_office,
        "Não Empregado": unemployed,
        "Vizualização Comparativa": visualizations
    }

    selection = side_bar.selectbox("Selecione", ["Dashboard", "Dados Brutos"])

    if selection == "Dados Brutos":
        st.subheader("Questions")
        st.dataframe(raw_data.columns)
        for key, value in sets.items():
            st.subheader(key)
            st.dataframe(value)

    elif selection == "Dashboard":
        _set_title("Análise Amostral")
        _amostra(visualizations, raw_data)

        _set_title("Análise de Perspectivas")
        _comparison(visualizations)

        _set_title("Outras Observações")
        _base_scatter(home_office)

if __name__ == "__main__":
    main()
