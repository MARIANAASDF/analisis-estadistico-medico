import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

st.title("Análisis Estadístico Médico desde Excel")

# Cargar archivo
uploaded_file = st.file_uploader("Cargar archivo Excel", type=["xlsx", "xls"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.subheader("Vista previa de los datos")
    st.dataframe(df)

    # Estadísticas descriptivas
    st.subheader("Estadísticas Descriptivas")
    st.write(df.describe())

    # Selección de variables para análisis
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    if len(numeric_cols) >= 2:
        var1 = st.selectbox("Variable 1", numeric_cols)
        var2 = st.selectbox("Variable 2", numeric_cols)

        # Prueba de correlación
        st.subheader(f"Correlación entre {var1} y {var2}")
        corr, p_value = stats.pearsonr(df[var1], df[var2])
        st.write(f"Coeficiente de correlación: {corr:.2f}")
        st.write(f"Valor p: {p_value:.4f}")

        # Gráfico
        fig, ax = plt.subplots()
        sns.scatterplot(x=var1, y=var2, data=df, ax=ax)
        st.pyplot(fig)

    # Exportar resumen
    if st.button("Exportar estadísticas descriptivas"):
        resumen = df.describe().transpose()
        resumen.to_excel("resumen.xlsx")
        with open("resumen.xlsx", "rb") as f:
            st.download_button("Descargar archivo", f, file_name="resumen.xlsx")