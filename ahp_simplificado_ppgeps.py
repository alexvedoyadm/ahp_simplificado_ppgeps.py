import streamlit as st
import pandas as pd
import numpy as np

tabela_ref = [
    {"ref": 0.6667, "valor": 0.3333},
    {"ref": 0.8000, "valor": 0.2000},
    {"ref": 0.8571, "valor": 0.1429},
    {"ref": 0.8889, "valor": 0.1111},
    {"ref": 0.0000, "valor": 1.0000},
    {"ref": -2.0000, "valor": 3.0000},
    {"ref": -4.0000, "valor": 5.0000},
    {"ref": -6.0000, "valor": 7.0000},
    {"ref": -8.0000, "valor": 9.0000},
    {"ref": 2.6667, "valor": 0.2000},
    {"ref": 2.8000, "valor": 0.1429},
    {"ref": 2.8571, "valor": 0.1111},
    {"ref": 2.8889, "valor": 0.1111},
    {"ref": 2.0000, "valor": 0.3333},
    {"ref": 0.0000, "valor": 1.0000},
    {"ref": -2.0000, "valor": 3.0000},
    {"ref": -4.0000, "valor": 5.0000},
    {"ref": -6.0000, "valor": 7.0000},
    {"ref": 4.6667, "valor": 0.1429},
    {"ref": 4.8000, "valor": 0.1111},
    {"ref": 4.8571, "valor": 0.1111},
    {"ref": 4.8889, "valor": 0.1111},
    {"ref": 4.0000, "valor": 0.2000},
    {"ref": 2.0000, "valor": 0.3333},
    {"ref": 0.0000, "valor": 1.0000},
    {"ref": -2.0000, "valor": 3.0000},
    {"ref": -4.0000, "valor": 5.0000},
    {"ref": 6.6667, "valor": 0.1111},
    {"ref": 6.8000, "valor": 0.2000},
    {"ref": 6.8571, "valor": 0.1111},
    {"ref": 6.8889, "valor": 0.1111},
    {"ref": 6.0000, "valor": 0.1429},
    {"ref": 4.0000, "valor": 0.2000},
    {"ref": 2.0000, "valor": 0.3333},
    {"ref": 0.0000, "valor": 1.0000},
    {"ref": -2.0000, "valor": 3.0000},
    {"ref": 8.6667, "valor": 0.1111},
    {"ref": 8.8000, "valor": 0.1111},
    {"ref": 8.8571, "valor": 0.1111},
    {"ref": 8.8889, "valor": 0.1111},
    {"ref": 8.0000, "valor": 0.1111},
    {"ref": 6.0000, "valor": 0.1429},
    {"ref": 4.0000, "valor": 0.2000},
    {"ref": 2.0000, "valor": 0.3333},
    {"ref": 0.0000, "valor": 1.0000},
    {"ref": 0.0000, "valor": 1.0000},
    {"ref": 0.1333, "valor": 0.3333},
    {"ref": 0.1905, "valor": 0.2000},
    {"ref": 0.2222, "valor": 0.1429},
    {"ref": -0.6667, "valor": 3.0000},
    {"ref": -2.6667, "valor": 5.0000},
    {"ref": -4.6667, "valor": 7.0000},
    {"ref": -6.6667, "valor": 9.0000},
    {"ref": -8.6667, "valor": 9.0000},
    {"ref": -0.1333, "valor": 3.0000},
    {"ref": 0.0000, "valor": 1.0000},
    {"ref": 0.0571, "valor": 0.3333},
    {"ref": 0.0889, "valor": 0.2000},
    {"ref": -0.8000, "valor": 5.0000},
    {"ref": -2.8000, "valor": 7.0000},
    {"ref": -4.8000, "valor": 9.0000},
    {"ref": -6.8000, "valor": 9.0000},
    {"ref": -8.8000, "valor": 9.0000},
    {"ref": -0.1905, "valor": 5.0000},
    {"ref": -0.0571, "valor": 3.0000},
    {"ref": 0.0000, "valor": 1.0000},
    {"ref": 0.0317, "valor": 0.3333},
    {"ref": -0.8571, "valor": 7.0000},
    {"ref": -2.8571, "valor": 9.0000},
    {"ref": -4.8571, "valor": 9.0000},
    {"ref": -6.8571, "valor": 9.0000},
    {"ref": -8.8571, "valor": 9.0000},
    {"ref": -0.2222, "valor": 7.0000},
    {"ref": -0.0889, "valor": 5.0000},
    {"ref": -0.0317, "valor": 3.0000},
    {"ref": 0.0000, "valor": 1.0000},
    {"ref": -0.8889, "valor": 9.0000},
    {"ref": -2.8889, "valor": 9.0000},
    {"ref": -4.8889, "valor": 9.0000},
    {"ref": -6.8889, "valor": 9.0000},
    {"ref": -8.8889, "valor": 9.0000}
]

tabela_cr = {
    3: 0.58,
    4: 0.9,
    5: 1.12,
    6: 1.24,
    7: 1.32,
    8: 1.41,
    9: 1.45,
    10: 1.49,
    11: 1.53,
    12: 1.57,
    13: 1.61,
    14: 1.65,
    15: 1.69,
    16: 1.73,
    17: 1.77,
    18: 1.81,
    19: 1.85,
    20: 1.89,
}



def pagina_numero_critérios():
    st.title("Para quantos critérios você quer atribuir pesos?")
    num_critérios = st.number_input(
        "Você deve utilizar entre 3 e 20 critérios", min_value=3, max_value=20, step=1
    )

    if st.button("Ok"):
        if 3 <= num_critérios <= 20:
            st.session_state.num_critérios = num_critérios
            st.session_state.criterios = [None] * num_critérios
            st.session_state.importancia_valores = (
                []
            )  # Lista para armazenar os valores de importância
            st.session_state.current_step = "nome_criterios"
        else:
            st.warning("A quantidade de critérios deve variar apenas entre 3 e 20.")

    return False


def pagina_nome_critérios():
    st.title("Nomeie os critérios")

    for i in range(st.session_state.num_critérios):
        st.session_state.criterios[i] = st.text_input(
            f"Nome do Critério {i + 1}:", key=f"critério_{i + 1}"
        )

    if all(st.session_state.criterios) and st.button("Prosseguir"):
        st.session_state.current_step = "elicitacao_pesos"

    st.warning("Você deve preencher todos os nomes dos critérios antes de prosseguir.")


def convert_slider_value(value):
    # Mapeie os valores do slider para as conversões específicas
    conversions = {1: 1, 2: 1 / 3, 3: 1 / 5, 4: 1 / 7, 5: 1 / 9, 6: 3, 7: 5, 8: 7, 9: 9}
    return conversions[value]


def pagina_elicitacao_pesos():
    st.title("Aqui você deverá definir a relação de importância entre os critérios.")

    if "num_critérios" not in st.session_state:
        st.warning("Por favor, insira o número de critérios na página anterior.")
        return

    num_critérios = st.session_state.num_critérios

    if num_critérios >= 2:
        c1_name = st.session_state.criterios[0]  # Name of the first criterion
        st.write(f"Aqui, você comparará os critérios com o critério {c1_name}.")

        importancia_valores = []  # Lista para armazenar os valores de importância

        for j in range(2, num_critérios + 1):
            valor = st.slider(
                f"Qual a relação de importância entre o critério {c1_name} e {st.session_state.criterios[j - 1]}?",
                1,
                9,
                5,
            )
            valor_convertido = convert_slider_value(valor)
            descricao_slider = {
                1: f"{c1_name} e {st.session_state.criterios[j - 1]} têm a mesma importância.",
                2: f"{c1_name} é um pouco menos importante que {st.session_state.criterios[j - 1]}.",
                3: f"{c1_name} é menos importante que {st.session_state.criterios[j - 1]}.",
                4: f"{c1_name} é muito menos importante que {st.session_state.criterios[j - 1]}.",
                5: f"{c1_name} é absolutamente menos importante que {st.session_state.criterios[j - 1]}.",
                6: f"{c1_name} é um pouco mais importante que {st.session_state.criterios[j - 1]}.",
                7: f"{c1_name} é mais importante que {st.session_state.criterios[j - 1]}.",
                8: f"{c1_name} é muito mais importante que {st.session_state.criterios[j - 1]}.",
                9: f"{c1_name} é absolutamente mais importante que {st.session_state.criterios[j - 1]}.",
            }
            st.write(descricao_slider[valor])
            importancia_valores.append(valor_convertido)

        st.session_state.importancia_valores = importancia_valores

        # Exibir a tabela de comparação
        data = {
            "Critério": st.session_state.criterios[1:],
            "Importância/Valor": importancia_valores,
        }
        df = pd.DataFrame(data)
        st.write(df)

    if st.button("Prosseguir para a Matriz de Decisão"):
        st.session_state.current_step = "matriz_decisao"



def calcular_matriz_decisao():
    num_critérios = st.session_state.num_critérios
    importancia_valores = st.session_state.importancia_valores

    if len(importancia_valores) != num_critérios - 1:
        st.warning(
            "Por favor, volte para a página de elicitacao_pesos e complete as comparações."
        )
        return None

    matriz_decisao = pd.DataFrame(
        np.ones((num_critérios, num_critérios)),
        columns=[f"C{i}" for i in range(1, num_critérios + 1)],
        index=[f"C{i}" for i in range(1, num_critérios + 1)],
    )

    for i in range(2, num_critérios + 1):
        matriz_decisao.iloc[0, i - 1] = importancia_valores[i - 2]
        # Preencher a parte de baixo com o inverso


    return matriz_decisao





def gerar_segunda_matriz(matriz_decisao):
    segunda_matriz = matriz_decisao.copy()
    num_critérios = st.session_state.num_critérios


    if num_critérios == 3:
        valor_criterio_2 = matriz_decisao.iloc[0, 1]
        for i in range(2, len(segunda_matriz.columns)):
            segunda_matriz.iloc[1, i] = valor_criterio_2 - matriz_decisao.iloc[0, i]
        valor_criterio_3 = matriz_decisao.iloc[0, 2]
        for i in range(3, len(segunda_matriz.columns)):
            segunda_matriz.iloc[2, i] = valor_criterio_3 - matriz_decisao.iloc[0, i]
    if num_critérios == 4:
        valor_criterio_2 = matriz_decisao.iloc[0, 1]
        for i in range(2, len(segunda_matriz.columns)):
            segunda_matriz.iloc[1, i] = valor_criterio_2 - matriz_decisao.iloc[0, i]
        valor_criterio_3 = matriz_decisao.iloc[0, 2]
        for i in range(3, len(segunda_matriz.columns)):
            segunda_matriz.iloc[2, i] = valor_criterio_3 - matriz_decisao.iloc[0, i]
        valor_criterio_4 = matriz_decisao.iloc[0, 3]
        for i in range(4, len(segunda_matriz.columns)):
            segunda_matriz.iloc[3, i] = valor_criterio_4 - matriz_decisao.iloc[0, i]
    if num_critérios == 5:
        valor_criterio_2 = matriz_decisao.iloc[0, 1]
        for i in range(2, len(segunda_matriz.columns)):
            segunda_matriz.iloc[1, i] = valor_criterio_2 - matriz_decisao.iloc[0, i]
        valor_criterio_3 = matriz_decisao.iloc[0, 2]
        for i in range(3, len(segunda_matriz.columns)):
            segunda_matriz.iloc[2, i] = valor_criterio_3 - matriz_decisao.iloc[0, i]
        valor_criterio_4 = matriz_decisao.iloc[0, 3]
        for i in range(4, len(segunda_matriz.columns)):
            segunda_matriz.iloc[3, i] = valor_criterio_4 - matriz_decisao.iloc[0, i]
        valor_criterio_5 = matriz_decisao.iloc[0, 4]
        for i in range(5, len(segunda_matriz.columns)):
            segunda_matriz.iloc[4, i] = valor_criterio_5 - matriz_decisao.iloc[0, i]
    if num_critérios == 6:
        valor_criterio_2 = matriz_decisao.iloc[0, 1]
        for i in range(2, len(segunda_matriz.columns)):
            segunda_matriz.iloc[1, i] = valor_criterio_2 - matriz_decisao.iloc[0, i]
        valor_criterio_3 = matriz_decisao.iloc[0, 2]
        for i in range(3, len(segunda_matriz.columns)):
            segunda_matriz.iloc[2, i] = valor_criterio_3 - matriz_decisao.iloc[0, i]
        valor_criterio_4 = matriz_decisao.iloc[0, 3]
        for i in range(4, len(segunda_matriz.columns)):
            segunda_matriz.iloc[3, i] = valor_criterio_4 - matriz_decisao.iloc[0, i]
        valor_criterio_5 = matriz_decisao.iloc[0, 4]
        for i in range(5, len(segunda_matriz.columns)):
            segunda_matriz.iloc[4, i] = valor_criterio_5 - matriz_decisao.iloc[0, i]
        valor_criterio_6 = matriz_decisao.iloc[0, 5]
        for i in range(6, len(segunda_matriz.columns)):
            segunda_matriz.iloc[5, i] = valor_criterio_6 - matriz_decisao.iloc[0, i]
    if num_critérios == 7:
        valor_criterio_2 = matriz_decisao.iloc[0, 1]
        for i in range(2, len(segunda_matriz.columns)):
            segunda_matriz.iloc[1, i] = valor_criterio_2 - matriz_decisao.iloc[0, i]
        valor_criterio_3 = matriz_decisao.iloc[0, 2]
        for i in range(3, len(segunda_matriz.columns)):
            segunda_matriz.iloc[2, i] = valor_criterio_3 - matriz_decisao.iloc[0, i]
        valor_criterio_4 = matriz_decisao.iloc[0, 3]
        for i in range(4, len(segunda_matriz.columns)):
            segunda_matriz.iloc[3, i] = valor_criterio_4 - matriz_decisao.iloc[0, i]
        valor_criterio_5 = matriz_decisao.iloc[0, 4]
        for i in range(5, len(segunda_matriz.columns)):
            segunda_matriz.iloc[4, i] = valor_criterio_5 - matriz_decisao.iloc[0, i]
        valor_criterio_6 = matriz_decisao.iloc[0, 5]
        for i in range(6, len(segunda_matriz.columns)):
            segunda_matriz.iloc[5, i] = valor_criterio_6 - matriz_decisao.iloc[0, i]
        valor_criterio_7 = matriz_decisao.iloc[0, 6]
        for i in range(7, len(segunda_matriz.columns)):
            segunda_matriz.iloc[6, i] = valor_criterio_7 - matriz_decisao.iloc[0, i]
    if num_critérios == 8:
        valor_criterio_2 = matriz_decisao.iloc[0, 1]
        for i in range(2, len(segunda_matriz.columns)):
            segunda_matriz.iloc[1, i] = valor_criterio_2 - matriz_decisao.iloc[0, i]
        valor_criterio_3 = matriz_decisao.iloc[0, 2]
        for i in range(3, len(segunda_matriz.columns)):
            segunda_matriz.iloc[2, i] = valor_criterio_3 - matriz_decisao.iloc[0, i]
        valor_criterio_4 = matriz_decisao.iloc[0, 3]
        for i in range(4, len(segunda_matriz.columns)):
            segunda_matriz.iloc[3, i] = valor_criterio_4 - matriz_decisao.iloc[0, i]
        valor_criterio_5 = matriz_decisao.iloc[0, 4]
        for i in range(5, len(segunda_matriz.columns)):
            segunda_matriz.iloc[4, i] = valor_criterio_5 - matriz_decisao.iloc[0, i]
        valor_criterio_6 = matriz_decisao.iloc[0, 5]
        for i in range(6, len(segunda_matriz.columns)):
            segunda_matriz.iloc[5, i] = valor_criterio_6 - matriz_decisao.iloc[0, i]
        valor_criterio_7 = matriz_decisao.iloc[0, 6]
        for i in range(7, len(segunda_matriz.columns)):
            segunda_matriz.iloc[6, i] = valor_criterio_7 - matriz_decisao.iloc[0, i]
        valor_criterio_8 = matriz_decisao.iloc[0, 7]
        for i in range(8, len(segunda_matriz.columns)):
            segunda_matriz.iloc[7, i] = valor_criterio_8 - matriz_decisao.iloc[0, i]
    if num_critérios == 9:
        valor_criterio_2 = matriz_decisao.iloc[0, 1]
        for i in range(2, len(segunda_matriz.columns)):
            segunda_matriz.iloc[1, i] = valor_criterio_2 - matriz_decisao.iloc[0, i]
        valor_criterio_3 = matriz_decisao.iloc[0, 2]
        for i in range(3, len(segunda_matriz.columns)):
            segunda_matriz.iloc[2, i] = valor_criterio_3 - matriz_decisao.iloc[0, i]
        valor_criterio_4 = matriz_decisao.iloc[0, 3]
        for i in range(4, len(segunda_matriz.columns)):
            segunda_matriz.iloc[3, i] = valor_criterio_4 - matriz_decisao.iloc[0, i]
        valor_criterio_5 = matriz_decisao.iloc[0, 4]
        for i in range(5, len(segunda_matriz.columns)):
            segunda_matriz.iloc[4, i] = valor_criterio_5 - matriz_decisao.iloc[0, i]
        valor_criterio_6 = matriz_decisao.iloc[0, 5]
        for i in range(6, len(segunda_matriz.columns)):
            segunda_matriz.iloc[5, i] = valor_criterio_6 - matriz_decisao.iloc[0, i]
        valor_criterio_7 = matriz_decisao.iloc[0, 6]
        for i in range(7, len(segunda_matriz.columns)):
            segunda_matriz.iloc[6, i] = valor_criterio_7 - matriz_decisao.iloc[0, i]
        valor_criterio_8 = matriz_decisao.iloc[0, 7]
        for i in range(8, len(segunda_matriz.columns)):
            segunda_matriz.iloc[7, i] = valor_criterio_8 - matriz_decisao.iloc[0, i]
        valor_criterio_9 = matriz_decisao.iloc[0, 8]
        for i in range(9, len(segunda_matriz.columns)):
            segunda_matriz.iloc[8, i] = valor_criterio_9 - matriz_decisao.iloc[0, i]
    if num_critérios == 10:
        valor_criterio_2 = matriz_decisao.iloc[0, 1]
        for i in range(2, len(segunda_matriz.columns)):
            segunda_matriz.iloc[1, i] = valor_criterio_2 - matriz_decisao.iloc[0, i]
        valor_criterio_3 = matriz_decisao.iloc[0, 2]
        for i in range(3, len(segunda_matriz.columns)):
            segunda_matriz.iloc[2, i] = valor_criterio_3 - matriz_decisao.iloc[0, i]
        valor_criterio_4 = matriz_decisao.iloc[0, 3]
        for i in range(4, len(segunda_matriz.columns)):
            segunda_matriz.iloc[3, i] = valor_criterio_4 - matriz_decisao.iloc[0, i]
        valor_criterio_5 = matriz_decisao.iloc[0, 4]
        for i in range(5, len(segunda_matriz.columns)):
            segunda_matriz.iloc[4, i] = valor_criterio_5 - matriz_decisao.iloc[0, i]
        valor_criterio_6 = matriz_decisao.iloc[0, 5]
        for i in range(6, len(segunda_matriz.columns)):
            segunda_matriz.iloc[5, i] = valor_criterio_6 - matriz_decisao.iloc[0, i]
        valor_criterio_7 = matriz_decisao.iloc[0, 6]
        for i in range(7, len(segunda_matriz.columns)):
            segunda_matriz.iloc[6, i] = valor_criterio_7 - matriz_decisao.iloc[0, i]
        valor_criterio_8 = matriz_decisao.iloc[0, 7]
        for i in range(8, len(segunda_matriz.columns)):
            segunda_matriz.iloc[7, i] = valor_criterio_8 - matriz_decisao.iloc[0, i]
        valor_criterio_9 = matriz_decisao.iloc[0, 8]
        for i in range(9, len(segunda_matriz.columns)):
            segunda_matriz.iloc[8, i] = valor_criterio_9 - matriz_decisao.iloc[0, i]
        valor_criterio_10 = matriz_decisao.iloc[0, 9]
        for i in range(10, len(segunda_matriz.columns)):
            segunda_matriz.iloc[9, i] = valor_criterio_10 - matriz_decisao.iloc[0, i]
    if num_critérios == 11:
        valor_criterio_2 = matriz_decisao.iloc[0, 1]
        for i in range(2, len(segunda_matriz.columns)):
            segunda_matriz.iloc[1, i] = valor_criterio_2 - matriz_decisao.iloc[0, i]
        valor_criterio_3 = matriz_decisao.iloc[0, 2]
        for i in range(3, len(segunda_matriz.columns)):
            segunda_matriz.iloc[2, i] = valor_criterio_3 - matriz_decisao.iloc[0, i]
        valor_criterio_4 = matriz_decisao.iloc[0, 3]
        for i in range(4, len(segunda_matriz.columns)):
            segunda_matriz.iloc[3, i] = valor_criterio_4 - matriz_decisao.iloc[0, i]
        valor_criterio_5 = matriz_decisao.iloc[0, 4]
        for i in range(5, len(segunda_matriz.columns)):
            segunda_matriz.iloc[4, i] = valor_criterio_5 - matriz_decisao.iloc[0, i]
        valor_criterio_6 = matriz_decisao.iloc[0, 5]
        for i in range(6, len(segunda_matriz.columns)):
            segunda_matriz.iloc[5, i] = valor_criterio_6 - matriz_decisao.iloc[0, i]
        valor_criterio_7 = matriz_decisao.iloc[0, 6]
        for i in range(7, len(segunda_matriz.columns)):
            segunda_matriz.iloc[6, i] = valor_criterio_7 - matriz_decisao.iloc[0, i]
        valor_criterio_8 = matriz_decisao.iloc[0, 7]
        for i in range(8, len(segunda_matriz.columns)):
            segunda_matriz.iloc[7, i] = valor_criterio_8 - matriz_decisao.iloc[0, i]
        valor_criterio_9 = matriz_decisao.iloc[0, 8]
        for i in range(9, len(segunda_matriz.columns)):
            segunda_matriz.iloc[8, i] = valor_criterio_9 - matriz_decisao.iloc[0, i]
        valor_criterio_10 = matriz_decisao.iloc[0, 9]
        for i in range(10, len(segunda_matriz.columns)):
            segunda_matriz.iloc[9, i] = valor_criterio_10 - matriz_decisao.iloc[0, i]
        valor_criterio_11 = matriz_decisao.iloc[0, 10]
        for i in range(11, len(segunda_matriz.columns)):
            segunda_matriz.iloc[10, i] = valor_criterio_11 - matriz_decisao.iloc[0, i]
    if num_critérios == 12:
        valor_criterio_2 = matriz_decisao.iloc[0, 1]
        for i in range(2, len(segunda_matriz.columns)):
            segunda_matriz.iloc[1, i] = valor_criterio_2 - matriz_decisao.iloc[0, i]
        valor_criterio_3 = matriz_decisao.iloc[0, 2]
        for i in range(3, len(segunda_matriz.columns)):
            segunda_matriz.iloc[2, i] = valor_criterio_3 - matriz_decisao.iloc[0, i]
        valor_criterio_4 = matriz_decisao.iloc[0, 3]
        for i in range(4, len(segunda_matriz.columns)):
            segunda_matriz.iloc[3, i] = valor_criterio_4 - matriz_decisao.iloc[0, i]
        valor_criterio_5 = matriz_decisao.iloc[0, 4]
        for i in range(5, len(segunda_matriz.columns)):
            segunda_matriz.iloc[4, i] = valor_criterio_5 - matriz_decisao.iloc[0, i]
        valor_criterio_6 = matriz_decisao.iloc[0, 5]
        for i in range(6, len(segunda_matriz.columns)):
            segunda_matriz.iloc[5, i] = valor_criterio_6 - matriz_decisao.iloc[0, i]
        valor_criterio_7 = matriz_decisao.iloc[0, 6]
        for i in range(7, len(segunda_matriz.columns)):
            segunda_matriz.iloc[6, i] = valor_criterio_7 - matriz_decisao.iloc[0, i]
        valor_criterio_8 = matriz_decisao.iloc[0, 7]
        for i in range(8, len(segunda_matriz.columns)):
            segunda_matriz.iloc[7, i] = valor_criterio_8 - matriz_decisao.iloc[0, i]
        valor_criterio_9 = matriz_decisao.iloc[0, 8]
        for i in range(9, len(segunda_matriz.columns)):
            segunda_matriz.iloc[8, i] = valor_criterio_9 - matriz_decisao.iloc[0, i]
        valor_criterio_10 = matriz_decisao.iloc[0, 9]
        for i in range(10, len(segunda_matriz.columns)):
            segunda_matriz.iloc[9, i] = valor_criterio_10 - matriz_decisao.iloc[0, i]
        valor_criterio_11 = matriz_decisao.iloc[0, 10]
        for i in range(11, len(segunda_matriz.columns)):
            segunda_matriz.iloc[10, i] = valor_criterio_11 - matriz_decisao.iloc[0, i]
        valor_criterio_12 = matriz_decisao.iloc[0, 11]
        for i in range(12, len(segunda_matriz.columns)):
            segunda_matriz.iloc[11, i] = valor_criterio_12 - matriz_decisao.iloc[0, i]
    if num_critérios == 13:
        valor_criterio_2 = matriz_decisao.iloc[0, 1]
        for i in range(2, len(segunda_matriz.columns)):
            segunda_matriz.iloc[1, i] = valor_criterio_2 - matriz_decisao.iloc[0, i]
        valor_criterio_3 = matriz_decisao.iloc[0, 2]
        for i in range(3, len(segunda_matriz.columns)):
            segunda_matriz.iloc[2, i] = valor_criterio_3 - matriz_decisao.iloc[0, i]
        valor_criterio_4 = matriz_decisao.iloc[0, 3]
        for i in range(4, len(segunda_matriz.columns)):
            segunda_matriz.iloc[3, i] = valor_criterio_4 - matriz_decisao.iloc[0, i]
        valor_criterio_5 = matriz_decisao.iloc[0, 4]
        for i in range(5, len(segunda_matriz.columns)):
            segunda_matriz.iloc[4, i] = valor_criterio_5 - matriz_decisao.iloc[0, i]
        valor_criterio_6 = matriz_decisao.iloc[0, 5]
        for i in range(6, len(segunda_matriz.columns)):
            segunda_matriz.iloc[5, i] = valor_criterio_6 - matriz_decisao.iloc[0, i]
        valor_criterio_7 = matriz_decisao.iloc[0, 6]
        for i in range(7, len(segunda_matriz.columns)):
            segunda_matriz.iloc[6, i] = valor_criterio_7 - matriz_decisao.iloc[0, i]
        valor_criterio_8 = matriz_decisao.iloc[0, 7]
        for i in range(8, len(segunda_matriz.columns)):
            segunda_matriz.iloc[7, i] = valor_criterio_8 - matriz_decisao.iloc[0, i]
        valor_criterio_9 = matriz_decisao.iloc[0, 8]
        for i in range(9, len(segunda_matriz.columns)):
            segunda_matriz.iloc[8, i] = valor_criterio_9 - matriz_decisao.iloc[0, i]
        valor_criterio_10 = matriz_decisao.iloc[0, 9]
        for i in range(10, len(segunda_matriz.columns)):
            segunda_matriz.iloc[9, i] = valor_criterio_10 - matriz_decisao.iloc[0, i]
        valor_criterio_11 = matriz_decisao.iloc[0, 10]
        for i in range(11, len(segunda_matriz.columns)):
            segunda_matriz.iloc[10, i] = valor_criterio_11 - matriz_decisao.iloc[0, i]
        valor_criterio_12 = matriz_decisao.iloc[0, 11]
        for i in range(12, len(segunda_matriz.columns)):
            segunda_matriz.iloc[11, i] = valor_criterio_12 - matriz_decisao.iloc[0, i]
        valor_criterio_13 = matriz_decisao.iloc[0, 12]
        for i in range(13, len(segunda_matriz.columns)):
            segunda_matriz.iloc[12, i] = valor_criterio_13 - matriz_decisao.iloc[0, i]
    if num_critérios == 14:
        valor_criterio_2 = matriz_decisao.iloc[0, 1]
        for i in range(2, len(segunda_matriz.columns)):
            segunda_matriz.iloc[1, i] = valor_criterio_2 - matriz_decisao.iloc[0, i]
        valor_criterio_3 = matriz_decisao.iloc[0, 2]
        for i in range(3, len(segunda_matriz.columns)):
            segunda_matriz.iloc[2, i] = valor_criterio_3 - matriz_decisao.iloc[0, i]
        valor_criterio_4 = matriz_decisao.iloc[0, 3]
        for i in range(4, len(segunda_matriz.columns)):
            segunda_matriz.iloc[3, i] = valor_criterio_4 - matriz_decisao.iloc[0, i]
        valor_criterio_5 = matriz_decisao.iloc[0, 4]
        for i in range(5, len(segunda_matriz.columns)):
            segunda_matriz.iloc[4, i] = valor_criterio_5 - matriz_decisao.iloc[0, i]
        valor_criterio_6 = matriz_decisao.iloc[0, 5]
        for i in range(6, len(segunda_matriz.columns)):
            segunda_matriz.iloc[5, i] = valor_criterio_6 - matriz_decisao.iloc[0, i]
        valor_criterio_7 = matriz_decisao.iloc[0, 6]
        for i in range(7, len(segunda_matriz.columns)):
            segunda_matriz.iloc[6, i] = valor_criterio_7 - matriz_decisao.iloc[0, i]
        valor_criterio_8 = matriz_decisao.iloc[0, 7]
        for i in range(8, len(segunda_matriz.columns)):
            segunda_matriz.iloc[7, i] = valor_criterio_8 - matriz_decisao.iloc[0, i]
        valor_criterio_9 = matriz_decisao.iloc[0, 8]
        for i in range(9, len(segunda_matriz.columns)):
            segunda_matriz.iloc[8, i] = valor_criterio_9 - matriz_decisao.iloc[0, i]
        valor_criterio_10 = matriz_decisao.iloc[0, 9]
        for i in range(10, len(segunda_matriz.columns)):
            segunda_matriz.iloc[9, i] = valor_criterio_10 - matriz_decisao.iloc[0, i]
        valor_criterio_11 = matriz_decisao.iloc[0, 10]
        for i in range(11, len(segunda_matriz.columns)):
            segunda_matriz.iloc[10, i] = valor_criterio_11 - matriz_decisao.iloc[0, i]
        valor_criterio_12 = matriz_decisao.iloc[0, 11]
        for i in range(12, len(segunda_matriz.columns)):
            segunda_matriz.iloc[11, i] = valor_criterio_12 - matriz_decisao.iloc[0, i]
        valor_criterio_13 = matriz_decisao.iloc[0, 12]
        for i in range(13, len(segunda_matriz.columns)):
            segunda_matriz.iloc[12, i] = valor_criterio_13 - matriz_decisao.iloc[0, i]
        valor_criterio_14 = matriz_decisao.iloc[0, 13]
        for i in range(14, len(segunda_matriz.columns)):
            segunda_matriz.iloc[13, i] = valor_criterio_14 - matriz_decisao.iloc[0, i]
    if num_critérios == 15:
        valor_criterio_2 = matriz_decisao.iloc[0, 1]
        for i in range(2, len(segunda_matriz.columns)):
            segunda_matriz.iloc[1, i] = valor_criterio_2 - matriz_decisao.iloc[0, i]
        valor_criterio_3 = matriz_decisao.iloc[0, 2]
        for i in range(3, len(segunda_matriz.columns)):
            segunda_matriz.iloc[2, i] = valor_criterio_3 - matriz_decisao.iloc[0, i]
        valor_criterio_4 = matriz_decisao.iloc[0, 3]
        for i in range(4, len(segunda_matriz.columns)):
            segunda_matriz.iloc[3, i] = valor_criterio_4 - matriz_decisao.iloc[0, i]
        valor_criterio_5 = matriz_decisao.iloc[0, 4]
        for i in range(5, len(segunda_matriz.columns)):
            segunda_matriz.iloc[4, i] = valor_criterio_5 - matriz_decisao.iloc[0, i]
        valor_criterio_6 = matriz_decisao.iloc[0, 5]
        for i in range(6, len(segunda_matriz.columns)):
            segunda_matriz.iloc[5, i] = valor_criterio_6 - matriz_decisao.iloc[0, i]
        valor_criterio_7 = matriz_decisao.iloc[0, 6]
        for i in range(7, len(segunda_matriz.columns)):
            segunda_matriz.iloc[6, i] = valor_criterio_7 - matriz_decisao.iloc[0, i]
        valor_criterio_8 = matriz_decisao.iloc[0, 7]
        for i in range(8, len(segunda_matriz.columns)):
            segunda_matriz.iloc[7, i] = valor_criterio_8 - matriz_decisao.iloc[0, i]
        valor_criterio_9 = matriz_decisao.iloc[0, 8]
        for i in range(9, len(segunda_matriz.columns)):
            segunda_matriz.iloc[8, i] = valor_criterio_9 - matriz_decisao.iloc[0, i]
        valor_criterio_10 = matriz_decisao.iloc[0, 9]
        for i in range(10, len(segunda_matriz.columns)):
            segunda_matriz.iloc[9, i] = valor_criterio_10 - matriz_decisao.iloc[0, i]
        valor_criterio_11 = matriz_decisao.iloc[0, 10]
        for i in range(11, len(segunda_matriz.columns)):
            segunda_matriz.iloc[10, i] = valor_criterio_11 - matriz_decisao.iloc[0, i]
        valor_criterio_12 = matriz_decisao.iloc[0, 11]
        for i in range(12, len(segunda_matriz.columns)):
            segunda_matriz.iloc[11, i] = valor_criterio_12 - matriz_decisao.iloc[0, i]
        valor_criterio_13 = matriz_decisao.iloc[0, 12]
        for i in range(13, len(segunda_matriz.columns)):
            segunda_matriz.iloc[12, i] = valor_criterio_13 - matriz_decisao.iloc[0, i]
        valor_criterio_14 = matriz_decisao.iloc[0, 13]
        for i in range(14, len(segunda_matriz.columns)):
            segunda_matriz.iloc[13, i] = valor_criterio_14 - matriz_decisao.iloc[0, i]
        valor_criterio_15 = matriz_decisao.iloc[0, 14]
        for i in range(15, len(segunda_matriz.columns)):
            segunda_matriz.iloc[14, i] = valor_criterio_15 - matriz_decisao.iloc[0, i]
    if num_critérios == 16:
        valor_criterio_2 = matriz_decisao.iloc[0, 1]
        for i in range(2, len(segunda_matriz.columns)):
            segunda_matriz.iloc[1, i] = valor_criterio_2 - matriz_decisao.iloc[0, i]
        valor_criterio_3 = matriz_decisao.iloc[0, 2]
        for i in range(3, len(segunda_matriz.columns)):
            segunda_matriz.iloc[2, i] = valor_criterio_3 - matriz_decisao.iloc[0, i]
        valor_criterio_4 = matriz_decisao.iloc[0, 3]
        for i in range(4, len(segunda_matriz.columns)):
            segunda_matriz.iloc[3, i] = valor_criterio_4 - matriz_decisao.iloc[0, i]
        valor_criterio_5 = matriz_decisao.iloc[0, 4]
        for i in range(5, len(segunda_matriz.columns)):
            segunda_matriz.iloc[4, i] = valor_criterio_5 - matriz_decisao.iloc[0, i]
        valor_criterio_6 = matriz_decisao.iloc[0, 5]
        for i in range(6, len(segunda_matriz.columns)):
            segunda_matriz.iloc[5, i] = valor_criterio_6 - matriz_decisao.iloc[0, i]
        valor_criterio_7 = matriz_decisao.iloc[0, 6]
        for i in range(7, len(segunda_matriz.columns)):
            segunda_matriz.iloc[6, i] = valor_criterio_7 - matriz_decisao.iloc[0, i]
        valor_criterio_8 = matriz_decisao.iloc[0, 7]
        for i in range(8, len(segunda_matriz.columns)):
            segunda_matriz.iloc[7, i] = valor_criterio_8 - matriz_decisao.iloc[0, i]
        valor_criterio_9 = matriz_decisao.iloc[0, 8]
        for i in range(9, len(segunda_matriz.columns)):
            segunda_matriz.iloc[8, i] = valor_criterio_9 - matriz_decisao.iloc[0, i]
        valor_criterio_10 = matriz_decisao.iloc[0, 9]
        for i in range(10, len(segunda_matriz.columns)):
            segunda_matriz.iloc[9, i] = valor_criterio_10 - matriz_decisao.iloc[0, i]
        valor_criterio_11 = matriz_decisao.iloc[0, 10]
        for i in range(11, len(segunda_matriz.columns)):
            segunda_matriz.iloc[10, i] = valor_criterio_11 - matriz_decisao.iloc[0, i]
        valor_criterio_12 = matriz_decisao.iloc[0, 11]
        for i in range(12, len(segunda_matriz.columns)):
            segunda_matriz.iloc[11, i] = valor_criterio_12 - matriz_decisao.iloc[0, i]
        valor_criterio_13 = matriz_decisao.iloc[0, 12]
        for i in range(13, len(segunda_matriz.columns)):
            segunda_matriz.iloc[12, i] = valor_criterio_13 - matriz_decisao.iloc[0, i]
        valor_criterio_14 = matriz_decisao.iloc[0, 13]
        for i in range(14, len(segunda_matriz.columns)):
            segunda_matriz.iloc[13, i] = valor_criterio_14 - matriz_decisao.iloc[0, i]
        valor_criterio_15 = matriz_decisao.iloc[0, 14]
        for i in range(15, len(segunda_matriz.columns)):
            segunda_matriz.iloc[14, i] = valor_criterio_15 - matriz_decisao.iloc[0, i]
        valor_criterio_16 = matriz_decisao.iloc[0, 15]
        for i in range(16, len(segunda_matriz.columns)):
            segunda_matriz.iloc[15, i] = valor_criterio_16 - matriz_decisao.iloc[0, i]
    if num_critérios == 17:
        valor_criterio_2 = matriz_decisao.iloc[0, 1]
        for i in range(2, len(segunda_matriz.columns)):
            segunda_matriz.iloc[1, i] = valor_criterio_2 - matriz_decisao.iloc[0, i]
        valor_criterio_3 = matriz_decisao.iloc[0, 2]
        for i in range(3, len(segunda_matriz.columns)):
            segunda_matriz.iloc[2, i] = valor_criterio_3 - matriz_decisao.iloc[0, i]
        valor_criterio_4 = matriz_decisao.iloc[0, 3]
        for i in range(4, len(segunda_matriz.columns)):
            segunda_matriz.iloc[3, i] = valor_criterio_4 - matriz_decisao.iloc[0, i]
        valor_criterio_5 = matriz_decisao.iloc[0, 4]
        for i in range(5, len(segunda_matriz.columns)):
            segunda_matriz.iloc[4, i] = valor_criterio_5 - matriz_decisao.iloc[0, i]
        valor_criterio_6 = matriz_decisao.iloc[0, 5]
        for i in range(6, len(segunda_matriz.columns)):
            segunda_matriz.iloc[5, i] = valor_criterio_6 - matriz_decisao.iloc[0, i]
        valor_criterio_7 = matriz_decisao.iloc[0, 6]
        for i in range(7, len(segunda_matriz.columns)):
            segunda_matriz.iloc[6, i] = valor_criterio_7 - matriz_decisao.iloc[0, i]
        valor_criterio_8 = matriz_decisao.iloc[0, 7]
        for i in range(8, len(segunda_matriz.columns)):
            segunda_matriz.iloc[7, i] = valor_criterio_8 - matriz_decisao.iloc[0, i]
        valor_criterio_9 = matriz_decisao.iloc[0, 8]
        for i in range(9, len(segunda_matriz.columns)):
            segunda_matriz.iloc[8, i] = valor_criterio_9 - matriz_decisao.iloc[0, i]
        valor_criterio_10 = matriz_decisao.iloc[0, 9]
        for i in range(10, len(segunda_matriz.columns)):
            segunda_matriz.iloc[9, i] = valor_criterio_10 - matriz_decisao.iloc[0, i]
        valor_criterio_11 = matriz_decisao.iloc[0, 10]
        for i in range(11, len(segunda_matriz.columns)):
            segunda_matriz.iloc[10, i] = valor_criterio_11 - matriz_decisao.iloc[0, i]
        valor_criterio_12 = matriz_decisao.iloc[0, 11]
        for i in range(12, len(segunda_matriz.columns)):
            segunda_matriz.iloc[11, i] = valor_criterio_12 - matriz_decisao.iloc[0, i]
        valor_criterio_13 = matriz_decisao.iloc[0, 12]
        for i in range(13, len(segunda_matriz.columns)):
            segunda_matriz.iloc[12, i] = valor_criterio_13 - matriz_decisao.iloc[0, i]
        valor_criterio_14 = matriz_decisao.iloc[0, 13]
        for i in range(14, len(segunda_matriz.columns)):
            segunda_matriz.iloc[13, i] = valor_criterio_14 - matriz_decisao.iloc[0, i]
        valor_criterio_15 = matriz_decisao.iloc[0, 14]
        for i in range(15, len(segunda_matriz.columns)):
            segunda_matriz.iloc[14, i] = valor_criterio_15 - matriz_decisao.iloc[0, i]
        valor_criterio_16 = matriz_decisao.iloc[0, 15]
        for i in range(16, len(segunda_matriz.columns)):
            segunda_matriz.iloc[15, i] = valor_criterio_16 - matriz_decisao.iloc[0, i]
        valor_criterio_17 = matriz_decisao.iloc[0, 16]
        for i in range(17, len(segunda_matriz.columns)):
            segunda_matriz.iloc[16, i] = valor_criterio_17 - matriz_decisao.iloc[0, i]
    if num_critérios == 18:
        valor_criterio_2 = matriz_decisao.iloc[0, 1]
        for i in range(2, len(segunda_matriz.columns)):
            segunda_matriz.iloc[1, i] = valor_criterio_2 - matriz_decisao.iloc[0, i]
        valor_criterio_3 = matriz_decisao.iloc[0, 2]
        for i in range(3, len(segunda_matriz.columns)):
            segunda_matriz.iloc[2, i] = valor_criterio_3 - matriz_decisao.iloc[0, i]
        valor_criterio_4 = matriz_decisao.iloc[0, 3]
        for i in range(4, len(segunda_matriz.columns)):
            segunda_matriz.iloc[3, i] = valor_criterio_4 - matriz_decisao.iloc[0, i]
        valor_criterio_5 = matriz_decisao.iloc[0, 4]
        for i in range(5, len(segunda_matriz.columns)):
            segunda_matriz.iloc[4, i] = valor_criterio_5 - matriz_decisao.iloc[0, i]
        valor_criterio_6 = matriz_decisao.iloc[0, 5]
        for i in range(6, len(segunda_matriz.columns)):
            segunda_matriz.iloc[5, i] = valor_criterio_6 - matriz_decisao.iloc[0, i]
        valor_criterio_7 = matriz_decisao.iloc[0, 6]
        for i in range(7, len(segunda_matriz.columns)):
            segunda_matriz.iloc[6, i] = valor_criterio_7 - matriz_decisao.iloc[0, i]
        valor_criterio_8 = matriz_decisao.iloc[0, 7]
        for i in range(8, len(segunda_matriz.columns)):
            segunda_matriz.iloc[7, i] = valor_criterio_8 - matriz_decisao.iloc[0, i]
        valor_criterio_9 = matriz_decisao.iloc[0, 8]
        for i in range(9, len(segunda_matriz.columns)):
            segunda_matriz.iloc[8, i] = valor_criterio_9 - matriz_decisao.iloc[0, i]
        valor_criterio_10 = matriz_decisao.iloc[0, 9]
        for i in range(10, len(segunda_matriz.columns)):
            segunda_matriz.iloc[9, i] = valor_criterio_10 - matriz_decisao.iloc[0, i]
        valor_criterio_11 = matriz_decisao.iloc[0, 10]
        for i in range(11, len(segunda_matriz.columns)):
            segunda_matriz.iloc[10, i] = valor_criterio_11 - matriz_decisao.iloc[0, i]
        valor_criterio_12 = matriz_decisao.iloc[0, 11]
        for i in range(12, len(segunda_matriz.columns)):
            segunda_matriz.iloc[11, i] = valor_criterio_12 - matriz_decisao.iloc[0, i]
        valor_criterio_13 = matriz_decisao.iloc[0, 12]
        for i in range(13, len(segunda_matriz.columns)):
            segunda_matriz.iloc[12, i] = valor_criterio_13 - matriz_decisao.iloc[0, i]
        valor_criterio_14 = matriz_decisao.iloc[0, 13]
        for i in range(14, len(segunda_matriz.columns)):
            segunda_matriz.iloc[13, i] = valor_criterio_14 - matriz_decisao.iloc[0, i]
        valor_criterio_15 = matriz_decisao.iloc[0, 14]
        for i in range(15, len(segunda_matriz.columns)):
            segunda_matriz.iloc[14, i] = valor_criterio_15 - matriz_decisao.iloc[0, i]
        valor_criterio_16 = matriz_decisao.iloc[0, 15]
        for i in range(16, len(segunda_matriz.columns)):
            segunda_matriz.iloc[15, i] = valor_criterio_16 - matriz_decisao.iloc[0, i]
        valor_criterio_17 = matriz_decisao.iloc[0, 16]
        for i in range(17, len(segunda_matriz.columns)):
            segunda_matriz.iloc[16, i] = valor_criterio_17 - matriz_decisao.iloc[0, i]
        valor_criterio_18 = matriz_decisao.iloc[0, 17]
        for i in range(18, len(segunda_matriz.columns)):
            segunda_matriz.iloc[17, i] = valor_criterio_18 - matriz_decisao.iloc[0, i]
    if num_critérios == 19:
        valor_criterio_2 = matriz_decisao.iloc[0, 1]
        for i in range(2, len(segunda_matriz.columns)):
            segunda_matriz.iloc[1, i] = valor_criterio_2 - matriz_decisao.iloc[0, i]
        valor_criterio_3 = matriz_decisao.iloc[0, 2]
        for i in range(3, len(segunda_matriz.columns)):
            segunda_matriz.iloc[2, i] = valor_criterio_3 - matriz_decisao.iloc[0, i]
        valor_criterio_4 = matriz_decisao.iloc[0, 3]
        for i in range(4, len(segunda_matriz.columns)):
            segunda_matriz.iloc[3, i] = valor_criterio_4 - matriz_decisao.iloc[0, i]
        valor_criterio_5 = matriz_decisao.iloc[0, 4]
        for i in range(5, len(segunda_matriz.columns)):
            segunda_matriz.iloc[4, i] = valor_criterio_5 - matriz_decisao.iloc[0, i]
        valor_criterio_6 = matriz_decisao.iloc[0, 5]
        for i in range(6, len(segunda_matriz.columns)):
            segunda_matriz.iloc[5, i] = valor_criterio_6 - matriz_decisao.iloc[0, i]
        valor_criterio_7 = matriz_decisao.iloc[0, 6]
        for i in range(7, len(segunda_matriz.columns)):
            segunda_matriz.iloc[6, i] = valor_criterio_7 - matriz_decisao.iloc[0, i]
        valor_criterio_8 = matriz_decisao.iloc[0, 7]
        for i in range(8, len(segunda_matriz.columns)):
            segunda_matriz.iloc[7, i] = valor_criterio_8 - matriz_decisao.iloc[0, i]
        valor_criterio_9 = matriz_decisao.iloc[0, 8]
        for i in range(9, len(segunda_matriz.columns)):
            segunda_matriz.iloc[8, i] = valor_criterio_9 - matriz_decisao.iloc[0, i]
        valor_criterio_10 = matriz_decisao.iloc[0, 9]
        for i in range(10, len(segunda_matriz.columns)):
            segunda_matriz.iloc[9, i] = valor_criterio_10 - matriz_decisao.iloc[0, i]
        valor_criterio_11 = matriz_decisao.iloc[0, 10]
        for i in range(11, len(segunda_matriz.columns)):
            segunda_matriz.iloc[10, i] = valor_criterio_11 - matriz_decisao.iloc[0, i]
        valor_criterio_12 = matriz_decisao.iloc[0, 11]
        for i in range(12, len(segunda_matriz.columns)):
            segunda_matriz.iloc[11, i] = valor_criterio_12 - matriz_decisao.iloc[0, i]
        valor_criterio_13 = matriz_decisao.iloc[0, 12]
        for i in range(13, len(segunda_matriz.columns)):
            segunda_matriz.iloc[12, i] = valor_criterio_13 - matriz_decisao.iloc[0, i]
        valor_criterio_14 = matriz_decisao.iloc[0, 13]
        for i in range(14, len(segunda_matriz.columns)):
            segunda_matriz.iloc[13, i] = valor_criterio_14 - matriz_decisao.iloc[0, i]
        valor_criterio_15 = matriz_decisao.iloc[0, 14]
        for i in range(15, len(segunda_matriz.columns)):
            segunda_matriz.iloc[14, i] = valor_criterio_15 - matriz_decisao.iloc[0, i]
        valor_criterio_16 = matriz_decisao.iloc[0, 15]
        for i in range(16, len(segunda_matriz.columns)):
            segunda_matriz.iloc[15, i] = valor_criterio_16 - matriz_decisao.iloc[0, i]
        valor_criterio_17 = matriz_decisao.iloc[0, 16]
        for i in range(17, len(segunda_matriz.columns)):
            segunda_matriz.iloc[16, i] = valor_criterio_17 - matriz_decisao.iloc[0, i]
        valor_criterio_18 = matriz_decisao.iloc[0, 17]
        for i in range(18, len(segunda_matriz.columns)):
            segunda_matriz.iloc[17, i] = valor_criterio_18 - matriz_decisao.iloc[0, i]
        valor_criterio_19 = matriz_decisao.iloc[0, 18]
        for i in range(19, len(segunda_matriz.columns)):
            segunda_matriz.iloc[18, i] = valor_criterio_19 - matriz_decisao.iloc[0, i]
    if num_critérios == 20:
        valor_criterio_2 = matriz_decisao.iloc[0, 1]
        for i in range(2, len(segunda_matriz.columns)):
            segunda_matriz.iloc[1, i] = valor_criterio_2 - matriz_decisao.iloc[0, i]
        valor_criterio_3 = matriz_decisao.iloc[0, 2]
        for i in range(3, len(segunda_matriz.columns)):
            segunda_matriz.iloc[2, i] = valor_criterio_3 - matriz_decisao.iloc[0, i]
        valor_criterio_4 = matriz_decisao.iloc[0, 3]
        for i in range(4, len(segunda_matriz.columns)):
            segunda_matriz.iloc[3, i] = valor_criterio_4 - matriz_decisao.iloc[0, i]
        valor_criterio_5 = matriz_decisao.iloc[0, 4]
        for i in range(5, len(segunda_matriz.columns)):
            segunda_matriz.iloc[4, i] = valor_criterio_5 - matriz_decisao.iloc[0, i]
        valor_criterio_6 = matriz_decisao.iloc[0, 5]
        for i in range(6, len(segunda_matriz.columns)):
            segunda_matriz.iloc[5, i] = valor_criterio_6 - matriz_decisao.iloc[0, i]
        valor_criterio_7 = matriz_decisao.iloc[0, 6]
        for i in range(7, len(segunda_matriz.columns)):
            segunda_matriz.iloc[6, i] = valor_criterio_7 - matriz_decisao.iloc[0, i]
        valor_criterio_8 = matriz_decisao.iloc[0, 7]
        for i in range(8, len(segunda_matriz.columns)):
            segunda_matriz.iloc[7, i] = valor_criterio_8 - matriz_decisao.iloc[0, i]
        valor_criterio_9 = matriz_decisao.iloc[0, 8]
        for i in range(9, len(segunda_matriz.columns)):
            segunda_matriz.iloc[8, i] = valor_criterio_9 - matriz_decisao.iloc[0, i]
        valor_criterio_10 = matriz_decisao.iloc[0, 9]
        for i in range(10, len(segunda_matriz.columns)):
            segunda_matriz.iloc[9, i] = valor_criterio_10 - matriz_decisao.iloc[0, i]
        valor_criterio_11 = matriz_decisao.iloc[0, 10]
        for i in range(11, len(segunda_matriz.columns)):
            segunda_matriz.iloc[10, i] = valor_criterio_11 - matriz_decisao.iloc[0, i]
        valor_criterio_12 = matriz_decisao.iloc[0, 11]
        for i in range(12, len(segunda_matriz.columns)):
            segunda_matriz.iloc[11, i] = valor_criterio_12 - matriz_decisao.iloc[0, i]
        valor_criterio_13 = matriz_decisao.iloc[0, 12]
        for i in range(13, len(segunda_matriz.columns)):
            segunda_matriz.iloc[12, i] = valor_criterio_13 - matriz_decisao.iloc[0, i]
        valor_criterio_14 = matriz_decisao.iloc[0, 13]
        for i in range(14, len(segunda_matriz.columns)):
            segunda_matriz.iloc[13, i] = valor_criterio_14 - matriz_decisao.iloc[0, i]
        valor_criterio_15 = matriz_decisao.iloc[0, 14]
        for i in range(15, len(segunda_matriz.columns)):
            segunda_matriz.iloc[14, i] = valor_criterio_15 - matriz_decisao.iloc[0, i]
        valor_criterio_16 = matriz_decisao.iloc[0, 15]
        for i in range(16, len(segunda_matriz.columns)):
            segunda_matriz.iloc[15, i] = valor_criterio_16 - matriz_decisao.iloc[0, i]
        valor_criterio_17 = matriz_decisao.iloc[0, 16]
        for i in range(17, len(segunda_matriz.columns)):
            segunda_matriz.iloc[16, i] = valor_criterio_17 - matriz_decisao.iloc[0, i]
        valor_criterio_18 = matriz_decisao.iloc[0, 17]
        for i in range(18, len(segunda_matriz.columns)):
            segunda_matriz.iloc[17, i] = valor_criterio_18 - matriz_decisao.iloc[0, i]
        valor_criterio_19 = matriz_decisao.iloc[0, 18]
        for i in range(19, len(segunda_matriz.columns)):
            segunda_matriz.iloc[18, i] = valor_criterio_19 - matriz_decisao.iloc[0, i]
        valor_criterio_20 = matriz_decisao.iloc[0, 19]
        for i in range(20, len(segunda_matriz.columns)):
            segunda_matriz.iloc[19, i] = valor_criterio_20 - matriz_decisao.iloc[0, i]

    return segunda_matriz
        
def gerar_terceira_matriz(segunda_matriz):
    terceira_matriz = segunda_matriz.copy()
    num_critérios = st.session_state.num_critérios
    
 
    if num_critérios == 3:
        for i in range(2, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[1, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[1, i] = item["valor"]

                    c1 = terceira_matriz.iloc[0, 1]
                    inverso_c1 = 1 / c1
                    terceira_matriz.iloc[1, 0] = inverso_c1
                    c2 = terceira_matriz.iloc[0, 2]
                    inverso_c2 = 1 / c2
                    terceira_matriz.iloc[2, 0] = inverso_c2
                    c1_2 = terceira_matriz.iloc[1, 2]
                    inverso_c1_2 = 1 / c1_2
                    terceira_matriz.iloc[2, 1] = inverso_c1_2


        for i in range(3, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[2, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[2, i] = item["valor"]
                    
                    

        for i in range(4, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[3, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[3, i] = item["valor"]
                    


    if num_critérios == 4:
        for i in range(2, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[1, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[1, i] = item["valor"]
                    c1 = terceira_matriz.iloc[0, 1]
                    c2 = terceira_matriz.iloc[0, 2]
                    c3 = terceira_matriz.iloc[0, 3]
                
                    # Calcular os inversos
                    inverso_c1 = 1 / c1
                    inverso_c2 = 1 / c2
                    inverso_c3 = 1 / c3

                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[1, 0] = inverso_c1
                    terceira_matriz.iloc[2, 0] = inverso_c2
                    terceira_matriz.iloc[3, 0] = inverso_c3
                    
        for i in range(3, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[2, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[2, i] = item["valor"]
                     #Critério 2
                    c1_2 = terceira_matriz.iloc[1, 2]
                    c2_2 = terceira_matriz.iloc[1, 3]
                
                    # Calcular os inversos
                    inverso_c1_2 = 1 / c1_2
                    inverso_c2_2 = 1 / c2_2
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[2, 1] = inverso_c1_2
                    terceira_matriz.iloc[3, 1] = inverso_c2_2
                          #Critério 3
                    c1_3 = terceira_matriz.iloc[2, 3]
                    # Calcular os inversos
                    inverso_c1_3 = 1 / c1_3
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[3, 2] = inverso_c1_3
                

        for i in range(4, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[3, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[3, i] = item["valor"]
               

    if num_critérios == 5:
        for i in range(2, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[1, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[1, i] = item["valor"]
                    
        for i in range(3, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[2, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[2, i] = item["valor"]

        for i in range(4, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[3, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[3, i] = item["valor"]

                    #Inverter a Terceira Matriz
                    #Critério 1
                    c1 = terceira_matriz.iloc[0, 1]
                    c2 = terceira_matriz.iloc[0, 2]
                    c3 = terceira_matriz.iloc[0, 3]
                    c4 = terceira_matriz.iloc[0, 4]
                
                    # Calcular os inversos
                    inverso_c1 = 1 / c1
                    inverso_c2 = 1 / c2
                    inverso_c3 = 1 / c3
                    inverso_c4 = 1 / c4

                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[1, 0] = inverso_c1
                    terceira_matriz.iloc[2, 0] = inverso_c2
                    terceira_matriz.iloc[3, 0] = inverso_c3
                    terceira_matriz.iloc[4, 0] = inverso_c4
                
                    #Critério 2
                    c1_2 = terceira_matriz.iloc[1, 2]
                    c2_2 = terceira_matriz.iloc[1, 3]
                    c3_2 = terceira_matriz.iloc[1, 4]
                
                    # Calcular os inversos
                    inverso_c1_2 = 1 / c1_2
                    inverso_c2_2 = 1 / c2_2
                    inverso_c3_2 = 1 / c3_2
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[2, 1] = inverso_c1_2
                    terceira_matriz.iloc[3, 1] = inverso_c2_2
                    terceira_matriz.iloc[4, 1] = inverso_c3_2
                
                    #Critério 3
                    c1_3 = terceira_matriz.iloc[2, 3]
                    c2_3 = terceira_matriz.iloc[2, 4]

                    # Calcular os inversos
                    inverso_c1_3 = 1 / c1_3
                    inverso_c2_3 = 1 / c2_3
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[3, 2] = inverso_c1_3
                    terceira_matriz.iloc[4, 2] = inverso_c2_3

                #Critério 4
                    c1_4 = terceira_matriz.iloc[3, 4]
                
                    # Calcular os inversos
                    inverso_c1_4 = 1 / c1_4
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[4, 3] = inverso_c1_4

            
    if num_critérios == 6:
        for i in range(2, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[1, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[1, i] = item["valor"]
                     

        for i in range(3, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[2, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[2, i] = item["valor"]
                     

        for i in range(4, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[3, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[3, i] = item["valor"]
                     

        for i in range(5, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[4, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[4, i] = item["valor"]

                    #Inverter a Terceira Matriz
                    #Critério 1
                    c1 = terceira_matriz.iloc[0, 1]
                    c2 = terceira_matriz.iloc[0, 2]
                    c3 = terceira_matriz.iloc[0, 3]
                    c4 = terceira_matriz.iloc[0, 4]
                    c5 = terceira_matriz.iloc[0, 5]
                
                    # Calcular os inversos
                    inverso_c1 = 1 / c1
                    inverso_c2 = 1 / c2
                    inverso_c3 = 1 / c3
                    inverso_c4 = 1 / c4
                    inverso_c5 = 1 / c5

                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[1, 0] = inverso_c1
                    terceira_matriz.iloc[2, 0] = inverso_c2
                    terceira_matriz.iloc[3, 0] = inverso_c3
                    terceira_matriz.iloc[4, 0] = inverso_c4
                    terceira_matriz.iloc[5, 0] = inverso_c5
                
                    #Critério 2
                    c1_2 = terceira_matriz.iloc[1, 2]
                    c2_2 = terceira_matriz.iloc[1, 3]
                    c3_2 = terceira_matriz.iloc[1, 4]
                    c4_2 = terceira_matriz.iloc[1, 5]
                    
                
                    # Calcular os inversos
                    inverso_c1_2 = 1 / c1_2
                    inverso_c2_2 = 1 / c2_2
                    inverso_c3_2 = 1 / c3_2
                    inverso_c4_2 = 1 / c4_2

                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[2, 1] = inverso_c1_2
                    terceira_matriz.iloc[3, 1] = inverso_c2_2
                    terceira_matriz.iloc[4, 1] = inverso_c3_2
                    terceira_matriz.iloc[5, 1] = inverso_c4_2
                
                    #Critério 3
                    c1_3 = terceira_matriz.iloc[2, 3]
                    c2_3 = terceira_matriz.iloc[2, 4]
                    c3_3 = terceira_matriz.iloc[2, 5]

                    # Calcular os inversos
                    inverso_c1_3 = 1 / c1_3
                    inverso_c2_3 = 1 / c2_3
                    inverso_c3_3 = 1 / c3_3
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[3, 2] = inverso_c1_3
                    terceira_matriz.iloc[4, 2] = inverso_c2_3
                    terceira_matriz.iloc[5, 2] = inverso_c3_3

                    #Critério 4
                    c1_4 = terceira_matriz.iloc[3, 4]
                    c2_4 = terceira_matriz.iloc[3, 5]
                
                    # Calcular os inversos
                    inverso_c1_4 = 1 / c1_4
                    inverso_c2_4 = 1 / c2_4
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[4, 3] = inverso_c1_4
                    terceira_matriz.iloc[5, 3] = inverso_c2_4

                    #Critério 5
                    c1_5 = terceira_matriz.iloc[4, 5]
                                    
                    # Calcular os inversos
                    inverso_c1_5 = 1 / c1_5
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[5, 4] = inverso_c1_5

    if num_critérios == 7:
        for i in range(2, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[1, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[1, i] = item["valor"]
                     

        for i in range(3, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[2, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[2, i] = item["valor"]
                     

        for i in range(4, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[3, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[3, i] = item["valor"]
                     

        for i in range(5, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[4, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[4, i] = item["valor"]

        for i in range(6, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[5, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[5, i] = item["valor"]

                    #Inverter a Terceira Matriz
                    #Critério 1
                    c1 = terceira_matriz.iloc[0, 1]
                    c2 = terceira_matriz.iloc[0, 2]
                    c3 = terceira_matriz.iloc[0, 3]
                    c4 = terceira_matriz.iloc[0, 4]
                    c5 = terceira_matriz.iloc[0, 5]
                    c6 = terceira_matriz.iloc[0, 6]
                
                    # Calcular os inversos
                    inverso_c1 = 1 / c1
                    inverso_c2 = 1 / c2
                    inverso_c3 = 1 / c3
                    inverso_c4 = 1 / c4
                    inverso_c5 = 1 / c5
                    inverso_c6 = 1 / c6

                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[1, 0] = inverso_c1
                    terceira_matriz.iloc[2, 0] = inverso_c2
                    terceira_matriz.iloc[3, 0] = inverso_c3
                    terceira_matriz.iloc[4, 0] = inverso_c4
                    terceira_matriz.iloc[5, 0] = inverso_c5
                    terceira_matriz.iloc[6, 0] = inverso_c6
                
                    #Critério 2
                    c1_2 = terceira_matriz.iloc[1, 2]
                    c2_2 = terceira_matriz.iloc[1, 3]
                    c3_2 = terceira_matriz.iloc[1, 4]
                    c4_2 = terceira_matriz.iloc[1, 5]
                    c5_2 = terceira_matriz.iloc[1, 6]
                    
                
                    # Calcular os inversos
                    inverso_c1_2 = 1 / c1_2
                    inverso_c2_2 = 1 / c2_2
                    inverso_c3_2 = 1 / c3_2
                    inverso_c4_2 = 1 / c4_2
                    inverso_c5_2 = 1 / c5_2

                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[2, 1] = inverso_c1_2
                    terceira_matriz.iloc[3, 1] = inverso_c2_2
                    terceira_matriz.iloc[4, 1] = inverso_c3_2
                    terceira_matriz.iloc[5, 1] = inverso_c4_2
                    terceira_matriz.iloc[6, 1] = inverso_c5_2
                
                    #Critério 3
                    c1_3 = terceira_matriz.iloc[2, 3]
                    c2_3 = terceira_matriz.iloc[2, 4]
                    c3_3 = terceira_matriz.iloc[2, 5]
                    c4_3 = terceira_matriz.iloc[2, 6]

                    # Calcular os inversos
                    inverso_c1_3 = 1 / c1_3
                    inverso_c2_3 = 1 / c2_3
                    inverso_c3_3 = 1 / c3_3
                    inverso_c4_3 = 1 / c4_3
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[3, 2] = inverso_c1_3
                    terceira_matriz.iloc[4, 2] = inverso_c2_3
                    terceira_matriz.iloc[5, 2] = inverso_c3_3
                    terceira_matriz.iloc[6, 2] = inverso_c4_3

                    #Critério 4
                    c1_4 = terceira_matriz.iloc[3, 4]
                    c2_4 = terceira_matriz.iloc[3, 5]
                    c3_4 = terceira_matriz.iloc[3, 6]
                
                
                    # Calcular os inversos
                    inverso_c1_4 = 1 / c1_4
                    inverso_c2_4 = 1 / c2_4
                    inverso_c3_4 = 1 / c3_4
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[4, 3] = inverso_c1_4
                    terceira_matriz.iloc[5, 3] = inverso_c2_4
                    terceira_matriz.iloc[6, 3] = inverso_c3_4

                    #Critério 5
                    c1_5 = terceira_matriz.iloc[4, 5]
                    c2_5 = terceira_matriz.iloc[4, 6]
                                    
                    # Calcular os inversos
                    inverso_c1_5 = 1 / c1_5
                    inverso_c2_5 = 1 / c2_5
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[5, 4] = inverso_c1_5
                    terceira_matriz.iloc[6, 4] = inverso_c2_5

                     #Critério 6
                    c1_6 = terceira_matriz.iloc[5, 6]
                                    
                    # Calcular os inversos
                    inverso_c1_6 = 1 / c1_6
                  
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[6, 5] = inverso_c1_6
                   

    if num_critérios == 8:
        for i in range(2, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[1, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[1, i] = item["valor"]
                     

        for i in range(3, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[2, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[2, i] = item["valor"]
                     

        for i in range(4, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[3, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[3, i] = item["valor"]
                     

        for i in range(5, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[4, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[4, i] = item["valor"]

        for i in range(6, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[5, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[5, i] = item["valor"]
        
        for i in range(7, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[6, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[6, i] = item["valor"]

                      #Inverter a Terceira Matriz
                    #Critério 1
                    c1 = terceira_matriz.iloc[0, 1]
                    c2 = terceira_matriz.iloc[0, 2]
                    c3 = terceira_matriz.iloc[0, 3]
                    c4 = terceira_matriz.iloc[0, 4]
                    c5 = terceira_matriz.iloc[0, 5]
                    c6 = terceira_matriz.iloc[0, 6]
                    c7 = terceira_matriz.iloc[0, 7]
                
                    # Calcular os inversos
                    inverso_c1 = 1 / c1
                    inverso_c2 = 1 / c2
                    inverso_c3 = 1 / c3
                    inverso_c4 = 1 / c4
                    inverso_c5 = 1 / c5
                    inverso_c6 = 1 / c6
                    inverso_c7 = 1 / c7

                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[1, 0] = inverso_c1
                    terceira_matriz.iloc[2, 0] = inverso_c2
                    terceira_matriz.iloc[3, 0] = inverso_c3
                    terceira_matriz.iloc[4, 0] = inverso_c4
                    terceira_matriz.iloc[5, 0] = inverso_c5
                    terceira_matriz.iloc[6, 0] = inverso_c6
                    terceira_matriz.iloc[7, 0] = inverso_c7
                
                    #Critério 2
                    c1_2 = terceira_matriz.iloc[1, 2]
                    c2_2 = terceira_matriz.iloc[1, 3]
                    c3_2 = terceira_matriz.iloc[1, 4]
                    c4_2 = terceira_matriz.iloc[1, 5]
                    c5_2 = terceira_matriz.iloc[1, 6]
                    c6_2 = terceira_matriz.iloc[1, 7]
                    
                
                    # Calcular os inversos
                    inverso_c1_2 = 1 / c1_2
                    inverso_c2_2 = 1 / c2_2
                    inverso_c3_2 = 1 / c3_2
                    inverso_c4_2 = 1 / c4_2
                    inverso_c5_2 = 1 / c5_2
                    inverso_c6_2 = 1 / c6_2


                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[2, 1] = inverso_c1_2
                    terceira_matriz.iloc[3, 1] = inverso_c2_2
                    terceira_matriz.iloc[4, 1] = inverso_c3_2
                    terceira_matriz.iloc[5, 1] = inverso_c4_2
                    terceira_matriz.iloc[6, 1] = inverso_c5_2
                    terceira_matriz.iloc[7, 1] = inverso_c6_2
                
                    #Critério 3
                    c1_3 = terceira_matriz.iloc[2, 3]
                    c2_3 = terceira_matriz.iloc[2, 4]
                    c3_3 = terceira_matriz.iloc[2, 5]
                    c4_3 = terceira_matriz.iloc[2, 6]
                    c5_3 = terceira_matriz.iloc[2, 7]

                    # Calcular os inversos
                    inverso_c1_3 = 1 / c1_3
                    inverso_c2_3 = 1 / c2_3
                    inverso_c3_3 = 1 / c3_3
                    inverso_c4_3 = 1 / c4_3
                    inverso_c5_3 = 1 / c5_3
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[3, 2] = inverso_c1_3
                    terceira_matriz.iloc[4, 2] = inverso_c2_3
                    terceira_matriz.iloc[5, 2] = inverso_c3_3
                    terceira_matriz.iloc[6, 2] = inverso_c4_3
                    terceira_matriz.iloc[7, 2] = inverso_c5_3

                    #Critério 4
                    c1_4 = terceira_matriz.iloc[3, 4]
                    c2_4 = terceira_matriz.iloc[3, 5]
                    c3_4 = terceira_matriz.iloc[3, 6]
                    c4_4 = terceira_matriz.iloc[3, 7]
                
                
                    # Calcular os inversos
                    inverso_c1_4 = 1 / c1_4
                    inverso_c2_4 = 1 / c2_4
                    inverso_c3_4 = 1 / c3_4
                    inverso_c4_4 = 1 / c4_4
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[4, 3] = inverso_c1_4
                    terceira_matriz.iloc[5, 3] = inverso_c2_4
                    terceira_matriz.iloc[6, 3] = inverso_c3_4
                    terceira_matriz.iloc[7, 3] = inverso_c4_4

                    #Critério 5
                    c1_5 = terceira_matriz.iloc[4, 5]
                    c2_5 = terceira_matriz.iloc[4, 6]
                    c3_5 = terceira_matriz.iloc[4, 7]
                                    
                    # Calcular os inversos
                    inverso_c1_5 = 1 / c1_5
                    inverso_c2_5 = 1 / c2_5
                    inverso_c3_5 = 1 / c3_5
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[5, 4] = inverso_c1_5
                    terceira_matriz.iloc[6, 4] = inverso_c2_5
                    terceira_matriz.iloc[7, 4] = inverso_c3_5

                     #Critério 6
                    c1_6 = terceira_matriz.iloc[5, 6]
                    c2_6 = terceira_matriz.iloc[5, 7]
                                    
                    # Calcular os inversos
                    inverso_c1_6 = 1 / c1_6
                    inverso_c2_6 = 1 / c2_6
                  
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[6, 5] = inverso_c1_6
                    terceira_matriz.iloc[7, 5] = inverso_c2_6

                       #Critério 7
                    c1_7 = terceira_matriz.iloc[6, 7]
                                    
                    # Calcular os inversos
                    inverso_c1_7 = 1 / c1_7
                   
                  
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[7, 6] = inverso_c1_7


    if num_critérios == 9:
        for i in range(2, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[1, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[1, i] = item["valor"]                     
                                        
        for i in range(3, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[2, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[2, i] = item["valor"]
                     

        for i in range(4, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[3, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[3, i] = item["valor"]
                     

        for i in range(5, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[4, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[4, i] = item["valor"]

        for i in range(6, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[5, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[5, i] = item["valor"]
        
        for i in range(7, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[6, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[6, i] = item["valor"]
        for i in range(8, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[7, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[7, i] = item["valor"]

                     #Inverter a Terceira Matriz
                    #Critério 1
                    c1 = terceira_matriz.iloc[0, 1]
                    c2 = terceira_matriz.iloc[0, 2]
                    c3 = terceira_matriz.iloc[0, 3]
                    c4 = terceira_matriz.iloc[0, 4]
                    c5 = terceira_matriz.iloc[0, 5]
                    c6 = terceira_matriz.iloc[0, 6]
                    c7 = terceira_matriz.iloc[0, 7]
                    c8 = terceira_matriz.iloc[0, 8]
                
                    # Calcular os inversos
                    inverso_c1 = 1 / c1
                    inverso_c2 = 1 / c2
                    inverso_c3 = 1 / c3
                    inverso_c4 = 1 / c4
                    inverso_c5 = 1 / c5
                    inverso_c6 = 1 / c6
                    inverso_c7 = 1 / c7
                    inverso_c8 = 1 / c8

                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[1, 0] = inverso_c1
                    terceira_matriz.iloc[2, 0] = inverso_c2
                    terceira_matriz.iloc[3, 0] = inverso_c3
                    terceira_matriz.iloc[4, 0] = inverso_c4
                    terceira_matriz.iloc[5, 0] = inverso_c5
                    terceira_matriz.iloc[6, 0] = inverso_c6
                    terceira_matriz.iloc[7, 0] = inverso_c7
                    terceira_matriz.iloc[8, 0] = inverso_c8
                
                    #Critério 2
                    c1_2 = terceira_matriz.iloc[1, 2]
                    c2_2 = terceira_matriz.iloc[1, 3]
                    c3_2 = terceira_matriz.iloc[1, 4]
                    c4_2 = terceira_matriz.iloc[1, 5]
                    c5_2 = terceira_matriz.iloc[1, 6]
                    c6_2 = terceira_matriz.iloc[1, 7]
                    c7_2 = terceira_matriz.iloc[1, 8]
                    
                
                    # Calcular os inversos
                    inverso_c1_2 = 1 / c1_2
                    inverso_c2_2 = 1 / c2_2
                    inverso_c3_2 = 1 / c3_2
                    inverso_c4_2 = 1 / c4_2
                    inverso_c5_2 = 1 / c5_2
                    inverso_c6_2 = 1 / c6_2
                    inverso_c7_2 = 1 / c7_2


                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[2, 1] = inverso_c1_2
                    terceira_matriz.iloc[3, 1] = inverso_c2_2
                    terceira_matriz.iloc[4, 1] = inverso_c3_2
                    terceira_matriz.iloc[5, 1] = inverso_c4_2
                    terceira_matriz.iloc[6, 1] = inverso_c5_2
                    terceira_matriz.iloc[7, 1] = inverso_c6_2
                    terceira_matriz.iloc[8, 1] = inverso_c7_2
                    
                
                    #Critério 3
                    c1_3 = terceira_matriz.iloc[2, 3]
                    c2_3 = terceira_matriz.iloc[2, 4]
                    c3_3 = terceira_matriz.iloc[2, 5]
                    c4_3 = terceira_matriz.iloc[2, 6]
                    c5_3 = terceira_matriz.iloc[2, 7]
                    c6_3 = terceira_matriz.iloc[2, 8]

                    # Calcular os inversos
                    inverso_c1_3 = 1 / c1_3
                    inverso_c2_3 = 1 / c2_3
                    inverso_c3_3 = 1 / c3_3
                    inverso_c4_3 = 1 / c4_3
                    inverso_c5_3 = 1 / c5_3
                    inverso_c6_3 = 1 / c6_3
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[3, 2] = inverso_c1_3
                    terceira_matriz.iloc[4, 2] = inverso_c2_3
                    terceira_matriz.iloc[5, 2] = inverso_c3_3
                    terceira_matriz.iloc[6, 2] = inverso_c4_3
                    terceira_matriz.iloc[7, 2] = inverso_c5_3
                    terceira_matriz.iloc[8, 2] = inverso_c6_3

                    #Critério 4
                    c1_4 = terceira_matriz.iloc[3, 4]
                    c2_4 = terceira_matriz.iloc[3, 5]
                    c3_4 = terceira_matriz.iloc[3, 6]
                    c4_4 = terceira_matriz.iloc[3, 7]
                    c5_4 = terceira_matriz.iloc[3, 8]
                
                    # Calcular os inversos
                    inverso_c1_4 = 1 / c1_4
                    inverso_c2_4 = 1 / c2_4
                    inverso_c3_4 = 1 / c3_4
                    inverso_c4_4 = 1 / c4_4
                    inverso_c5_4 = 1 / c5_4
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[4, 3] = inverso_c1_4
                    terceira_matriz.iloc[5, 3] = inverso_c2_4
                    terceira_matriz.iloc[6, 3] = inverso_c3_4
                    terceira_matriz.iloc[7, 3] = inverso_c4_4
                    terceira_matriz.iloc[8, 3] = inverso_c5_4

                    #Critério 5
                    c1_5 = terceira_matriz.iloc[4, 5]
                    c2_5 = terceira_matriz.iloc[4, 6]
                    c3_5 = terceira_matriz.iloc[4, 7]
                    c4_5 = terceira_matriz.iloc[4, 8]
                                    
                    # Calcular os inversos
                    inverso_c1_5 = 1 / c1_5
                    inverso_c2_5 = 1 / c2_5
                    inverso_c3_5 = 1 / c3_5
                    inverso_c4_5 = 1 / c4_5
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[5, 4] = inverso_c1_5
                    terceira_matriz.iloc[6, 4] = inverso_c2_5
                    terceira_matriz.iloc[7, 4] = inverso_c3_5
                    terceira_matriz.iloc[8, 4] = inverso_c4_5


                     #Critério 6
                    c1_6 = terceira_matriz.iloc[5, 6]
                    c2_6 = terceira_matriz.iloc[5, 7]
                    c3_6 = terceira_matriz.iloc[5, 8]
                                    
                    # Calcular os inversos
                    inverso_c1_6 = 1 / c1_6
                    inverso_c2_6 = 1 / c2_6
                    inverso_c3_6 = 1 / c3_6
                  
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[6, 5] = inverso_c1_6
                    terceira_matriz.iloc[7, 5] = inverso_c2_6
                    terceira_matriz.iloc[8, 5] = inverso_c3_6

                       #Critério 7
                    c1_7 = terceira_matriz.iloc[6, 7]
                    c2_7 = terceira_matriz.iloc[6, 8]
                                    
                    # Calcular os inversos
                    inverso_c1_7 = 1 / c1_7
                    inverso_c2_7 = 1 / c2_7
                   
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[7, 6] = inverso_c1_7
                    terceira_matriz.iloc[8, 6] = inverso_c2_7

                    #Critério 8
                    c1_8 = terceira_matriz.iloc[8,7]
                                    
                    # Calcular os inversos
                    inverso_c1_8 = 1 / c1_8
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[7, 8] = inverso_c1_8
                    

    if num_critérios == 10:
        for i in range(2, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[1, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[1, i] = item["valor"]
                     

        for i in range(3, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[2, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[2, i] = item["valor"]
                     

        for i in range(4, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[3, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[3, i] = item["valor"]
                     

        for i in range(5, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[4, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[4, i] = item["valor"]

        for i in range(6, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[5, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[5, i] = item["valor"]
        
        for i in range(7, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[6, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[6, i] = item["valor"]
        for i in range(8, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[7, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[7, i] = item["valor"]
        for i in range(9, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[8, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[8, i] = item["valor"]

                    #Inverter a Terceira Matriz
                    #Critério 1
                    c1 = terceira_matriz.iloc[0, 1]
                    c2 = terceira_matriz.iloc[0, 2]
                    c3 = terceira_matriz.iloc[0, 3]
                    c4 = terceira_matriz.iloc[0, 4]
                    c5 = terceira_matriz.iloc[0, 5]
                    c6 = terceira_matriz.iloc[0, 6]
                    c7 = terceira_matriz.iloc[0, 7]
                    c8 = terceira_matriz.iloc[0, 8]
                    c9 = terceira_matriz.iloc[0, 9]
                
                    # Calcular os inversos
                    inverso_c1 = 1 / c1
                    inverso_c2 = 1 / c2
                    inverso_c3 = 1 / c3
                    inverso_c4 = 1 / c4
                    inverso_c5 = 1 / c5
                    inverso_c6 = 1 / c6
                    inverso_c7 = 1 / c7
                    inverso_c8 = 1 / c8
                    inverso_c9 = 1 / c9

                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[1, 0] = inverso_c1
                    terceira_matriz.iloc[2, 0] = inverso_c2
                    terceira_matriz.iloc[3, 0] = inverso_c3
                    terceira_matriz.iloc[4, 0] = inverso_c4
                    terceira_matriz.iloc[5, 0] = inverso_c5
                    terceira_matriz.iloc[6, 0] = inverso_c6
                    terceira_matriz.iloc[7, 0] = inverso_c7
                    terceira_matriz.iloc[8, 0] = inverso_c8
                    terceira_matriz.iloc[9, 0] = inverso_c9
                
                    #Critério 2
                    c1_2 = terceira_matriz.iloc[1, 2]
                    c2_2 = terceira_matriz.iloc[1, 3]
                    c3_2 = terceira_matriz.iloc[1, 4]
                    c4_2 = terceira_matriz.iloc[1, 5]
                    c5_2 = terceira_matriz.iloc[1, 6]
                    c6_2 = terceira_matriz.iloc[1, 7]
                    c7_2 = terceira_matriz.iloc[1, 8]
                    c8_2 = terceira_matriz.iloc[1, 9]
                    
                
                    # Calcular os inversos
                    inverso_c1_2 = 1 / c1_2
                    inverso_c2_2 = 1 / c2_2
                    inverso_c3_2 = 1 / c3_2
                    inverso_c4_2 = 1 / c4_2
                    inverso_c5_2 = 1 / c5_2
                    inverso_c6_2 = 1 / c6_2
                    inverso_c7_2 = 1 / c7_2
                    inverso_c8_2 = 1 / c8_2


                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[2, 1] = inverso_c1_2
                    terceira_matriz.iloc[3, 1] = inverso_c2_2
                    terceira_matriz.iloc[4, 1] = inverso_c3_2
                    terceira_matriz.iloc[5, 1] = inverso_c4_2
                    terceira_matriz.iloc[6, 1] = inverso_c5_2
                    terceira_matriz.iloc[7, 1] = inverso_c6_2
                    terceira_matriz.iloc[8, 1] = inverso_c7_2
                    terceira_matriz.iloc[8, 1] = inverso_c8_2
                    
                
                    #Critério 3
                    c1_3 = terceira_matriz.iloc[2, 3]
                    c2_3 = terceira_matriz.iloc[2, 4]
                    c3_3 = terceira_matriz.iloc[2, 5]
                    c4_3 = terceira_matriz.iloc[2, 6]
                    c5_3 = terceira_matriz.iloc[2, 7]
                    c6_3 = terceira_matriz.iloc[2, 8]
                    c7_3 = terceira_matriz.iloc[2, 9]

                    # Calcular os inversos
                    inverso_c1_3 = 1 / c1_3
                    inverso_c2_3 = 1 / c2_3
                    inverso_c3_3 = 1 / c3_3
                    inverso_c4_3 = 1 / c4_3
                    inverso_c5_3 = 1 / c5_3
                    inverso_c6_3 = 1 / c6_3
                    inverso_c7_3 = 1 / c7_3
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[3, 2] = inverso_c1_3
                    terceira_matriz.iloc[4, 2] = inverso_c2_3
                    terceira_matriz.iloc[5, 2] = inverso_c3_3
                    terceira_matriz.iloc[6, 2] = inverso_c4_3
                    terceira_matriz.iloc[7, 2] = inverso_c5_3
                    terceira_matriz.iloc[8, 2] = inverso_c6_3
                    terceira_matriz.iloc[9, 2] = inverso_c7_3

                    #Critério 4
                    c1_4 = terceira_matriz.iloc[3, 4]
                    c2_4 = terceira_matriz.iloc[3, 5]
                    c3_4 = terceira_matriz.iloc[3, 6]
                    c4_4 = terceira_matriz.iloc[3, 7]
                    c5_4 = terceira_matriz.iloc[3, 8]
                    c6_4 = terceira_matriz.iloc[3, 9]
                
                    # Calcular os inversos
                    inverso_c1_4 = 1 / c1_4
                    inverso_c2_4 = 1 / c2_4
                    inverso_c3_4 = 1 / c3_4
                    inverso_c4_4 = 1 / c4_4
                    inverso_c5_4 = 1 / c5_4
                    inverso_c6_4 = 1 / c6_4
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[4, 3] = inverso_c1_4
                    terceira_matriz.iloc[5, 3] = inverso_c2_4
                    terceira_matriz.iloc[6, 3] = inverso_c3_4
                    terceira_matriz.iloc[7, 3] = inverso_c4_4
                    terceira_matriz.iloc[8, 3] = inverso_c5_4
                    terceira_matriz.iloc[9, 3] = inverso_c6_4


                    #Critério 5
                    c1_5 = terceira_matriz.iloc[4, 5]
                    c2_5 = terceira_matriz.iloc[4, 6]
                    c3_5 = terceira_matriz.iloc[4, 7]
                    c4_5 = terceira_matriz.iloc[4, 8]
                    c5_5 = terceira_matriz.iloc[4, 9]
                                    
                    # Calcular os inversos
                    inverso_c1_5 = 1 / c1_5
                    inverso_c2_5 = 1 / c2_5
                    inverso_c3_5 = 1 / c3_5
                    inverso_c4_5 = 1 / c4_5
                    inverso_c5_5 = 1 / c5_5
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[5, 4] = inverso_c1_5
                    terceira_matriz.iloc[6, 4] = inverso_c2_5
                    terceira_matriz.iloc[7, 4] = inverso_c3_5
                    terceira_matriz.iloc[8, 4] = inverso_c4_5
                    terceira_matriz.iloc[9, 4] = inverso_c5_5


                     #Critério 6
                    c1_6 = terceira_matriz.iloc[5, 6]
                    c2_6 = terceira_matriz.iloc[5, 7]
                    c3_6 = terceira_matriz.iloc[5, 8]
                    c4_6 = terceira_matriz.iloc[5, 9]
                                    
                    # Calcular os inversos
                    inverso_c1_6 = 1 / c1_6
                    inverso_c2_6 = 1 / c2_6
                    inverso_c3_6 = 1 / c3_6
                    inverso_c4_6 = 1 / c4_6
                  
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[6, 5] = inverso_c1_6
                    terceira_matriz.iloc[7, 5] = inverso_c2_6
                    terceira_matriz.iloc[8, 5] = inverso_c3_6
                    terceira_matriz.iloc[9, 5] = inverso_c4_6

                       #Critério 7
                    c1_7 = terceira_matriz.iloc[6, 7]
                    c2_7 = terceira_matriz.iloc[6, 8]
                    c3_7 = terceira_matriz.iloc[6, 9]
                                    
                    # Calcular os inversos
                    inverso_c1_7 = 1 / c1_7
                    inverso_c2_7 = 1 / c2_7
                    inverso_c3_7 = 1 / c3_7
                   
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[7, 6] = inverso_c1_7
                    terceira_matriz.iloc[8, 6] = inverso_c2_7
                    terceira_matriz.iloc[9, 6] = inverso_c3_7

                    #Critério 8
                    c1_8 = terceira_matriz.iloc[7,8]
                    c2_8 = terceira_matriz.iloc[7,9]
                                    
                    # Calcular os inversos
                    inverso_c1_8 = 1 / c1_8
                    inverso_c2_8 = 1 / c2_8
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[8, 7] = inverso_c1_8
                    terceira_matriz.iloc[9, 7] = inverso_c2_8

                     #Critério 9
                    c1_9 = terceira_matriz.iloc[8,9]
                                    
                    # Calcular os inversos
                    inverso_c1_9 = 1 / c1_9
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[9, 8] = inverso_c1_8



    if num_critérios == 11:
        for i in range(2, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[1, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[1, i] = item["valor"]
                     

        for i in range(3, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[2, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[2, i] = item["valor"]
                     

        for i in range(4, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[3, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[3, i] = item["valor"]
                     

        for i in range(5, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[4, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[4, i] = item["valor"]

        for i in range(6, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[5, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[5, i] = item["valor"]
        
        for i in range(7, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[6, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[6, i] = item["valor"]
        for i in range(8, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[7, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[7, i] = item["valor"]
        for i in range(9, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[8, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[8, i] = item["valor"]
        for i in range(10, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[9, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[9, i] = item["valor"]

                    #Inverter a Terceira Matriz
                    #Critério 1
                    c1 = terceira_matriz.iloc[0, 1]
                    c2 = terceira_matriz.iloc[0, 2]
                    c3 = terceira_matriz.iloc[0, 3]
                    c4 = terceira_matriz.iloc[0, 4]
                    c5 = terceira_matriz.iloc[0, 5]
                    c6 = terceira_matriz.iloc[0, 6]
                    c7 = terceira_matriz.iloc[0, 7]
                    c8 = terceira_matriz.iloc[0, 8]
                    c9 = terceira_matriz.iloc[0, 9]
                    c10 = terceira_matriz.iloc[0, 10]
                
                    # Calcular os inversos
                    inverso_c1 = 1 / c1
                    inverso_c2 = 1 / c2
                    inverso_c3 = 1 / c3
                    inverso_c4 = 1 / c4
                    inverso_c5 = 1 / c5
                    inverso_c6 = 1 / c6
                    inverso_c7 = 1 / c7
                    inverso_c8 = 1 / c8
                    inverso_c9 = 1 / c9
                    inverso_c10 = 1 / c10

                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[1, 0] = inverso_c1
                    terceira_matriz.iloc[2, 0] = inverso_c2
                    terceira_matriz.iloc[3, 0] = inverso_c3
                    terceira_matriz.iloc[4, 0] = inverso_c4
                    terceira_matriz.iloc[5, 0] = inverso_c5
                    terceira_matriz.iloc[6, 0] = inverso_c6
                    terceira_matriz.iloc[7, 0] = inverso_c7
                    terceira_matriz.iloc[8, 0] = inverso_c8
                    terceira_matriz.iloc[9, 0] = inverso_c9
                    terceira_matriz.iloc[10, 0] = inverso_c10
                
                    #Critério 2
                    c1_2 = terceira_matriz.iloc[1, 2]
                    c2_2 = terceira_matriz.iloc[1, 3]
                    c3_2 = terceira_matriz.iloc[1, 4]
                    c4_2 = terceira_matriz.iloc[1, 5]
                    c5_2 = terceira_matriz.iloc[1, 6]
                    c6_2 = terceira_matriz.iloc[1, 7]
                    c7_2 = terceira_matriz.iloc[1, 8]
                    c8_2 = terceira_matriz.iloc[1, 9]
                    c9_2 = terceira_matriz.iloc[1, 10]
                    
                
                    # Calcular os inversos
                    inverso_c1_2 = 1 / c1_2
                    inverso_c2_2 = 1 / c2_2
                    inverso_c3_2 = 1 / c3_2
                    inverso_c4_2 = 1 / c4_2
                    inverso_c5_2 = 1 / c5_2
                    inverso_c6_2 = 1 / c6_2
                    inverso_c7_2 = 1 / c7_2
                    inverso_c8_2 = 1 / c8_2
                    inverso_c9_2 = 1 / c9_2



                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[2, 1] = inverso_c1_2
                    terceira_matriz.iloc[3, 1] = inverso_c2_2
                    terceira_matriz.iloc[4, 1] = inverso_c3_2
                    terceira_matriz.iloc[5, 1] = inverso_c4_2
                    terceira_matriz.iloc[6, 1] = inverso_c5_2
                    terceira_matriz.iloc[7, 1] = inverso_c6_2
                    terceira_matriz.iloc[8, 1] = inverso_c7_2
                    terceira_matriz.iloc[9, 1] = inverso_c8_2
                    terceira_matriz.iloc[10, 1] = inverso_c9_2
                    
                
                    #Critério 3
                    c1_3 = terceira_matriz.iloc[2, 3]
                    c2_3 = terceira_matriz.iloc[2, 4]
                    c3_3 = terceira_matriz.iloc[2, 5]
                    c4_3 = terceira_matriz.iloc[2, 6]
                    c5_3 = terceira_matriz.iloc[2, 7]
                    c6_3 = terceira_matriz.iloc[2, 8]
                    c7_3 = terceira_matriz.iloc[2, 9]
                    c8_3 = terceira_matriz.iloc[2, 10]

                    # Calcular os inversos
                    inverso_c1_3 = 1 / c1_3
                    inverso_c2_3 = 1 / c2_3
                    inverso_c3_3 = 1 / c3_3
                    inverso_c4_3 = 1 / c4_3
                    inverso_c5_3 = 1 / c5_3
                    inverso_c6_3 = 1 / c6_3
                    inverso_c7_3 = 1 / c7_3
                    inverso_c8_3 = 1 / c8_3
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[3, 2] = inverso_c1_3
                    terceira_matriz.iloc[4, 2] = inverso_c2_3
                    terceira_matriz.iloc[5, 2] = inverso_c3_3
                    terceira_matriz.iloc[6, 2] = inverso_c4_3
                    terceira_matriz.iloc[7, 2] = inverso_c5_3
                    terceira_matriz.iloc[8, 2] = inverso_c6_3
                    terceira_matriz.iloc[9, 2] = inverso_c7_3
                    terceira_matriz.iloc[10, 2] = inverso_c8_3


                    #Critério 4
                    c1_4 = terceira_matriz.iloc[3, 4]
                    c2_4 = terceira_matriz.iloc[3, 5]
                    c3_4 = terceira_matriz.iloc[3, 6]
                    c4_4 = terceira_matriz.iloc[3, 7]
                    c5_4 = terceira_matriz.iloc[3, 8]
                    c6_4 = terceira_matriz.iloc[3, 9]
                    c7_4 = terceira_matriz.iloc[3, 10]
                
                    # Calcular os inversos
                    inverso_c1_4 = 1 / c1_4
                    inverso_c2_4 = 1 / c2_4
                    inverso_c3_4 = 1 / c3_4
                    inverso_c4_4 = 1 / c4_4
                    inverso_c5_4 = 1 / c5_4
                    inverso_c6_4 = 1 / c6_4
                    inverso_c7_4 = 1 / c7_4
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[4, 3] = inverso_c1_4
                    terceira_matriz.iloc[5, 3] = inverso_c2_4
                    terceira_matriz.iloc[6, 3] = inverso_c3_4
                    terceira_matriz.iloc[7, 3] = inverso_c4_4
                    terceira_matriz.iloc[8, 3] = inverso_c5_4
                    terceira_matriz.iloc[9, 3] = inverso_c6_4
                    terceira_matriz.iloc[10, 3] = inverso_c7_4


                    #Critério 5
                    c1_5 = terceira_matriz.iloc[4, 5]
                    c2_5 = terceira_matriz.iloc[4, 6]
                    c3_5 = terceira_matriz.iloc[4, 7]
                    c4_5 = terceira_matriz.iloc[4, 8]
                    c5_5 = terceira_matriz.iloc[4, 9]
                    c6_5 = terceira_matriz.iloc[4, 10]
                                    
                    # Calcular os inversos
                    inverso_c1_5 = 1 / c1_5
                    inverso_c2_5 = 1 / c2_5
                    inverso_c3_5 = 1 / c3_5
                    inverso_c4_5 = 1 / c4_5
                    inverso_c5_5 = 1 / c5_5
                    inverso_c6_5 = 1 / c6_5
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[5, 4] = inverso_c1_5
                    terceira_matriz.iloc[6, 4] = inverso_c2_5
                    terceira_matriz.iloc[7, 4] = inverso_c3_5
                    terceira_matriz.iloc[8, 4] = inverso_c4_5
                    terceira_matriz.iloc[9, 4] = inverso_c5_5
                    terceira_matriz.iloc[10, 4] = inverso_c6_5


                     #Critério 6
                    c1_6 = terceira_matriz.iloc[5, 6]
                    c2_6 = terceira_matriz.iloc[5, 7]
                    c3_6 = terceira_matriz.iloc[5, 8]
                    c4_6 = terceira_matriz.iloc[5, 9]
                    c5_6 = terceira_matriz.iloc[5, 10]
                                    
                    # Calcular os inversos
                    inverso_c1_6 = 1 / c1_6
                    inverso_c2_6 = 1 / c2_6
                    inverso_c3_6 = 1 / c3_6
                    inverso_c4_6 = 1 / c4_6
                    inverso_c5_6 = 1 / c5_6
                  
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[6, 5] = inverso_c1_6
                    terceira_matriz.iloc[7, 5] = inverso_c2_6
                    terceira_matriz.iloc[8, 5] = inverso_c3_6
                    terceira_matriz.iloc[9, 5] = inverso_c4_6
                    terceira_matriz.iloc[10, 5] = inverso_c5_6

                       #Critério 7
                    c1_7 = terceira_matriz.iloc[6, 7]
                    c2_7 = terceira_matriz.iloc[6, 8]
                    c3_7 = terceira_matriz.iloc[6, 9]
                    c4_7 = terceira_matriz.iloc[6, 10]
                                    
                    # Calcular os inversos
                    inverso_c1_7 = 1 / c1_7
                    inverso_c2_7 = 1 / c2_7
                    inverso_c3_7 = 1 / c3_7
                    inverso_c4_7 = 1 / c4_7
                                     
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[7, 6] = inverso_c1_7
                    terceira_matriz.iloc[8, 6] = inverso_c2_7
                    terceira_matriz.iloc[9, 6] = inverso_c3_7
                    terceira_matriz.iloc[10, 6] = inverso_c4_7

                    #Critério 8
                    c1_8 = terceira_matriz.iloc[7,8]
                    c2_8 = terceira_matriz.iloc[7,9]
                    c3_8 = terceira_matriz.iloc[7,10]
                                    
                    # Calcular os inversos
                    inverso_c1_8 = 1 / c1_8
                    inverso_c2_8 = 1 / c2_8
                    inverso_c3_8 = 1 / c3_8
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[8, 7] = inverso_c1_8
                    terceira_matriz.iloc[9, 7] = inverso_c2_8
                    terceira_matriz.iloc[10, 7] = inverso_c3_8

                    #Critério 9
                    c1_9 = terceira_matriz.iloc[9,8]
                    c2_9 = terceira_matriz.iloc[10,8]
                                    
                    # Calcular os inversos
                    inverso_c1_9 = 1 / c1_9
                    inverso_c2_9 = 1 / c2_9
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[8, 9] = inverso_c1_9
                    terceira_matriz.iloc[8, 10] = inverso_c2_9
                    
                     #Critério 9
                    c1_10 = terceira_matriz.iloc[9,10]
                                                        
                    # Calcular os inversos
                    inverso_c1_10 = 1 / c1_10
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[10, 9] = inverso_c1_10
                

    if num_critérios == 12:
        for i in range(2, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[1, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[1, i] = item["valor"]
                     

        for i in range(3, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[2, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[2, i] = item["valor"]
                     

        for i in range(4, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[3, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[3, i] = item["valor"]
                     

        for i in range(5, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[4, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[4, i] = item["valor"]

        for i in range(6, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[5, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[5, i] = item["valor"]
        
        for i in range(7, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[6, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[6, i] = item["valor"]
        for i in range(8, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[7, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[7, i] = item["valor"]
        for i in range(9, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[8, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[8, i] = item["valor"]
        for i in range(10, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[9, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[9, i] = item["valor"]

        for i in range(11, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[10, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[10, i] = item["valor"]

                    #Inverter a Terceira Matriz
                    #Critério 1
                    c1 = terceira_matriz.iloc[0, 1]
                    c2 = terceira_matriz.iloc[0, 2]
                    c3 = terceira_matriz.iloc[0, 3]
                    c4 = terceira_matriz.iloc[0, 4]
                    c5 = terceira_matriz.iloc[0, 5]
                    c6 = terceira_matriz.iloc[0, 6]
                    c7 = terceira_matriz.iloc[0, 7]
                    c8 = terceira_matriz.iloc[0, 8]
                    c9 = terceira_matriz.iloc[0, 9]
                    c10 = terceira_matriz.iloc[0, 10]
                    c11 = terceira_matriz.iloc[0, 11]
                
                    # Calcular os inversos
                    inverso_c1 = 1 / c1
                    inverso_c2 = 1 / c2
                    inverso_c3 = 1 / c3
                    inverso_c4 = 1 / c4
                    inverso_c5 = 1 / c5
                    inverso_c6 = 1 / c6
                    inverso_c7 = 1 / c7
                    inverso_c8 = 1 / c8
                    inverso_c9 = 1 / c9
                    inverso_c10 = 1 / c10
                    inverso_c11 = 1 / c11

                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[1, 0] = inverso_c1
                    terceira_matriz.iloc[2, 0] = inverso_c2
                    terceira_matriz.iloc[3, 0] = inverso_c3
                    terceira_matriz.iloc[4, 0] = inverso_c4
                    terceira_matriz.iloc[5, 0] = inverso_c5
                    terceira_matriz.iloc[6, 0] = inverso_c6
                    terceira_matriz.iloc[7, 0] = inverso_c7
                    terceira_matriz.iloc[8, 0] = inverso_c8
                    terceira_matriz.iloc[9, 0] = inverso_c9
                    terceira_matriz.iloc[10, 0] = inverso_c10
                    terceira_matriz.iloc[11, 0] = inverso_c11
                
                    #Critério 2
                    c1_2 = terceira_matriz.iloc[1, 2]
                    c2_2 = terceira_matriz.iloc[1, 3]
                    c3_2 = terceira_matriz.iloc[1, 4]
                    c4_2 = terceira_matriz.iloc[1, 5]
                    c5_2 = terceira_matriz.iloc[1, 6]
                    c6_2 = terceira_matriz.iloc[1, 7]
                    c7_2 = terceira_matriz.iloc[1, 8]
                    c8_2 = terceira_matriz.iloc[1, 9]
                    c9_2 = terceira_matriz.iloc[1, 10]
                    c10_2 = terceira_matriz.iloc[1, 11]
                    
                
                    # Calcular os inversos
                    inverso_c1_2 = 1 / c1_2
                    inverso_c2_2 = 1 / c2_2
                    inverso_c3_2 = 1 / c3_2
                    inverso_c4_2 = 1 / c4_2
                    inverso_c5_2 = 1 / c5_2
                    inverso_c6_2 = 1 / c6_2
                    inverso_c7_2 = 1 / c7_2
                    inverso_c8_2 = 1 / c8_2
                    inverso_c9_2 = 1 / c9_2
                    inverso_c10_2 = 1 / c10_2



                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[2, 1] = inverso_c1_2
                    terceira_matriz.iloc[3, 1] = inverso_c2_2
                    terceira_matriz.iloc[4, 1] = inverso_c3_2
                    terceira_matriz.iloc[5, 1] = inverso_c4_2
                    terceira_matriz.iloc[6, 1] = inverso_c5_2
                    terceira_matriz.iloc[7, 1] = inverso_c6_2
                    terceira_matriz.iloc[8, 1] = inverso_c7_2
                    terceira_matriz.iloc[9, 1] = inverso_c8_2
                    terceira_matriz.iloc[10, 1] = inverso_c9_2
                    terceira_matriz.iloc[11, 1] = inverso_c10_2
                    
                
                    #Critério 3
                    c1_3 = terceira_matriz.iloc[2, 3]
                    c2_3 = terceira_matriz.iloc[2, 4]
                    c3_3 = terceira_matriz.iloc[2, 5]
                    c4_3 = terceira_matriz.iloc[2, 6]
                    c5_3 = terceira_matriz.iloc[2, 7]
                    c6_3 = terceira_matriz.iloc[2, 8]
                    c7_3 = terceira_matriz.iloc[2, 9]
                    c8_3 = terceira_matriz.iloc[2, 10]
                    c9_3 = terceira_matriz.iloc[2, 11]

                    # Calcular os inversos
                    inverso_c1_3 = 1 / c1_3
                    inverso_c2_3 = 1 / c2_3
                    inverso_c3_3 = 1 / c3_3
                    inverso_c4_3 = 1 / c4_3
                    inverso_c5_3 = 1 / c5_3
                    inverso_c6_3 = 1 / c6_3
                    inverso_c7_3 = 1 / c7_3
                    inverso_c8_3 = 1 / c8_3
                    inverso_c9_3 = 1 / c9_3
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[3, 2] = inverso_c1_3
                    terceira_matriz.iloc[4, 2] = inverso_c2_3
                    terceira_matriz.iloc[5, 2] = inverso_c3_3
                    terceira_matriz.iloc[6, 2] = inverso_c4_3
                    terceira_matriz.iloc[7, 2] = inverso_c5_3
                    terceira_matriz.iloc[8, 2] = inverso_c6_3
                    terceira_matriz.iloc[9, 2] = inverso_c7_3
                    terceira_matriz.iloc[10, 2] = inverso_c8_3
                    terceira_matriz.iloc[11, 2] = inverso_c9_3



                    #Critério 4
                    c1_4 = terceira_matriz.iloc[3, 4]
                    c2_4 = terceira_matriz.iloc[3, 5]
                    c3_4 = terceira_matriz.iloc[3, 6]
                    c4_4 = terceira_matriz.iloc[3, 7]
                    c5_4 = terceira_matriz.iloc[3, 8]
                    c6_4 = terceira_matriz.iloc[3, 9]
                    c7_4 = terceira_matriz.iloc[3, 10]
                    c8_4 = terceira_matriz.iloc[3, 11]
                
                    # Calcular os inversos
                    inverso_c1_4 = 1 / c1_4
                    inverso_c2_4 = 1 / c2_4
                    inverso_c3_4 = 1 / c3_4
                    inverso_c4_4 = 1 / c4_4
                    inverso_c5_4 = 1 / c5_4
                    inverso_c6_4 = 1 / c6_4
                    inverso_c7_4 = 1 / c7_4
                    inverso_c8_4 = 1 / c8_4
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[4, 3] = inverso_c1_4
                    terceira_matriz.iloc[5, 3] = inverso_c2_4
                    terceira_matriz.iloc[6, 3] = inverso_c3_4
                    terceira_matriz.iloc[7, 3] = inverso_c4_4
                    terceira_matriz.iloc[8, 3] = inverso_c5_4
                    terceira_matriz.iloc[9, 3] = inverso_c6_4
                    terceira_matriz.iloc[10, 3] = inverso_c7_4
                    terceira_matriz.iloc[11, 3] = inverso_c8_4


                    #Critério 5
                    c1_5 = terceira_matriz.iloc[4, 5]
                    c2_5 = terceira_matriz.iloc[4, 6]
                    c3_5 = terceira_matriz.iloc[4, 7]
                    c4_5 = terceira_matriz.iloc[4, 8]
                    c5_5 = terceira_matriz.iloc[4, 9]
                    c6_5 = terceira_matriz.iloc[4, 10]
                    c7_5 = terceira_matriz.iloc[4, 11]
                                    
                    # Calcular os inversos
                    inverso_c1_5 = 1 / c1_5
                    inverso_c2_5 = 1 / c2_5
                    inverso_c3_5 = 1 / c3_5
                    inverso_c4_5 = 1 / c4_5
                    inverso_c5_5 = 1 / c5_5
                    inverso_c6_5 = 1 / c6_5
                    inverso_c7_5 = 1 / c7_5
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[5, 4] = inverso_c1_5
                    terceira_matriz.iloc[6, 4] = inverso_c2_5
                    terceira_matriz.iloc[7, 4] = inverso_c3_5
                    terceira_matriz.iloc[8, 4] = inverso_c4_5
                    terceira_matriz.iloc[9, 4] = inverso_c5_5
                    terceira_matriz.iloc[10, 4] = inverso_c6_5
                    terceira_matriz.iloc[11, 4] = inverso_c7_5


                     #Critério 6
                    c1_6 = terceira_matriz.iloc[5, 6]
                    c2_6 = terceira_matriz.iloc[5, 7]
                    c3_6 = terceira_matriz.iloc[5, 8]
                    c4_6 = terceira_matriz.iloc[5, 9]
                    c5_6 = terceira_matriz.iloc[5, 10]
                    c6_6 = terceira_matriz.iloc[5, 11]
                                    
                    # Calcular os inversos
                    inverso_c1_6 = 1 / c1_6
                    inverso_c2_6 = 1 / c2_6
                    inverso_c3_6 = 1 / c3_6
                    inverso_c4_6 = 1 / c4_6
                    inverso_c5_6 = 1 / c5_6
                    inverso_c6_6 = 1 / c6_6
                    
                  
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[6, 5] = inverso_c1_6
                    terceira_matriz.iloc[7, 5] = inverso_c2_6
                    terceira_matriz.iloc[8, 5] = inverso_c3_6
                    terceira_matriz.iloc[9, 5] = inverso_c4_6
                    terceira_matriz.iloc[10, 5] = inverso_c5_6
                    terceira_matriz.iloc[11, 5] = inverso_c6_6


                       #Critério 7
                    c1_7 = terceira_matriz.iloc[6, 7]
                    c2_7 = terceira_matriz.iloc[6, 8]
                    c3_7 = terceira_matriz.iloc[6, 9]
                    c4_7 = terceira_matriz.iloc[6, 10]
                    c5_7 = terceira_matriz.iloc[6, 11]
                                    
                    # Calcular os inversos
                    inverso_c1_7 = 1 / c1_7
                    inverso_c2_7 = 1 / c2_7
                    inverso_c3_7 = 1 / c3_7
                    inverso_c4_7 = 1 / c4_7
                    inverso_c5_7 = 1 / c5_7
                    
                                     
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[7, 6] = inverso_c1_7
                    terceira_matriz.iloc[8, 6] = inverso_c2_7
                    terceira_matriz.iloc[9, 6] = inverso_c3_7
                    terceira_matriz.iloc[10, 6] = inverso_c4_7
                    terceira_matriz.iloc[11, 6] = inverso_c5_7

                    #Critério 8
                    c1_8 = terceira_matriz.iloc[7,8]
                    c2_8 = terceira_matriz.iloc[7,9]
                    c3_8 = terceira_matriz.iloc[7,10]
                    c4_8 = terceira_matriz.iloc[7,11]
                                    
                    # Calcular os inversos
                    inverso_c1_8 = 1 / c1_8
                    inverso_c2_8 = 1 / c2_8
                    inverso_c3_8 = 1 / c3_8
                    inverso_c4_8 = 1 / c4_8
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[8, 7] = inverso_c1_8
                    terceira_matriz.iloc[9, 7] = inverso_c2_8
                    terceira_matriz.iloc[10, 7] = inverso_c3_8
                    terceira_matriz.iloc[11, 7] = inverso_c4_8

                    #Critério 9
                    c1_9 = terceira_matriz.iloc[9,8]
                    c2_9 = terceira_matriz.iloc[10,8]
                    c3_9 = terceira_matriz.iloc[11,8]
                                    
                    # Calcular os inversos
                    inverso_c1_9 = 1 / c1_9
                    inverso_c2_9 = 1 / c2_9
                    inverso_c3_9 = 1 / c3_9
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[8, 9] = inverso_c1_9
                    terceira_matriz.iloc[8, 10] = inverso_c2_9
                    terceira_matriz.iloc[8, 11] = inverso_c3_9 
                    
                     #Critério 10
                    c1_10 = terceira_matriz.iloc[9,10]
                    c2_10 = terceira_matriz.iloc[9,11]
                                                        
                    # Calcular os inversos
                    inverso_c1_10 = 1 / c1_10
                    inverso_c2_10 = 1 / c2_10
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[10, 9] = inverso_c1_10
                    terceira_matriz.iloc[11, 9] = inverso_c2_10

                       # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[9, 9] = inverso_c1_9
                    terceira_matriz.iloc[9, 10] = inverso_c2_9
                    terceira_matriz.iloc[9, 11] = inverso_c3_9 
                    
                     #Critério 11
                    c1_11 = terceira_matriz.iloc[10,11]
                                                     
                    # Calcular os inversos
                    inverso_c1_11 = 1 / c1_11
                                   
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[11, 10] = inverso_c1_11
                            
        
    if num_critérios == 13:
        for i in range(2, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[1, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[1, i] = item["valor"]
                     

        for i in range(3, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[2, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[2, i] = item["valor"]
                     

        for i in range(4, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[3, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[3, i] = item["valor"]
                     

        for i in range(5, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[4, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[4, i] = item["valor"]

        for i in range(6, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[5, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[5, i] = item["valor"]
        
        for i in range(7, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[6, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[6, i] = item["valor"]
        for i in range(8, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[7, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[7, i] = item["valor"]
        for i in range(9, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[8, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[8, i] = item["valor"]
        for i in range(10, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[9, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[9, i] = item["valor"]

        for i in range(11, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[10, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[10, i] = item["valor"]
        
        for i in range(12, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[11, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[11, i] = item["valor"]

                    #Inverter a Terceira Matriz
                    #Critério 1
                    c1 = terceira_matriz.iloc[0, 1]
                    c2 = terceira_matriz.iloc[0, 2]
                    c3 = terceira_matriz.iloc[0, 3]
                    c4 = terceira_matriz.iloc[0, 4]
                    c5 = terceira_matriz.iloc[0, 5]
                    c6 = terceira_matriz.iloc[0, 6]
                    c7 = terceira_matriz.iloc[0, 7]
                    c8 = terceira_matriz.iloc[0, 8]
                    c9 = terceira_matriz.iloc[0, 9]
                    c10 = terceira_matriz.iloc[0, 10]
                    c11 = terceira_matriz.iloc[0, 11]
                    c12 = terceira_matriz.iloc[0, 12]
                
                    # Calcular os inversos
                    inverso_c1 = 1 / c1
                    inverso_c2 = 1 / c2
                    inverso_c3 = 1 / c3
                    inverso_c4 = 1 / c4
                    inverso_c5 = 1 / c5
                    inverso_c6 = 1 / c6
                    inverso_c7 = 1 / c7
                    inverso_c8 = 1 / c8
                    inverso_c9 = 1 / c9
                    inverso_c10 = 1 / c10
                    inverso_c11 = 1 / c11
                    inverso_c12 = 1 / c12

                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[1, 0] = inverso_c1
                    terceira_matriz.iloc[2, 0] = inverso_c2
                    terceira_matriz.iloc[3, 0] = inverso_c3
                    terceira_matriz.iloc[4, 0] = inverso_c4
                    terceira_matriz.iloc[5, 0] = inverso_c5
                    terceira_matriz.iloc[6, 0] = inverso_c6
                    terceira_matriz.iloc[7, 0] = inverso_c7
                    terceira_matriz.iloc[8, 0] = inverso_c8
                    terceira_matriz.iloc[9, 0] = inverso_c9
                    terceira_matriz.iloc[10, 0] = inverso_c10
                    terceira_matriz.iloc[11, 0] = inverso_c11
                    terceira_matriz.iloc[12, 0] = inverso_c12
                
                    #Critério 2
                    c1_2 = terceira_matriz.iloc[1, 2]
                    c2_2 = terceira_matriz.iloc[1, 3]
                    c3_2 = terceira_matriz.iloc[1, 4]
                    c4_2 = terceira_matriz.iloc[1, 5]
                    c5_2 = terceira_matriz.iloc[1, 6]
                    c6_2 = terceira_matriz.iloc[1, 7]
                    c7_2 = terceira_matriz.iloc[1, 8]
                    c8_2 = terceira_matriz.iloc[1, 9]
                    c9_2 = terceira_matriz.iloc[1, 10]
                    c10_2 = terceira_matriz.iloc[1, 11]
                    c11_2 = terceira_matriz.iloc[1, 12]
                    
                
                    # Calcular os inversos
                    inverso_c1_2 = 1 / c1_2
                    inverso_c2_2 = 1 / c2_2
                    inverso_c3_2 = 1 / c3_2
                    inverso_c4_2 = 1 / c4_2
                    inverso_c5_2 = 1 / c5_2
                    inverso_c6_2 = 1 / c6_2
                    inverso_c7_2 = 1 / c7_2
                    inverso_c8_2 = 1 / c8_2
                    inverso_c9_2 = 1 / c9_2
                    inverso_c10_2 = 1 / c10_2
                    inverso_c11_2 = 1 / c11_2



                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[2, 1] = inverso_c1_2
                    terceira_matriz.iloc[3, 1] = inverso_c2_2
                    terceira_matriz.iloc[4, 1] = inverso_c3_2
                    terceira_matriz.iloc[5, 1] = inverso_c4_2
                    terceira_matriz.iloc[6, 1] = inverso_c5_2
                    terceira_matriz.iloc[7, 1] = inverso_c6_2
                    terceira_matriz.iloc[8, 1] = inverso_c7_2
                    terceira_matriz.iloc[9, 1] = inverso_c8_2
                    terceira_matriz.iloc[10, 1] = inverso_c9_2
                    terceira_matriz.iloc[11, 1] = inverso_c10_2
                    terceira_matriz.iloc[12, 1] = inverso_c11_2
                    
                
                    #Critério 3
                    c1_3 = terceira_matriz.iloc[2, 3]
                    c2_3 = terceira_matriz.iloc[2, 4]
                    c3_3 = terceira_matriz.iloc[2, 5]
                    c4_3 = terceira_matriz.iloc[2, 6]
                    c5_3 = terceira_matriz.iloc[2, 7]
                    c6_3 = terceira_matriz.iloc[2, 8]
                    c7_3 = terceira_matriz.iloc[2, 9]
                    c8_3 = terceira_matriz.iloc[2, 10]
                    c9_3 = terceira_matriz.iloc[2, 11]
                    c10_3 = terceira_matriz.iloc[2, 12]

                    # Calcular os inversos
                    inverso_c1_3 = 1 / c1_3
                    inverso_c2_3 = 1 / c2_3
                    inverso_c3_3 = 1 / c3_3
                    inverso_c4_3 = 1 / c4_3
                    inverso_c5_3 = 1 / c5_3
                    inverso_c6_3 = 1 / c6_3
                    inverso_c7_3 = 1 / c7_3
                    inverso_c8_3 = 1 / c8_3
                    inverso_c9_3 = 1 / c9_3
                    inverso_c10_3 = 1 / c10_3
                
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[3, 2] = inverso_c1_3
                    terceira_matriz.iloc[4, 2] = inverso_c2_3
                    terceira_matriz.iloc[5, 2] = inverso_c3_3
                    terceira_matriz.iloc[6, 2] = inverso_c4_3
                    terceira_matriz.iloc[7, 2] = inverso_c5_3
                    terceira_matriz.iloc[8, 2] = inverso_c6_3
                    terceira_matriz.iloc[9, 2] = inverso_c7_3
                    terceira_matriz.iloc[10, 2] = inverso_c8_3
                    terceira_matriz.iloc[11, 2] = inverso_c9_3
                    terceira_matriz.iloc[12, 2] = inverso_c10_3



                    #Critério 4
                    c1_4 = terceira_matriz.iloc[3, 4]
                    c2_4 = terceira_matriz.iloc[3, 5]
                    c3_4 = terceira_matriz.iloc[3, 6]
                    c4_4 = terceira_matriz.iloc[3, 7]
                    c5_4 = terceira_matriz.iloc[3, 8]
                    c6_4 = terceira_matriz.iloc[3, 9]
                    c7_4 = terceira_matriz.iloc[3, 10]
                    c8_4 = terceira_matriz.iloc[3, 11]
                    c9_4 = terceira_matriz.iloc[3, 12]
                
                    # Calcular os inversos
                    inverso_c1_4 = 1 / c1_4
                    inverso_c2_4 = 1 / c2_4
                    inverso_c3_4 = 1 / c3_4
                    inverso_c4_4 = 1 / c4_4
                    inverso_c5_4 = 1 / c5_4
                    inverso_c6_4 = 1 / c6_4
                    inverso_c7_4 = 1 / c7_4
                    inverso_c8_4 = 1 / c8_4
                    inverso_c9_4 = 1 / c9_4
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[4, 3] = inverso_c1_4
                    terceira_matriz.iloc[5, 3] = inverso_c2_4
                    terceira_matriz.iloc[6, 3] = inverso_c3_4
                    terceira_matriz.iloc[7, 3] = inverso_c4_4
                    terceira_matriz.iloc[8, 3] = inverso_c5_4
                    terceira_matriz.iloc[9, 3] = inverso_c6_4
                    terceira_matriz.iloc[10, 3] = inverso_c7_4
                    terceira_matriz.iloc[11, 3] = inverso_c8_4
                    terceira_matriz.iloc[12, 3] = inverso_c9_4


                    #Critério 5
                    c1_5 = terceira_matriz.iloc[4, 5]
                    c2_5 = terceira_matriz.iloc[4, 6]
                    c3_5 = terceira_matriz.iloc[4, 7]
                    c4_5 = terceira_matriz.iloc[4, 8]
                    c5_5 = terceira_matriz.iloc[4, 9]
                    c6_5 = terceira_matriz.iloc[4, 10]
                    c7_5 = terceira_matriz.iloc[4, 11]
                    c8_5 = terceira_matriz.iloc[4, 12]
                                    
                    # Calcular os inversos
                    inverso_c1_5 = 1 / c1_5
                    inverso_c2_5 = 1 / c2_5
                    inverso_c3_5 = 1 / c3_5
                    inverso_c4_5 = 1 / c4_5
                    inverso_c5_5 = 1 / c5_5
                    inverso_c6_5 = 1 / c6_5
                    inverso_c7_5 = 1 / c7_5
                    inverso_c8_5 = 1 / c8_5
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[5, 4] = inverso_c1_5
                    terceira_matriz.iloc[6, 4] = inverso_c2_5
                    terceira_matriz.iloc[7, 4] = inverso_c3_5
                    terceira_matriz.iloc[8, 4] = inverso_c4_5
                    terceira_matriz.iloc[9, 4] = inverso_c5_5
                    terceira_matriz.iloc[10, 4] = inverso_c6_5
                    terceira_matriz.iloc[11, 4] = inverso_c7_5
                    terceira_matriz.iloc[12, 4] = inverso_c8_5


                     #Critério 6
                    c1_6 = terceira_matriz.iloc[5, 6]
                    c2_6 = terceira_matriz.iloc[5, 7]
                    c3_6 = terceira_matriz.iloc[5, 8]
                    c4_6 = terceira_matriz.iloc[5, 9]
                    c5_6 = terceira_matriz.iloc[5, 10]
                    c6_6 = terceira_matriz.iloc[5, 11]
                    c7_6 = terceira_matriz.iloc[5, 12]
                                    
                                    
                    # Calcular os inversos
                    inverso_c1_6 = 1 / c1_6
                    inverso_c2_6 = 1 / c2_6
                    inverso_c3_6 = 1 / c3_6
                    inverso_c4_6 = 1 / c4_6
                    inverso_c5_6 = 1 / c5_6
                    inverso_c6_6 = 1 / c6_6
                    inverso_c7_6 = 1 / c7_6
                    
                  
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[6, 5] = inverso_c1_6
                    terceira_matriz.iloc[7, 5] = inverso_c2_6
                    terceira_matriz.iloc[8, 5] = inverso_c3_6
                    terceira_matriz.iloc[9, 5] = inverso_c4_6
                    terceira_matriz.iloc[10, 5] = inverso_c5_6
                    terceira_matriz.iloc[11, 5] = inverso_c6_6
                    terceira_matriz.iloc[12, 5] = inverso_c7_6


                       #Critério 7
                    c1_7 = terceira_matriz.iloc[6, 7]
                    c2_7 = terceira_matriz.iloc[6, 8]
                    c3_7 = terceira_matriz.iloc[6, 9]
                    c4_7 = terceira_matriz.iloc[6, 10]
                    c5_7 = terceira_matriz.iloc[6, 11]
                    c6_7 = terceira_matriz.iloc[6, 12]
                                    
                    # Calcular os inversos
                    inverso_c1_7 = 1 / c1_7
                    inverso_c2_7 = 1 / c2_7
                    inverso_c3_7 = 1 / c3_7
                    inverso_c4_7 = 1 / c4_7
                    inverso_c5_7 = 1 / c5_7
                    inverso_c6_7 = 1 / c6_7
                    
                                     
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[7, 6] = inverso_c1_7
                    terceira_matriz.iloc[8, 6] = inverso_c2_7
                    terceira_matriz.iloc[9, 6] = inverso_c3_7
                    terceira_matriz.iloc[10, 6] = inverso_c4_7
                    terceira_matriz.iloc[11, 6] = inverso_c5_7
                    terceira_matriz.iloc[12, 6] = inverso_c6_7

                    #Critério 8
                    c1_8 = terceira_matriz.iloc[7,8]
                    c2_8 = terceira_matriz.iloc[7,9]
                    c3_8 = terceira_matriz.iloc[7,10]
                    c4_8 = terceira_matriz.iloc[7,11]
                    c5_8 = terceira_matriz.iloc[7,12]
                                    
                    # Calcular os inversos
                    inverso_c1_8 = 1 / c1_8
                    inverso_c2_8 = 1 / c2_8
                    inverso_c3_8 = 1 / c3_8
                    inverso_c4_8 = 1 / c4_8
                    inverso_c5_8 = 1 / c5_8
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[8, 7] = inverso_c1_8
                    terceira_matriz.iloc[9, 7] = inverso_c2_8
                    terceira_matriz.iloc[10, 7] = inverso_c3_8
                    terceira_matriz.iloc[11, 7] = inverso_c4_8
                    terceira_matriz.iloc[12, 7] = inverso_c5_8

                    #Critério 9
                    c1_9 = terceira_matriz.iloc[9,8]
                    c2_9 = terceira_matriz.iloc[10,8]
                    c3_9 = terceira_matriz.iloc[11,8]
                    c4_9 = terceira_matriz.iloc[12,8]
                                    
                    # Calcular os inversos
                    inverso_c1_9 = 1 / c1_9
                    inverso_c2_9 = 1 / c2_9
                    inverso_c3_9 = 1 / c3_9
                    inverso_c4_9 = 1 / c4_9
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[8, 9] = inverso_c1_9
                    terceira_matriz.iloc[8, 10] = inverso_c2_9
                    terceira_matriz.iloc[8, 11] = inverso_c3_9 
                    terceira_matriz.iloc[8, 12] = inverso_c4_9 
                    
                     #Critério 10
                    c1_10 = terceira_matriz.iloc[9,10]
                    c2_10 = terceira_matriz.iloc[9,11]
                    c3_10 = terceira_matriz.iloc[9,12]
                                                        
                    # Calcular os inversos
                    inverso_c1_10 = 1 / c1_10
                    inverso_c2_10 = 1 / c2_10
                    inverso_c3_10 = 1 / c3_10
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[10, 9] = inverso_c1_10
                    terceira_matriz.iloc[11, 9] = inverso_c2_10
                    terceira_matriz.iloc[12, 9] = inverso_c3_10


                      #Critério 11
                    c1_11 = terceira_matriz.iloc[9,11]
                    c2_11 = terceira_matriz.iloc[9,12]
                                                                    
                    # Calcular os inversos
                    inverso_c1_11 = 1 / c1_11
                    inverso_c2_11 = 1 / c2_11
                                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[11, 9] = inverso_c1_11
                    terceira_matriz.iloc[12, 9] = inverso_c2_11
                
                                       
                     #Critério 12
                    c1_12 = terceira_matriz.iloc[11,12]
                                                     
                    # Calcular os inversos
                    inverso_c1_12 = 1 / c1_12
                                   
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[12, 11] = inverso_c1_12        


    if num_critérios == 14:
        for i in range(2, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[1, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[1, i] = item["valor"]
                     

        for i in range(3, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[2, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[2, i] = item["valor"]
                     

        for i in range(4, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[3, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[3, i] = item["valor"]
                     

        for i in range(5, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[4, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[4, i] = item["valor"]

        for i in range(6, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[5, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[5, i] = item["valor"]
        
        for i in range(7, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[6, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[6, i] = item["valor"]
        for i in range(8, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[7, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[7, i] = item["valor"]
        for i in range(9, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[8, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[8, i] = item["valor"]
        for i in range(10, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[9, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[9, i] = item["valor"]

        for i in range(11, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[10, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[10, i] = item["valor"]
        
        for i in range(12, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[11, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[11, i] = item["valor"]
        
        for i in range(13, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[12, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[12, i] = item["valor"]

                    #Inverter a Terceira Matriz
                    #Critério 1
                    c1 = terceira_matriz.iloc[0, 1]
                    c2 = terceira_matriz.iloc[0, 2]
                    c3 = terceira_matriz.iloc[0, 3]
                    c4 = terceira_matriz.iloc[0, 4]
                    c5 = terceira_matriz.iloc[0, 5]
                    c6 = terceira_matriz.iloc[0, 6]
                    c7 = terceira_matriz.iloc[0, 7]
                    c8 = terceira_matriz.iloc[0, 8]
                    c9 = terceira_matriz.iloc[0, 9]
                    c10 = terceira_matriz.iloc[0, 10]
                    c11 = terceira_matriz.iloc[0, 11]
                    c12 = terceira_matriz.iloc[0, 12]
                    c13 = terceira_matriz.iloc[0, 13]
                
                    # Calcular os inversos
                    inverso_c1 = 1 / c1
                    inverso_c2 = 1 / c2
                    inverso_c3 = 1 / c3
                    inverso_c4 = 1 / c4
                    inverso_c5 = 1 / c5
                    inverso_c6 = 1 / c6
                    inverso_c7 = 1 / c7
                    inverso_c8 = 1 / c8
                    inverso_c9 = 1 / c9
                    inverso_c10 = 1 / c10
                    inverso_c11 = 1 / c11
                    inverso_c12 = 1 / c12
                    inverso_c13 = 1 / c13

                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[1, 0] = inverso_c1
                    terceira_matriz.iloc[2, 0] = inverso_c2
                    terceira_matriz.iloc[3, 0] = inverso_c3
                    terceira_matriz.iloc[4, 0] = inverso_c4
                    terceira_matriz.iloc[5, 0] = inverso_c5
                    terceira_matriz.iloc[6, 0] = inverso_c6
                    terceira_matriz.iloc[7, 0] = inverso_c7
                    terceira_matriz.iloc[8, 0] = inverso_c8
                    terceira_matriz.iloc[9, 0] = inverso_c9
                    terceira_matriz.iloc[10, 0] = inverso_c10
                    terceira_matriz.iloc[11, 0] = inverso_c11
                    terceira_matriz.iloc[12, 0] = inverso_c12
                    terceira_matriz.iloc[13, 0] = inverso_c13
                
                    #Critério 2
                    c1_2 = terceira_matriz.iloc[1, 2]
                    c2_2 = terceira_matriz.iloc[1, 3]
                    c3_2 = terceira_matriz.iloc[1, 4]
                    c4_2 = terceira_matriz.iloc[1, 5]
                    c5_2 = terceira_matriz.iloc[1, 6]
                    c6_2 = terceira_matriz.iloc[1, 7]
                    c7_2 = terceira_matriz.iloc[1, 8]
                    c8_2 = terceira_matriz.iloc[1, 9]
                    c9_2 = terceira_matriz.iloc[1, 10]
                    c10_2 = terceira_matriz.iloc[1, 11]
                    c11_2 = terceira_matriz.iloc[1, 12]
                    c12_2 = terceira_matriz.iloc[1, 13]
                    
                
                    # Calcular os inversos
                    inverso_c1_2 = 1 / c1_2
                    inverso_c2_2 = 1 / c2_2
                    inverso_c3_2 = 1 / c3_2
                    inverso_c4_2 = 1 / c4_2
                    inverso_c5_2 = 1 / c5_2
                    inverso_c6_2 = 1 / c6_2
                    inverso_c7_2 = 1 / c7_2
                    inverso_c8_2 = 1 / c8_2
                    inverso_c9_2 = 1 / c9_2
                    inverso_c10_2 = 1 / c10_2
                    inverso_c11_2 = 1 / c11_2
                    inverso_c12_2 = 1 / c12_2



                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[2, 1] = inverso_c1_2
                    terceira_matriz.iloc[3, 1] = inverso_c2_2
                    terceira_matriz.iloc[4, 1] = inverso_c3_2
                    terceira_matriz.iloc[5, 1] = inverso_c4_2
                    terceira_matriz.iloc[6, 1] = inverso_c5_2
                    terceira_matriz.iloc[7, 1] = inverso_c6_2
                    terceira_matriz.iloc[8, 1] = inverso_c7_2
                    terceira_matriz.iloc[9, 1] = inverso_c8_2
                    terceira_matriz.iloc[10, 1] = inverso_c9_2
                    terceira_matriz.iloc[11, 1] = inverso_c10_2
                    terceira_matriz.iloc[12, 1] = inverso_c11_2
                    terceira_matriz.iloc[13, 1] = inverso_c12_2
                    
                
                    #Critério 3
                    c1_3 = terceira_matriz.iloc[2, 3]
                    c2_3 = terceira_matriz.iloc[2, 4]
                    c3_3 = terceira_matriz.iloc[2, 5]
                    c4_3 = terceira_matriz.iloc[2, 6]
                    c5_3 = terceira_matriz.iloc[2, 7]
                    c6_3 = terceira_matriz.iloc[2, 8]
                    c7_3 = terceira_matriz.iloc[2, 9]
                    c8_3 = terceira_matriz.iloc[2, 10]
                    c9_3 = terceira_matriz.iloc[2, 11]
                    c10_3 = terceira_matriz.iloc[2, 12]
                    c11_3 = terceira_matriz.iloc[2, 13]

                    # Calcular os inversos
                    inverso_c1_3 = 1 / c1_3
                    inverso_c2_3 = 1 / c2_3
                    inverso_c3_3 = 1 / c3_3
                    inverso_c4_3 = 1 / c4_3
                    inverso_c5_3 = 1 / c5_3
                    inverso_c6_3 = 1 / c6_3
                    inverso_c7_3 = 1 / c7_3
                    inverso_c8_3 = 1 / c8_3
                    inverso_c9_3 = 1 / c9_3
                    inverso_c10_3 = 1 / c10_3
                    inverso_c11_3 = 1 / c11_3
                
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[3, 2] = inverso_c1_3
                    terceira_matriz.iloc[4, 2] = inverso_c2_3
                    terceira_matriz.iloc[5, 2] = inverso_c3_3
                    terceira_matriz.iloc[6, 2] = inverso_c4_3
                    terceira_matriz.iloc[7, 2] = inverso_c5_3
                    terceira_matriz.iloc[8, 2] = inverso_c6_3
                    terceira_matriz.iloc[9, 2] = inverso_c7_3
                    terceira_matriz.iloc[10, 2] = inverso_c8_3
                    terceira_matriz.iloc[11, 2] = inverso_c9_3
                    terceira_matriz.iloc[12, 2] = inverso_c10_3
                    terceira_matriz.iloc[13, 2] = inverso_c11_3


                    #Critério 4
                    c1_4 = terceira_matriz.iloc[3, 4]
                    c2_4 = terceira_matriz.iloc[3, 5]
                    c3_4 = terceira_matriz.iloc[3, 6]
                    c4_4 = terceira_matriz.iloc[3, 7]
                    c5_4 = terceira_matriz.iloc[3, 8]
                    c6_4 = terceira_matriz.iloc[3, 9]
                    c7_4 = terceira_matriz.iloc[3, 10]
                    c8_4 = terceira_matriz.iloc[3, 11]
                    c9_4 = terceira_matriz.iloc[3, 12]
                    c10_4 = terceira_matriz.iloc[3, 13]
                
                    # Calcular os inversos
                    inverso_c1_4 = 1 / c1_4
                    inverso_c2_4 = 1 / c2_4
                    inverso_c3_4 = 1 / c3_4
                    inverso_c4_4 = 1 / c4_4
                    inverso_c5_4 = 1 / c5_4
                    inverso_c6_4 = 1 / c6_4
                    inverso_c7_4 = 1 / c7_4
                    inverso_c8_4 = 1 / c8_4
                    inverso_c9_4 = 1 / c9_4
                    inverso_c10_4 = 1 / c10_4
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[4, 3] = inverso_c1_4
                    terceira_matriz.iloc[5, 3] = inverso_c2_4
                    terceira_matriz.iloc[6, 3] = inverso_c3_4
                    terceira_matriz.iloc[7, 3] = inverso_c4_4
                    terceira_matriz.iloc[8, 3] = inverso_c5_4
                    terceira_matriz.iloc[9, 3] = inverso_c6_4
                    terceira_matriz.iloc[10, 3] = inverso_c7_4
                    terceira_matriz.iloc[11, 3] = inverso_c8_4
                    terceira_matriz.iloc[12, 3] = inverso_c9_4
                    terceira_matriz.iloc[13, 3] = inverso_c10_4


                    #Critério 5
                    c1_5 = terceira_matriz.iloc[4, 5]
                    c2_5 = terceira_matriz.iloc[4, 6]
                    c3_5 = terceira_matriz.iloc[4, 7]
                    c4_5 = terceira_matriz.iloc[4, 8]
                    c5_5 = terceira_matriz.iloc[4, 9]
                    c6_5 = terceira_matriz.iloc[4, 10]
                    c7_5 = terceira_matriz.iloc[4, 11]
                    c8_5 = terceira_matriz.iloc[4, 12]
                    c9_5 = terceira_matriz.iloc[4, 13]
                                    
                    # Calcular os inversos
                    inverso_c1_5 = 1 / c1_5
                    inverso_c2_5 = 1 / c2_5
                    inverso_c3_5 = 1 / c3_5
                    inverso_c4_5 = 1 / c4_5
                    inverso_c5_5 = 1 / c5_5
                    inverso_c6_5 = 1 / c6_5
                    inverso_c7_5 = 1 / c7_5
                    inverso_c8_5 = 1 / c8_5
                    inverso_c9_5 = 1 / c9_5
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[5, 4] = inverso_c1_5
                    terceira_matriz.iloc[6, 4] = inverso_c2_5
                    terceira_matriz.iloc[7, 4] = inverso_c3_5
                    terceira_matriz.iloc[8, 4] = inverso_c4_5
                    terceira_matriz.iloc[9, 4] = inverso_c5_5
                    terceira_matriz.iloc[10, 4] = inverso_c6_5
                    terceira_matriz.iloc[11, 4] = inverso_c7_5
                    terceira_matriz.iloc[12, 4] = inverso_c8_5
                    terceira_matriz.iloc[13, 4] = inverso_c9_5


                     #Critério 6
                    c1_6 = terceira_matriz.iloc[5, 6]
                    c2_6 = terceira_matriz.iloc[5, 7]
                    c3_6 = terceira_matriz.iloc[5, 8]
                    c4_6 = terceira_matriz.iloc[5, 9]
                    c5_6 = terceira_matriz.iloc[5, 10]
                    c6_6 = terceira_matriz.iloc[5, 11]
                    c7_6 = terceira_matriz.iloc[5, 12]
                    c8_6 = terceira_matriz.iloc[5, 13]
                                    
                                    
                    # Calcular os inversos
                    inverso_c1_6 = 1 / c1_6
                    inverso_c2_6 = 1 / c2_6
                    inverso_c3_6 = 1 / c3_6
                    inverso_c4_6 = 1 / c4_6
                    inverso_c5_6 = 1 / c5_6
                    inverso_c6_6 = 1 / c6_6
                    inverso_c7_6 = 1 / c7_6
                    inverso_c8_6 = 1 / c8_6
                                      
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[6, 5] = inverso_c1_6
                    terceira_matriz.iloc[7, 5] = inverso_c2_6
                    terceira_matriz.iloc[8, 5] = inverso_c3_6
                    terceira_matriz.iloc[9, 5] = inverso_c4_6
                    terceira_matriz.iloc[10, 5] = inverso_c5_6
                    terceira_matriz.iloc[11, 5] = inverso_c6_6
                    terceira_matriz.iloc[12, 5] = inverso_c7_6
                    terceira_matriz.iloc[13, 5] = inverso_c8_6


                       #Critério 7
                    c1_7 = terceira_matriz.iloc[6, 7]
                    c2_7 = terceira_matriz.iloc[6, 8]
                    c3_7 = terceira_matriz.iloc[6, 9]
                    c4_7 = terceira_matriz.iloc[6, 10]
                    c5_7 = terceira_matriz.iloc[6, 11]
                    c6_7 = terceira_matriz.iloc[6, 12]
                    c7_7 = terceira_matriz.iloc[6, 13]
                                    
                    # Calcular os inversos
                    inverso_c1_7 = 1 / c1_7
                    inverso_c2_7 = 1 / c2_7
                    inverso_c3_7 = 1 / c3_7
                    inverso_c4_7 = 1 / c4_7
                    inverso_c5_7 = 1 / c5_7
                    inverso_c6_7 = 1 / c6_7
                    inverso_c7_7 = 1 / c7_7
                    
                                     
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[7, 6] = inverso_c1_7
                    terceira_matriz.iloc[8, 6] = inverso_c2_7
                    terceira_matriz.iloc[9, 6] = inverso_c3_7
                    terceira_matriz.iloc[10, 6] = inverso_c4_7
                    terceira_matriz.iloc[11, 6] = inverso_c5_7
                    terceira_matriz.iloc[12, 6] = inverso_c6_7
                    terceira_matriz.iloc[13, 6] = inverso_c7_7


                    #Critério 8
                    c1_8 = terceira_matriz.iloc[7,8]
                    c2_8 = terceira_matriz.iloc[7,9]
                    c3_8 = terceira_matriz.iloc[7,10]
                    c4_8 = terceira_matriz.iloc[7,11]
                    c5_8 = terceira_matriz.iloc[7,12]
                    c6_8 = terceira_matriz.iloc[7,13]
                                    
                    # Calcular os inversos
                    inverso_c1_8 = 1 / c1_8
                    inverso_c2_8 = 1 / c2_8
                    inverso_c3_8 = 1 / c3_8
                    inverso_c4_8 = 1 / c4_8
                    inverso_c5_8 = 1 / c5_8
                    inverso_c6_8 = 1 / c6_8
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[8, 7] = inverso_c1_8
                    terceira_matriz.iloc[9, 7] = inverso_c2_8
                    terceira_matriz.iloc[10, 7] = inverso_c3_8
                    terceira_matriz.iloc[11, 7] = inverso_c4_8
                    terceira_matriz.iloc[12, 7] = inverso_c5_8
                    terceira_matriz.iloc[13, 7] = inverso_c6_8

                    #Critério 9
                    c1_9 = terceira_matriz.iloc[8, 9]
                    c2_9 = terceira_matriz.iloc[8, 10]
                    c3_9 = terceira_matriz.iloc[8, 11]
                    c4_9 = terceira_matriz.iloc[8, 12]
                    c5_9 = terceira_matriz.iloc[8, 13]
                                    
                    # Calcular os inversos
                    inverso_c1_9 = 1 / c1_9
                    inverso_c2_9 = 1 / c2_9
                    inverso_c3_9 = 1 / c3_9
                    inverso_c4_9 = 1 / c4_9
                    inverso_c5_9 = 1 / c5_9
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[9, 8] = inverso_c1_9
                    terceira_matriz.iloc[10, 8] = inverso_c2_9
                    terceira_matriz.iloc[11, 8] = inverso_c3_9 
                    terceira_matriz.iloc[12, 8] = inverso_c4_9 
                    terceira_matriz.iloc[13, 8] = inverso_c5_9 
                    
                     #Critério 10
                    c1_10 = terceira_matriz.iloc[9,10]
                    c2_10 = terceira_matriz.iloc[9,11]
                    c3_10 = terceira_matriz.iloc[9,12]
                    c4_10 = terceira_matriz.iloc[9,13]
                                                        
                    # Calcular os inversos
                    inverso_c1_10 = 1 / c1_10
                    inverso_c2_10 = 1 / c2_10
                    inverso_c3_10 = 1 / c3_10
                    inverso_c4_10 = 1 / c4_10
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[10, 9] = inverso_c1_10
                    terceira_matriz.iloc[11, 9] = inverso_c2_10
                    terceira_matriz.iloc[12, 9] = inverso_c3_10
                    terceira_matriz.iloc[13, 9] = inverso_c4_10


                    #Critério 11
                    c1_11 = terceira_matriz.iloc[10,11]
                    c2_11 = terceira_matriz.iloc[10,12]
                    c3_11 = terceira_matriz.iloc[10,13]
                                     
                                                                    
                    # Calcular os inversos
                    inverso_c1_11 = 1 / c1_11
                    inverso_c2_11 = 1 / c2_11
                    inverso_c3_11 = 1 / c3_11
                                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[11, 10] = inverso_c1_11
                    terceira_matriz.iloc[12, 10] = inverso_c2_11
                    terceira_matriz.iloc[13, 10] = inverso_c3_11
                
                                       
                     #Critério 12
                    c1_12 = terceira_matriz.iloc[11,12]
                    c2_12 = terceira_matriz.iloc[11,13]
                                                     
                    # Calcular os inversos
                    inverso_c1_12 = 1 / c1_12
                    inverso_c2_12 = 1 / c2_12
                                   
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[12, 11] = inverso_c1_12
                    terceira_matriz.iloc[13, 11] = inverso_c2_12    
                                         
                     #Critério 13
                    c1_13 = terceira_matriz.iloc[12,13]
                                                     
                    # Calcular os inversos
                    inverso_c1_13 = 1 / c1_13
                                   
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[13, 12] = inverso_c1_13         


    if num_critérios == 15:
        for i in range(2, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[1, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[1, i] = item["valor"]
                     

        for i in range(3, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[2, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[2, i] = item["valor"]
                     

        for i in range(4, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[3, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[3, i] = item["valor"]
                     

        for i in range(5, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[4, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[4, i] = item["valor"]

        for i in range(6, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[5, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[5, i] = item["valor"]
        
        for i in range(7, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[6, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[6, i] = item["valor"]
        for i in range(8, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[7, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[7, i] = item["valor"]
        for i in range(9, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[8, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[8, i] = item["valor"]
        for i in range(10, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[9, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[9, i] = item["valor"]

        for i in range(11, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[10, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[10, i] = item["valor"]
        
        for i in range(12, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[11, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[11, i] = item["valor"]
        
        for i in range(13, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[12, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[12, i] = item["valor"]
        
        for i in range(14, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[13, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[13, i] = item["valor"]

                    #Inverter a Terceira Matriz
                    #Critério 1
                    c1 = terceira_matriz.iloc[0, 1]
                    c2 = terceira_matriz.iloc[0, 2]
                    c3 = terceira_matriz.iloc[0, 3]
                    c4 = terceira_matriz.iloc[0, 4]
                    c5 = terceira_matriz.iloc[0, 5]
                    c6 = terceira_matriz.iloc[0, 6]
                    c7 = terceira_matriz.iloc[0, 7]
                    c8 = terceira_matriz.iloc[0, 8]
                    c9 = terceira_matriz.iloc[0, 9]
                    c10 = terceira_matriz.iloc[0, 10]
                    c11 = terceira_matriz.iloc[0, 11]
                    c12 = terceira_matriz.iloc[0, 12]
                    c13 = terceira_matriz.iloc[0, 13]
                    c14 = terceira_matriz.iloc[0, 14]
                
                    # Calcular os inversos
                    inverso_c1 = 1 / c1
                    inverso_c2 = 1 / c2
                    inverso_c3 = 1 / c3
                    inverso_c4 = 1 / c4
                    inverso_c5 = 1 / c5
                    inverso_c6 = 1 / c6
                    inverso_c7 = 1 / c7
                    inverso_c8 = 1 / c8
                    inverso_c9 = 1 / c9
                    inverso_c10 = 1 / c10
                    inverso_c11 = 1 / c11
                    inverso_c12 = 1 / c12
                    inverso_c13 = 1 / c13
                    inverso_c14 = 1 / c14


                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[1, 0] = inverso_c1
                    terceira_matriz.iloc[2, 0] = inverso_c2
                    terceira_matriz.iloc[3, 0] = inverso_c3
                    terceira_matriz.iloc[4, 0] = inverso_c4
                    terceira_matriz.iloc[5, 0] = inverso_c5
                    terceira_matriz.iloc[6, 0] = inverso_c6
                    terceira_matriz.iloc[7, 0] = inverso_c7
                    terceira_matriz.iloc[8, 0] = inverso_c8
                    terceira_matriz.iloc[9, 0] = inverso_c9
                    terceira_matriz.iloc[10, 0] = inverso_c10
                    terceira_matriz.iloc[11, 0] = inverso_c11
                    terceira_matriz.iloc[12, 0] = inverso_c12
                    terceira_matriz.iloc[13, 0] = inverso_c13
                    terceira_matriz.iloc[14, 0] = inverso_c14
                
                    #Critério 2
                    c1_2 = terceira_matriz.iloc[1, 2]
                    c2_2 = terceira_matriz.iloc[1, 3]
                    c3_2 = terceira_matriz.iloc[1, 4]
                    c4_2 = terceira_matriz.iloc[1, 5]
                    c5_2 = terceira_matriz.iloc[1, 6]
                    c6_2 = terceira_matriz.iloc[1, 7]
                    c7_2 = terceira_matriz.iloc[1, 8]
                    c8_2 = terceira_matriz.iloc[1, 9]
                    c9_2 = terceira_matriz.iloc[1, 10]
                    c10_2 = terceira_matriz.iloc[1, 11]
                    c11_2 = terceira_matriz.iloc[1, 12]
                    c12_2 = terceira_matriz.iloc[1, 13]
                    c13_2 = terceira_matriz.iloc[1, 14]
                    
                
                    # Calcular os inversos
                    inverso_c1_2 = 1 / c1_2
                    inverso_c2_2 = 1 / c2_2
                    inverso_c3_2 = 1 / c3_2
                    inverso_c4_2 = 1 / c4_2
                    inverso_c5_2 = 1 / c5_2
                    inverso_c6_2 = 1 / c6_2
                    inverso_c7_2 = 1 / c7_2
                    inverso_c8_2 = 1 / c8_2
                    inverso_c9_2 = 1 / c9_2
                    inverso_c10_2 = 1 / c10_2
                    inverso_c11_2 = 1 / c11_2
                    inverso_c12_2 = 1 / c12_2
                    inverso_c13_2 = 1 / c13_2



                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[2, 1] = inverso_c1_2
                    terceira_matriz.iloc[3, 1] = inverso_c2_2
                    terceira_matriz.iloc[4, 1] = inverso_c3_2
                    terceira_matriz.iloc[5, 1] = inverso_c4_2
                    terceira_matriz.iloc[6, 1] = inverso_c5_2
                    terceira_matriz.iloc[7, 1] = inverso_c6_2
                    terceira_matriz.iloc[8, 1] = inverso_c7_2
                    terceira_matriz.iloc[9, 1] = inverso_c8_2
                    terceira_matriz.iloc[10, 1] = inverso_c9_2
                    terceira_matriz.iloc[11, 1] = inverso_c10_2
                    terceira_matriz.iloc[12, 1] = inverso_c11_2
                    terceira_matriz.iloc[13, 1] = inverso_c12_2
                    terceira_matriz.iloc[14, 1] = inverso_c13_2
                    
                
                    #Critério 3
                    c1_3 = terceira_matriz.iloc[2, 3]
                    c2_3 = terceira_matriz.iloc[2, 4]
                    c3_3 = terceira_matriz.iloc[2, 5]
                    c4_3 = terceira_matriz.iloc[2, 6]
                    c5_3 = terceira_matriz.iloc[2, 7]
                    c6_3 = terceira_matriz.iloc[2, 8]
                    c7_3 = terceira_matriz.iloc[2, 9]
                    c8_3 = terceira_matriz.iloc[2, 10]
                    c9_3 = terceira_matriz.iloc[2, 11]
                    c10_3 = terceira_matriz.iloc[2, 12]
                    c11_3 = terceira_matriz.iloc[2, 13]
                    c12_3 = terceira_matriz.iloc[2, 14]

                    # Calcular os inversos
                    inverso_c1_3 = 1 / c1_3
                    inverso_c2_3 = 1 / c2_3
                    inverso_c3_3 = 1 / c3_3
                    inverso_c4_3 = 1 / c4_3
                    inverso_c5_3 = 1 / c5_3
                    inverso_c6_3 = 1 / c6_3
                    inverso_c7_3 = 1 / c7_3
                    inverso_c8_3 = 1 / c8_3
                    inverso_c9_3 = 1 / c9_3
                    inverso_c10_3 = 1 / c10_3
                    inverso_c11_3 = 1 / c11_3
                    inverso_c12_3 = 1 / c12_3
                
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[3, 2] = inverso_c1_3
                    terceira_matriz.iloc[4, 2] = inverso_c2_3
                    terceira_matriz.iloc[5, 2] = inverso_c3_3
                    terceira_matriz.iloc[6, 2] = inverso_c4_3
                    terceira_matriz.iloc[7, 2] = inverso_c5_3
                    terceira_matriz.iloc[8, 2] = inverso_c6_3
                    terceira_matriz.iloc[9, 2] = inverso_c7_3
                    terceira_matriz.iloc[10, 2] = inverso_c8_3
                    terceira_matriz.iloc[11, 2] = inverso_c9_3
                    terceira_matriz.iloc[12, 2] = inverso_c10_3
                    terceira_matriz.iloc[13, 2] = inverso_c11_3
                    terceira_matriz.iloc[14, 2] = inverso_c12_3


                    #Critério 4
                    c1_4 = terceira_matriz.iloc[3, 4]
                    c2_4 = terceira_matriz.iloc[3, 5]
                    c3_4 = terceira_matriz.iloc[3, 6]
                    c4_4 = terceira_matriz.iloc[3, 7]
                    c5_4 = terceira_matriz.iloc[3, 8]
                    c6_4 = terceira_matriz.iloc[3, 9]
                    c7_4 = terceira_matriz.iloc[3, 10]
                    c8_4 = terceira_matriz.iloc[3, 11]
                    c9_4 = terceira_matriz.iloc[3, 12]
                    c10_4 = terceira_matriz.iloc[3, 13]
                    c11_4 = terceira_matriz.iloc[3, 14]
                
                    # Calcular os inversos
                    inverso_c1_4 = 1 / c1_4
                    inverso_c2_4 = 1 / c2_4
                    inverso_c3_4 = 1 / c3_4
                    inverso_c4_4 = 1 / c4_4
                    inverso_c5_4 = 1 / c5_4
                    inverso_c6_4 = 1 / c6_4
                    inverso_c7_4 = 1 / c7_4
                    inverso_c8_4 = 1 / c8_4
                    inverso_c9_4 = 1 / c9_4
                    inverso_c10_4 = 1 / c10_4
                    inverso_c11_4 = 1 / c11_4
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[4, 3] = inverso_c1_4
                    terceira_matriz.iloc[5, 3] = inverso_c2_4
                    terceira_matriz.iloc[6, 3] = inverso_c3_4
                    terceira_matriz.iloc[7, 3] = inverso_c4_4
                    terceira_matriz.iloc[8, 3] = inverso_c5_4
                    terceira_matriz.iloc[9, 3] = inverso_c6_4
                    terceira_matriz.iloc[10, 3] = inverso_c7_4
                    terceira_matriz.iloc[11, 3] = inverso_c8_4
                    terceira_matriz.iloc[12, 3] = inverso_c9_4
                    terceira_matriz.iloc[13, 3] = inverso_c10_4
                    terceira_matriz.iloc[14, 3] = inverso_c11_4


                    #Critério 5
                    c1_5 = terceira_matriz.iloc[4, 5]
                    c2_5 = terceira_matriz.iloc[4, 6]
                    c3_5 = terceira_matriz.iloc[4, 7]
                    c4_5 = terceira_matriz.iloc[4, 8]
                    c5_5 = terceira_matriz.iloc[4, 9]
                    c6_5 = terceira_matriz.iloc[4, 10]
                    c7_5 = terceira_matriz.iloc[4, 11]
                    c8_5 = terceira_matriz.iloc[4, 12]
                    c9_5 = terceira_matriz.iloc[4, 13]
                    c10_5 = terceira_matriz.iloc[4, 14]
                                    
                    # Calcular os inversos
                    inverso_c1_5 = 1 / c1_5
                    inverso_c2_5 = 1 / c2_5
                    inverso_c3_5 = 1 / c3_5
                    inverso_c4_5 = 1 / c4_5
                    inverso_c5_5 = 1 / c5_5
                    inverso_c6_5 = 1 / c6_5
                    inverso_c7_5 = 1 / c7_5
                    inverso_c8_5 = 1 / c8_5
                    inverso_c9_5 = 1 / c9_5
                    inverso_c10_5 = 1 / c10_5
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[5, 4] = inverso_c1_5
                    terceira_matriz.iloc[6, 4] = inverso_c2_5
                    terceira_matriz.iloc[7, 4] = inverso_c3_5
                    terceira_matriz.iloc[8, 4] = inverso_c4_5
                    terceira_matriz.iloc[9, 4] = inverso_c5_5
                    terceira_matriz.iloc[10, 4] = inverso_c6_5
                    terceira_matriz.iloc[11, 4] = inverso_c7_5
                    terceira_matriz.iloc[12, 4] = inverso_c8_5
                    terceira_matriz.iloc[13, 4] = inverso_c9_5
                    terceira_matriz.iloc[14, 4] = inverso_c10_5


                     #Critério 6
                    c1_6 = terceira_matriz.iloc[5, 6]
                    c2_6 = terceira_matriz.iloc[5, 7]
                    c3_6 = terceira_matriz.iloc[5, 8]
                    c4_6 = terceira_matriz.iloc[5, 9]
                    c5_6 = terceira_matriz.iloc[5, 10]
                    c6_6 = terceira_matriz.iloc[5, 11]
                    c7_6 = terceira_matriz.iloc[5, 12]
                    c8_6 = terceira_matriz.iloc[5, 13]
                    c9_6 = terceira_matriz.iloc[5, 14]
                                    
                                    
                    # Calcular os inversos
                    inverso_c1_6 = 1 / c1_6
                    inverso_c2_6 = 1 / c2_6
                    inverso_c3_6 = 1 / c3_6
                    inverso_c4_6 = 1 / c4_6
                    inverso_c5_6 = 1 / c5_6
                    inverso_c6_6 = 1 / c6_6
                    inverso_c7_6 = 1 / c7_6
                    inverso_c8_6 = 1 / c8_6
                    inverso_c9_6 = 1 / c9_6
                                      
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[6, 5] = inverso_c1_6
                    terceira_matriz.iloc[7, 5] = inverso_c2_6
                    terceira_matriz.iloc[8, 5] = inverso_c3_6
                    terceira_matriz.iloc[9, 5] = inverso_c4_6
                    terceira_matriz.iloc[10, 5] = inverso_c5_6
                    terceira_matriz.iloc[11, 5] = inverso_c6_6
                    terceira_matriz.iloc[12, 5] = inverso_c7_6
                    terceira_matriz.iloc[13, 5] = inverso_c8_6
                    terceira_matriz.iloc[14, 5] = inverso_c9_6


                       #Critério 7
                    c1_7 = terceira_matriz.iloc[6, 7]
                    c2_7 = terceira_matriz.iloc[6, 8]
                    c3_7 = terceira_matriz.iloc[6, 9]
                    c4_7 = terceira_matriz.iloc[6, 10]
                    c5_7 = terceira_matriz.iloc[6, 11]
                    c6_7 = terceira_matriz.iloc[6, 12]
                    c7_7 = terceira_matriz.iloc[6, 13]
                    c8_7 = terceira_matriz.iloc[6, 14]
                                    
                    # Calcular os inversos
                    inverso_c1_7 = 1 / c1_7
                    inverso_c2_7 = 1 / c2_7
                    inverso_c3_7 = 1 / c3_7
                    inverso_c4_7 = 1 / c4_7
                    inverso_c5_7 = 1 / c5_7
                    inverso_c6_7 = 1 / c6_7
                    inverso_c7_7 = 1 / c7_7
                    inverso_c8_7 = 1 / c8_7
                    
                                     
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[7, 6] = inverso_c1_7
                    terceira_matriz.iloc[8, 6] = inverso_c2_7
                    terceira_matriz.iloc[9, 6] = inverso_c3_7
                    terceira_matriz.iloc[10, 6] = inverso_c4_7
                    terceira_matriz.iloc[11, 6] = inverso_c5_7
                    terceira_matriz.iloc[12, 6] = inverso_c6_7
                    terceira_matriz.iloc[13, 6] = inverso_c7_7
                    terceira_matriz.iloc[14, 6] = inverso_c8_7


                    #Critério 8
                    c1_8 = terceira_matriz.iloc[7,8]
                    c2_8 = terceira_matriz.iloc[7,9]
                    c3_8 = terceira_matriz.iloc[7,10]
                    c4_8 = terceira_matriz.iloc[7,11]
                    c5_8 = terceira_matriz.iloc[7,12]
                    c6_8 = terceira_matriz.iloc[7,13]
                    c7_8 = terceira_matriz.iloc[7,14]
                                    
                    # Calcular os inversos
                    inverso_c1_8 = 1 / c1_8
                    inverso_c2_8 = 1 / c2_8
                    inverso_c3_8 = 1 / c3_8
                    inverso_c4_8 = 1 / c4_8
                    inverso_c5_8 = 1 / c5_8
                    inverso_c6_8 = 1 / c6_8
                    inverso_c7_8 = 1 / c7_8
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[8, 7] = inverso_c1_8
                    terceira_matriz.iloc[9, 7] = inverso_c2_8
                    terceira_matriz.iloc[10, 7] = inverso_c3_8
                    terceira_matriz.iloc[11, 7] = inverso_c4_8
                    terceira_matriz.iloc[12, 7] = inverso_c5_8
                    terceira_matriz.iloc[13, 7] = inverso_c6_8
                    terceira_matriz.iloc[14, 7] = inverso_c7_8

                    #Critério 9
                    c1_9 = terceira_matriz.iloc[8, 9]
                    c2_9 = terceira_matriz.iloc[8, 10]
                    c3_9 = terceira_matriz.iloc[8, 11]
                    c4_9 = terceira_matriz.iloc[8, 12]
                    c5_9 = terceira_matriz.iloc[8, 13]
                    c6_9 = terceira_matriz.iloc[8, 14]
                                    
                    # Calcular os inversos
                    inverso_c1_9 = 1 / c1_9
                    inverso_c2_9 = 1 / c2_9
                    inverso_c3_9 = 1 / c3_9
                    inverso_c4_9 = 1 / c4_9
                    inverso_c5_9 = 1 / c5_9
                    inverso_c6_9 = 1 / c6_9
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[9, 8] = inverso_c1_9
                    terceira_matriz.iloc[10, 8] = inverso_c2_9
                    terceira_matriz.iloc[11, 8] = inverso_c3_9 
                    terceira_matriz.iloc[12, 8] = inverso_c4_9 
                    terceira_matriz.iloc[13, 8] = inverso_c5_9
                    terceira_matriz.iloc[14, 8] = inverso_c6_9  
                    
                     #Critério 10
                    c1_10 = terceira_matriz.iloc[9,10]
                    c2_10 = terceira_matriz.iloc[9,11]
                    c3_10 = terceira_matriz.iloc[9,12]
                    c4_10 = terceira_matriz.iloc[9,13]
                    c5_10 = terceira_matriz.iloc[9,14]
                                                        
                    # Calcular os inversos
                    inverso_c1_10 = 1 / c1_10
                    inverso_c2_10 = 1 / c2_10
                    inverso_c3_10 = 1 / c3_10
                    inverso_c4_10 = 1 / c4_10
                    inverso_c5_10 = 1 / c5_10
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[10, 9] = inverso_c1_10
                    terceira_matriz.iloc[11, 9] = inverso_c2_10
                    terceira_matriz.iloc[12, 9] = inverso_c3_10
                    terceira_matriz.iloc[13, 9] = inverso_c4_10
                    terceira_matriz.iloc[14, 9] = inverso_c5_10


                    #Critério 11
                    c1_11 = terceira_matriz.iloc[10,11]
                    c2_11 = terceira_matriz.iloc[10,12]
                    c3_11 = terceira_matriz.iloc[10,13]
                    c4_11 = terceira_matriz.iloc[10,14]
                                     
                                                                    
                    # Calcular os inversos
                    inverso_c1_11 = 1 / c1_11
                    inverso_c2_11 = 1 / c2_11
                    inverso_c3_11 = 1 / c3_11
                    inverso_c4_11 = 1 / c4_11
                                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[11, 10] = inverso_c1_11
                    terceira_matriz.iloc[12, 10] = inverso_c2_11
                    terceira_matriz.iloc[13, 10] = inverso_c3_11
                    terceira_matriz.iloc[14, 10] = inverso_c4_11
                
                                       
                     #Critério 12
                    c1_12 = terceira_matriz.iloc[11,12]
                    c2_12 = terceira_matriz.iloc[11,13]
                    c3_12 = terceira_matriz.iloc[11,14]
                                                     
                    # Calcular os inversos
                    inverso_c1_12 = 1 / c1_12
                    inverso_c2_12 = 1 / c2_12
                    inverso_c3_12 = 1 / c3_12
                                   
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[12, 11] = inverso_c1_12
                    terceira_matriz.iloc[13, 11] = inverso_c2_12
                    terceira_matriz.iloc[14, 11] = inverso_c3_12     
                                         
                     #Critério 13
                    c1_13 = terceira_matriz.iloc[12,13]
                    c2_13 = terceira_matriz.iloc[12,14]
                                                     
                    # Calcular os inversos
                    inverso_c1_13 = 1 / c1_13
                    inverso_c2_13 = 1 / c2_13
                                   
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[13, 12] = inverso_c1_13
                    terceira_matriz.iloc[14, 12] = inverso_c2_13   
                    
                    #Critério 14
                    c1_14 = terceira_matriz.iloc[13,14]
                  
                                                     
                    # Calcular os inversos
                    inverso_c1_14 = 1 / c1_14
                                                       
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[14, 13] = inverso_c1_14


    if num_critérios == 16:
        for i in range(2, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[1, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[1, i] = item["valor"]
                     

        for i in range(3, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[2, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[2, i] = item["valor"]
                     

        for i in range(4, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[3, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[3, i] = item["valor"]
                     

        for i in range(5, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[4, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[4, i] = item["valor"]

        for i in range(6, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[5, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[5, i] = item["valor"]
        
        for i in range(7, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[6, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[6, i] = item["valor"]
        for i in range(8, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[7, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[7, i] = item["valor"]
        for i in range(9, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[8, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[8, i] = item["valor"]
        for i in range(10, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[9, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[9, i] = item["valor"]

        for i in range(11, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[10, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[10, i] = item["valor"]
        
        for i in range(12, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[11, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[11, i] = item["valor"]
        
        for i in range(13, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[12, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[12, i] = item["valor"]
        
        for i in range(14, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[13, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[13, i] = item["valor"]

        for i in range(15, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[14, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[14, i] = item["valor"]

                    #Inverter a Terceira Matriz
                    #Critério 1
                    c1 = terceira_matriz.iloc[0, 1]
                    c2 = terceira_matriz.iloc[0, 2]
                    c3 = terceira_matriz.iloc[0, 3]
                    c4 = terceira_matriz.iloc[0, 4]
                    c5 = terceira_matriz.iloc[0, 5]
                    c6 = terceira_matriz.iloc[0, 6]
                    c7 = terceira_matriz.iloc[0, 7]
                    c8 = terceira_matriz.iloc[0, 8]
                    c9 = terceira_matriz.iloc[0, 9]
                    c10 = terceira_matriz.iloc[0, 10]
                    c11 = terceira_matriz.iloc[0, 11]
                    c12 = terceira_matriz.iloc[0, 12]
                    c13 = terceira_matriz.iloc[0, 13]
                    c14 = terceira_matriz.iloc[0, 14]
                    c15 = terceira_matriz.iloc[0, 15]
                
                    # Calcular os inversos
                    inverso_c1 = 1 / c1
                    inverso_c2 = 1 / c2
                    inverso_c3 = 1 / c3
                    inverso_c4 = 1 / c4
                    inverso_c5 = 1 / c5
                    inverso_c6 = 1 / c6
                    inverso_c7 = 1 / c7
                    inverso_c8 = 1 / c8
                    inverso_c9 = 1 / c9
                    inverso_c10 = 1 / c10
                    inverso_c11 = 1 / c11
                    inverso_c12 = 1 / c12
                    inverso_c13 = 1 / c13
                    inverso_c14 = 1 / c14
                    inverso_c15 = 1 / c15


                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[1, 0] = inverso_c1
                    terceira_matriz.iloc[2, 0] = inverso_c2
                    terceira_matriz.iloc[3, 0] = inverso_c3
                    terceira_matriz.iloc[4, 0] = inverso_c4
                    terceira_matriz.iloc[5, 0] = inverso_c5
                    terceira_matriz.iloc[6, 0] = inverso_c6
                    terceira_matriz.iloc[7, 0] = inverso_c7
                    terceira_matriz.iloc[8, 0] = inverso_c8
                    terceira_matriz.iloc[9, 0] = inverso_c9
                    terceira_matriz.iloc[10, 0] = inverso_c10
                    terceira_matriz.iloc[11, 0] = inverso_c11
                    terceira_matriz.iloc[12, 0] = inverso_c12
                    terceira_matriz.iloc[13, 0] = inverso_c13
                    terceira_matriz.iloc[14, 0] = inverso_c14
                    terceira_matriz.iloc[15, 0] = inverso_c15
                
                    #Critério 2
                    c1_2 = terceira_matriz.iloc[1, 2]
                    c2_2 = terceira_matriz.iloc[1, 3]
                    c3_2 = terceira_matriz.iloc[1, 4]
                    c4_2 = terceira_matriz.iloc[1, 5]
                    c5_2 = terceira_matriz.iloc[1, 6]
                    c6_2 = terceira_matriz.iloc[1, 7]
                    c7_2 = terceira_matriz.iloc[1, 8]
                    c8_2 = terceira_matriz.iloc[1, 9]
                    c9_2 = terceira_matriz.iloc[1, 10]
                    c10_2 = terceira_matriz.iloc[1, 11]
                    c11_2 = terceira_matriz.iloc[1, 12]
                    c12_2 = terceira_matriz.iloc[1, 13]
                    c13_2 = terceira_matriz.iloc[1, 14]
                    c14_2 = terceira_matriz.iloc[1, 15]
                    
                
                    # Calcular os inversos
                    inverso_c1_2 = 1 / c1_2
                    inverso_c2_2 = 1 / c2_2
                    inverso_c3_2 = 1 / c3_2
                    inverso_c4_2 = 1 / c4_2
                    inverso_c5_2 = 1 / c5_2
                    inverso_c6_2 = 1 / c6_2
                    inverso_c7_2 = 1 / c7_2
                    inverso_c8_2 = 1 / c8_2
                    inverso_c9_2 = 1 / c9_2
                    inverso_c10_2 = 1 / c10_2
                    inverso_c11_2 = 1 / c11_2
                    inverso_c12_2 = 1 / c12_2
                    inverso_c13_2 = 1 / c13_2
                    inverso_c14_2 = 1 / c14_2



                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[2, 1] = inverso_c1_2
                    terceira_matriz.iloc[3, 1] = inverso_c2_2
                    terceira_matriz.iloc[4, 1] = inverso_c3_2
                    terceira_matriz.iloc[5, 1] = inverso_c4_2
                    terceira_matriz.iloc[6, 1] = inverso_c5_2
                    terceira_matriz.iloc[7, 1] = inverso_c6_2
                    terceira_matriz.iloc[8, 1] = inverso_c7_2
                    terceira_matriz.iloc[9, 1] = inverso_c8_2
                    terceira_matriz.iloc[10, 1] = inverso_c9_2
                    terceira_matriz.iloc[11, 1] = inverso_c10_2
                    terceira_matriz.iloc[12, 1] = inverso_c11_2
                    terceira_matriz.iloc[13, 1] = inverso_c12_2
                    terceira_matriz.iloc[14, 1] = inverso_c13_2
                    terceira_matriz.iloc[15, 1] = inverso_c14_2
                    
                
                    #Critério 3
                    c1_3 = terceira_matriz.iloc[2, 3]
                    c2_3 = terceira_matriz.iloc[2, 4]
                    c3_3 = terceira_matriz.iloc[2, 5]
                    c4_3 = terceira_matriz.iloc[2, 6]
                    c5_3 = terceira_matriz.iloc[2, 7]
                    c6_3 = terceira_matriz.iloc[2, 8]
                    c7_3 = terceira_matriz.iloc[2, 9]
                    c8_3 = terceira_matriz.iloc[2, 10]
                    c9_3 = terceira_matriz.iloc[2, 11]
                    c10_3 = terceira_matriz.iloc[2, 12]
                    c11_3 = terceira_matriz.iloc[2, 13]
                    c12_3 = terceira_matriz.iloc[2, 14]
                    c13_3 = terceira_matriz.iloc[2, 15]

                    # Calcular os inversos
                    inverso_c1_3 = 1 / c1_3
                    inverso_c2_3 = 1 / c2_3
                    inverso_c3_3 = 1 / c3_3
                    inverso_c4_3 = 1 / c4_3
                    inverso_c5_3 = 1 / c5_3
                    inverso_c6_3 = 1 / c6_3
                    inverso_c7_3 = 1 / c7_3
                    inverso_c8_3 = 1 / c8_3
                    inverso_c9_3 = 1 / c9_3
                    inverso_c10_3 = 1 / c10_3
                    inverso_c11_3 = 1 / c11_3
                    inverso_c12_3 = 1 / c12_3
                    inverso_c13_3 = 1 / c13_3
                
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[3, 2] = inverso_c1_3
                    terceira_matriz.iloc[4, 2] = inverso_c2_3
                    terceira_matriz.iloc[5, 2] = inverso_c3_3
                    terceira_matriz.iloc[6, 2] = inverso_c4_3
                    terceira_matriz.iloc[7, 2] = inverso_c5_3
                    terceira_matriz.iloc[8, 2] = inverso_c6_3
                    terceira_matriz.iloc[9, 2] = inverso_c7_3
                    terceira_matriz.iloc[10, 2] = inverso_c8_3
                    terceira_matriz.iloc[11, 2] = inverso_c9_3
                    terceira_matriz.iloc[12, 2] = inverso_c10_3
                    terceira_matriz.iloc[13, 2] = inverso_c11_3
                    terceira_matriz.iloc[14, 2] = inverso_c12_3
                    terceira_matriz.iloc[15, 2] = inverso_c13_3


                    #Critério 4
                    c1_4 = terceira_matriz.iloc[3, 4]
                    c2_4 = terceira_matriz.iloc[3, 5]
                    c3_4 = terceira_matriz.iloc[3, 6]
                    c4_4 = terceira_matriz.iloc[3, 7]
                    c5_4 = terceira_matriz.iloc[3, 8]
                    c6_4 = terceira_matriz.iloc[3, 9]
                    c7_4 = terceira_matriz.iloc[3, 10]
                    c8_4 = terceira_matriz.iloc[3, 11]
                    c9_4 = terceira_matriz.iloc[3, 12]
                    c10_4 = terceira_matriz.iloc[3, 13]
                    c11_4 = terceira_matriz.iloc[3, 14]
                    c12_4 = terceira_matriz.iloc[3, 15]
                
                    # Calcular os inversos
                    inverso_c1_4 = 1 / c1_4
                    inverso_c2_4 = 1 / c2_4
                    inverso_c3_4 = 1 / c3_4
                    inverso_c4_4 = 1 / c4_4
                    inverso_c5_4 = 1 / c5_4
                    inverso_c6_4 = 1 / c6_4
                    inverso_c7_4 = 1 / c7_4
                    inverso_c8_4 = 1 / c8_4
                    inverso_c9_4 = 1 / c9_4
                    inverso_c10_4 = 1 / c10_4
                    inverso_c11_4 = 1 / c11_4
                    inverso_c12_4 = 1 / c12_4
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[4, 3] = inverso_c1_4
                    terceira_matriz.iloc[5, 3] = inverso_c2_4
                    terceira_matriz.iloc[6, 3] = inverso_c3_4
                    terceira_matriz.iloc[7, 3] = inverso_c4_4
                    terceira_matriz.iloc[8, 3] = inverso_c5_4
                    terceira_matriz.iloc[9, 3] = inverso_c6_4
                    terceira_matriz.iloc[10, 3] = inverso_c7_4
                    terceira_matriz.iloc[11, 3] = inverso_c8_4
                    terceira_matriz.iloc[12, 3] = inverso_c9_4
                    terceira_matriz.iloc[13, 3] = inverso_c10_4
                    terceira_matriz.iloc[14, 3] = inverso_c11_4
                    terceira_matriz.iloc[15, 3] = inverso_c12_4


                    #Critério 5
                    c1_5 = terceira_matriz.iloc[4, 5]
                    c2_5 = terceira_matriz.iloc[4, 6]
                    c3_5 = terceira_matriz.iloc[4, 7]
                    c4_5 = terceira_matriz.iloc[4, 8]
                    c5_5 = terceira_matriz.iloc[4, 9]
                    c6_5 = terceira_matriz.iloc[4, 10]
                    c7_5 = terceira_matriz.iloc[4, 11]
                    c8_5 = terceira_matriz.iloc[4, 12]
                    c9_5 = terceira_matriz.iloc[4, 13]
                    c10_5 = terceira_matriz.iloc[4, 14]
                    c11_5 = terceira_matriz.iloc[4, 15]
                                    
                    # Calcular os inversos
                    inverso_c1_5 = 1 / c1_5
                    inverso_c2_5 = 1 / c2_5
                    inverso_c3_5 = 1 / c3_5
                    inverso_c4_5 = 1 / c4_5
                    inverso_c5_5 = 1 / c5_5
                    inverso_c6_5 = 1 / c6_5
                    inverso_c7_5 = 1 / c7_5
                    inverso_c8_5 = 1 / c8_5
                    inverso_c9_5 = 1 / c9_5
                    inverso_c10_5 = 1 / c10_5
                    inverso_c11_5 = 1 / c11_5
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[5, 4] = inverso_c1_5
                    terceira_matriz.iloc[6, 4] = inverso_c2_5
                    terceira_matriz.iloc[7, 4] = inverso_c3_5
                    terceira_matriz.iloc[8, 4] = inverso_c4_5
                    terceira_matriz.iloc[9, 4] = inverso_c5_5
                    terceira_matriz.iloc[10, 4] = inverso_c6_5
                    terceira_matriz.iloc[11, 4] = inverso_c7_5
                    terceira_matriz.iloc[12, 4] = inverso_c8_5
                    terceira_matriz.iloc[13, 4] = inverso_c9_5
                    terceira_matriz.iloc[14, 4] = inverso_c10_5
                    terceira_matriz.iloc[15, 4] = inverso_c11_5


                     #Critério 6
                    c1_6 = terceira_matriz.iloc[5, 6]
                    c2_6 = terceira_matriz.iloc[5, 7]
                    c3_6 = terceira_matriz.iloc[5, 8]
                    c4_6 = terceira_matriz.iloc[5, 9]
                    c5_6 = terceira_matriz.iloc[5, 10]
                    c6_6 = terceira_matriz.iloc[5, 11]
                    c7_6 = terceira_matriz.iloc[5, 12]
                    c8_6 = terceira_matriz.iloc[5, 13]
                    c9_6 = terceira_matriz.iloc[5, 14]
                    c10_6 = terceira_matriz.iloc[5, 15]
                                    
                                    
                    # Calcular os inversos
                    inverso_c1_6 = 1 / c1_6
                    inverso_c2_6 = 1 / c2_6
                    inverso_c3_6 = 1 / c3_6
                    inverso_c4_6 = 1 / c4_6
                    inverso_c5_6 = 1 / c5_6
                    inverso_c6_6 = 1 / c6_6
                    inverso_c7_6 = 1 / c7_6
                    inverso_c8_6 = 1 / c8_6
                    inverso_c9_6 = 1 / c9_6
                    inverso_c10_6 = 1 / c10_6
                                      
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[6, 5] = inverso_c1_6
                    terceira_matriz.iloc[7, 5] = inverso_c2_6
                    terceira_matriz.iloc[8, 5] = inverso_c3_6
                    terceira_matriz.iloc[9, 5] = inverso_c4_6
                    terceira_matriz.iloc[10, 5] = inverso_c5_6
                    terceira_matriz.iloc[11, 5] = inverso_c6_6
                    terceira_matriz.iloc[12, 5] = inverso_c7_6
                    terceira_matriz.iloc[13, 5] = inverso_c8_6
                    terceira_matriz.iloc[14, 5] = inverso_c9_6
                    terceira_matriz.iloc[15, 5] = inverso_c10_6


                    #Critério 7
                    c1_7 = terceira_matriz.iloc[6, 7]
                    c2_7 = terceira_matriz.iloc[6, 8]
                    c3_7 = terceira_matriz.iloc[6, 9]
                    c4_7 = terceira_matriz.iloc[6, 10]
                    c5_7 = terceira_matriz.iloc[6, 11]
                    c6_7 = terceira_matriz.iloc[6, 12]
                    c7_7 = terceira_matriz.iloc[6, 13]
                    c8_7 = terceira_matriz.iloc[6, 14]
                    c9_7 = terceira_matriz.iloc[6, 15]
                                    
                    # Calcular os inversos
                    inverso_c1_7 = 1 / c1_7
                    inverso_c2_7 = 1 / c2_7
                    inverso_c3_7 = 1 / c3_7
                    inverso_c4_7 = 1 / c4_7
                    inverso_c5_7 = 1 / c5_7
                    inverso_c6_7 = 1 / c6_7
                    inverso_c7_7 = 1 / c7_7
                    inverso_c8_7 = 1 / c8_7
                    inverso_c9_7 = 1 / c9_7
                                                         
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[7, 6] = inverso_c1_7
                    terceira_matriz.iloc[8, 6] = inverso_c2_7
                    terceira_matriz.iloc[9, 6] = inverso_c3_7
                    terceira_matriz.iloc[10, 6] = inverso_c4_7
                    terceira_matriz.iloc[11, 6] = inverso_c5_7
                    terceira_matriz.iloc[12, 6] = inverso_c6_7
                    terceira_matriz.iloc[13, 6] = inverso_c7_7
                    terceira_matriz.iloc[14, 6] = inverso_c8_7
                    terceira_matriz.iloc[15, 6] = inverso_c9_7


                    #Critério 8
                    c1_8 = terceira_matriz.iloc[7,8]
                    c2_8 = terceira_matriz.iloc[7,9]
                    c3_8 = terceira_matriz.iloc[7,10]
                    c4_8 = terceira_matriz.iloc[7,11]
                    c5_8 = terceira_matriz.iloc[7,12]
                    c6_8 = terceira_matriz.iloc[7,13]
                    c7_8 = terceira_matriz.iloc[7,14]
                    c8_8 = terceira_matriz.iloc[7,15]
                                    
                    # Calcular os inversos
                    inverso_c1_8 = 1 / c1_8
                    inverso_c2_8 = 1 / c2_8
                    inverso_c3_8 = 1 / c3_8
                    inverso_c4_8 = 1 / c4_8
                    inverso_c5_8 = 1 / c5_8
                    inverso_c6_8 = 1 / c6_8
                    inverso_c7_8 = 1 / c7_8
                    inverso_c8_8 = 1 / c8_8
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[8, 7] = inverso_c1_8
                    terceira_matriz.iloc[9, 7] = inverso_c2_8
                    terceira_matriz.iloc[10, 7] = inverso_c3_8
                    terceira_matriz.iloc[11, 7] = inverso_c4_8
                    terceira_matriz.iloc[12, 7] = inverso_c5_8
                    terceira_matriz.iloc[13, 7] = inverso_c6_8
                    terceira_matriz.iloc[14, 7] = inverso_c7_8
                    terceira_matriz.iloc[15, 7] = inverso_c8_8

                    #Critério 9
                    c1_9 = terceira_matriz.iloc[8, 9]
                    c2_9 = terceira_matriz.iloc[8, 10]
                    c3_9 = terceira_matriz.iloc[8, 11]
                    c4_9 = terceira_matriz.iloc[8, 12]
                    c5_9 = terceira_matriz.iloc[8, 13]
                    c6_9 = terceira_matriz.iloc[8, 14]
                    c7_9 = terceira_matriz.iloc[8, 15]
                                    
                    # Calcular os inversos
                    inverso_c1_9 = 1 / c1_9
                    inverso_c2_9 = 1 / c2_9
                    inverso_c3_9 = 1 / c3_9
                    inverso_c4_9 = 1 / c4_9
                    inverso_c5_9 = 1 / c5_9
                    inverso_c6_9 = 1 / c6_9
                    inverso_c7_9 = 1 / c7_9
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[9, 8] = inverso_c1_9
                    terceira_matriz.iloc[10, 8] = inverso_c2_9
                    terceira_matriz.iloc[11, 8] = inverso_c3_9 
                    terceira_matriz.iloc[12, 8] = inverso_c4_9 
                    terceira_matriz.iloc[13, 8] = inverso_c5_9
                    terceira_matriz.iloc[14, 8] = inverso_c6_9 
                    terceira_matriz.iloc[15, 8] = inverso_c7_9   
                    
                     #Critério 10
                    c1_10 = terceira_matriz.iloc[9,10]
                    c2_10 = terceira_matriz.iloc[9,11]
                    c3_10 = terceira_matriz.iloc[9,12]
                    c4_10 = terceira_matriz.iloc[9,13]
                    c5_10 = terceira_matriz.iloc[9,14]
                    c6_10 = terceira_matriz.iloc[9,15]
                                                        
                    # Calcular os inversos
                    inverso_c1_10 = 1 / c1_10
                    inverso_c2_10 = 1 / c2_10
                    inverso_c3_10 = 1 / c3_10
                    inverso_c4_10 = 1 / c4_10
                    inverso_c5_10 = 1 / c5_10
                    inverso_c6_10 = 1 / c6_10
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[10, 9] = inverso_c1_10
                    terceira_matriz.iloc[11, 9] = inverso_c2_10
                    terceira_matriz.iloc[12, 9] = inverso_c3_10
                    terceira_matriz.iloc[13, 9] = inverso_c4_10
                    terceira_matriz.iloc[14, 9] = inverso_c5_10
                    terceira_matriz.iloc[15, 9] = inverso_c6_10


                    #Critério 11
                    c1_11 = terceira_matriz.iloc[10,11]
                    c2_11 = terceira_matriz.iloc[10,12]
                    c3_11 = terceira_matriz.iloc[10,13]
                    c4_11 = terceira_matriz.iloc[10,14]
                    c5_11 = terceira_matriz.iloc[10,15]
                                     
                                                                    
                    # Calcular os inversos
                    inverso_c1_11 = 1 / c1_11
                    inverso_c2_11 = 1 / c2_11
                    inverso_c3_11 = 1 / c3_11
                    inverso_c4_11 = 1 / c4_11
                    inverso_c5_11 = 1 / c5_11
                                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[11, 10] = inverso_c1_11
                    terceira_matriz.iloc[12, 10] = inverso_c2_11
                    terceira_matriz.iloc[13, 10] = inverso_c3_11
                    terceira_matriz.iloc[14, 10] = inverso_c4_11
                    terceira_matriz.iloc[15, 10] = inverso_c5_11
                
                                       
                     #Critério 12
                    c1_12 = terceira_matriz.iloc[11,12]
                    c2_12 = terceira_matriz.iloc[11,13]
                    c3_12 = terceira_matriz.iloc[11,14]
                    c4_12 = terceira_matriz.iloc[11,15]
                                                     
                    # Calcular os inversos
                    inverso_c1_12 = 1 / c1_12
                    inverso_c2_12 = 1 / c2_12
                    inverso_c3_12 = 1 / c3_12
                    inverso_c4_12 = 1 / c4_12
                                   
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[12, 11] = inverso_c1_12
                    terceira_matriz.iloc[13, 11] = inverso_c2_12
                    terceira_matriz.iloc[14, 11] = inverso_c3_12  
                    terceira_matriz.iloc[15, 11] = inverso_c4_12     
                                         
                     #Critério 13
                    c1_13 = terceira_matriz.iloc[12,13]
                    c2_13 = terceira_matriz.iloc[12,14]
                    c3_13 = terceira_matriz.iloc[12,15]
                                                     
                    # Calcular os inversos
                    inverso_c1_13 = 1 / c1_13
                    inverso_c2_13 = 1 / c2_13
                    inverso_c3_13 = 1 / c3_13
                                   
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[13, 12] = inverso_c1_13
                    terceira_matriz.iloc[14, 12] = inverso_c2_13
                    terceira_matriz.iloc[15, 12] = inverso_c3_13   
                    
                    #Critério 14
                    c1_14 = terceira_matriz.iloc[13,14]
                    c2_14 = terceira_matriz.iloc[13,15]
                                                                      
                    # Calcular os inversos
                    inverso_c1_14 = 1 / c1_14
                    inverso_c2_14 = 1 / c2_14
                                                       
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[14, 13] = inverso_c1_14
                    terceira_matriz.iloc[15, 13] = inverso_c2_14

                    #Critério 15
                    c1_15 = terceira_matriz.iloc[14,15]
                                                                
                    # Calcular os inversos
                    inverso_c1_15 = 1 / c1_15
                                                                           
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[15, 14] = inverso_c1_15

    if num_critérios == 17:
        for i in range(2, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[1, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[1, i] = item["valor"]
                     

        for i in range(3, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[2, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[2, i] = item["valor"]
                     

        for i in range(4, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[3, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[3, i] = item["valor"]
                     

        for i in range(5, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[4, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[4, i] = item["valor"]

        for i in range(6, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[5, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[5, i] = item["valor"]
        
        for i in range(7, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[6, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[6, i] = item["valor"]
        for i in range(8, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[7, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[7, i] = item["valor"]
        for i in range(9, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[8, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[8, i] = item["valor"]
        for i in range(10, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[9, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[9, i] = item["valor"]

        for i in range(11, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[10, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[10, i] = item["valor"]
        
        for i in range(12, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[11, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[11, i] = item["valor"]
        
        for i in range(13, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[12, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[12, i] = item["valor"]
        
        for i in range(14, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[13, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[13, i] = item["valor"]

        for i in range(15, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[14, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[14, i] = item["valor"]

        for i in range(16, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[15, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[15, i] = item["valor"]

                    #Inverter a Terceira Matriz
                    #Critério 1
                    c1 = terceira_matriz.iloc[0, 1]
                    c2 = terceira_matriz.iloc[0, 2]
                    c3 = terceira_matriz.iloc[0, 3]
                    c4 = terceira_matriz.iloc[0, 4]
                    c5 = terceira_matriz.iloc[0, 5]
                    c6 = terceira_matriz.iloc[0, 6]
                    c7 = terceira_matriz.iloc[0, 7]
                    c8 = terceira_matriz.iloc[0, 8]
                    c9 = terceira_matriz.iloc[0, 9]
                    c10 = terceira_matriz.iloc[0, 10]
                    c11 = terceira_matriz.iloc[0, 11]
                    c12 = terceira_matriz.iloc[0, 12]
                    c13 = terceira_matriz.iloc[0, 13]
                    c14 = terceira_matriz.iloc[0, 14]
                    c15 = terceira_matriz.iloc[0, 15]
                    c16 = terceira_matriz.iloc[0, 16]
                
                    # Calcular os inversos
                    inverso_c1 = 1 / c1
                    inverso_c2 = 1 / c2
                    inverso_c3 = 1 / c3
                    inverso_c4 = 1 / c4
                    inverso_c5 = 1 / c5
                    inverso_c6 = 1 / c6
                    inverso_c7 = 1 / c7
                    inverso_c8 = 1 / c8
                    inverso_c9 = 1 / c9
                    inverso_c10 = 1 / c10
                    inverso_c11 = 1 / c11
                    inverso_c12 = 1 / c12
                    inverso_c13 = 1 / c13
                    inverso_c14 = 1 / c14
                    inverso_c15 = 1 / c15
                    inverso_c16 = 1 / c16


                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[1, 0] = inverso_c1
                    terceira_matriz.iloc[2, 0] = inverso_c2
                    terceira_matriz.iloc[3, 0] = inverso_c3
                    terceira_matriz.iloc[4, 0] = inverso_c4
                    terceira_matriz.iloc[5, 0] = inverso_c5
                    terceira_matriz.iloc[6, 0] = inverso_c6
                    terceira_matriz.iloc[7, 0] = inverso_c7
                    terceira_matriz.iloc[8, 0] = inverso_c8
                    terceira_matriz.iloc[9, 0] = inverso_c9
                    terceira_matriz.iloc[10, 0] = inverso_c10
                    terceira_matriz.iloc[11, 0] = inverso_c11
                    terceira_matriz.iloc[12, 0] = inverso_c12
                    terceira_matriz.iloc[13, 0] = inverso_c13
                    terceira_matriz.iloc[14, 0] = inverso_c14
                    terceira_matriz.iloc[15, 0] = inverso_c15
                    terceira_matriz.iloc[16, 0] = inverso_c16
                
                    #Critério 2
                    c1_2 = terceira_matriz.iloc[1, 2]
                    c2_2 = terceira_matriz.iloc[1, 3]
                    c3_2 = terceira_matriz.iloc[1, 4]
                    c4_2 = terceira_matriz.iloc[1, 5]
                    c5_2 = terceira_matriz.iloc[1, 6]
                    c6_2 = terceira_matriz.iloc[1, 7]
                    c7_2 = terceira_matriz.iloc[1, 8]
                    c8_2 = terceira_matriz.iloc[1, 9]
                    c9_2 = terceira_matriz.iloc[1, 10]
                    c10_2 = terceira_matriz.iloc[1, 11]
                    c11_2 = terceira_matriz.iloc[1, 12]
                    c12_2 = terceira_matriz.iloc[1, 13]
                    c13_2 = terceira_matriz.iloc[1, 14]
                    c14_2 = terceira_matriz.iloc[1, 15]
                    c15_2 = terceira_matriz.iloc[1, 16]
                    
                
                    # Calcular os inversos
                    inverso_c1_2 = 1 / c1_2
                    inverso_c2_2 = 1 / c2_2
                    inverso_c3_2 = 1 / c3_2
                    inverso_c4_2 = 1 / c4_2
                    inverso_c5_2 = 1 / c5_2
                    inverso_c6_2 = 1 / c6_2
                    inverso_c7_2 = 1 / c7_2
                    inverso_c8_2 = 1 / c8_2
                    inverso_c9_2 = 1 / c9_2
                    inverso_c10_2 = 1 / c10_2
                    inverso_c11_2 = 1 / c11_2
                    inverso_c12_2 = 1 / c12_2
                    inverso_c13_2 = 1 / c13_2
                    inverso_c14_2 = 1 / c14_2
                    inverso_c15_2 = 1 / c15_2



                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[2, 1] = inverso_c1_2
                    terceira_matriz.iloc[3, 1] = inverso_c2_2
                    terceira_matriz.iloc[4, 1] = inverso_c3_2
                    terceira_matriz.iloc[5, 1] = inverso_c4_2
                    terceira_matriz.iloc[6, 1] = inverso_c5_2
                    terceira_matriz.iloc[7, 1] = inverso_c6_2
                    terceira_matriz.iloc[8, 1] = inverso_c7_2
                    terceira_matriz.iloc[9, 1] = inverso_c8_2
                    terceira_matriz.iloc[10, 1] = inverso_c9_2
                    terceira_matriz.iloc[11, 1] = inverso_c10_2
                    terceira_matriz.iloc[12, 1] = inverso_c11_2
                    terceira_matriz.iloc[13, 1] = inverso_c12_2
                    terceira_matriz.iloc[14, 1] = inverso_c13_2
                    terceira_matriz.iloc[15, 1] = inverso_c14_2
                    terceira_matriz.iloc[16, 1] = inverso_c15_2
                    
                
                    #Critério 3
                    c1_3 = terceira_matriz.iloc[2, 3]
                    c2_3 = terceira_matriz.iloc[2, 4]
                    c3_3 = terceira_matriz.iloc[2, 5]
                    c4_3 = terceira_matriz.iloc[2, 6]
                    c5_3 = terceira_matriz.iloc[2, 7]
                    c6_3 = terceira_matriz.iloc[2, 8]
                    c7_3 = terceira_matriz.iloc[2, 9]
                    c8_3 = terceira_matriz.iloc[2, 10]
                    c9_3 = terceira_matriz.iloc[2, 11]
                    c10_3 = terceira_matriz.iloc[2, 12]
                    c11_3 = terceira_matriz.iloc[2, 13]
                    c12_3 = terceira_matriz.iloc[2, 14]
                    c13_3 = terceira_matriz.iloc[2, 15]
                    c14_3 = terceira_matriz.iloc[2, 16]

                    # Calcular os inversos
                    inverso_c1_3 = 1 / c1_3
                    inverso_c2_3 = 1 / c2_3
                    inverso_c3_3 = 1 / c3_3
                    inverso_c4_3 = 1 / c4_3
                    inverso_c5_3 = 1 / c5_3
                    inverso_c6_3 = 1 / c6_3
                    inverso_c7_3 = 1 / c7_3
                    inverso_c8_3 = 1 / c8_3
                    inverso_c9_3 = 1 / c9_3
                    inverso_c10_3 = 1 / c10_3
                    inverso_c11_3 = 1 / c11_3
                    inverso_c12_3 = 1 / c12_3
                    inverso_c13_3 = 1 / c13_3
                    inverso_c14_3 = 1 / c14_3
                
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[3, 2] = inverso_c1_3
                    terceira_matriz.iloc[4, 2] = inverso_c2_3
                    terceira_matriz.iloc[5, 2] = inverso_c3_3
                    terceira_matriz.iloc[6, 2] = inverso_c4_3
                    terceira_matriz.iloc[7, 2] = inverso_c5_3
                    terceira_matriz.iloc[8, 2] = inverso_c6_3
                    terceira_matriz.iloc[9, 2] = inverso_c7_3
                    terceira_matriz.iloc[10, 2] = inverso_c8_3
                    terceira_matriz.iloc[11, 2] = inverso_c9_3
                    terceira_matriz.iloc[12, 2] = inverso_c10_3
                    terceira_matriz.iloc[13, 2] = inverso_c11_3
                    terceira_matriz.iloc[14, 2] = inverso_c12_3
                    terceira_matriz.iloc[15, 2] = inverso_c13_3
                    terceira_matriz.iloc[16, 2] = inverso_c14_3


                    #Critério 4
                    c1_4 = terceira_matriz.iloc[3, 4]
                    c2_4 = terceira_matriz.iloc[3, 5]
                    c3_4 = terceira_matriz.iloc[3, 6]
                    c4_4 = terceira_matriz.iloc[3, 7]
                    c5_4 = terceira_matriz.iloc[3, 8]
                    c6_4 = terceira_matriz.iloc[3, 9]
                    c7_4 = terceira_matriz.iloc[3, 10]
                    c8_4 = terceira_matriz.iloc[3, 11]
                    c9_4 = terceira_matriz.iloc[3, 12]
                    c10_4 = terceira_matriz.iloc[3, 13]
                    c11_4 = terceira_matriz.iloc[3, 14]
                    c12_4 = terceira_matriz.iloc[3, 15]
                    c13_4 = terceira_matriz.iloc[3, 16]
                
                    # Calcular os inversos
                    inverso_c1_4 = 1 / c1_4
                    inverso_c2_4 = 1 / c2_4
                    inverso_c3_4 = 1 / c3_4
                    inverso_c4_4 = 1 / c4_4
                    inverso_c5_4 = 1 / c5_4
                    inverso_c6_4 = 1 / c6_4
                    inverso_c7_4 = 1 / c7_4
                    inverso_c8_4 = 1 / c8_4
                    inverso_c9_4 = 1 / c9_4
                    inverso_c10_4 = 1 / c10_4
                    inverso_c11_4 = 1 / c11_4
                    inverso_c12_4 = 1 / c12_4
                    inverso_c13_4 = 1 / c13_4
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[4, 3] = inverso_c1_4
                    terceira_matriz.iloc[5, 3] = inverso_c2_4
                    terceira_matriz.iloc[6, 3] = inverso_c3_4
                    terceira_matriz.iloc[7, 3] = inverso_c4_4
                    terceira_matriz.iloc[8, 3] = inverso_c5_4
                    terceira_matriz.iloc[9, 3] = inverso_c6_4
                    terceira_matriz.iloc[10, 3] = inverso_c7_4
                    terceira_matriz.iloc[11, 3] = inverso_c8_4
                    terceira_matriz.iloc[12, 3] = inverso_c9_4
                    terceira_matriz.iloc[13, 3] = inverso_c10_4
                    terceira_matriz.iloc[14, 3] = inverso_c11_4
                    terceira_matriz.iloc[15, 3] = inverso_c12_4
                    terceira_matriz.iloc[16, 3] = inverso_c13_4


                    #Critério 5
                    c1_5 = terceira_matriz.iloc[4, 5]
                    c2_5 = terceira_matriz.iloc[4, 6]
                    c3_5 = terceira_matriz.iloc[4, 7]
                    c4_5 = terceira_matriz.iloc[4, 8]
                    c5_5 = terceira_matriz.iloc[4, 9]
                    c6_5 = terceira_matriz.iloc[4, 10]
                    c7_5 = terceira_matriz.iloc[4, 11]
                    c8_5 = terceira_matriz.iloc[4, 12]
                    c9_5 = terceira_matriz.iloc[4, 13]
                    c10_5 = terceira_matriz.iloc[4, 14]
                    c11_5 = terceira_matriz.iloc[4, 15]
                    c12_5 = terceira_matriz.iloc[4, 16]
                                    
                    # Calcular os inversos
                    inverso_c1_5 = 1 / c1_5
                    inverso_c2_5 = 1 / c2_5
                    inverso_c3_5 = 1 / c3_5
                    inverso_c4_5 = 1 / c4_5
                    inverso_c5_5 = 1 / c5_5
                    inverso_c6_5 = 1 / c6_5
                    inverso_c7_5 = 1 / c7_5
                    inverso_c8_5 = 1 / c8_5
                    inverso_c9_5 = 1 / c9_5
                    inverso_c10_5 = 1 / c10_5
                    inverso_c11_5 = 1 / c11_5
                    inverso_c12_5 = 1 / c12_5
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[5, 4] = inverso_c1_5
                    terceira_matriz.iloc[6, 4] = inverso_c2_5
                    terceira_matriz.iloc[7, 4] = inverso_c3_5
                    terceira_matriz.iloc[8, 4] = inverso_c4_5
                    terceira_matriz.iloc[9, 4] = inverso_c5_5
                    terceira_matriz.iloc[10, 4] = inverso_c6_5
                    terceira_matriz.iloc[11, 4] = inverso_c7_5
                    terceira_matriz.iloc[12, 4] = inverso_c8_5
                    terceira_matriz.iloc[13, 4] = inverso_c9_5
                    terceira_matriz.iloc[14, 4] = inverso_c10_5
                    terceira_matriz.iloc[15, 4] = inverso_c11_5
                    terceira_matriz.iloc[16, 4] = inverso_c12_5


                     #Critério 6
                    c1_6 = terceira_matriz.iloc[5, 6]
                    c2_6 = terceira_matriz.iloc[5, 7]
                    c3_6 = terceira_matriz.iloc[5, 8]
                    c4_6 = terceira_matriz.iloc[5, 9]
                    c5_6 = terceira_matriz.iloc[5, 10]
                    c6_6 = terceira_matriz.iloc[5, 11]
                    c7_6 = terceira_matriz.iloc[5, 12]
                    c8_6 = terceira_matriz.iloc[5, 13]
                    c9_6 = terceira_matriz.iloc[5, 14]
                    c10_6 = terceira_matriz.iloc[5, 15]
                    c11_6 = terceira_matriz.iloc[5, 16]
                                    
                                    
                    # Calcular os inversos
                    inverso_c1_6 = 1 / c1_6
                    inverso_c2_6 = 1 / c2_6
                    inverso_c3_6 = 1 / c3_6
                    inverso_c4_6 = 1 / c4_6
                    inverso_c5_6 = 1 / c5_6
                    inverso_c6_6 = 1 / c6_6
                    inverso_c7_6 = 1 / c7_6
                    inverso_c8_6 = 1 / c8_6
                    inverso_c9_6 = 1 / c9_6
                    inverso_c10_6 = 1 / c10_6
                    inverso_c11_6 = 1 / c11_6
                                      
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[6, 5] = inverso_c1_6
                    terceira_matriz.iloc[7, 5] = inverso_c2_6
                    terceira_matriz.iloc[8, 5] = inverso_c3_6
                    terceira_matriz.iloc[9, 5] = inverso_c4_6
                    terceira_matriz.iloc[10, 5] = inverso_c5_6
                    terceira_matriz.iloc[11, 5] = inverso_c6_6
                    terceira_matriz.iloc[12, 5] = inverso_c7_6
                    terceira_matriz.iloc[13, 5] = inverso_c8_6
                    terceira_matriz.iloc[14, 5] = inverso_c9_6
                    terceira_matriz.iloc[15, 5] = inverso_c10_6
                    terceira_matriz.iloc[16, 5] = inverso_c11_6


                    #Critério 7
                    c1_7 = terceira_matriz.iloc[6, 7]
                    c2_7 = terceira_matriz.iloc[6, 8]
                    c3_7 = terceira_matriz.iloc[6, 9]
                    c4_7 = terceira_matriz.iloc[6, 10]
                    c5_7 = terceira_matriz.iloc[6, 11]
                    c6_7 = terceira_matriz.iloc[6, 12]
                    c7_7 = terceira_matriz.iloc[6, 13]
                    c8_7 = terceira_matriz.iloc[6, 14]
                    c9_7 = terceira_matriz.iloc[6, 15]
                    c10_7 = terceira_matriz.iloc[6, 16]
                                    
                    # Calcular os inversos
                    inverso_c1_7 = 1 / c1_7
                    inverso_c2_7 = 1 / c2_7
                    inverso_c3_7 = 1 / c3_7
                    inverso_c4_7 = 1 / c4_7
                    inverso_c5_7 = 1 / c5_7
                    inverso_c6_7 = 1 / c6_7
                    inverso_c7_7 = 1 / c7_7
                    inverso_c8_7 = 1 / c8_7
                    inverso_c9_7 = 1 / c9_7
                    inverso_c10_7 = 1 / c10_7
                                                         
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[7, 6] = inverso_c1_7
                    terceira_matriz.iloc[8, 6] = inverso_c2_7
                    terceira_matriz.iloc[9, 6] = inverso_c3_7
                    terceira_matriz.iloc[10, 6] = inverso_c4_7
                    terceira_matriz.iloc[11, 6] = inverso_c5_7
                    terceira_matriz.iloc[12, 6] = inverso_c6_7
                    terceira_matriz.iloc[13, 6] = inverso_c7_7
                    terceira_matriz.iloc[14, 6] = inverso_c8_7
                    terceira_matriz.iloc[15, 6] = inverso_c9_7
                    terceira_matriz.iloc[16, 6] = inverso_c10_7


                    #Critério 8
                    c1_8 = terceira_matriz.iloc[7,8]
                    c2_8 = terceira_matriz.iloc[7,9]
                    c3_8 = terceira_matriz.iloc[7,10]
                    c4_8 = terceira_matriz.iloc[7,11]
                    c5_8 = terceira_matriz.iloc[7,12]
                    c6_8 = terceira_matriz.iloc[7,13]
                    c7_8 = terceira_matriz.iloc[7,14]
                    c8_8 = terceira_matriz.iloc[7,15]
                    c9_8 = terceira_matriz.iloc[7,16]
                                    
                    # Calcular os inversos
                    inverso_c1_8 = 1 / c1_8
                    inverso_c2_8 = 1 / c2_8
                    inverso_c3_8 = 1 / c3_8
                    inverso_c4_8 = 1 / c4_8
                    inverso_c5_8 = 1 / c5_8
                    inverso_c6_8 = 1 / c6_8
                    inverso_c7_8 = 1 / c7_8
                    inverso_c8_8 = 1 / c8_8
                    inverso_c9_8 = 1 / c9_8
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[8, 7] = inverso_c1_8
                    terceira_matriz.iloc[9, 7] = inverso_c2_8
                    terceira_matriz.iloc[10, 7] = inverso_c3_8
                    terceira_matriz.iloc[11, 7] = inverso_c4_8
                    terceira_matriz.iloc[12, 7] = inverso_c5_8
                    terceira_matriz.iloc[13, 7] = inverso_c6_8
                    terceira_matriz.iloc[14, 7] = inverso_c7_8
                    terceira_matriz.iloc[15, 7] = inverso_c8_8
                    terceira_matriz.iloc[16, 7] = inverso_c9_8

                    #Critério 9
                    c1_9 = terceira_matriz.iloc[8, 9]
                    c2_9 = terceira_matriz.iloc[8, 10]
                    c3_9 = terceira_matriz.iloc[8, 11]
                    c4_9 = terceira_matriz.iloc[8, 12]
                    c5_9 = terceira_matriz.iloc[8, 13]
                    c6_9 = terceira_matriz.iloc[8, 14]
                    c7_9 = terceira_matriz.iloc[8, 15]
                    c8_9 = terceira_matriz.iloc[8, 16]
                                    
                    # Calcular os inversos
                    inverso_c1_9 = 1 / c1_9
                    inverso_c2_9 = 1 / c2_9
                    inverso_c3_9 = 1 / c3_9
                    inverso_c4_9 = 1 / c4_9
                    inverso_c5_9 = 1 / c5_9
                    inverso_c6_9 = 1 / c6_9
                    inverso_c7_9 = 1 / c7_9
                    inverso_c8_9 = 1 / c8_9
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[9, 8] = inverso_c1_9
                    terceira_matriz.iloc[10, 8] = inverso_c2_9
                    terceira_matriz.iloc[11, 8] = inverso_c3_9 
                    terceira_matriz.iloc[12, 8] = inverso_c4_9 
                    terceira_matriz.iloc[13, 8] = inverso_c5_9
                    terceira_matriz.iloc[14, 8] = inverso_c6_9 
                    terceira_matriz.iloc[15, 8] = inverso_c7_9 
                    terceira_matriz.iloc[16, 8] = inverso_c8_9    
                    
                     #Critério 10
                    c1_10 = terceira_matriz.iloc[9,10]
                    c2_10 = terceira_matriz.iloc[9,11]
                    c3_10 = terceira_matriz.iloc[9,12]
                    c4_10 = terceira_matriz.iloc[9,13]
                    c5_10 = terceira_matriz.iloc[9,14]
                    c6_10 = terceira_matriz.iloc[9,15]
                    c7_10 = terceira_matriz.iloc[9,16]
                                                        
                    # Calcular os inversos
                    inverso_c1_10 = 1 / c1_10
                    inverso_c2_10 = 1 / c2_10
                    inverso_c3_10 = 1 / c3_10
                    inverso_c4_10 = 1 / c4_10
                    inverso_c5_10 = 1 / c5_10
                    inverso_c6_10 = 1 / c6_10
                    inverso_c7_10 = 1 / c7_10
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[10, 9] = inverso_c1_10
                    terceira_matriz.iloc[11, 9] = inverso_c2_10
                    terceira_matriz.iloc[12, 9] = inverso_c3_10
                    terceira_matriz.iloc[13, 9] = inverso_c4_10
                    terceira_matriz.iloc[14, 9] = inverso_c5_10
                    terceira_matriz.iloc[15, 9] = inverso_c6_10
                    terceira_matriz.iloc[16, 9] = inverso_c7_10


                    #Critério 11
                    c1_11 = terceira_matriz.iloc[10,11]
                    c2_11 = terceira_matriz.iloc[10,12]
                    c3_11 = terceira_matriz.iloc[10,13]
                    c4_11 = terceira_matriz.iloc[10,14]
                    c5_11 = terceira_matriz.iloc[10,15]
                    c6_11 = terceira_matriz.iloc[10,16]
                                     
                                                                    
                    # Calcular os inversos
                    inverso_c1_11 = 1 / c1_11
                    inverso_c2_11 = 1 / c2_11
                    inverso_c3_11 = 1 / c3_11
                    inverso_c4_11 = 1 / c4_11
                    inverso_c5_11 = 1 / c5_11
                    inverso_c6_11 = 1 / c6_11
                                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[11, 10] = inverso_c1_11
                    terceira_matriz.iloc[12, 10] = inverso_c2_11
                    terceira_matriz.iloc[13, 10] = inverso_c3_11
                    terceira_matriz.iloc[14, 10] = inverso_c4_11
                    terceira_matriz.iloc[15, 10] = inverso_c5_11
                    terceira_matriz.iloc[16, 10] = inverso_c6_11
                
                                       
                     #Critério 12
                    c1_12 = terceira_matriz.iloc[11,12]
                    c2_12 = terceira_matriz.iloc[11,13]
                    c3_12 = terceira_matriz.iloc[11,14]
                    c4_12 = terceira_matriz.iloc[11,15]
                    c5_12 = terceira_matriz.iloc[11,16]
                                                     
                    # Calcular os inversos
                    inverso_c1_12 = 1 / c1_12
                    inverso_c2_12 = 1 / c2_12
                    inverso_c3_12 = 1 / c3_12
                    inverso_c4_12 = 1 / c4_12
                    inverso_c5_12 = 1 / c5_12
                                   
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[12, 11] = inverso_c1_12
                    terceira_matriz.iloc[13, 11] = inverso_c2_12
                    terceira_matriz.iloc[14, 11] = inverso_c3_12  
                    terceira_matriz.iloc[15, 11] = inverso_c4_12 
                    terceira_matriz.iloc[16, 11] = inverso_c5_12     
                                         
                     #Critério 13
                    c1_13 = terceira_matriz.iloc[12,13]
                    c2_13 = terceira_matriz.iloc[12,14]
                    c3_13 = terceira_matriz.iloc[12,15]
                    c4_13 = terceira_matriz.iloc[12,16]
                                                     
                    # Calcular os inversos
                    inverso_c1_13 = 1 / c1_13
                    inverso_c2_13 = 1 / c2_13
                    inverso_c3_13 = 1 / c3_13
                    inverso_c4_13 = 1 / c4_13
                                   
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[13, 12] = inverso_c1_13
                    terceira_matriz.iloc[14, 12] = inverso_c2_13
                    terceira_matriz.iloc[15, 12] = inverso_c3_13 
                    terceira_matriz.iloc[16, 12] = inverso_c4_13   
                    
                    #Critério 14
                    c1_14 = terceira_matriz.iloc[13,14]
                    c2_14 = terceira_matriz.iloc[13,15]
                    c3_14 = terceira_matriz.iloc[13,16]
                                                                      
                    # Calcular os inversos
                    inverso_c1_14 = 1 / c1_14
                    inverso_c2_14 = 1 / c2_14
                    inverso_c3_14 = 1 / c3_14
                                                       
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[14, 13] = inverso_c1_14
                    terceira_matriz.iloc[15, 13] = inverso_c2_14
                    terceira_matriz.iloc[16, 13] = inverso_c3_14

                    #Critério 15
                    c1_15 = terceira_matriz.iloc[14,15]
                    c2_15 = terceira_matriz.iloc[14,16]
                                                                
                    # Calcular os inversos
                    inverso_c1_15 = 1 / c1_15
                    inverso_c2_15 = 1 / c2_15
                                                                           
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[15, 14] = inverso_c1_15
                    terceira_matriz.iloc[16, 14] = inverso_c2_15

                     #Critério 15
                    c1_15 = terceira_matriz.iloc[15,16]
                                                                
                    # Calcular os inversos
                    inverso_c1_15 = 1 / c1_15
                                                                           
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[16, 15] = inverso_c1_15
      
                    
    if num_critérios == 18:
        for i in range(2, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[1, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[1, i] = item["valor"]
                     

        for i in range(3, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[2, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[2, i] = item["valor"]
                     

        for i in range(4, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[3, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[3, i] = item["valor"]
                     

        for i in range(5, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[4, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[4, i] = item["valor"]

        for i in range(6, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[5, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[5, i] = item["valor"]
        
        for i in range(7, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[6, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[6, i] = item["valor"]
        for i in range(8, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[7, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[7, i] = item["valor"]
        for i in range(9, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[8, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[8, i] = item["valor"]
        for i in range(10, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[9, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[9, i] = item["valor"]

        for i in range(11, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[10, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[10, i] = item["valor"]
        
        for i in range(12, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[11, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[11, i] = item["valor"]
        
        for i in range(13, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[12, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[12, i] = item["valor"]
        
        for i in range(14, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[13, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[13, i] = item["valor"]

        for i in range(15, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[14, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[14, i] = item["valor"]

        for i in range(16, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[15, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[15, i] = item["valor"]
        
        for i in range(17, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[16, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[16, i] = item["valor"]

                              #Inverter a Terceira Matriz
                    #Critério 1
                    c1 = terceira_matriz.iloc[0, 1]
                    c2 = terceira_matriz.iloc[0, 2]
                    c3 = terceira_matriz.iloc[0, 3]
                    c4 = terceira_matriz.iloc[0, 4]
                    c5 = terceira_matriz.iloc[0, 5]
                    c6 = terceira_matriz.iloc[0, 6]
                    c7 = terceira_matriz.iloc[0, 7]
                    c8 = terceira_matriz.iloc[0, 8]
                    c9 = terceira_matriz.iloc[0, 9]
                    c10 = terceira_matriz.iloc[0, 10]
                    c11 = terceira_matriz.iloc[0, 11]
                    c12 = terceira_matriz.iloc[0, 12]
                    c13 = terceira_matriz.iloc[0, 13]
                    c14 = terceira_matriz.iloc[0, 14]
                    c15 = terceira_matriz.iloc[0, 15]
                    c16 = terceira_matriz.iloc[0, 16]
                    c17 = terceira_matriz.iloc[0, 17]
                
                    # Calcular os inversos
                    inverso_c1 = 1 / c1
                    inverso_c2 = 1 / c2
                    inverso_c3 = 1 / c3
                    inverso_c4 = 1 / c4
                    inverso_c5 = 1 / c5
                    inverso_c6 = 1 / c6
                    inverso_c7 = 1 / c7
                    inverso_c8 = 1 / c8
                    inverso_c9 = 1 / c9
                    inverso_c10 = 1 / c10
                    inverso_c11 = 1 / c11
                    inverso_c12 = 1 / c12
                    inverso_c13 = 1 / c13
                    inverso_c14 = 1 / c14
                    inverso_c15 = 1 / c15
                    inverso_c16 = 1 / c16
                    inverso_c17 = 1 / c17


                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[1, 0] = inverso_c1
                    terceira_matriz.iloc[2, 0] = inverso_c2
                    terceira_matriz.iloc[3, 0] = inverso_c3
                    terceira_matriz.iloc[4, 0] = inverso_c4
                    terceira_matriz.iloc[5, 0] = inverso_c5
                    terceira_matriz.iloc[6, 0] = inverso_c6
                    terceira_matriz.iloc[7, 0] = inverso_c7
                    terceira_matriz.iloc[8, 0] = inverso_c8
                    terceira_matriz.iloc[9, 0] = inverso_c9
                    terceira_matriz.iloc[10, 0] = inverso_c10
                    terceira_matriz.iloc[11, 0] = inverso_c11
                    terceira_matriz.iloc[12, 0] = inverso_c12
                    terceira_matriz.iloc[13, 0] = inverso_c13
                    terceira_matriz.iloc[14, 0] = inverso_c14
                    terceira_matriz.iloc[15, 0] = inverso_c15
                    terceira_matriz.iloc[16, 0] = inverso_c16
                    terceira_matriz.iloc[17, 0] = inverso_c17
                
                    #Critério 2
                    c1_2 = terceira_matriz.iloc[1, 2]
                    c2_2 = terceira_matriz.iloc[1, 3]
                    c3_2 = terceira_matriz.iloc[1, 4]
                    c4_2 = terceira_matriz.iloc[1, 5]
                    c5_2 = terceira_matriz.iloc[1, 6]
                    c6_2 = terceira_matriz.iloc[1, 7]
                    c7_2 = terceira_matriz.iloc[1, 8]
                    c8_2 = terceira_matriz.iloc[1, 9]
                    c9_2 = terceira_matriz.iloc[1, 10]
                    c10_2 = terceira_matriz.iloc[1, 11]
                    c11_2 = terceira_matriz.iloc[1, 12]
                    c12_2 = terceira_matriz.iloc[1, 13]
                    c13_2 = terceira_matriz.iloc[1, 14]
                    c14_2 = terceira_matriz.iloc[1, 15]
                    c15_2 = terceira_matriz.iloc[1, 16]
                    c16_2 = terceira_matriz.iloc[1, 17]
                    
                
                    # Calcular os inversos
                    inverso_c1_2 = 1 / c1_2
                    inverso_c2_2 = 1 / c2_2
                    inverso_c3_2 = 1 / c3_2
                    inverso_c4_2 = 1 / c4_2
                    inverso_c5_2 = 1 / c5_2
                    inverso_c6_2 = 1 / c6_2
                    inverso_c7_2 = 1 / c7_2
                    inverso_c8_2 = 1 / c8_2
                    inverso_c9_2 = 1 / c9_2
                    inverso_c10_2 = 1 / c10_2
                    inverso_c11_2 = 1 / c11_2
                    inverso_c12_2 = 1 / c12_2
                    inverso_c13_2 = 1 / c13_2
                    inverso_c14_2 = 1 / c14_2
                    inverso_c15_2 = 1 / c15_2
                    inverso_c16_2 = 1 / c16_2



                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[2, 1] = inverso_c1_2
                    terceira_matriz.iloc[3, 1] = inverso_c2_2
                    terceira_matriz.iloc[4, 1] = inverso_c3_2
                    terceira_matriz.iloc[5, 1] = inverso_c4_2
                    terceira_matriz.iloc[6, 1] = inverso_c5_2
                    terceira_matriz.iloc[7, 1] = inverso_c6_2
                    terceira_matriz.iloc[8, 1] = inverso_c7_2
                    terceira_matriz.iloc[9, 1] = inverso_c8_2
                    terceira_matriz.iloc[10, 1] = inverso_c9_2
                    terceira_matriz.iloc[11, 1] = inverso_c10_2
                    terceira_matriz.iloc[12, 1] = inverso_c11_2
                    terceira_matriz.iloc[13, 1] = inverso_c12_2
                    terceira_matriz.iloc[14, 1] = inverso_c13_2
                    terceira_matriz.iloc[15, 1] = inverso_c14_2
                    terceira_matriz.iloc[16, 1] = inverso_c15_2
                    terceira_matriz.iloc[17, 1] = inverso_c16_2
                    
                
                    #Critério 3
                    c1_3 = terceira_matriz.iloc[2, 3]
                    c2_3 = terceira_matriz.iloc[2, 4]
                    c3_3 = terceira_matriz.iloc[2, 5]
                    c4_3 = terceira_matriz.iloc[2, 6]
                    c5_3 = terceira_matriz.iloc[2, 7]
                    c6_3 = terceira_matriz.iloc[2, 8]
                    c7_3 = terceira_matriz.iloc[2, 9]
                    c8_3 = terceira_matriz.iloc[2, 10]
                    c9_3 = terceira_matriz.iloc[2, 11]
                    c10_3 = terceira_matriz.iloc[2, 12]
                    c11_3 = terceira_matriz.iloc[2, 13]
                    c12_3 = terceira_matriz.iloc[2, 14]
                    c13_3 = terceira_matriz.iloc[2, 15]
                    c14_3 = terceira_matriz.iloc[2, 16]
                    c15_3 = terceira_matriz.iloc[2, 17]

                    # Calcular os inversos
                    inverso_c1_3 = 1 / c1_3
                    inverso_c2_3 = 1 / c2_3
                    inverso_c3_3 = 1 / c3_3
                    inverso_c4_3 = 1 / c4_3
                    inverso_c5_3 = 1 / c5_3
                    inverso_c6_3 = 1 / c6_3
                    inverso_c7_3 = 1 / c7_3
                    inverso_c8_3 = 1 / c8_3
                    inverso_c9_3 = 1 / c9_3
                    inverso_c10_3 = 1 / c10_3
                    inverso_c11_3 = 1 / c11_3
                    inverso_c12_3 = 1 / c12_3
                    inverso_c13_3 = 1 / c13_3
                    inverso_c14_3 = 1 / c14_3
                    inverso_c15_3 = 1 / c15_3
                
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[3, 2] = inverso_c1_3
                    terceira_matriz.iloc[4, 2] = inverso_c2_3
                    terceira_matriz.iloc[5, 2] = inverso_c3_3
                    terceira_matriz.iloc[6, 2] = inverso_c4_3
                    terceira_matriz.iloc[7, 2] = inverso_c5_3
                    terceira_matriz.iloc[8, 2] = inverso_c6_3
                    terceira_matriz.iloc[9, 2] = inverso_c7_3
                    terceira_matriz.iloc[10, 2] = inverso_c8_3
                    terceira_matriz.iloc[11, 2] = inverso_c9_3
                    terceira_matriz.iloc[12, 2] = inverso_c10_3
                    terceira_matriz.iloc[13, 2] = inverso_c11_3
                    terceira_matriz.iloc[14, 2] = inverso_c12_3
                    terceira_matriz.iloc[15, 2] = inverso_c13_3
                    terceira_matriz.iloc[16, 2] = inverso_c14_3
                    terceira_matriz.iloc[17, 2] = inverso_c15_3


                    #Critério 4
                    c1_4 = terceira_matriz.iloc[3, 4]
                    c2_4 = terceira_matriz.iloc[3, 5]
                    c3_4 = terceira_matriz.iloc[3, 6]
                    c4_4 = terceira_matriz.iloc[3, 7]
                    c5_4 = terceira_matriz.iloc[3, 8]
                    c6_4 = terceira_matriz.iloc[3, 9]
                    c7_4 = terceira_matriz.iloc[3, 10]
                    c8_4 = terceira_matriz.iloc[3, 11]
                    c9_4 = terceira_matriz.iloc[3, 12]
                    c10_4 = terceira_matriz.iloc[3, 13]
                    c11_4 = terceira_matriz.iloc[3, 14]
                    c12_4 = terceira_matriz.iloc[3, 15]
                    c13_4 = terceira_matriz.iloc[3, 16]
                    c14_4 = terceira_matriz.iloc[3, 17]
                
                    # Calcular os inversos
                    inverso_c1_4 = 1 / c1_4
                    inverso_c2_4 = 1 / c2_4
                    inverso_c3_4 = 1 / c3_4
                    inverso_c4_4 = 1 / c4_4
                    inverso_c5_4 = 1 / c5_4
                    inverso_c6_4 = 1 / c6_4
                    inverso_c7_4 = 1 / c7_4
                    inverso_c8_4 = 1 / c8_4
                    inverso_c9_4 = 1 / c9_4
                    inverso_c10_4 = 1 / c10_4
                    inverso_c11_4 = 1 / c11_4
                    inverso_c12_4 = 1 / c12_4
                    inverso_c13_4 = 1 / c13_4
                    inverso_c14_4 = 1 / c14_4
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[4, 3] = inverso_c1_4
                    terceira_matriz.iloc[5, 3] = inverso_c2_4
                    terceira_matriz.iloc[6, 3] = inverso_c3_4
                    terceira_matriz.iloc[7, 3] = inverso_c4_4
                    terceira_matriz.iloc[8, 3] = inverso_c5_4
                    terceira_matriz.iloc[9, 3] = inverso_c6_4
                    terceira_matriz.iloc[10, 3] = inverso_c7_4
                    terceira_matriz.iloc[11, 3] = inverso_c8_4
                    terceira_matriz.iloc[12, 3] = inverso_c9_4
                    terceira_matriz.iloc[13, 3] = inverso_c10_4
                    terceira_matriz.iloc[14, 3] = inverso_c11_4
                    terceira_matriz.iloc[15, 3] = inverso_c12_4
                    terceira_matriz.iloc[16, 3] = inverso_c13_4
                    terceira_matriz.iloc[17, 3] = inverso_c14_4


                    #Critério 5
                    c1_5 = terceira_matriz.iloc[4, 5]
                    c2_5 = terceira_matriz.iloc[4, 6]
                    c3_5 = terceira_matriz.iloc[4, 7]
                    c4_5 = terceira_matriz.iloc[4, 8]
                    c5_5 = terceira_matriz.iloc[4, 9]
                    c6_5 = terceira_matriz.iloc[4, 10]
                    c7_5 = terceira_matriz.iloc[4, 11]
                    c8_5 = terceira_matriz.iloc[4, 12]
                    c9_5 = terceira_matriz.iloc[4, 13]
                    c10_5 = terceira_matriz.iloc[4, 14]
                    c11_5 = terceira_matriz.iloc[4, 15]
                    c12_5 = terceira_matriz.iloc[4, 16]
                    c13_5 = terceira_matriz.iloc[4, 17]
                                    
                    # Calcular os inversos
                    inverso_c1_5 = 1 / c1_5
                    inverso_c2_5 = 1 / c2_5
                    inverso_c3_5 = 1 / c3_5
                    inverso_c4_5 = 1 / c4_5
                    inverso_c5_5 = 1 / c5_5
                    inverso_c6_5 = 1 / c6_5
                    inverso_c7_5 = 1 / c7_5
                    inverso_c8_5 = 1 / c8_5
                    inverso_c9_5 = 1 / c9_5
                    inverso_c10_5 = 1 / c10_5
                    inverso_c11_5 = 1 / c11_5
                    inverso_c12_5 = 1 / c12_5
                    inverso_c13_5 = 1 / c13_5
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[5, 4] = inverso_c1_5
                    terceira_matriz.iloc[6, 4] = inverso_c2_5
                    terceira_matriz.iloc[7, 4] = inverso_c3_5
                    terceira_matriz.iloc[8, 4] = inverso_c4_5
                    terceira_matriz.iloc[9, 4] = inverso_c5_5
                    terceira_matriz.iloc[10, 4] = inverso_c6_5
                    terceira_matriz.iloc[11, 4] = inverso_c7_5
                    terceira_matriz.iloc[12, 4] = inverso_c8_5
                    terceira_matriz.iloc[13, 4] = inverso_c9_5
                    terceira_matriz.iloc[14, 4] = inverso_c10_5
                    terceira_matriz.iloc[15, 4] = inverso_c11_5
                    terceira_matriz.iloc[16, 4] = inverso_c12_5
                    terceira_matriz.iloc[17, 4] = inverso_c13_5


                     #Critério 6
                    c1_6 = terceira_matriz.iloc[5, 6]
                    c2_6 = terceira_matriz.iloc[5, 7]
                    c3_6 = terceira_matriz.iloc[5, 8]
                    c4_6 = terceira_matriz.iloc[5, 9]
                    c5_6 = terceira_matriz.iloc[5, 10]
                    c6_6 = terceira_matriz.iloc[5, 11]
                    c7_6 = terceira_matriz.iloc[5, 12]
                    c8_6 = terceira_matriz.iloc[5, 13]
                    c9_6 = terceira_matriz.iloc[5, 14]
                    c10_6 = terceira_matriz.iloc[5, 15]
                    c11_6 = terceira_matriz.iloc[5, 16]
                    c12_6 = terceira_matriz.iloc[5, 17]
                                    
                                    
                    # Calcular os inversos
                    inverso_c1_6 = 1 / c1_6
                    inverso_c2_6 = 1 / c2_6
                    inverso_c3_6 = 1 / c3_6
                    inverso_c4_6 = 1 / c4_6
                    inverso_c5_6 = 1 / c5_6
                    inverso_c6_6 = 1 / c6_6
                    inverso_c7_6 = 1 / c7_6
                    inverso_c8_6 = 1 / c8_6
                    inverso_c9_6 = 1 / c9_6
                    inverso_c10_6 = 1 / c10_6
                    inverso_c11_6 = 1 / c11_6
                    inverso_c12_6 = 1 / c12_6
                                      
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[6, 5] = inverso_c1_6
                    terceira_matriz.iloc[7, 5] = inverso_c2_6
                    terceira_matriz.iloc[8, 5] = inverso_c3_6
                    terceira_matriz.iloc[9, 5] = inverso_c4_6
                    terceira_matriz.iloc[10, 5] = inverso_c5_6
                    terceira_matriz.iloc[11, 5] = inverso_c6_6
                    terceira_matriz.iloc[12, 5] = inverso_c7_6
                    terceira_matriz.iloc[13, 5] = inverso_c8_6
                    terceira_matriz.iloc[14, 5] = inverso_c9_6
                    terceira_matriz.iloc[15, 5] = inverso_c10_6
                    terceira_matriz.iloc[16, 5] = inverso_c11_6
                    terceira_matriz.iloc[17, 5] = inverso_c12_6


                    #Critério 7
                    c1_7 = terceira_matriz.iloc[6, 7]
                    c2_7 = terceira_matriz.iloc[6, 8]
                    c3_7 = terceira_matriz.iloc[6, 9]
                    c4_7 = terceira_matriz.iloc[6, 10]
                    c5_7 = terceira_matriz.iloc[6, 11]
                    c6_7 = terceira_matriz.iloc[6, 12]
                    c7_7 = terceira_matriz.iloc[6, 13]
                    c8_7 = terceira_matriz.iloc[6, 14]
                    c9_7 = terceira_matriz.iloc[6, 15]
                    c10_7 = terceira_matriz.iloc[6, 16]
                    c11_7 = terceira_matriz.iloc[6, 17]
                                                       
                    # Calcular os inversos
                    inverso_c1_7 = 1 / c1_7
                    inverso_c2_7 = 1 / c2_7
                    inverso_c3_7 = 1 / c3_7
                    inverso_c4_7 = 1 / c4_7
                    inverso_c5_7 = 1 / c5_7
                    inverso_c6_7 = 1 / c6_7
                    inverso_c7_7 = 1 / c7_7
                    inverso_c8_7 = 1 / c8_7
                    inverso_c9_7 = 1 / c9_7
                    inverso_c10_7 = 1 / c10_7
                    inverso_c11_7 = 1 / c11_7
                                                         
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[7, 6] = inverso_c1_7
                    terceira_matriz.iloc[8, 6] = inverso_c2_7
                    terceira_matriz.iloc[9, 6] = inverso_c3_7
                    terceira_matriz.iloc[10, 6] = inverso_c4_7
                    terceira_matriz.iloc[11, 6] = inverso_c5_7
                    terceira_matriz.iloc[12, 6] = inverso_c6_7
                    terceira_matriz.iloc[13, 6] = inverso_c7_7
                    terceira_matriz.iloc[14, 6] = inverso_c8_7
                    terceira_matriz.iloc[15, 6] = inverso_c9_7
                    terceira_matriz.iloc[16, 6] = inverso_c10_7
                    terceira_matriz.iloc[17, 6] = inverso_c11_7


                    #Critério 8
                    c1_8 = terceira_matriz.iloc[7,8]
                    c2_8 = terceira_matriz.iloc[7,9]
                    c3_8 = terceira_matriz.iloc[7,10]
                    c4_8 = terceira_matriz.iloc[7,11]
                    c5_8 = terceira_matriz.iloc[7,12]
                    c6_8 = terceira_matriz.iloc[7,13]
                    c7_8 = terceira_matriz.iloc[7,14]
                    c8_8 = terceira_matriz.iloc[7,15]
                    c9_8 = terceira_matriz.iloc[7,16]
                    c10_8 = terceira_matriz.iloc[7,17]
                                    
                    # Calcular os inversos
                    inverso_c1_8 = 1 / c1_8
                    inverso_c2_8 = 1 / c2_8
                    inverso_c3_8 = 1 / c3_8
                    inverso_c4_8 = 1 / c4_8
                    inverso_c5_8 = 1 / c5_8
                    inverso_c6_8 = 1 / c6_8
                    inverso_c7_8 = 1 / c7_8
                    inverso_c8_8 = 1 / c8_8
                    inverso_c9_8 = 1 / c9_8
                    inverso_c10_8 = 1 / c10_8
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[8, 7] = inverso_c1_8
                    terceira_matriz.iloc[9, 7] = inverso_c2_8
                    terceira_matriz.iloc[10, 7] = inverso_c3_8
                    terceira_matriz.iloc[11, 7] = inverso_c4_8
                    terceira_matriz.iloc[12, 7] = inverso_c5_8
                    terceira_matriz.iloc[13, 7] = inverso_c6_8
                    terceira_matriz.iloc[14, 7] = inverso_c7_8
                    terceira_matriz.iloc[15, 7] = inverso_c8_8
                    terceira_matriz.iloc[16, 7] = inverso_c9_8
                    terceira_matriz.iloc[17, 7] = inverso_c10_8

                    #Critério 9
                    c1_9 = terceira_matriz.iloc[8, 9]
                    c2_9 = terceira_matriz.iloc[8, 10]
                    c3_9 = terceira_matriz.iloc[8, 11]
                    c4_9 = terceira_matriz.iloc[8, 12]
                    c5_9 = terceira_matriz.iloc[8, 13]
                    c6_9 = terceira_matriz.iloc[8, 14]
                    c7_9 = terceira_matriz.iloc[8, 15]
                    c8_9 = terceira_matriz.iloc[8, 16]
                    c9_9 = terceira_matriz.iloc[8, 17]
                                    
                    # Calcular os inversos
                    inverso_c1_9 = 1 / c1_9
                    inverso_c2_9 = 1 / c2_9
                    inverso_c3_9 = 1 / c3_9
                    inverso_c4_9 = 1 / c4_9
                    inverso_c5_9 = 1 / c5_9
                    inverso_c6_9 = 1 / c6_9
                    inverso_c7_9 = 1 / c7_9
                    inverso_c8_9 = 1 / c8_9
                    inverso_c9_9 = 1 / c9_9
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[9, 8] = inverso_c1_9
                    terceira_matriz.iloc[10, 8] = inverso_c2_9
                    terceira_matriz.iloc[11, 8] = inverso_c3_9 
                    terceira_matriz.iloc[12, 8] = inverso_c4_9 
                    terceira_matriz.iloc[13, 8] = inverso_c5_9
                    terceira_matriz.iloc[14, 8] = inverso_c6_9 
                    terceira_matriz.iloc[15, 8] = inverso_c7_9 
                    terceira_matriz.iloc[16, 8] = inverso_c8_9 
                    terceira_matriz.iloc[17, 8] = inverso_c9_9    
                    
                     #Critério 10
                    c1_10 = terceira_matriz.iloc[9,10]
                    c2_10 = terceira_matriz.iloc[9,11]
                    c3_10 = terceira_matriz.iloc[9,12]
                    c4_10 = terceira_matriz.iloc[9,13]
                    c5_10 = terceira_matriz.iloc[9,14]
                    c6_10 = terceira_matriz.iloc[9,15]
                    c7_10 = terceira_matriz.iloc[9,16]
                    c8_10 = terceira_matriz.iloc[9,17]
                                                        
                    # Calcular os inversos
                    inverso_c1_10 = 1 / c1_10
                    inverso_c2_10 = 1 / c2_10
                    inverso_c3_10 = 1 / c3_10
                    inverso_c4_10 = 1 / c4_10
                    inverso_c5_10 = 1 / c5_10
                    inverso_c6_10 = 1 / c6_10
                    inverso_c7_10 = 1 / c7_10
                    inverso_c8_10 = 1 / c8_10
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[10, 9] = inverso_c1_10
                    terceira_matriz.iloc[11, 9] = inverso_c2_10
                    terceira_matriz.iloc[12, 9] = inverso_c3_10
                    terceira_matriz.iloc[13, 9] = inverso_c4_10
                    terceira_matriz.iloc[14, 9] = inverso_c5_10
                    terceira_matriz.iloc[15, 9] = inverso_c6_10
                    terceira_matriz.iloc[16, 9] = inverso_c7_10
                    terceira_matriz.iloc[17, 9] = inverso_c8_10


                    #Critério 11
                    c1_11 = terceira_matriz.iloc[10,11]
                    c2_11 = terceira_matriz.iloc[10,12]
                    c3_11 = terceira_matriz.iloc[10,13]
                    c4_11 = terceira_matriz.iloc[10,14]
                    c5_11 = terceira_matriz.iloc[10,15]
                    c6_11 = terceira_matriz.iloc[10,16]
                    c7_11 = terceira_matriz.iloc[10,17]
                                     
                                                                    
                    # Calcular os inversos
                    inverso_c1_11 = 1 / c1_11
                    inverso_c2_11 = 1 / c2_11
                    inverso_c3_11 = 1 / c3_11
                    inverso_c4_11 = 1 / c4_11
                    inverso_c5_11 = 1 / c5_11
                    inverso_c6_11 = 1 / c6_11
                    inverso_c7_11 = 1 / c7_11
                                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[11, 10] = inverso_c1_11
                    terceira_matriz.iloc[12, 10] = inverso_c2_11
                    terceira_matriz.iloc[13, 10] = inverso_c3_11
                    terceira_matriz.iloc[14, 10] = inverso_c4_11
                    terceira_matriz.iloc[15, 10] = inverso_c5_11
                    terceira_matriz.iloc[16, 10] = inverso_c6_11
                    terceira_matriz.iloc[17, 10] = inverso_c7_11
                
                                       
                    #Critério 12
                    c1_12 = terceira_matriz.iloc[11,12]
                    c2_12 = terceira_matriz.iloc[11,13]
                    c3_12 = terceira_matriz.iloc[11,14]
                    c4_12 = terceira_matriz.iloc[11,15]
                    c5_12 = terceira_matriz.iloc[11,16]
                    c6_12 = terceira_matriz.iloc[11,17]
                    
                                                     
                    # Calcular os inversos
                    inverso_c1_12 = 1 / c1_12
                    inverso_c2_12 = 1 / c2_12
                    inverso_c3_12 = 1 / c3_12
                    inverso_c4_12 = 1 / c4_12
                    inverso_c5_12 = 1 / c5_12
                    inverso_c6_12 = 1 / c6_12
                                   
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[12, 11] = inverso_c1_12
                    terceira_matriz.iloc[13, 11] = inverso_c2_12
                    terceira_matriz.iloc[14, 11] = inverso_c3_12  
                    terceira_matriz.iloc[15, 11] = inverso_c4_12 
                    terceira_matriz.iloc[16, 11] = inverso_c5_12
                    terceira_matriz.iloc[17, 11] = inverso_c6_12     
                                         
                     #Critério 13
                    c1_13 = terceira_matriz.iloc[12,13]
                    c2_13 = terceira_matriz.iloc[12,14]
                    c3_13 = terceira_matriz.iloc[12,15]
                    c4_13 = terceira_matriz.iloc[12,16]
                    c5_13 = terceira_matriz.iloc[12,17]
                                                     
                    # Calcular os inversos
                    inverso_c1_13 = 1 / c1_13
                    inverso_c2_13 = 1 / c2_13
                    inverso_c3_13 = 1 / c3_13
                    inverso_c4_13 = 1 / c4_13
                    inverso_c5_13 = 1 / c5_13
                                   
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[13, 12] = inverso_c1_13
                    terceira_matriz.iloc[14, 12] = inverso_c2_13
                    terceira_matriz.iloc[15, 12] = inverso_c3_13 
                    terceira_matriz.iloc[16, 12] = inverso_c4_13 
                    terceira_matriz.iloc[17, 12] = inverso_c5_13   
                    
                    #Critério 14
                    c1_14 = terceira_matriz.iloc[13,14]
                    c2_14 = terceira_matriz.iloc[13,15]
                    c3_14 = terceira_matriz.iloc[13,16]
                    c4_14 = terceira_matriz.iloc[13,17]
                                                                      
                    # Calcular os inversos
                    inverso_c1_14 = 1 / c1_14
                    inverso_c2_14 = 1 / c2_14
                    inverso_c3_14 = 1 / c3_14
                    inverso_c4_14 = 1 / c4_14
                                                       
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[14, 13] = inverso_c1_14
                    terceira_matriz.iloc[15, 13] = inverso_c2_14
                    terceira_matriz.iloc[16, 13] = inverso_c3_14
                    terceira_matriz.iloc[17, 13] = inverso_c4_14

                    #Critério 15
                    c1_15 = terceira_matriz.iloc[14,15]
                    c2_15 = terceira_matriz.iloc[14,16]
                    c3_15 = terceira_matriz.iloc[14,17]
                                                                
                    # Calcular os inversos
                    inverso_c1_15 = 1 / c1_15
                    inverso_c2_15 = 1 / c2_15
                    inverso_c3_15 = 1 / c3_15
                                                                           
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[15, 14] = inverso_c1_15
                    terceira_matriz.iloc[16, 14] = inverso_c2_15
                    terceira_matriz.iloc[17, 14] = inverso_c3_15

                     #Critério 16
                    c1_15 = terceira_matriz.iloc[15,16]
                    c2_15 = terceira_matriz.iloc[15,17]
                                                                
                    # Calcular os inversos
                    inverso_c1_15 = 1 / c1_15
                    inverso_c2_15 = 1 / c2_15
                                                                           
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[16, 15] = inverso_c1_15
                    terceira_matriz.iloc[17, 15] = inverso_c2_15
                    
                    #Critério 17
                    c1_16 = terceira_matriz.iloc[16,17]
                                                                
                    # Calcular os inversos
                    inverso_c1_16 = 1 / c1_16
                                                                           
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[17, 16] = inverso_c1_16
        
    if num_critérios == 19:
        for i in range(2, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[1, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[1, i] = item["valor"]
                     

        for i in range(3, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[2, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[2, i] = item["valor"]
                     

        for i in range(4, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[3, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[3, i] = item["valor"]
                     

        for i in range(5, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[4, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[4, i] = item["valor"]

        for i in range(6, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[5, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[5, i] = item["valor"]
        
        for i in range(7, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[6, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[6, i] = item["valor"]
        for i in range(8, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[7, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[7, i] = item["valor"]
        for i in range(9, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[8, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[8, i] = item["valor"]
        for i in range(10, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[9, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[9, i] = item["valor"]

        for i in range(11, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[10, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[10, i] = item["valor"]
        
        for i in range(12, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[11, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[11, i] = item["valor"]
        
        for i in range(13, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[12, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[12, i] = item["valor"]
        
        for i in range(14, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[13, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[13, i] = item["valor"]

        for i in range(15, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[14, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[14, i] = item["valor"]

        for i in range(16, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[15, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[15, i] = item["valor"]
        
        for i in range(17, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[16, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[16, i] = item["valor"]
        
        for i in range(18, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[17, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[17, i] = item["valor"]

                    #Inverter a Terceira Matriz
                    #Critério 1
                    c1 = terceira_matriz.iloc[0, 1]
                    c2 = terceira_matriz.iloc[0, 2]
                    c3 = terceira_matriz.iloc[0, 3]
                    c4 = terceira_matriz.iloc[0, 4]
                    c5 = terceira_matriz.iloc[0, 5]
                    c6 = terceira_matriz.iloc[0, 6]
                    c7 = terceira_matriz.iloc[0, 7]
                    c8 = terceira_matriz.iloc[0, 8]
                    c9 = terceira_matriz.iloc[0, 9]
                    c10 = terceira_matriz.iloc[0, 10]
                    c11 = terceira_matriz.iloc[0, 11]
                    c12 = terceira_matriz.iloc[0, 12]
                    c13 = terceira_matriz.iloc[0, 13]
                    c14 = terceira_matriz.iloc[0, 14]
                    c15 = terceira_matriz.iloc[0, 15]
                    c16 = terceira_matriz.iloc[0, 16]
                    c17 = terceira_matriz.iloc[0, 17]
                    c18 = terceira_matriz.iloc[0, 18]
                
                    # Calcular os inversos
                    inverso_c1 = 1 / c1
                    inverso_c2 = 1 / c2
                    inverso_c3 = 1 / c3
                    inverso_c4 = 1 / c4
                    inverso_c5 = 1 / c5
                    inverso_c6 = 1 / c6
                    inverso_c7 = 1 / c7
                    inverso_c8 = 1 / c8
                    inverso_c9 = 1 / c9
                    inverso_c10 = 1 / c10
                    inverso_c11 = 1 / c11
                    inverso_c12 = 1 / c12
                    inverso_c13 = 1 / c13
                    inverso_c14 = 1 / c14
                    inverso_c15 = 1 / c15
                    inverso_c16 = 1 / c16
                    inverso_c17 = 1 / c17
                    inverso_c18 = 1 / c18


                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[1, 0] = inverso_c1
                    terceira_matriz.iloc[2, 0] = inverso_c2
                    terceira_matriz.iloc[3, 0] = inverso_c3
                    terceira_matriz.iloc[4, 0] = inverso_c4
                    terceira_matriz.iloc[5, 0] = inverso_c5
                    terceira_matriz.iloc[6, 0] = inverso_c6
                    terceira_matriz.iloc[7, 0] = inverso_c7
                    terceira_matriz.iloc[8, 0] = inverso_c8
                    terceira_matriz.iloc[9, 0] = inverso_c9
                    terceira_matriz.iloc[10, 0] = inverso_c10
                    terceira_matriz.iloc[11, 0] = inverso_c11
                    terceira_matriz.iloc[12, 0] = inverso_c12
                    terceira_matriz.iloc[13, 0] = inverso_c13
                    terceira_matriz.iloc[14, 0] = inverso_c14
                    terceira_matriz.iloc[15, 0] = inverso_c15
                    terceira_matriz.iloc[16, 0] = inverso_c16
                    terceira_matriz.iloc[17, 0] = inverso_c17
                    terceira_matriz.iloc[18, 0] = inverso_c18
                
                    #Critério 2
                    c1_2 = terceira_matriz.iloc[1, 2]
                    c2_2 = terceira_matriz.iloc[1, 3]
                    c3_2 = terceira_matriz.iloc[1, 4]
                    c4_2 = terceira_matriz.iloc[1, 5]
                    c5_2 = terceira_matriz.iloc[1, 6]
                    c6_2 = terceira_matriz.iloc[1, 7]
                    c7_2 = terceira_matriz.iloc[1, 8]
                    c8_2 = terceira_matriz.iloc[1, 9]
                    c9_2 = terceira_matriz.iloc[1, 10]
                    c10_2 = terceira_matriz.iloc[1, 11]
                    c11_2 = terceira_matriz.iloc[1, 12]
                    c12_2 = terceira_matriz.iloc[1, 13]
                    c13_2 = terceira_matriz.iloc[1, 14]
                    c14_2 = terceira_matriz.iloc[1, 15]
                    c15_2 = terceira_matriz.iloc[1, 16]
                    c16_2 = terceira_matriz.iloc[1, 17]
                    c17_2 = terceira_matriz.iloc[1, 18]
                    
                
                    # Calcular os inversos
                    inverso_c1_2 = 1 / c1_2
                    inverso_c2_2 = 1 / c2_2
                    inverso_c3_2 = 1 / c3_2
                    inverso_c4_2 = 1 / c4_2
                    inverso_c5_2 = 1 / c5_2
                    inverso_c6_2 = 1 / c6_2
                    inverso_c7_2 = 1 / c7_2
                    inverso_c8_2 = 1 / c8_2
                    inverso_c9_2 = 1 / c9_2
                    inverso_c10_2 = 1 / c10_2
                    inverso_c11_2 = 1 / c11_2
                    inverso_c12_2 = 1 / c12_2
                    inverso_c13_2 = 1 / c13_2
                    inverso_c14_2 = 1 / c14_2
                    inverso_c15_2 = 1 / c15_2
                    inverso_c16_2 = 1 / c16_2
                    inverso_c17_2 = 1 / c17_2



                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[2, 1] = inverso_c1_2
                    terceira_matriz.iloc[3, 1] = inverso_c2_2
                    terceira_matriz.iloc[4, 1] = inverso_c3_2
                    terceira_matriz.iloc[5, 1] = inverso_c4_2
                    terceira_matriz.iloc[6, 1] = inverso_c5_2
                    terceira_matriz.iloc[7, 1] = inverso_c6_2
                    terceira_matriz.iloc[8, 1] = inverso_c7_2
                    terceira_matriz.iloc[9, 1] = inverso_c8_2
                    terceira_matriz.iloc[10, 1] = inverso_c9_2
                    terceira_matriz.iloc[11, 1] = inverso_c10_2
                    terceira_matriz.iloc[12, 1] = inverso_c11_2
                    terceira_matriz.iloc[13, 1] = inverso_c12_2
                    terceira_matriz.iloc[14, 1] = inverso_c13_2
                    terceira_matriz.iloc[15, 1] = inverso_c14_2
                    terceira_matriz.iloc[16, 1] = inverso_c15_2
                    terceira_matriz.iloc[17, 1] = inverso_c16_2
                    terceira_matriz.iloc[18, 1] = inverso_c17_2
                    
                
                    #Critério 3
                    c1_3 = terceira_matriz.iloc[2, 3]
                    c2_3 = terceira_matriz.iloc[2, 4]
                    c3_3 = terceira_matriz.iloc[2, 5]
                    c4_3 = terceira_matriz.iloc[2, 6]
                    c5_3 = terceira_matriz.iloc[2, 7]
                    c6_3 = terceira_matriz.iloc[2, 8]
                    c7_3 = terceira_matriz.iloc[2, 9]
                    c8_3 = terceira_matriz.iloc[2, 10]
                    c9_3 = terceira_matriz.iloc[2, 11]
                    c10_3 = terceira_matriz.iloc[2, 12]
                    c11_3 = terceira_matriz.iloc[2, 13]
                    c12_3 = terceira_matriz.iloc[2, 14]
                    c13_3 = terceira_matriz.iloc[2, 15]
                    c14_3 = terceira_matriz.iloc[2, 16]
                    c15_3 = terceira_matriz.iloc[2, 17]
                    c16_3 = terceira_matriz.iloc[2, 18]
                    

                    # Calcular os inversos
                    inverso_c1_3 = 1 / c1_3
                    inverso_c2_3 = 1 / c2_3
                    inverso_c3_3 = 1 / c3_3
                    inverso_c4_3 = 1 / c4_3
                    inverso_c5_3 = 1 / c5_3
                    inverso_c6_3 = 1 / c6_3
                    inverso_c7_3 = 1 / c7_3
                    inverso_c8_3 = 1 / c8_3
                    inverso_c9_3 = 1 / c9_3
                    inverso_c10_3 = 1 / c10_3
                    inverso_c11_3 = 1 / c11_3
                    inverso_c12_3 = 1 / c12_3
                    inverso_c13_3 = 1 / c13_3
                    inverso_c14_3 = 1 / c14_3
                    inverso_c15_3 = 1 / c15_3
                    inverso_c16_3 = 1 / c16_3
                
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[3, 2] = inverso_c1_3
                    terceira_matriz.iloc[4, 2] = inverso_c2_3
                    terceira_matriz.iloc[5, 2] = inverso_c3_3
                    terceira_matriz.iloc[6, 2] = inverso_c4_3
                    terceira_matriz.iloc[7, 2] = inverso_c5_3
                    terceira_matriz.iloc[8, 2] = inverso_c6_3
                    terceira_matriz.iloc[9, 2] = inverso_c7_3
                    terceira_matriz.iloc[10, 2] = inverso_c8_3
                    terceira_matriz.iloc[11, 2] = inverso_c9_3
                    terceira_matriz.iloc[12, 2] = inverso_c10_3
                    terceira_matriz.iloc[13, 2] = inverso_c11_3
                    terceira_matriz.iloc[14, 2] = inverso_c12_3
                    terceira_matriz.iloc[15, 2] = inverso_c13_3
                    terceira_matriz.iloc[16, 2] = inverso_c14_3
                    terceira_matriz.iloc[17, 2] = inverso_c15_3
                    terceira_matriz.iloc[18, 2] = inverso_c16_3                    


                    #Critério 4
                    c1_4 = terceira_matriz.iloc[3, 4]
                    c2_4 = terceira_matriz.iloc[3, 5]
                    c3_4 = terceira_matriz.iloc[3, 6]
                    c4_4 = terceira_matriz.iloc[3, 7]
                    c5_4 = terceira_matriz.iloc[3, 8]
                    c6_4 = terceira_matriz.iloc[3, 9]
                    c7_4 = terceira_matriz.iloc[3, 10]
                    c8_4 = terceira_matriz.iloc[3, 11]
                    c9_4 = terceira_matriz.iloc[3, 12]
                    c10_4 = terceira_matriz.iloc[3, 13]
                    c11_4 = terceira_matriz.iloc[3, 14]
                    c12_4 = terceira_matriz.iloc[3, 15]
                    c13_4 = terceira_matriz.iloc[3, 16]
                    c14_4 = terceira_matriz.iloc[3, 17]
                    c15_4 = terceira_matriz.iloc[3, 18]
                
                    # Calcular os inversos
                    inverso_c1_4 = 1 / c1_4
                    inverso_c2_4 = 1 / c2_4
                    inverso_c3_4 = 1 / c3_4
                    inverso_c4_4 = 1 / c4_4
                    inverso_c5_4 = 1 / c5_4
                    inverso_c6_4 = 1 / c6_4
                    inverso_c7_4 = 1 / c7_4
                    inverso_c8_4 = 1 / c8_4
                    inverso_c9_4 = 1 / c9_4
                    inverso_c10_4 = 1 / c10_4
                    inverso_c11_4 = 1 / c11_4
                    inverso_c12_4 = 1 / c12_4
                    inverso_c13_4 = 1 / c13_4
                    inverso_c14_4 = 1 / c14_4
                    inverso_c15_4 = 1 / c15_4
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[4, 3] = inverso_c1_4
                    terceira_matriz.iloc[5, 3] = inverso_c2_4
                    terceira_matriz.iloc[6, 3] = inverso_c3_4
                    terceira_matriz.iloc[7, 3] = inverso_c4_4
                    terceira_matriz.iloc[8, 3] = inverso_c5_4
                    terceira_matriz.iloc[9, 3] = inverso_c6_4
                    terceira_matriz.iloc[10, 3] = inverso_c7_4
                    terceira_matriz.iloc[11, 3] = inverso_c8_4
                    terceira_matriz.iloc[12, 3] = inverso_c9_4
                    terceira_matriz.iloc[13, 3] = inverso_c10_4
                    terceira_matriz.iloc[14, 3] = inverso_c11_4
                    terceira_matriz.iloc[15, 3] = inverso_c12_4
                    terceira_matriz.iloc[16, 3] = inverso_c13_4
                    terceira_matriz.iloc[17, 3] = inverso_c14_4
                    terceira_matriz.iloc[18, 3] = inverso_c15_4


                    #Critério 5
                    c1_5 = terceira_matriz.iloc[4, 5]
                    c2_5 = terceira_matriz.iloc[4, 6]
                    c3_5 = terceira_matriz.iloc[4, 7]
                    c4_5 = terceira_matriz.iloc[4, 8]
                    c5_5 = terceira_matriz.iloc[4, 9]
                    c6_5 = terceira_matriz.iloc[4, 10]
                    c7_5 = terceira_matriz.iloc[4, 11]
                    c8_5 = terceira_matriz.iloc[4, 12]
                    c9_5 = terceira_matriz.iloc[4, 13]
                    c10_5 = terceira_matriz.iloc[4, 14]
                    c11_5 = terceira_matriz.iloc[4, 15]
                    c12_5 = terceira_matriz.iloc[4, 16]
                    c13_5 = terceira_matriz.iloc[4, 17]
                    c14_5 = terceira_matriz.iloc[4, 18]
                                    
                    # Calcular os inversos
                    inverso_c1_5 = 1 / c1_5
                    inverso_c2_5 = 1 / c2_5
                    inverso_c3_5 = 1 / c3_5
                    inverso_c4_5 = 1 / c4_5
                    inverso_c5_5 = 1 / c5_5
                    inverso_c6_5 = 1 / c6_5
                    inverso_c7_5 = 1 / c7_5
                    inverso_c8_5 = 1 / c8_5
                    inverso_c9_5 = 1 / c9_5
                    inverso_c10_5 = 1 / c10_5
                    inverso_c11_5 = 1 / c11_5
                    inverso_c12_5 = 1 / c12_5
                    inverso_c13_5 = 1 / c13_5
                    inverso_c14_5 = 1 / c14_5
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[5, 4] = inverso_c1_5
                    terceira_matriz.iloc[6, 4] = inverso_c2_5
                    terceira_matriz.iloc[7, 4] = inverso_c3_5
                    terceira_matriz.iloc[8, 4] = inverso_c4_5
                    terceira_matriz.iloc[9, 4] = inverso_c5_5
                    terceira_matriz.iloc[10, 4] = inverso_c6_5
                    terceira_matriz.iloc[11, 4] = inverso_c7_5
                    terceira_matriz.iloc[12, 4] = inverso_c8_5
                    terceira_matriz.iloc[13, 4] = inverso_c9_5
                    terceira_matriz.iloc[14, 4] = inverso_c10_5
                    terceira_matriz.iloc[15, 4] = inverso_c11_5
                    terceira_matriz.iloc[16, 4] = inverso_c12_5
                    terceira_matriz.iloc[17, 4] = inverso_c13_5
                    terceira_matriz.iloc[18, 4] = inverso_c14_5


                     #Critério 6
                    c1_6 = terceira_matriz.iloc[5, 6]
                    c2_6 = terceira_matriz.iloc[5, 7]
                    c3_6 = terceira_matriz.iloc[5, 8]
                    c4_6 = terceira_matriz.iloc[5, 9]
                    c5_6 = terceira_matriz.iloc[5, 10]
                    c6_6 = terceira_matriz.iloc[5, 11]
                    c7_6 = terceira_matriz.iloc[5, 12]
                    c8_6 = terceira_matriz.iloc[5, 13]
                    c9_6 = terceira_matriz.iloc[5, 14]
                    c10_6 = terceira_matriz.iloc[5, 15]
                    c11_6 = terceira_matriz.iloc[5, 16]
                    c12_6 = terceira_matriz.iloc[5, 17]
                    c13_6 = terceira_matriz.iloc[5, 18]
                                    
                                    
                    # Calcular os inversos
                    inverso_c1_6 = 1 / c1_6
                    inverso_c2_6 = 1 / c2_6
                    inverso_c3_6 = 1 / c3_6
                    inverso_c4_6 = 1 / c4_6
                    inverso_c5_6 = 1 / c5_6
                    inverso_c6_6 = 1 / c6_6
                    inverso_c7_6 = 1 / c7_6
                    inverso_c8_6 = 1 / c8_6
                    inverso_c9_6 = 1 / c9_6
                    inverso_c10_6 = 1 / c10_6
                    inverso_c11_6 = 1 / c11_6
                    inverso_c12_6 = 1 / c12_6
                    inverso_c13_6 = 1 / c13_6
                                      
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[6, 5] = inverso_c1_6
                    terceira_matriz.iloc[7, 5] = inverso_c2_6
                    terceira_matriz.iloc[8, 5] = inverso_c3_6
                    terceira_matriz.iloc[9, 5] = inverso_c4_6
                    terceira_matriz.iloc[10, 5] = inverso_c5_6
                    terceira_matriz.iloc[11, 5] = inverso_c6_6
                    terceira_matriz.iloc[12, 5] = inverso_c7_6
                    terceira_matriz.iloc[13, 5] = inverso_c8_6
                    terceira_matriz.iloc[14, 5] = inverso_c9_6
                    terceira_matriz.iloc[15, 5] = inverso_c10_6
                    terceira_matriz.iloc[16, 5] = inverso_c11_6
                    terceira_matriz.iloc[17, 5] = inverso_c12_6
                    terceira_matriz.iloc[18, 5] = inverso_c13_6


                    #Critério 7
                    c1_7 = terceira_matriz.iloc[6, 7]
                    c2_7 = terceira_matriz.iloc[6, 8]
                    c3_7 = terceira_matriz.iloc[6, 9]
                    c4_7 = terceira_matriz.iloc[6, 10]
                    c5_7 = terceira_matriz.iloc[6, 11]
                    c6_7 = terceira_matriz.iloc[6, 12]
                    c7_7 = terceira_matriz.iloc[6, 13]
                    c8_7 = terceira_matriz.iloc[6, 14]
                    c9_7 = terceira_matriz.iloc[6, 15]
                    c10_7 = terceira_matriz.iloc[6, 16]
                    c11_7 = terceira_matriz.iloc[6, 17]
                    c12_7 = terceira_matriz.iloc[6, 18]
                                                       
                    # Calcular os inversos
                    inverso_c1_7 = 1 / c1_7
                    inverso_c2_7 = 1 / c2_7
                    inverso_c3_7 = 1 / c3_7
                    inverso_c4_7 = 1 / c4_7
                    inverso_c5_7 = 1 / c5_7
                    inverso_c6_7 = 1 / c6_7
                    inverso_c7_7 = 1 / c7_7
                    inverso_c8_7 = 1 / c8_7
                    inverso_c9_7 = 1 / c9_7
                    inverso_c10_7 = 1 / c10_7
                    inverso_c11_7 = 1 / c11_7
                    inverso_c12_7 = 1 / c12_7
                                                         
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[7, 6] = inverso_c1_7
                    terceira_matriz.iloc[8, 6] = inverso_c2_7
                    terceira_matriz.iloc[9, 6] = inverso_c3_7
                    terceira_matriz.iloc[10, 6] = inverso_c4_7
                    terceira_matriz.iloc[11, 6] = inverso_c5_7
                    terceira_matriz.iloc[12, 6] = inverso_c6_7
                    terceira_matriz.iloc[13, 6] = inverso_c7_7
                    terceira_matriz.iloc[14, 6] = inverso_c8_7
                    terceira_matriz.iloc[15, 6] = inverso_c9_7
                    terceira_matriz.iloc[16, 6] = inverso_c10_7
                    terceira_matriz.iloc[17, 6] = inverso_c11_7
                    terceira_matriz.iloc[18, 6] = inverso_c12_7


                    #Critério 8
                    c1_8 = terceira_matriz.iloc[7,8]
                    c2_8 = terceira_matriz.iloc[7,9]
                    c3_8 = terceira_matriz.iloc[7,10]
                    c4_8 = terceira_matriz.iloc[7,11]
                    c5_8 = terceira_matriz.iloc[7,12]
                    c6_8 = terceira_matriz.iloc[7,13]
                    c7_8 = terceira_matriz.iloc[7,14]
                    c8_8 = terceira_matriz.iloc[7,15]
                    c9_8 = terceira_matriz.iloc[7,16]
                    c10_8 = terceira_matriz.iloc[7,17]
                    c11_8 = terceira_matriz.iloc[7,18]
                                    
                    # Calcular os inversos
                    inverso_c1_8 = 1 / c1_8
                    inverso_c2_8 = 1 / c2_8
                    inverso_c3_8 = 1 / c3_8
                    inverso_c4_8 = 1 / c4_8
                    inverso_c5_8 = 1 / c5_8
                    inverso_c6_8 = 1 / c6_8
                    inverso_c7_8 = 1 / c7_8
                    inverso_c8_8 = 1 / c8_8
                    inverso_c9_8 = 1 / c9_8
                    inverso_c10_8 = 1 / c10_8
                    inverso_c11_8 = 1 / c11_8
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[8, 7] = inverso_c1_8
                    terceira_matriz.iloc[9, 7] = inverso_c2_8
                    terceira_matriz.iloc[10, 7] = inverso_c3_8
                    terceira_matriz.iloc[11, 7] = inverso_c4_8
                    terceira_matriz.iloc[12, 7] = inverso_c5_8
                    terceira_matriz.iloc[13, 7] = inverso_c6_8
                    terceira_matriz.iloc[14, 7] = inverso_c7_8
                    terceira_matriz.iloc[15, 7] = inverso_c8_8
                    terceira_matriz.iloc[16, 7] = inverso_c9_8
                    terceira_matriz.iloc[17, 7] = inverso_c10_8
                    terceira_matriz.iloc[18, 7] = inverso_c11_8

                    #Critério 9
                    c1_9 = terceira_matriz.iloc[8, 9]
                    c2_9 = terceira_matriz.iloc[8, 10]
                    c3_9 = terceira_matriz.iloc[8, 11]
                    c4_9 = terceira_matriz.iloc[8, 12]
                    c5_9 = terceira_matriz.iloc[8, 13]
                    c6_9 = terceira_matriz.iloc[8, 14]
                    c7_9 = terceira_matriz.iloc[8, 15]
                    c8_9 = terceira_matriz.iloc[8, 16]
                    c9_9 = terceira_matriz.iloc[8, 17]
                    c10_9 = terceira_matriz.iloc[8, 18]
                                    
                    # Calcular os inversos
                    inverso_c1_9 = 1 / c1_9
                    inverso_c2_9 = 1 / c2_9
                    inverso_c3_9 = 1 / c3_9
                    inverso_c4_9 = 1 / c4_9
                    inverso_c5_9 = 1 / c5_9
                    inverso_c6_9 = 1 / c6_9
                    inverso_c7_9 = 1 / c7_9
                    inverso_c8_9 = 1 / c8_9
                    inverso_c9_9 = 1 / c9_9
                    inverso_c10_9 = 1 / c10_9
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[9, 8] = inverso_c1_9
                    terceira_matriz.iloc[10, 8] = inverso_c2_9
                    terceira_matriz.iloc[11, 8] = inverso_c3_9 
                    terceira_matriz.iloc[12, 8] = inverso_c4_9 
                    terceira_matriz.iloc[13, 8] = inverso_c5_9
                    terceira_matriz.iloc[14, 8] = inverso_c6_9 
                    terceira_matriz.iloc[15, 8] = inverso_c7_9 
                    terceira_matriz.iloc[16, 8] = inverso_c8_9 
                    terceira_matriz.iloc[17, 8] = inverso_c9_9 
                    terceira_matriz.iloc[18, 8] = inverso_c10_9    
                    
                     #Critério 10
                    c1_10 = terceira_matriz.iloc[9,10]
                    c2_10 = terceira_matriz.iloc[9,11]
                    c3_10 = terceira_matriz.iloc[9,12]
                    c4_10 = terceira_matriz.iloc[9,13]
                    c5_10 = terceira_matriz.iloc[9,14]
                    c6_10 = terceira_matriz.iloc[9,15]
                    c7_10 = terceira_matriz.iloc[9,16]
                    c8_10 = terceira_matriz.iloc[9,17]
                    c9_10 = terceira_matriz.iloc[9,18]
                                                        
                    # Calcular os inversos
                    inverso_c1_10 = 1 / c1_10
                    inverso_c2_10 = 1 / c2_10
                    inverso_c3_10 = 1 / c3_10
                    inverso_c4_10 = 1 / c4_10
                    inverso_c5_10 = 1 / c5_10
                    inverso_c6_10 = 1 / c6_10
                    inverso_c7_10 = 1 / c7_10
                    inverso_c8_10 = 1 / c8_10
                    inverso_c9_10 = 1 / c9_10
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[10, 9] = inverso_c1_10
                    terceira_matriz.iloc[11, 9] = inverso_c2_10
                    terceira_matriz.iloc[12, 9] = inverso_c3_10
                    terceira_matriz.iloc[13, 9] = inverso_c4_10
                    terceira_matriz.iloc[14, 9] = inverso_c5_10
                    terceira_matriz.iloc[15, 9] = inverso_c6_10
                    terceira_matriz.iloc[16, 9] = inverso_c7_10
                    terceira_matriz.iloc[17, 9] = inverso_c8_10
                    terceira_matriz.iloc[18, 9] = inverso_c9_10


                    #Critério 11
                    c1_11 = terceira_matriz.iloc[10,11]
                    c2_11 = terceira_matriz.iloc[10,12]
                    c3_11 = terceira_matriz.iloc[10,13]
                    c4_11 = terceira_matriz.iloc[10,14]
                    c5_11 = terceira_matriz.iloc[10,15]
                    c6_11 = terceira_matriz.iloc[10,16]
                    c7_11 = terceira_matriz.iloc[10,17]
                    c8_11 = terceira_matriz.iloc[10,18]
                                     
                                                                    
                    # Calcular os inversos
                    inverso_c1_11 = 1 / c1_11
                    inverso_c2_11 = 1 / c2_11
                    inverso_c3_11 = 1 / c3_11
                    inverso_c4_11 = 1 / c4_11
                    inverso_c5_11 = 1 / c5_11
                    inverso_c6_11 = 1 / c6_11
                    inverso_c7_11 = 1 / c7_11
                    inverso_c8_11 = 1 / c8_11
                                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[11, 10] = inverso_c1_11
                    terceira_matriz.iloc[12, 10] = inverso_c2_11
                    terceira_matriz.iloc[13, 10] = inverso_c3_11
                    terceira_matriz.iloc[14, 10] = inverso_c4_11
                    terceira_matriz.iloc[15, 10] = inverso_c5_11
                    terceira_matriz.iloc[16, 10] = inverso_c6_11
                    terceira_matriz.iloc[17, 10] = inverso_c7_11
                    terceira_matriz.iloc[18, 10] = inverso_c8_11
                
                                       
                    #Critério 12
                    c1_12 = terceira_matriz.iloc[11,12]
                    c2_12 = terceira_matriz.iloc[11,13]
                    c3_12 = terceira_matriz.iloc[11,14]
                    c4_12 = terceira_matriz.iloc[11,15]
                    c5_12 = terceira_matriz.iloc[11,16]
                    c6_12 = terceira_matriz.iloc[11,17]
                    c7_12 = terceira_matriz.iloc[11,18]
                    
                                                     
                    # Calcular os inversos
                    inverso_c1_12 = 1 / c1_12
                    inverso_c2_12 = 1 / c2_12
                    inverso_c3_12 = 1 / c3_12
                    inverso_c4_12 = 1 / c4_12
                    inverso_c5_12 = 1 / c5_12
                    inverso_c6_12 = 1 / c6_12
                    inverso_c7_12 = 1 / c7_12
                                   
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[12, 11] = inverso_c1_12
                    terceira_matriz.iloc[13, 11] = inverso_c2_12
                    terceira_matriz.iloc[14, 11] = inverso_c3_12  
                    terceira_matriz.iloc[15, 11] = inverso_c4_12 
                    terceira_matriz.iloc[16, 11] = inverso_c5_12
                    terceira_matriz.iloc[17, 11] = inverso_c6_12 
                    terceira_matriz.iloc[18, 11] = inverso_c7_12     
                                         
                     #Critério 13
                    c1_13 = terceira_matriz.iloc[12,13]
                    c2_13 = terceira_matriz.iloc[12,14]
                    c3_13 = terceira_matriz.iloc[12,15]
                    c4_13 = terceira_matriz.iloc[12,16]
                    c5_13 = terceira_matriz.iloc[12,17]
                    c6_13 = terceira_matriz.iloc[12,18]
                                                     
                    # Calcular os inversos
                    inverso_c1_13 = 1 / c1_13
                    inverso_c2_13 = 1 / c2_13
                    inverso_c3_13 = 1 / c3_13
                    inverso_c4_13 = 1 / c4_13
                    inverso_c5_13 = 1 / c5_13
                    inverso_c6_13 = 1 / c6_13
                                   
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[13, 12] = inverso_c1_13
                    terceira_matriz.iloc[14, 12] = inverso_c2_13
                    terceira_matriz.iloc[15, 12] = inverso_c3_13 
                    terceira_matriz.iloc[16, 12] = inverso_c4_13 
                    terceira_matriz.iloc[17, 12] = inverso_c5_13 
                    terceira_matriz.iloc[18, 12] = inverso_c6_13   
                    
                    #Critério 14
                    c1_14 = terceira_matriz.iloc[13,14]
                    c2_14 = terceira_matriz.iloc[13,15]
                    c3_14 = terceira_matriz.iloc[13,16]
                    c4_14 = terceira_matriz.iloc[13,17]
                    c5_14 = terceira_matriz.iloc[13,18]
                                                                      
                    # Calcular os inversos
                    inverso_c1_14 = 1 / c1_14
                    inverso_c2_14 = 1 / c2_14
                    inverso_c3_14 = 1 / c3_14
                    inverso_c4_14 = 1 / c4_14
                    inverso_c5_14 = 1 / c5_14
                                                       
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[14, 13] = inverso_c1_14
                    terceira_matriz.iloc[15, 13] = inverso_c2_14
                    terceira_matriz.iloc[16, 13] = inverso_c3_14
                    terceira_matriz.iloc[17, 13] = inverso_c4_14
                    terceira_matriz.iloc[18, 13] = inverso_c5_14

                    #Critério 15
                    c1_15 = terceira_matriz.iloc[14,15]
                    c2_15 = terceira_matriz.iloc[14,16]
                    c3_15 = terceira_matriz.iloc[14,17]
                    c4_15 = terceira_matriz.iloc[14,18]
                                                                
                    # Calcular os inversos
                    inverso_c1_15 = 1 / c1_15
                    inverso_c2_15 = 1 / c2_15
                    inverso_c3_15 = 1 / c3_15
                    inverso_c4_15 = 1 / c4_15
                                                                           
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[15, 14] = inverso_c1_15
                    terceira_matriz.iloc[16, 14] = inverso_c2_15
                    terceira_matriz.iloc[17, 14] = inverso_c3_15
                    terceira_matriz.iloc[18, 14] = inverso_c4_15

                     #Critério 16
                    c1_15 = terceira_matriz.iloc[15,16]
                    c2_15 = terceira_matriz.iloc[15,17]
                    c3_15 = terceira_matriz.iloc[15,18]
                                                                
                    # Calcular os inversos
                    inverso_c1_15 = 1 / c1_15
                    inverso_c2_15 = 1 / c2_15
                    inverso_c3_15 = 1 / c3_15
                                                                           
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[16, 15] = inverso_c1_15
                    terceira_matriz.iloc[17, 15] = inverso_c2_15
                    terceira_matriz.iloc[18, 15] = inverso_c3_15
                    
                    #Critério 17
                    c1_16 = terceira_matriz.iloc[16,17]
                    c2_16 = terceira_matriz.iloc[16,18]
                                                                
                    # Calcular os inversos
                    inverso_c1_16 = 1 / c1_16
                    inverso_c2_16 = 1 / c2_16
                                                                           
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[17, 16] = inverso_c1_16
                    terceira_matriz.iloc[18, 16] = inverso_c2_16

                    #Critério 18
                    c1_17 = terceira_matriz.iloc[17,18]
                                                                                    
                    # Calcular os inversos
                    inverso_c1_17 = 1 / c1_17
                                                                                               
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[18, 17] = inverso_c1_17
                           


    if num_critérios == 20:
        for i in range(2, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[1, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[1, i] = item["valor"]
                     

        for i in range(3, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[2, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[2, i] = item["valor"]
                     

        for i in range(4, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[3, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[3, i] = item["valor"]
                     

        for i in range(5, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[4, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[4, i] = item["valor"]

        for i in range(6, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[5, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[5, i] = item["valor"]
        
        for i in range(7, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[6, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[6, i] = item["valor"]
        for i in range(8, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[7, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[7, i] = item["valor"]
        for i in range(9, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[8, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[8, i] = item["valor"]
        for i in range(10, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[9, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[9, i] = item["valor"]

        for i in range(11, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[10, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[10, i] = item["valor"]
        
        for i in range(12, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[11, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[11, i] = item["valor"]
        
        for i in range(13, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[12, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[12, i] = item["valor"]
        
        for i in range(14, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[13, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[13, i] = item["valor"]

        for i in range(15, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[14, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[14, i] = item["valor"]

        for i in range(16, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[15, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[15, i] = item["valor"]
        
        for i in range(17, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[16, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[16, i] = item["valor"]
        
        for i in range(18, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[17, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[17, i] = item["valor"]

        for i in range(19, len(terceira_matriz.columns)):
            valor_procurado = terceira_matriz.iloc[18, i]
            valor_procurado_arredondado = round(valor_procurado, 2)  # Arredonda para duas casas decimais

            for item in tabela_ref:
                ref_arredondado = round(item["ref"], 2)  # Arredonda o "ref" da tabela_ref para duas casas decimais

                if ref_arredondado == valor_procurado_arredondado:
                    terceira_matriz.iloc[18, i] = item["valor"]

                    
                                #Inverter a Terceira Matriz
                    #Critério 1
                    c1 = terceira_matriz.iloc[0, 1]
                    c2 = terceira_matriz.iloc[0, 2]
                    c3 = terceira_matriz.iloc[0, 3]
                    c4 = terceira_matriz.iloc[0, 4]
                    c5 = terceira_matriz.iloc[0, 5]
                    c6 = terceira_matriz.iloc[0, 6]
                    c7 = terceira_matriz.iloc[0, 7]
                    c8 = terceira_matriz.iloc[0, 8]
                    c9 = terceira_matriz.iloc[0, 9]
                    c10 = terceira_matriz.iloc[0, 10]
                    c11 = terceira_matriz.iloc[0, 11]
                    c12 = terceira_matriz.iloc[0, 12]
                    c13 = terceira_matriz.iloc[0, 13]
                    c14 = terceira_matriz.iloc[0, 14]
                    c15 = terceira_matriz.iloc[0, 15]
                    c16 = terceira_matriz.iloc[0, 16]
                    c17 = terceira_matriz.iloc[0, 17]
                    c18 = terceira_matriz.iloc[0, 18]
                    c19 = terceira_matriz.iloc[0, 19]
                
                    # Calcular os inversos
                    inverso_c1 = 1 / c1
                    inverso_c2 = 1 / c2
                    inverso_c3 = 1 / c3
                    inverso_c4 = 1 / c4
                    inverso_c5 = 1 / c5
                    inverso_c6 = 1 / c6
                    inverso_c7 = 1 / c7
                    inverso_c8 = 1 / c8
                    inverso_c9 = 1 / c9
                    inverso_c10 = 1 / c10
                    inverso_c11 = 1 / c11
                    inverso_c12 = 1 / c12
                    inverso_c13 = 1 / c13
                    inverso_c14 = 1 / c14
                    inverso_c15 = 1 / c15
                    inverso_c16 = 1 / c16
                    inverso_c17 = 1 / c17
                    inverso_c18 = 1 / c18
                    inverso_c19 = 1 / c19


                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[1, 0] = inverso_c1
                    terceira_matriz.iloc[2, 0] = inverso_c2
                    terceira_matriz.iloc[3, 0] = inverso_c3
                    terceira_matriz.iloc[4, 0] = inverso_c4
                    terceira_matriz.iloc[5, 0] = inverso_c5
                    terceira_matriz.iloc[6, 0] = inverso_c6
                    terceira_matriz.iloc[7, 0] = inverso_c7
                    terceira_matriz.iloc[8, 0] = inverso_c8
                    terceira_matriz.iloc[9, 0] = inverso_c9
                    terceira_matriz.iloc[10, 0] = inverso_c10
                    terceira_matriz.iloc[11, 0] = inverso_c11
                    terceira_matriz.iloc[12, 0] = inverso_c12
                    terceira_matriz.iloc[13, 0] = inverso_c13
                    terceira_matriz.iloc[14, 0] = inverso_c14
                    terceira_matriz.iloc[15, 0] = inverso_c15
                    terceira_matriz.iloc[16, 0] = inverso_c16
                    terceira_matriz.iloc[17, 0] = inverso_c17
                    terceira_matriz.iloc[18, 0] = inverso_c18
                    terceira_matriz.iloc[19, 0] = inverso_c19

                
                    #Critério 2
                    c1_2 = terceira_matriz.iloc[1, 2]
                    c2_2 = terceira_matriz.iloc[1, 3]
                    c3_2 = terceira_matriz.iloc[1, 4]
                    c4_2 = terceira_matriz.iloc[1, 5]
                    c5_2 = terceira_matriz.iloc[1, 6]
                    c6_2 = terceira_matriz.iloc[1, 7]
                    c7_2 = terceira_matriz.iloc[1, 8]
                    c8_2 = terceira_matriz.iloc[1, 9]
                    c9_2 = terceira_matriz.iloc[1, 10]
                    c10_2 = terceira_matriz.iloc[1, 11]
                    c11_2 = terceira_matriz.iloc[1, 12]
                    c12_2 = terceira_matriz.iloc[1, 13]
                    c13_2 = terceira_matriz.iloc[1, 14]
                    c14_2 = terceira_matriz.iloc[1, 15]
                    c15_2 = terceira_matriz.iloc[1, 16]
                    c16_2 = terceira_matriz.iloc[1, 17]
                    c17_2 = terceira_matriz.iloc[1, 18]
                    c18_2 = terceira_matriz.iloc[1, 19]
                    
                
                    # Calcular os inversos
                    inverso_c1_2 = 1 / c1_2
                    inverso_c2_2 = 1 / c2_2
                    inverso_c3_2 = 1 / c3_2
                    inverso_c4_2 = 1 / c4_2
                    inverso_c5_2 = 1 / c5_2
                    inverso_c6_2 = 1 / c6_2
                    inverso_c7_2 = 1 / c7_2
                    inverso_c8_2 = 1 / c8_2
                    inverso_c9_2 = 1 / c9_2
                    inverso_c10_2 = 1 / c10_2
                    inverso_c11_2 = 1 / c11_2
                    inverso_c12_2 = 1 / c12_2
                    inverso_c13_2 = 1 / c13_2
                    inverso_c14_2 = 1 / c14_2
                    inverso_c15_2 = 1 / c15_2
                    inverso_c16_2 = 1 / c16_2
                    inverso_c17_2 = 1 / c17_2
                    inverso_c18_2 = 1 / c18_2



                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[2, 1] = inverso_c1_2
                    terceira_matriz.iloc[3, 1] = inverso_c2_2
                    terceira_matriz.iloc[4, 1] = inverso_c3_2
                    terceira_matriz.iloc[5, 1] = inverso_c4_2
                    terceira_matriz.iloc[6, 1] = inverso_c5_2
                    terceira_matriz.iloc[7, 1] = inverso_c6_2
                    terceira_matriz.iloc[8, 1] = inverso_c7_2
                    terceira_matriz.iloc[9, 1] = inverso_c8_2
                    terceira_matriz.iloc[10, 1] = inverso_c9_2
                    terceira_matriz.iloc[11, 1] = inverso_c10_2
                    terceira_matriz.iloc[12, 1] = inverso_c11_2
                    terceira_matriz.iloc[13, 1] = inverso_c12_2
                    terceira_matriz.iloc[14, 1] = inverso_c13_2
                    terceira_matriz.iloc[15, 1] = inverso_c14_2
                    terceira_matriz.iloc[16, 1] = inverso_c15_2
                    terceira_matriz.iloc[17, 1] = inverso_c16_2
                    terceira_matriz.iloc[18, 1] = inverso_c17_2
                    terceira_matriz.iloc[19, 1] = inverso_c18_2
                    
                
                    #Critério 3
                    c1_3 = terceira_matriz.iloc[2, 3]
                    c2_3 = terceira_matriz.iloc[2, 4]
                    c3_3 = terceira_matriz.iloc[2, 5]
                    c4_3 = terceira_matriz.iloc[2, 6]
                    c5_3 = terceira_matriz.iloc[2, 7]
                    c6_3 = terceira_matriz.iloc[2, 8]
                    c7_3 = terceira_matriz.iloc[2, 9]
                    c8_3 = terceira_matriz.iloc[2, 10]
                    c9_3 = terceira_matriz.iloc[2, 11]
                    c10_3 = terceira_matriz.iloc[2, 12]
                    c11_3 = terceira_matriz.iloc[2, 13]
                    c12_3 = terceira_matriz.iloc[2, 14]
                    c13_3 = terceira_matriz.iloc[2, 15]
                    c14_3 = terceira_matriz.iloc[2, 16]
                    c15_3 = terceira_matriz.iloc[2, 17]
                    c16_3 = terceira_matriz.iloc[2, 18]
                    c17_3 = terceira_matriz.iloc[2, 19]
                    

                    # Calcular os inversos
                    inverso_c1_3 = 1 / c1_3
                    inverso_c2_3 = 1 / c2_3
                    inverso_c3_3 = 1 / c3_3
                    inverso_c4_3 = 1 / c4_3
                    inverso_c5_3 = 1 / c5_3
                    inverso_c6_3 = 1 / c6_3
                    inverso_c7_3 = 1 / c7_3
                    inverso_c8_3 = 1 / c8_3
                    inverso_c9_3 = 1 / c9_3
                    inverso_c10_3 = 1 / c10_3
                    inverso_c11_3 = 1 / c11_3
                    inverso_c12_3 = 1 / c12_3
                    inverso_c13_3 = 1 / c13_3
                    inverso_c14_3 = 1 / c14_3
                    inverso_c15_3 = 1 / c15_3
                    inverso_c16_3 = 1 / c16_3
                    inverso_c17_3 = 1 / c17_3
                
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[3, 2] = inverso_c1_3
                    terceira_matriz.iloc[4, 2] = inverso_c2_3
                    terceira_matriz.iloc[5, 2] = inverso_c3_3
                    terceira_matriz.iloc[6, 2] = inverso_c4_3
                    terceira_matriz.iloc[7, 2] = inverso_c5_3
                    terceira_matriz.iloc[8, 2] = inverso_c6_3
                    terceira_matriz.iloc[9, 2] = inverso_c7_3
                    terceira_matriz.iloc[10, 2] = inverso_c8_3
                    terceira_matriz.iloc[11, 2] = inverso_c9_3
                    terceira_matriz.iloc[12, 2] = inverso_c10_3
                    terceira_matriz.iloc[13, 2] = inverso_c11_3
                    terceira_matriz.iloc[14, 2] = inverso_c12_3
                    terceira_matriz.iloc[15, 2] = inverso_c13_3
                    terceira_matriz.iloc[16, 2] = inverso_c14_3
                    terceira_matriz.iloc[17, 2] = inverso_c15_3
                    terceira_matriz.iloc[18, 2] = inverso_c16_3   
                    terceira_matriz.iloc[19, 2] = inverso_c17_3                    


                    #Critério 4
                    c1_4 = terceira_matriz.iloc[3, 4]
                    c2_4 = terceira_matriz.iloc[3, 5]
                    c3_4 = terceira_matriz.iloc[3, 6]
                    c4_4 = terceira_matriz.iloc[3, 7]
                    c5_4 = terceira_matriz.iloc[3, 8]
                    c6_4 = terceira_matriz.iloc[3, 9]
                    c7_4 = terceira_matriz.iloc[3, 10]
                    c8_4 = terceira_matriz.iloc[3, 11]
                    c9_4 = terceira_matriz.iloc[3, 12]
                    c10_4 = terceira_matriz.iloc[3, 13]
                    c11_4 = terceira_matriz.iloc[3, 14]
                    c12_4 = terceira_matriz.iloc[3, 15]
                    c13_4 = terceira_matriz.iloc[3, 16]
                    c14_4 = terceira_matriz.iloc[3, 17]
                    c15_4 = terceira_matriz.iloc[3, 18]
                    c16_4 = terceira_matriz.iloc[3, 19]
                
                    # Calcular os inversos
                    inverso_c1_4 = 1 / c1_4
                    inverso_c2_4 = 1 / c2_4
                    inverso_c3_4 = 1 / c3_4
                    inverso_c4_4 = 1 / c4_4
                    inverso_c5_4 = 1 / c5_4
                    inverso_c6_4 = 1 / c6_4
                    inverso_c7_4 = 1 / c7_4
                    inverso_c8_4 = 1 / c8_4
                    inverso_c9_4 = 1 / c9_4
                    inverso_c10_4 = 1 / c10_4
                    inverso_c11_4 = 1 / c11_4
                    inverso_c12_4 = 1 / c12_4
                    inverso_c13_4 = 1 / c13_4
                    inverso_c14_4 = 1 / c14_4
                    inverso_c15_4 = 1 / c15_4
                    inverso_c16_4 = 1 / c16_4
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[4, 3] = inverso_c1_4
                    terceira_matriz.iloc[5, 3] = inverso_c2_4
                    terceira_matriz.iloc[6, 3] = inverso_c3_4
                    terceira_matriz.iloc[7, 3] = inverso_c4_4
                    terceira_matriz.iloc[8, 3] = inverso_c5_4
                    terceira_matriz.iloc[9, 3] = inverso_c6_4
                    terceira_matriz.iloc[10, 3] = inverso_c7_4
                    terceira_matriz.iloc[11, 3] = inverso_c8_4
                    terceira_matriz.iloc[12, 3] = inverso_c9_4
                    terceira_matriz.iloc[13, 3] = inverso_c10_4
                    terceira_matriz.iloc[14, 3] = inverso_c11_4
                    terceira_matriz.iloc[15, 3] = inverso_c12_4
                    terceira_matriz.iloc[16, 3] = inverso_c13_4
                    terceira_matriz.iloc[17, 3] = inverso_c14_4
                    terceira_matriz.iloc[18, 3] = inverso_c15_4
                    terceira_matriz.iloc[19, 3] = inverso_c16_4


                    #Critério 5
                    c1_5 = terceira_matriz.iloc[4, 5]
                    c2_5 = terceira_matriz.iloc[4, 6]
                    c3_5 = terceira_matriz.iloc[4, 7]
                    c4_5 = terceira_matriz.iloc[4, 8]
                    c5_5 = terceira_matriz.iloc[4, 9]
                    c6_5 = terceira_matriz.iloc[4, 10]
                    c7_5 = terceira_matriz.iloc[4, 11]
                    c8_5 = terceira_matriz.iloc[4, 12]
                    c9_5 = terceira_matriz.iloc[4, 13]
                    c10_5 = terceira_matriz.iloc[4, 14]
                    c11_5 = terceira_matriz.iloc[4, 15]
                    c12_5 = terceira_matriz.iloc[4, 16]
                    c13_5 = terceira_matriz.iloc[4, 17]
                    c14_5 = terceira_matriz.iloc[4, 18]
                    c15_5 = terceira_matriz.iloc[4, 19]
                                    
                    # Calcular os inversos
                    inverso_c1_5 = 1 / c1_5
                    inverso_c2_5 = 1 / c2_5
                    inverso_c3_5 = 1 / c3_5
                    inverso_c4_5 = 1 / c4_5
                    inverso_c5_5 = 1 / c5_5
                    inverso_c6_5 = 1 / c6_5
                    inverso_c7_5 = 1 / c7_5
                    inverso_c8_5 = 1 / c8_5
                    inverso_c9_5 = 1 / c9_5
                    inverso_c10_5 = 1 / c10_5
                    inverso_c11_5 = 1 / c11_5
                    inverso_c12_5 = 1 / c12_5
                    inverso_c13_5 = 1 / c13_5
                    inverso_c14_5 = 1 / c14_5
                    inverso_c15_5 = 1 / c15_5
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[5, 4] = inverso_c1_5
                    terceira_matriz.iloc[6, 4] = inverso_c2_5
                    terceira_matriz.iloc[7, 4] = inverso_c3_5
                    terceira_matriz.iloc[8, 4] = inverso_c4_5
                    terceira_matriz.iloc[9, 4] = inverso_c5_5
                    terceira_matriz.iloc[10, 4] = inverso_c6_5
                    terceira_matriz.iloc[11, 4] = inverso_c7_5
                    terceira_matriz.iloc[12, 4] = inverso_c8_5
                    terceira_matriz.iloc[13, 4] = inverso_c9_5
                    terceira_matriz.iloc[14, 4] = inverso_c10_5
                    terceira_matriz.iloc[15, 4] = inverso_c11_5
                    terceira_matriz.iloc[16, 4] = inverso_c12_5
                    terceira_matriz.iloc[17, 4] = inverso_c13_5
                    terceira_matriz.iloc[18, 4] = inverso_c14_5
                    terceira_matriz.iloc[19, 4] = inverso_c15_5



                     #Critério 6
                    c1_6 = terceira_matriz.iloc[5, 6]
                    c2_6 = terceira_matriz.iloc[5, 7]
                    c3_6 = terceira_matriz.iloc[5, 8]
                    c4_6 = terceira_matriz.iloc[5, 9]
                    c5_6 = terceira_matriz.iloc[5, 10]
                    c6_6 = terceira_matriz.iloc[5, 11]
                    c7_6 = terceira_matriz.iloc[5, 12]
                    c8_6 = terceira_matriz.iloc[5, 13]
                    c9_6 = terceira_matriz.iloc[5, 14]
                    c10_6 = terceira_matriz.iloc[5, 15]
                    c11_6 = terceira_matriz.iloc[5, 16]
                    c12_6 = terceira_matriz.iloc[5, 17]
                    c13_6 = terceira_matriz.iloc[5, 18]
                    c14_6 = terceira_matriz.iloc[5, 19]
                                    
                                    
                    # Calcular os inversos
                    inverso_c1_6 = 1 / c1_6
                    inverso_c2_6 = 1 / c2_6
                    inverso_c3_6 = 1 / c3_6
                    inverso_c4_6 = 1 / c4_6
                    inverso_c5_6 = 1 / c5_6
                    inverso_c6_6 = 1 / c6_6
                    inverso_c7_6 = 1 / c7_6
                    inverso_c8_6 = 1 / c8_6
                    inverso_c9_6 = 1 / c9_6
                    inverso_c10_6 = 1 / c10_6
                    inverso_c11_6 = 1 / c11_6
                    inverso_c12_6 = 1 / c12_6
                    inverso_c13_6 = 1 / c13_6
                    inverso_c14_6 = 1 / c14_6
                                      
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[6, 5] = inverso_c1_6
                    terceira_matriz.iloc[7, 5] = inverso_c2_6
                    terceira_matriz.iloc[8, 5] = inverso_c3_6
                    terceira_matriz.iloc[9, 5] = inverso_c4_6
                    terceira_matriz.iloc[10, 5] = inverso_c5_6
                    terceira_matriz.iloc[11, 5] = inverso_c6_6
                    terceira_matriz.iloc[12, 5] = inverso_c7_6
                    terceira_matriz.iloc[13, 5] = inverso_c8_6
                    terceira_matriz.iloc[14, 5] = inverso_c9_6
                    terceira_matriz.iloc[15, 5] = inverso_c10_6
                    terceira_matriz.iloc[16, 5] = inverso_c11_6
                    terceira_matriz.iloc[17, 5] = inverso_c12_6
                    terceira_matriz.iloc[18, 5] = inverso_c13_6
                    terceira_matriz.iloc[19, 5] = inverso_c14_6


                    #Critério 7
                    c1_7 = terceira_matriz.iloc[6, 7]
                    c2_7 = terceira_matriz.iloc[6, 8]
                    c3_7 = terceira_matriz.iloc[6, 9]
                    c4_7 = terceira_matriz.iloc[6, 10]
                    c5_7 = terceira_matriz.iloc[6, 11]
                    c6_7 = terceira_matriz.iloc[6, 12]
                    c7_7 = terceira_matriz.iloc[6, 13]
                    c8_7 = terceira_matriz.iloc[6, 14]
                    c9_7 = terceira_matriz.iloc[6, 15]
                    c10_7 = terceira_matriz.iloc[6, 16]
                    c11_7 = terceira_matriz.iloc[6, 17]
                    c12_7 = terceira_matriz.iloc[6, 18]
                    c13_7 = terceira_matriz.iloc[6, 19]
                                                       
                    # Calcular os inversos
                    inverso_c1_7 = 1 / c1_7
                    inverso_c2_7 = 1 / c2_7
                    inverso_c3_7 = 1 / c3_7
                    inverso_c4_7 = 1 / c4_7
                    inverso_c5_7 = 1 / c5_7
                    inverso_c6_7 = 1 / c6_7
                    inverso_c7_7 = 1 / c7_7
                    inverso_c8_7 = 1 / c8_7
                    inverso_c9_7 = 1 / c9_7
                    inverso_c10_7 = 1 / c10_7
                    inverso_c11_7 = 1 / c11_7
                    inverso_c12_7 = 1 / c12_7
                    inverso_c13_7 = 1 / c13_7
                                                         
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[7, 6] = inverso_c1_7
                    terceira_matriz.iloc[8, 6] = inverso_c2_7
                    terceira_matriz.iloc[9, 6] = inverso_c3_7
                    terceira_matriz.iloc[10, 6] = inverso_c4_7
                    terceira_matriz.iloc[11, 6] = inverso_c5_7
                    terceira_matriz.iloc[12, 6] = inverso_c6_7
                    terceira_matriz.iloc[13, 6] = inverso_c7_7
                    terceira_matriz.iloc[14, 6] = inverso_c8_7
                    terceira_matriz.iloc[15, 6] = inverso_c9_7
                    terceira_matriz.iloc[16, 6] = inverso_c10_7
                    terceira_matriz.iloc[17, 6] = inverso_c11_7
                    terceira_matriz.iloc[18, 6] = inverso_c12_7
                    terceira_matriz.iloc[19, 6] = inverso_c13_7


                    #Critério 8
                    c1_8 = terceira_matriz.iloc[7,8]
                    c2_8 = terceira_matriz.iloc[7,9]
                    c3_8 = terceira_matriz.iloc[7,10]
                    c4_8 = terceira_matriz.iloc[7,11]
                    c5_8 = terceira_matriz.iloc[7,12]
                    c6_8 = terceira_matriz.iloc[7,13]
                    c7_8 = terceira_matriz.iloc[7,14]
                    c8_8 = terceira_matriz.iloc[7,15]
                    c9_8 = terceira_matriz.iloc[7,16]
                    c10_8 = terceira_matriz.iloc[7,17]
                    c11_8 = terceira_matriz.iloc[7,18]
                    c12_8 = terceira_matriz.iloc[7,19]
                                    
                    # Calcular os inversos
                    inverso_c1_8 = 1 / c1_8
                    inverso_c2_8 = 1 / c2_8
                    inverso_c3_8 = 1 / c3_8
                    inverso_c4_8 = 1 / c4_8
                    inverso_c5_8 = 1 / c5_8
                    inverso_c6_8 = 1 / c6_8
                    inverso_c7_8 = 1 / c7_8
                    inverso_c8_8 = 1 / c8_8
                    inverso_c9_8 = 1 / c9_8
                    inverso_c10_8 = 1 / c10_8
                    inverso_c11_8 = 1 / c11_8
                    inverso_c12_8 = 1 / c12_8
                
                
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[8, 7] = inverso_c1_8
                    terceira_matriz.iloc[9, 7] = inverso_c2_8
                    terceira_matriz.iloc[10, 7] = inverso_c3_8
                    terceira_matriz.iloc[11, 7] = inverso_c4_8
                    terceira_matriz.iloc[12, 7] = inverso_c5_8
                    terceira_matriz.iloc[13, 7] = inverso_c6_8
                    terceira_matriz.iloc[14, 7] = inverso_c7_8
                    terceira_matriz.iloc[15, 7] = inverso_c8_8
                    terceira_matriz.iloc[16, 7] = inverso_c9_8
                    terceira_matriz.iloc[17, 7] = inverso_c10_8
                    terceira_matriz.iloc[18, 7] = inverso_c11_8
                    terceira_matriz.iloc[19, 7] = inverso_c12_8

                    #Critério 9
                    c1_9 = terceira_matriz.iloc[8, 9]
                    c2_9 = terceira_matriz.iloc[8, 10]
                    c3_9 = terceira_matriz.iloc[8, 11]
                    c4_9 = terceira_matriz.iloc[8, 12]
                    c5_9 = terceira_matriz.iloc[8, 13]
                    c6_9 = terceira_matriz.iloc[8, 14]
                    c7_9 = terceira_matriz.iloc[8, 15]
                    c8_9 = terceira_matriz.iloc[8, 16]
                    c9_9 = terceira_matriz.iloc[8, 17]
                    c10_9 = terceira_matriz.iloc[8, 18]
                    c11_9 = terceira_matriz.iloc[8, 19]
                                    
                    # Calcular os inversos
                    inverso_c1_9 = 1 / c1_9
                    inverso_c2_9 = 1 / c2_9
                    inverso_c3_9 = 1 / c3_9
                    inverso_c4_9 = 1 / c4_9
                    inverso_c5_9 = 1 / c5_9
                    inverso_c6_9 = 1 / c6_9
                    inverso_c7_9 = 1 / c7_9
                    inverso_c8_9 = 1 / c8_9
                    inverso_c9_9 = 1 / c9_9
                    inverso_c10_9 = 1 / c10_9
                    inverso_c11_9 = 1 / c11_9
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[9, 8] = inverso_c1_9
                    terceira_matriz.iloc[10, 8] = inverso_c2_9
                    terceira_matriz.iloc[11, 8] = inverso_c3_9 
                    terceira_matriz.iloc[12, 8] = inverso_c4_9 
                    terceira_matriz.iloc[13, 8] = inverso_c5_9
                    terceira_matriz.iloc[14, 8] = inverso_c6_9 
                    terceira_matriz.iloc[15, 8] = inverso_c7_9 
                    terceira_matriz.iloc[16, 8] = inverso_c8_9 
                    terceira_matriz.iloc[17, 8] = inverso_c9_9 
                    terceira_matriz.iloc[18, 8] = inverso_c10_9 
                    terceira_matriz.iloc[19, 8] = inverso_c11_9    
                    
                     #Critério 10
                    c1_10 = terceira_matriz.iloc[9,10]
                    c2_10 = terceira_matriz.iloc[9,11]
                    c3_10 = terceira_matriz.iloc[9,12]
                    c4_10 = terceira_matriz.iloc[9,13]
                    c5_10 = terceira_matriz.iloc[9,14]
                    c6_10 = terceira_matriz.iloc[9,15]
                    c7_10 = terceira_matriz.iloc[9,16]
                    c8_10 = terceira_matriz.iloc[9,17]
                    c9_10 = terceira_matriz.iloc[9,18]
                    c10_10 = terceira_matriz.iloc[9,19]
                                                        
                    # Calcular os inversos
                    inverso_c1_10 = 1 / c1_10
                    inverso_c2_10 = 1 / c2_10
                    inverso_c3_10 = 1 / c3_10
                    inverso_c4_10 = 1 / c4_10
                    inverso_c5_10 = 1 / c5_10
                    inverso_c6_10 = 1 / c6_10
                    inverso_c7_10 = 1 / c7_10
                    inverso_c8_10 = 1 / c8_10
                    inverso_c9_10 = 1 / c9_10
                    inverso_c10_10 = 1 / c10_10
                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[10, 9] = inverso_c1_10
                    terceira_matriz.iloc[11, 9] = inverso_c2_10
                    terceira_matriz.iloc[12, 9] = inverso_c3_10
                    terceira_matriz.iloc[13, 9] = inverso_c4_10
                    terceira_matriz.iloc[14, 9] = inverso_c5_10
                    terceira_matriz.iloc[15, 9] = inverso_c6_10
                    terceira_matriz.iloc[16, 9] = inverso_c7_10
                    terceira_matriz.iloc[17, 9] = inverso_c8_10
                    terceira_matriz.iloc[18, 9] = inverso_c9_10
                    terceira_matriz.iloc[19, 9] = inverso_c10_10


                    #Critério 11
                    c1_11 = terceira_matriz.iloc[10,11]
                    c2_11 = terceira_matriz.iloc[10,12]
                    c3_11 = terceira_matriz.iloc[10,13]
                    c4_11 = terceira_matriz.iloc[10,14]
                    c5_11 = terceira_matriz.iloc[10,15]
                    c6_11 = terceira_matriz.iloc[10,16]
                    c7_11 = terceira_matriz.iloc[10,17]
                    c8_11 = terceira_matriz.iloc[10,18]
                    c9_11 = terceira_matriz.iloc[10,19]
                                     
                                                                    
                    # Calcular os inversos
                    inverso_c1_11 = 1 / c1_11
                    inverso_c2_11 = 1 / c2_11
                    inverso_c3_11 = 1 / c3_11
                    inverso_c4_11 = 1 / c4_11
                    inverso_c5_11 = 1 / c5_11
                    inverso_c6_11 = 1 / c6_11
                    inverso_c7_11 = 1 / c7_11
                    inverso_c8_11 = 1 / c8_11
                    inverso_c9_11 = 1 / c9_11
                                
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[11, 10] = inverso_c1_11
                    terceira_matriz.iloc[12, 10] = inverso_c2_11
                    terceira_matriz.iloc[13, 10] = inverso_c3_11
                    terceira_matriz.iloc[14, 10] = inverso_c4_11
                    terceira_matriz.iloc[15, 10] = inverso_c5_11
                    terceira_matriz.iloc[16, 10] = inverso_c6_11
                    terceira_matriz.iloc[17, 10] = inverso_c7_11
                    terceira_matriz.iloc[18, 10] = inverso_c8_11
                    terceira_matriz.iloc[19, 10] = inverso_c9_11
                
                                       
                    #Critério 12
                    c1_12 = terceira_matriz.iloc[11,12]
                    c2_12 = terceira_matriz.iloc[11,13]
                    c3_12 = terceira_matriz.iloc[11,14]
                    c4_12 = terceira_matriz.iloc[11,15]
                    c5_12 = terceira_matriz.iloc[11,16]
                    c6_12 = terceira_matriz.iloc[11,17]
                    c7_12 = terceira_matriz.iloc[11,18]
                    c8_12 = terceira_matriz.iloc[11,19]
                    
                                                     
                    # Calcular os inversos
                    inverso_c1_12 = 1 / c1_12
                    inverso_c2_12 = 1 / c2_12
                    inverso_c3_12 = 1 / c3_12
                    inverso_c4_12 = 1 / c4_12
                    inverso_c5_12 = 1 / c5_12
                    inverso_c6_12 = 1 / c6_12
                    inverso_c7_12 = 1 / c7_12
                    inverso_c8_12 = 1 / c8_12
                                   
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[12, 11] = inverso_c1_12
                    terceira_matriz.iloc[13, 11] = inverso_c2_12
                    terceira_matriz.iloc[14, 11] = inverso_c3_12  
                    terceira_matriz.iloc[15, 11] = inverso_c4_12 
                    terceira_matriz.iloc[16, 11] = inverso_c5_12
                    terceira_matriz.iloc[17, 11] = inverso_c6_12 
                    terceira_matriz.iloc[18, 11] = inverso_c7_12 
                    terceira_matriz.iloc[19, 11] = inverso_c8_12     
                                         
                     #Critério 13
                    c1_13 = terceira_matriz.iloc[12,13]
                    c2_13 = terceira_matriz.iloc[12,14]
                    c3_13 = terceira_matriz.iloc[12,15]
                    c4_13 = terceira_matriz.iloc[12,16]
                    c5_13 = terceira_matriz.iloc[12,17]
                    c6_13 = terceira_matriz.iloc[12,18]
                    c7_13 = terceira_matriz.iloc[12,19]
                                                     
                    # Calcular os inversos
                    inverso_c1_13 = 1 / c1_13
                    inverso_c2_13 = 1 / c2_13
                    inverso_c3_13 = 1 / c3_13
                    inverso_c4_13 = 1 / c4_13
                    inverso_c5_13 = 1 / c5_13
                    inverso_c6_13 = 1 / c6_13
                    inverso_c7_13 = 1 / c7_13
                                   
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[13, 12] = inverso_c1_13
                    terceira_matriz.iloc[14, 12] = inverso_c2_13
                    terceira_matriz.iloc[15, 12] = inverso_c3_13 
                    terceira_matriz.iloc[16, 12] = inverso_c4_13 
                    terceira_matriz.iloc[17, 12] = inverso_c5_13 
                    terceira_matriz.iloc[18, 12] = inverso_c6_13
                    terceira_matriz.iloc[19, 12] = inverso_c7_13   
                    
                    #Critério 14
                    c1_14 = terceira_matriz.iloc[13,14]
                    c2_14 = terceira_matriz.iloc[13,15]
                    c3_14 = terceira_matriz.iloc[13,16]
                    c4_14 = terceira_matriz.iloc[13,17]
                    c5_14 = terceira_matriz.iloc[13,18]
                    c6_14 = terceira_matriz.iloc[13,19]
                                                                      
                    # Calcular os inversos
                    inverso_c1_14 = 1 / c1_14
                    inverso_c2_14 = 1 / c2_14
                    inverso_c3_14 = 1 / c3_14
                    inverso_c4_14 = 1 / c4_14
                    inverso_c5_14 = 1 / c5_14
                    inverso_c6_14 = 1 / c6_14
                                                       
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[14, 13] = inverso_c1_14
                    terceira_matriz.iloc[15, 13] = inverso_c2_14
                    terceira_matriz.iloc[16, 13] = inverso_c3_14
                    terceira_matriz.iloc[17, 13] = inverso_c4_14
                    terceira_matriz.iloc[18, 13] = inverso_c5_14
                    terceira_matriz.iloc[19, 13] = inverso_c6_14

                    #Critério 15
                    c1_15 = terceira_matriz.iloc[14,15]
                    c2_15 = terceira_matriz.iloc[14,16]
                    c3_15 = terceira_matriz.iloc[14,17]
                    c4_15 = terceira_matriz.iloc[14,18]
                    c5_15 = terceira_matriz.iloc[14,19]
                                                                
                    # Calcular os inversos
                    inverso_c1_15 = 1 / c1_15
                    inverso_c2_15 = 1 / c2_15
                    inverso_c3_15 = 1 / c3_15
                    inverso_c4_15 = 1 / c4_15
                    inverso_c5_15 = 1 / c5_15
                                                                           
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[15, 14] = inverso_c1_15
                    terceira_matriz.iloc[16, 14] = inverso_c2_15
                    terceira_matriz.iloc[17, 14] = inverso_c3_15
                    terceira_matriz.iloc[18, 14] = inverso_c4_15
                    terceira_matriz.iloc[19, 14] = inverso_c5_15

                     #Critério 16
                    c1_15 = terceira_matriz.iloc[15,16]
                    c2_15 = terceira_matriz.iloc[15,17]
                    c3_15 = terceira_matriz.iloc[15,18]
                    c4_15 = terceira_matriz.iloc[15,19]
                                                                
                    # Calcular os inversos
                    inverso_c1_15 = 1 / c1_15
                    inverso_c2_15 = 1 / c2_15
                    inverso_c3_15 = 1 / c3_15
                    inverso_c4_15 = 1 / c4_15
                                                                           
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[16, 15] = inverso_c1_15
                    terceira_matriz.iloc[17, 15] = inverso_c2_15
                    terceira_matriz.iloc[18, 15] = inverso_c3_15
                    terceira_matriz.iloc[19, 15] = inverso_c4_15
                    
                    #Critério 17
                    c1_16 = terceira_matriz.iloc[16,17]
                    c2_16 = terceira_matriz.iloc[16,18]
                    c3_16 = terceira_matriz.iloc[16,19]
                                                                
                    # Calcular os inversos
                    inverso_c1_16 = 1 / c1_16
                    inverso_c2_16 = 1 / c2_16
                    inverso_c3_16 = 1 / c3_16
                                                                           
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[17, 16] = inverso_c1_16
                    terceira_matriz.iloc[18, 16] = inverso_c2_16
                    terceira_matriz.iloc[18, 16] = inverso_c3_16

                    #Critério 18
                    c1_17 = terceira_matriz.iloc[17,18]
                    c2_17 = terceira_matriz.iloc[17,19]
                                                                                    
                    # Calcular os inversos
                    inverso_c1_17 = 1 / c1_17
                    inverso_c2_17 = 1 / c2_17
                                                                                               
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[18, 17] = inverso_c1_17
                    terceira_matriz.iloc[19, 17] = inverso_c2_17

                     #Critério 19
                    c1_18 = terceira_matriz.iloc[19,18]
                                                                                    
                    # Calcular os inversos
                    inverso_c1_18 = 1 / c1_18
                                                                                               
                    # Atribuir os inversos aos locais desejados na segunda e terceira linhas
                    terceira_matriz.iloc[19, 18] = inverso_c1_18
                           


    


    return terceira_matriz






def calcular_autovetor(terceira_matriz):
    autovetor = terceira_matriz.copy()
    num_critérios = st.session_state.num_critérios

    for i in range(num_critérios):
        if autovetor.index[i] != "Soma das Colunas" and autovetor.index[i] != "Soma das Linhas":
            media_geometrica = autovetor.iloc[i, :].prod() ** (1 / num_critérios)
            autovetor.loc[autovetor.index[i], "Média Geométrica"] = media_geometrica


    return autovetor

def calcular_peso(autovetor):
    peso = autovetor.copy()
    num_critérios = st.session_state.num_critérios
    
    # Calcule a soma de todas as médias geométricas
    soma_medias_geométricas = autovetor["Média Geométrica"].sum()

    # Calcule o peso para cada critério
    for i in range(num_critérios):
        if peso.index[i] != "Soma das Colunas" and peso.index[i] != "Soma das Linhas":
            peso.loc[peso.index[i], "Peso"] = peso.loc[peso.index[i], "Média Geométrica"] / soma_medias_geométricas

    return peso

def somar_criterios(terceira_matriz):

    soma_criterios = terceira_matriz.sum(axis=0)

    return soma_criterios

def produto_matricial(soma_criterios, peso):
    
    valor1 = soma_criterios.to_numpy().reshape(1, -1)
    valor2 = peso["Peso"].to_numpy().reshape(-1, 1)
    matriz_resultante = np.dot(valor1, valor2)
    return matriz_resultante

def ci(matriz_resultante):
    num_critérios = st.session_state.num_critérios
    resultado_ci = (matriz_resultante - num_critérios) / (num_critérios - 1)
    return resultado_ci

def calcular_cr(resultado_ci, tabela_cr):
    num_critérios = st.session_state.num_critérios
    if num_critérios in tabela_cr:
        ri = tabela_cr[num_critérios]
        cr = resultado_ci / ri
        return cr
    else:
        return None 

def rankear_peso(peso):
    # Sort the criteria based on their weights in descending order
    sorted_peso = peso[peso.index != "Soma das Colunas"].sort_values(by="Peso", ascending=False)

    # Calculate the weight percent for each criterion
    total_weight = sorted_peso["Peso"].sum()
    sorted_peso["Weight Percent"] = (sorted_peso["Peso"] / total_weight) * 100

    # Create a ranking table with position and the sorted criteria
    ranking = pd.DataFrame({
        "Posição": range(1, len(sorted_peso) + 1),
        "Critério": sorted_peso.index,
        "Peso": sorted_peso["Peso"],
        "%": sorted_peso["Weight Percent"]
    })

    return ranking

  #  num_critérios = st.session_state.num_critérios
    
   # soma_values = terceira_matriz.loc["Soma"].tolist()
    #pesos_values = terceira_matriz.loc["Pesos"].tolist()
    #auto_vetor_values = terceira_matriz.loc["Auto Vetor"].tolist()

    #vetor1 = quarta_matriz.loc["Soma"].values
    #vetor2 = quarta_matriz.loc["Pesos"].values
    #lambda_max = np.dot(vetor1, vetor2)

    # Extrair a linha Σ (soma das colunas)
   # linha_sigma = terceira_matriz.loc["Σ"].values
    # Extrair a coluna "Auto Vetor"
    #coluna_auto_vetor = terceira_matriz["Auto Vetor"].values
    # Calculate λmax
   # lambda_max = np.matmul(linha_sigma, coluna_auto_vetor)

    # Calculate CI (Consistency Index)
    #consistency_i = (lambda_max - num_critérios) / (num_critérios - 1)


    # Calculate CR (Consistency R)
    #consistency_r = consistency_i / tabela_cr[num_critérios]

    # Create the Consistência DataFrame
    #consistencia = pd.DataFrame({
    #    'λmax': [lambda_max],
     #   'CI': [consistency_i],
    #   'CR': [consistency_r]
    #})

    #consistencia['λmax'] = consistencia['λmax'].round(4)
    #consistencia['CI'] = consistencia['CI'].round(4)
    #consistencia['CR'] = consistencia['CR'].round(4)

    #return consistencia

# Configuração da página Streamlit
st.set_page_config(
    page_title="AHP PPGEPS",
    page_icon="✅",
    layout="wide",
)




# Execução do aplicativo
if "current_step" not in st.session_state:
    st.session_state.current_step = "numero_critérios"
if st.session_state.current_step == "pagina_numero_critérios":
    pagina_numero_critérios()

if st.session_state.current_step == "numero_critérios":
    st.title("Analytic Hierarchy Process (AHP)")
    if not pagina_numero_critérios():
        st.stop()
elif st.session_state.current_step == "nome_criterios":
    pagina_nome_critérios()
elif st.session_state.current_step == "elicitacao_pesos":
    pagina_elicitacao_pesos()
# ...
if st.session_state.current_step == "matriz_decisao":
    st.title("Matriz de Decisão")

    if "num_critérios" not in st.session_state:
        st.warning("Por favor, insira o número de critérios na página anterior.")
    else:
        matriz_decisao = calcular_matriz_decisao()
        if matriz_decisao is not None:
            st.write(matriz_decisao)

           # Primeiro, calcule a matriz de decisão
            matriz_decisao = calcular_matriz_decisao()

            # Em seguida, gere a segunda matriz usando a função gerar_segunda_matriz
            segunda_matriz = gerar_segunda_matriz(matriz_decisao)

           
            st.write("Matriz de Decisão Subtração:")
            st.write(segunda_matriz)

            # Agora você pode chamar a função para gerar a terceira matriz
            terceira_matriz = gerar_terceira_matriz(segunda_matriz)
            st.title("Terceira Matriz")
            st.write(terceira_matriz)

            autovetor = calcular_autovetor(terceira_matriz)
            st.title("Auto Vetor")
            st.write(autovetor)

            peso = calcular_peso(autovetor)
            st.title("Peso")
            st.write(peso)

            soma_criterios = somar_criterios(terceira_matriz)
            st.title("Soma")
            st.write(soma_criterios)

            matriz_resultante = produto_matricial(soma_criterios, peso)
            st.title("λmax")
            st.write(matriz_resultante)

            resultado_ci = ci(matriz_resultante)
            st.title("CI")
            st.write(resultado_ci)

            cr = calcular_cr(resultado_ci, tabela_cr)
            st.title("CR")
            st.write(cr)

            ranking = rankear_peso(peso)
            st.write("Ranking de Pesos:")
            st.write(ranking)



            


            