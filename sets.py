# Create an empty set

s = set() # Conjunto vacio

s.add(1)
s.add(2)
s.add(3)
s.add("juan")
s.add(3) # Ningun conjunto imprime 2 veces lo mismo

print(s)
s.remove("juan") #Aqui removi directamente el nombre, no por indice!
print(s)

print(f"The set has {len(s)} elements.") # Len te dice cuantos elementos tiene el set o la lista etc.


