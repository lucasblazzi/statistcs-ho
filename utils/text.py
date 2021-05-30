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


sample_text = "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?"


abstract = "A pesquisa tem como objetivo principal fazer a **comparação entre perspectivas e o cenário real do trabalho " \
         "em home office no contexto de estudantes da Universidade Federal de Itajubá**. O foco do trabalho foi na " \
         "comparação de visões relacionadas a nivel de impacto nos estudos, relação da carga horária presencial com a " \
         "remota, nível de performance e vontade x satisfação no home office.\n" \
         "Para atingir o objetivo, foi aplicado um questionário via Google Forms **(disponbilizado de 18/05/2021 até " \
         "28/05/2021 e limitado por e-mail)** para estudantes da UNIFEI. O questionário foi divido em dois setores, sendo um para pessoas que já " \
         "trabalharam em home office e outro para os que nunca tiveram contato com esse método, seja trabalhando " \
         "presencialmente ou não estando empregado. Foram utilizadas perguntas (qualitativas e quantitativas) de suposição e de aplicação como: " \
         "Como você acredita que o trabalho remoto possa afetar os estudos? vs O trabalho remoto afetou os estudos? " \
         "diferenciando os dois grupos (as questões aplicadas podem ser visualizadas na aba de dados). Por fim, esse " \
         "levantamento resultou em uma **amostra de 105 alunos** que foram organizadas e divididas em tabelas para visualização, " \
         "que também podem ser vistas na aba de dados.\n As análises de resultado abaixo foram feitas a partir da proporção " \
           "relativa de respostas em cada agrupamento."

sample_analysis = "A partir da coleta dos dados podemos notar que a maioria dos alunos que responderam o questionário " \
                  "se encaixaram no grupo de 'Não empregado' (62.7%) que associado aos que trabalham presencialmente (14.3%) " \
                  "levaram a um agrupamento DE pessoas que nunca " \
                  "trabalharam remotamente (77.1%) vs. pessoas que tiveram contato com home office (22.9%), percebendo assim uma assimetria na categorização das amostras, fator esse " \
                  "que motivou a equipe a trabalhar com proporções relativas para a comparação dos dados, já que a média " \
                  "dos dados poderia ser tendenciosa.<br><br><br><br><br><br><br><br><br><br><br><br><br><br>" \
                   "Além disso, como os integrantes da equipe cursam Sistemas de " \
                  "Informação, a divulgação do questionário foi mais participativa nesse grupo, resultando em uma maior " \
                  "concentração de respostas de curso (31.13%). Esse fator deve ser levado em " \
                  "consideração já que esse grupo tende a ter uma visão diferente em relação ao trabalho, por já possuir " \
                  "um maior costume com passar grandes horas no computador."

performance_text = "Para a comparação de performance foram realizadas as perguntas 'Você acredita que o rendimento no " \
                   "trabalho remoto em relação ao presencial é?' (Grupo sem contato com home office) e " \
                   "'Você acredita que o seu rendimento com trabalho remoto é:' (Grupo que trabalha home office), " \
                   "os resultados foram organizados em três categorias: Menor, Maior e Igual. A partir dos resultados " \
                   "foi observada a proporção relativa para a análise, que resultou no grafico a esquerda." \
                   "<br><br><br>Os resultados mostraram que existe uma divergência nas expectativas do trabalho remoto " \
                   "relacionado a rendimento, muitos acreditam que não irão performar suficiente e que seu rendimento " \
                   "seria menor em home office (54.32%), o contrário é levantado pelos que trabalham efetivamente nesse " \
                   "mecanismo (75% afirmam rendimento maior em relação ao trabalho presencial)."

work_hours_text = "Para a comparação de perspectivas relacionadas a diferença de carga horária esperada, foi utilizada a " \
                  "mesma estratégia da etapa anterior, com as questões 'Você acredita que a carga horária do trabalho " \
                  "remoto em relação ao presencial é:' e 'Se você já trabalhou presencialmente, acredita que no trabalho " \
                  "remoto sua carga horária:', resultando em repostas fechadas de Maior, Menor ou Igual." \
                  "<br><br><br>Nesse caso, foi interessante analisar que existe uma tendência em acreditar que a carga " \
                  "horária no trabalho remoto é menor em relação ao presencial (14.81%), o que é contradizente ao relatado pelos " \
                  "que trabalham nesse modelo."

academic_impact_text = "Por fim, foi feita a comparação de visões relacionadas ao impacto no rendimento acadêmico dos " \
                       "alunos. Essa etapa foi feita através das perguntas: 'Como você acredita que o trabalho remoto " \
                       "possa afetar os estudos?' e 'O trabalho remoto afetou os estudos?', resultando em respostas " \
                       "que foram agrupadas em: Neutro, Negativamente e Positivamente." \
                       "<br><br><br>Nessa análise o destaque vai para o relato de maior impacto negativo rendimento acadêmico no modelo de " \
                       "home office (50%). Uma tentativa de análise de correlação foi feita para tentar identificar o problema " \
                       ", mas foi inconclusiva e será mostrada no fim da análise."

satsxwill_text = "Para tentativa de comparação entre vontade de trabalhar em home office (grupo que não teve contato com home office) " \
                 "e satisfação com o trabalho remoto (grupo que trabalha em home office) foi solicitado que cada grupo atribuísse uma " \
                 "nota de 0 a 10 para suas respectivas avaliações. Assim, foi possível fazer uma análise de distribuição dos resultados " \
                 "em cada grupo." \
                 "<br><br>A partir dos dados foram montados o histrograma, o boxplot e o cálculo de variáveis de média e desvio padrão " \
                 "dos dados. Foi notado que a vontade de trabalhar remotamente é bem distribuida e divide opiniões, que pode ser observado " \
                 "através da distribuição dos dados no histrograma, assim como maior simetria do box plot, que abrange todos os valores (0 a 10) " \
                 "na cerca do boxplot, resultado de uma média 6.16 e mediana 6. " \
                 "<br><br>No caso da avaliação de satisfação, pode se perceber uma maior concentração dos dados em uma perspectiva mais positiva " \
                 "de satisfação, isso por que o box plot se concentra mais a direita, agrupando na cerca valores entre 5 e 10, demontrando uma " \
                 "mediana 8 e media 8.041, confirmando uma assimetria gráfica, assim como um contentamento dos trabalhadores home office com o " \
                 "modelo de trabalho."
