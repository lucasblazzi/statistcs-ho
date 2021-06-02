import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
from PIL import Image

from utils.fetch import get_data
from utils.plot import plot_scatter
from utils.plot import plot_bar
from utils.plot import plot_table
from utils.plot import plot_pie
from utils.plot import plot_box
from utils.plot import plot_multi_bar
from utils.plot import plot_histogram

from utils.text import sample_text
from utils.text import performance_text
from utils.text import work_hours_text
from utils.text import academic_impact_text
from utils.text import question_mapping
from utils.text import abstract
from utils.text import sample_analysis
from utils.text import satsxwill_text

st.set_page_config(layout='wide')
pd.set_option('display.max_colwidth', None)

side_bar = st.sidebar


def _header():
    st.title('MAT013 - Probabilidade e Estatistica')
    st.header('Análise comparativa de perspectivas relacionadas ao Home Office')
    st.markdown("____")
    st.markdown(abstract, unsafe_allow_html=True)


def _amostra(visualizations, raw_data):
    cols = st.beta_columns(3)
    amostras = ("Tipo de trabalho", "Categoria")
    for i, amostra in enumerate(amostras):
        count_amostra = visualizations[amostra].value_counts()
        amostra_bar = plot_pie(count_amostra, x=amostra, y=count_amostra.index,
                              title=amostra)
        cols[i].plotly_chart(amostra_bar)

    count_raw = raw_data["Curso"].value_counts()
    raw_bar = plot_bar(count_raw, x=count_raw.index, y="Curso",
                          title="Distribuição por curso", width=800, height=500, color=count_raw.index)
    cols[0].plotly_chart(raw_bar)
    cols[2].markdown("<br><br>", unsafe_allow_html=True)
    cols[2].markdown(sample_analysis, unsafe_allow_html=True)


def _comparison(visualizations):
    compare = ("Performance", "Carga Horária", "Impacto nos estudos")
    results = (performance_text , work_hours_text, academic_impact_text)
    for comp, res in zip(compare, results):
        cols = st.beta_columns([0.55, 0.45])
        fig = plot_multi_bar(visualizations, comp)
        cols[0].plotly_chart(fig)
        cols[1].markdown("<br><br><br>", unsafe_allow_html=True)
        cols[1].markdown(res, unsafe_allow_html=True)


def _base_scatter(home_office):
    st.markdown("____")
    cols = st.beta_columns([0.7, 0.3])
    x = "Qual é seu nível de satisfação com o trabalho remoto?"
    y = "Horas trabalhadas"
    f = plot_scatter(home_office, x, y)
    cols[0].plotly_chart(f)
    cols[1].markdown("<br><br>", unsafe_allow_html=True)
    cols[1].write(sample_text)


def _satsxreal(visualizations):
    cols = st.beta_columns([0.4, 0.3, 0.3])
    comp = {"Não Remoto": "Vontade de trabalhar home office (Não Remoto)",
            "Remoto" :"Satisfação com o Home Office (Remoto)"}
    i = 0
    c = 0
    for k, val in comp.items():
        v = visualizations.loc[visualizations["Categoria"] == k]
        hist = plot_histogram(v, title=val)
        box = plot_box(v, val, k, "Vontade x Satisfação")
        cols[i].plotly_chart(hist)
        if c > 0:
            cols[i+1].markdown("<br><br>", unsafe_allow_html=True)
        cols[i+1].plotly_chart(box)
        table = plot_table(v, "Vontade x Satisfação", title=val)
        cols[i+2].plotly_chart(table)
        c+=1
    st.markdown(satsxwill_text, unsafe_allow_html=True)


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
        "Nunca trabalhou home office": not_home_office,
        "Vizualização Comparativa": visualizations
    }

    selection = side_bar.selectbox("Selecione", ["Dashboard", "Dados"])
    image = Image.open("infografico.png")

    if selection == "Dados":
        st.image(image)
        st.subheader("Questões")
        st.dataframe(raw_data.columns)
        exclude = ("Qual é a sua vontade de trabalhar remotamente?", "Vontade x Satisfação")
        for key, value in sets.items():
            st.subheader(key)
            st.dataframe(value)
            for i, column in enumerate(value.columns):
                if i == 0 or column in exclude or key == "Dados Brutos":
                    continue
                st.dataframe(value[column].value_counts())
            st.markdown("____")

    elif selection == "Dashboard":
        _header()
        _set_title("Contextualização e Análise Amostral")
        _amostra(visualizations, raw_data)

        _set_title("Análise de Perspectivas")
        _comparison(visualizations)

        _set_title("Outras Observações")
        _satsxreal(visualizations)

        st.markdown("____")
        st.image(image)

if __name__ == "__main__":
    main()
