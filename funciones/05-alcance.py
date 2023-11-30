# def saludar():
#     saludo = "Hola Mundo!"
#     print(saludo)


# def saludaChanchito():
#     saludo = "Hola Chanchito!"
#     print(saludo)


# saludar()
# saludaChanchito()
# saludar()

# Las variables definidas fuera de la funcion son variables globales

saludo = "Hola Global"

# Usar variables globales es una mala practica!!!

# Las variables definidas dentro de la funcion son variables locales


def saludar():
    # De esta forma se llama a una variable global dentro de una funcion (evitar hacerlo)
    global saludo
    saludo = "Hola Mundo!"


def saludaChanchito():
    saludo = "Hola Chanchito!"
    print(saludo)


print(saludo)
saludar()
print(saludo)
