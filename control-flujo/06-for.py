# for itera una lista de elementos
# lo podemos usar para buscar elementos

# for numero in range(5):
#    print(numero, numero * ' Hola mundo')

# buscar = 3
# for numero in range(5):
#    print(numero)
#    if numero == buscar:
#        print("encontrado", buscar)
#        break

# range(5) es un iterable
buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("No encontre el numero buscado")

for char in "Ultimate python":
    print(char)
