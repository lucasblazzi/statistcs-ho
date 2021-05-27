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


def _amostra(visualizations):
    st.subheader("Amostra")
    i = 0
    cols = st.beta_columns(2)
    amostras = ("Tipo de trabalho", "Categoria")
    for amostra in amostras:
        count_amostra = visualizations[amostra].value_counts()
        amostra_bar = get_bar(count_amostra, x=amostra, y=count_amostra.index,
                              title=f"Amostra - {amostra}")
        cols[i].plotly_chart(amostra_bar)
        i += 1


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

    selection = side_bar.selectbox("Selecione", ["Dados Brutos", "Dashboard"])

    if selection == "Dados Brutos":
        st.subheader("Questions")
        st.dataframe(raw_data.columns)
        for key, value in sets.items():
            st.subheader(key)
            st.dataframe(value)

    elif selection == "Dashboard":
        _amostra(visualizations)
        _base_scatter(home_office)
        _comparison(visualizations)


if __name__ == "__main__":
    main()
