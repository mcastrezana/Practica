def suma(*numeros):  # el * significa que se trata de algo q es iterable (parametros iterables)
    resultado = 0
    for numero in numeros:
        resultado += numero
    # hay q tener mucho cuidado con la identancion para no generar un loop infinito
    print(resultado)


suma(2, 5, 7)
suma(2, 5)
suma(2, 8, 7, 45, 32)
