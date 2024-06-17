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
