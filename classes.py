class Pokemon():
    def __init__(self, nombre, nivel, hp, tipo):
        self.name = nombre
        self.level = nivel
        self.vida = hp
        self.type = tipo
        
pikachu = Pokemon("pikachu",20,100, "electrico")
charmander = Pokemon("Charmander", 50, 95,"Fuego")

print(f"Las caracteristicas del pokemon {pikachu.name}")
print(f"Tiene un nivel {pikachu.level}")
print(f"El HP es de {pikachu.vida}")
print(f"Es de tipo {pikachu.type}")

print(f"Las caracteristicas del pokemon {charmander.name}")
print(f"Tiene un nivel {charmander.level}")
print(f"El HP es de {charmander.vida}")
print(f"Es de tipo {charmander.type}")



