import streamlit as st
import pandas as pd
import pickle
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

# Cargar el archivo CSV
data = pd.read_csv('Steel_industry_data.csv')

# Cargar el modelo preentrenado
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


# Función para predecir "usage_kwh"
def predecir_usage_kwh(input_data):
    prediction = model.predict([input_data])
    return prediction[0]


# Mostrar los datos en una grilla y permitir selección de filas
gb = GridOptionsBuilder.from_dataframe(data)
gb.configure_selection('single', use_checkbox=True)
grid_options = gb.build()

grid_response = AgGrid(
    data,
    gridOptions=grid_options,
    update_mode=GridUpdateMode.SELECTION_CHANGED,
    height=400,
    allow_unsafe_jscode=True,
    theme='streamlit'
)

selected_rows = grid_response['selected_rows']

# Si se selecciona una fila, almacena los datos en el estado de la sesión
if selected_rows and len(selected_rows) > 0:
    selected_row_data = selected_rows[0]
    for key in selected_row_data:
        st.session_state[key] = selected_row_data[key]

# Crear el formulario
with st.form(key='data_form'):
    fields = {}
    for col in data.columns:
        if col != 'usage_kwh':
            if col in st.session_state:
                fields[col] = st.text_input(col, value=st.session_state[col])
            else:
                fields[col] = st.text_input(col, value='')

    submit_button = st.form_submit_button(label='Procesar')

# Funcionalidad del botón "Procesar"
if submit_button:
    input_data = [float(fields[col]) for col in fields]
    predicted_usage_kwh = predecir_usage_kwh(input_data)
    st.write(f'Predicción de usage_kwh: {predicted_usage_kwh}')

# Funcionalidad del botón "Limpiar y reiniciar"
if st.button(label='Limpiar y reiniciar'):
    st.session_state.clear()
    st.experimental_rerun()
