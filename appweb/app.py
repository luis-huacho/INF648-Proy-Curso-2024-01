import pickle
import joblib
from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import os

app = Flask(__name__)

# Ruta del archivo CSV
csv_file_path = 'Steel_industry_data.csv'

# Ruta del modelo
model_path = './model.pkl'


# Cargar el modelo
def load_model():
    model = joblib.load(model_path)
    return model


# Predicción
def predict(model, data):
    predictions = model.predict(data)
    return predictions


# Función para leer y procesar el CSV
def load_and_process_data():
    df = pd.read_csv(csv_file_path)
    df.drop(columns=['date'], inplace=True)
    encoder = OneHotEncoder(sparse_output=False)
    encoded_columns = encoder.fit_transform(df[['WeekStatus', 'Day_of_week', 'Load_Type']])
    encoded_df = pd.DataFrame(encoded_columns,
                              columns=encoder.get_feature_names_out(['WeekStatus', 'Day_of_week', 'Load_Type']))
    #df = df.join(encoded_df).drop(columns=['WeekStatus', 'Day_of_week', 'Load_Type'])
    #df.reset_index(drop=True, inplace=True)  # Asegurarse de que el índice sea continuo y comenzar desde 0
    return df, encoder


data, encoder = load_and_process_data()
df = data.drop(columns=['Usage_kWh'])  # Excluir la columna "Usage_kWh"
model = load_model()  # Cargar el modelo


@app.route('/')
def index():
    random_rows = df.head(500).to_dict(orient='records')
    return render_template('index.html', rows=random_rows, columns=df.columns)


@app.route('/get_row', methods=['POST'])
def get_row():
    index = int(request.form['index'])
    row = df.iloc[index].to_dict()
    return jsonify(row)


@app.route('/process', methods=['POST'])
def process():
    form_data = request.form.to_dict()
    processed_df = pd.DataFrame([form_data])

    try:
        prediction = predict(model, processed_df)
    except Exception as e:
        prediction = [9999]

    processed_df['Usage_kWh_Pred'] = prediction[0]
    # processed_df['Usage_kWh_Real'] = data['Usage_kWh']

    return jsonify(processed_df.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=True)
