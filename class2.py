class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []        # Aqui pusimos una lista vacia para saber el numero de pasajeros (Alt + Z)
        
    def add_passengers(self,name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
        
    def open_seats(self):
        return self.capacity - len(self.passengers)
        
flight = Flight(2) # Creamos un objeto con capacidad de 3 pasajeros

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    success = flight.add_passengers(person)           # Instanciamos al objeto de flight con la funcion de agregar pasajeros
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No avaible seats for {person}.")
        