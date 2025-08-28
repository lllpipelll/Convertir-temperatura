import streamlit as st
import pandas as pd

# Título de la aplicación
st.title('Conversor de Grados Celsius a Fahrenheit 🌡️')
st.write('Esta aplicación web te permite convertir una temperatura de grados Celsius a Fahrenheit.')

# ----------------- Conversor -----------------
st.header('Conversor')

# Campo para que el usuario ingrese la temperatura en Celsius usando text_input
celsius_str = st.text_input('Ingresa la temperatura en grados Celsius:')

# Botón para realizar la conversión
if st.button('Convertir'):
    if celsius_str:
        try:
            # Convierte la entrada de texto a un número flotante
            celsius = float(celsius_str)
            
            # Fórmula de conversión: F = (C * 9/5) + 32
            fahrenheit = (celsius * 9/5) + 32
            
            # Muestra el resultado
            st.success(f'**{celsius} °C** equivale a **{fahrenheit:.2f} °F**')
        except ValueError:
            # Muestra un mensaje de error si la entrada no es un número válido
            st.error('Por favor, ingresa un número válido.')
    else:
        st.warning('Por favor, ingresa un valor para convertir.')

# ----------------- Tabla de Referencia -----------------
st.header('Tabla de Referencia')
st.write('A continuación, se muestra una tabla con valores de conversión comunes para tu referencia.')

# Crea un DataFrame de pandas con datos de ejemplo
data = {
    'Celsius (°C)': [-10, 0, 10, 20, 30, 40],
    'Fahrenheit (°F)': [-14, 32, 50, 68, 86, 104]
}
df = pd.DataFrame(data)

# Muestra la tabla en Streamlit
st.table(df)

# ----------------- Información Adicional -----------------
st.markdown("""
<br>
---
**¿Cómo funciona la conversión?**
<br>
La fórmula para convertir de Celsius a Fahrenheit es:
$$ F = (C \\times \\frac{9}{5}) + 32 $$
Donde:
- $F$ es la temperatura en Fahrenheit.
- $C$ es la temperatura en Celsius.
<br>
---
<br>
Desarrollado con ❤️ usando **Streamlit**.
""", unsafe_allow_html=True)
