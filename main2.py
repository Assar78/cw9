import pickle
from .model import Person

def show_obj(file_name):
    with (file_name, "rb") as f:
        for person in pickle.load(f):
            print(person)

show_obj("person.pkl")