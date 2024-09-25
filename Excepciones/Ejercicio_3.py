# Programa para intentar acceder a una clave inexistente en un diccionario con manejo de excepción KeyError

try:
    # Definir un diccionario con algunas claves y valores
    mi_diccionario = {
        "nombre": "Ana",
        "edad": 25,
        "ciudad": "Madrid"
    }
    
    # Intentar acceder a una clave que no existe
    valor = mi_diccionario["profesion"]
    
    # Mostrar el valor si no ocurre un error
    print(f"El valor de la clave 'profesion' es: {valor}")

except KeyError:
    # Capturar el error de clave inexistente y mostrar un mensaje
    print("Error: La clave 'profesion' no existe en el diccionario.")