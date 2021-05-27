import pandas as pd

question_mapping = {
    "Impacto nos estudos": ("Como você acredita que o trabalho remoto possa afetar os estudos?",
                            "O trabalho remoto afetou os estudos?"
                            ),

    "Carga Horária": ("Você acredita que a carga horária do trabalho remoto em relação ao presencial é:",
                      "Se você já trabalhou presencialmente, acredita que no trabalho remoto sua carga horária:"
                      ),

    "Performance": ("Você acredita que o rendimento no trabalho remoto em relação ao presencial é?",
                    "Você acredita que o seu rendimento com trabalho remoto é:"
                    ),

    "Vontade x Satisfação": ("Qual é a sua vontade de trabalhar remotamente?",
                             "Qual é seu nível de satisfação com o trabalho remoto?"
                             ),

    "Tipo de trabalho": ("Tipo de trabalho",
                         "Tipo de trabalho"
                         ),
}


def get_data(name):
    return pd.read_csv(f"{name}.csv", encoding="utf-8")


home = get_data("home_office")
x = home[question_mapping["Performance"][1]],
y = home[question_mapping["Performance"][1]].value_counts()
print(y)