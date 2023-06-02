import pickle
class Person:

    def __init__(self, name, age, address) -> None:
        self.name = name
        self.age = age 
        self.address = address

object1 = Person("Ali", 18, "mashhad")
object2 = Person("mohamad hosein", 20, "tehran")
object3 = Person("mohmmad", 21, "tabriz")
lst_person = [object1, object2, object3]

def save_objects(person:list):
    with ("person.pkl","wb") as f:
        pickle.dump(person ,f)





    