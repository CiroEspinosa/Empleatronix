import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('EMPLEATRONIX')
df = pd.read_csv('data/employees.csv')
st.write("Todos los datos sobre los empleados en una aplicación.")

# if st.checkbox('Mostrar la tabla'):
st.write(df)

st.divider()
cols = st.columns(3)
fig, ax = plt.subplots()
color_bars = cols[0].color_picker('Elige un color para las barras', "#3475B3")
toggle_show_name = cols[1].toggle('Mostrar el nombre',value=True)
toggle_show_salary = cols[2].toggle('Mostrar sueldo en la barra',value=False)

bars = ax.barh(df['full name'], df['salary'], color=color_bars)


plt.xticks(rotation=90)

if toggle_show_name:
    plt.yticks(df['full name'])
else:
    plt.yticks([])

if toggle_show_salary:
    ax.bar_label(bars,fmt='%.0f €',padding=3)
else:
    ax.yaxis.label.set_visible(False)

plt.xlim(0, 4500)

st.pyplot(fig)

st.write("© Ciro León Espinosa Avilés")