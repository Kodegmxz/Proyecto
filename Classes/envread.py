from dotenv import load_dotenv
import os

load_dotenv('.env')  # Carga las variables desde el archivo .env

# Accede a las variables de entorno
db_User = os.getenv("USER")
db_Password = os.getenv("PASSWORD")
db_Host = os.getenv("HOST")
db_DB = os.getenv("DATABASE")