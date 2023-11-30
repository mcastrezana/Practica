def get_product(**datos):  # ** kwargs, al llamar a la funcion tenemos q nombrar los parametros
    print(datos["id"], datos["name"])


get_product(id="23",
            name="iPhone",
            desc="Esto es un iphone")
