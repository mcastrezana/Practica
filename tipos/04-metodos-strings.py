animal = "  chanCHito feliz  "
print(animal.upper())  # Convierte todo a mayusculas

print(animal.lower())  # Convierte todo a minusculas

# Strip: elimina los espacios sobrantes; Capitalize: cambia la primer letra a mayuscula
print(animal.strip().capitalize())

print(animal.title())  # Cambia la primer letra de cada palabra a mayuscula

print(animal.strip())  # Elimina espacios sobrantes

print(animal.lstrip())  # Elimina los espacios sobrantes de la izquierda

print(animal.rstrip())  # Elimina los espacios sobrantes de la derecha

# Busca la cadena de caracteres que indiquemos y nos devuelve el indice
print(animal.find("CH"))

# Si find nos devuelve un valor negativo significa que no encontro el string buscado
print(animal.find("cH"))

# Reemplaza los caracteres, sino encuentra la cadena de caracteres no realiza nada,
# replace debe de recibir necesariamente dos argumentos el primero es la cadena que
# se va a cambiar y la segunda es elvalor q va a reemplazar
print(animal.replace("nCH", "j"))

# Devuelve un booleano dociendo si se encuentra o no la cadena de caracteres
# esta dentro de una variable
print("nCH" in animal)

# Devuelve un booleano si NO se encuentra dentro del string
print("nCH" not in animal)
