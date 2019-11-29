import pyrebase
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = "../../.env"
load_dotenv(dotenv_path=env_path)

firebaseConfig = {
  "apiKey": os.getenv("API_KEY"),
  "authDomain": os.getenv("AUTH_DOMAIN"),
  "databaseURL": os.getenv("DB_URL"),
  "projectId": os.getenv("ID"),
  "storageBucket": os.getenv("STORAGE_BUCKET"),
  "messagingSenderId": os.getenv("MESSAGIN_SENDER_ID"),
  "appId": os.getenv("APP_ID"),
  "measurementId": os.getenv("MEASUREMENT_ID")
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
user = auth.sign_in_with_email_and_password("geraldkan99@gmail.com", os.getenv("PASSWORD"))

db = firebase.database()