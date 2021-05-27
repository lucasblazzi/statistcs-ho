import pandas as pd
import os

from .text import question_mapping


directory = os.path.dirname(__file__)
data_path = os.path.join(directory, "data")


def label_category(row):
    if row["Tipo de trabalho"] == "Remoto":
        return "Remoto"
    else:
        return "Não Remoto"


def viz_compose(dfs):
    vis_result = pd.concat(dfs, ignore_index=True, sort=False)
    vis_result["Categoria"] = vis_result.apply(lambda row: label_category(row), axis=1)
    vis_result.loc[vis_result["Performance"] == "Igual ao presencial", "Performance"] = "Igual"

    vis_result.loc[vis_result["Carga Horária"] == "Aumentou", "Carga Horária"] = "Maior"
    vis_result.loc[vis_result["Carga Horária"] == "Sem alteções", "Carga Horária"] = "Igual"
    vis_result.loc[vis_result["Carga Horária"] == "Diminuiu", "Carga Horária"] = "Menor"

    return vis_result


def data_normalize():
    df = pd.read_csv(f"{data_path}/raw_mat013_forms.csv", encoding="utf-8").drop(columns=["Carimbo de data/hora"])

    work_group = df.groupby(df["Categorização do trabalho"])
    employed = work_group.get_group("Empregado")
    unemployed = work_group.get_group("Não empregado").dropna(axis=1, how='all')
    unemployed["Tipo de trabalho"] = "Não empregado"

    work_type = employed.groupby(employed["Tipo de trabalho"])
    home_office = work_type.get_group("Remoto").dropna(axis=1, how='all')
    on_office = work_type.get_group("Presencial").dropna(axis=1, how='all')
    not_home_office = pd.concat([unemployed, on_office], ignore_index=True, sort=False)

    # visualizations
    normalized_unemployed = pd.DataFrame()
    normalized_on_office = pd.DataFrame()
    normalized_home_office = pd.DataFrame()

    visualizations = ("Tipo de trabalho", "Impacto nos estudos", "Carga Horária", "Performance", "Vontade x Satisfação")
    for vis in visualizations:
        normalized_unemployed[vis] = unemployed[question_mapping[vis][0]]
        normalized_on_office[vis] = on_office[question_mapping[vis][0]]
        normalized_home_office[vis] = home_office[question_mapping[vis][1]]

    vis_df = [normalized_unemployed, normalized_on_office, normalized_home_office]
    vis_result = viz_compose(vis_df)

    unemployed.to_csv(f"{data_path}\\unemployed.csv", encoding="utf-8")
    home_office.to_csv(f"{data_path}\\home_office.csv", encoding="utf-8")
    on_office.to_csv(f"{data_path}\\on_office.csv", encoding="utf-8")
    vis_result.to_csv(f"{data_path}\\visualizations.csv", encoding="utf-8")
    not_home_office.to_csv(f"{data_path}\\not_home_office.csv", encoding="utf-8")


def get_data(name):
    return pd.read_csv(f"{data_path}\\{name}.csv", encoding="utf-8")
