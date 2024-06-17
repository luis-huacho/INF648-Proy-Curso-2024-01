 ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░       ░▒▓████████▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░
░▒▓█▓▒▒▓███▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓███████▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░             ░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░             ░▒▓█▓▒░
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░       ░▒▓██████▓▒░       ░▒▓███████▓▒░

Profesores:
--------------
Dr. César Beltrán
Mg. César Olivares


Integrantes:
--------------
19910608 	EDWARD JUVENAL ROSALES DIAZ
20040848 	JAVIER JORGE ENRIQUE MOLINA VILLANUEVA
20244806 	ASUNCIÓN LUIS HUACHO LAZO


Archivos:
--------------
- Análisis Exploratorio de los Datos (EDA): EDA_Steel_Industry_Energy_Consumption.ipynb
- Desarrollo de Modelos trabajados: Modelos_Steel_Industry_Energy_Consumption.ipynb
- Desarrollo de registro de pruebas de Modelos trabajados: MLflow_Steel_Industry_Energy_Consumption.ipynb


Dataset: "Steel Industry Energy Consumption"
--------------
https://archive.ics.uci.edu/dataset/851/steel+industry+energy+consumption


Referencias de código y modelos
--------------
XGboost: https://www.kaggle.com/code/carlmcbrideellis/an-introduction-to-xgboost-regression/notebook
Cubist: https://pypi.org/project/cubist/
Optuna:
- https://optuna.readthedocs.io/
- https://www.youtube.com/watch?v=t-INgABWULw
- https://www.kaggle.com/code/mustafagerme/optimization-of-random-forest-model-using-optuna


Fuente Docker Compose:
--------------
https://github.com/minio/blog-assets/tree/main/mlflow-minio-setup


Instalar las librerias requeridas:
--------------
pip install -r requeriments-3.11.txt


MLflow, MinIO, PostgreSQL en entorno local
-----------------------------------------------------
1. Para ejecutar el Docker Compose, por primera vez, utilice:

sudo docker compose --env-file config.env up -d --build

Si ya lo ejecutó anteriormente, puede ejecutarlo en una siguiente oportunidad con:

sudo docker compose --env-file config.env up -d

2. Acceso a MLflow

http://localhost:5001/

3. Acceso a MinIO

http://localhost:9001/login
