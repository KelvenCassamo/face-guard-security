import pickle
import os

DATABASE_PATH = "face_database.pkl"

# Função para carregar ou criar a database
def load_database():
    if os.path.exists(DATABASE_PATH):
        with open(DATABASE_PATH, "rb") as file:
            return pickle.load(file)
    return {}

def save_database(database):
    with open(DATABASE_PATH, "wb") as file:
        pickle.dump(database, file)
