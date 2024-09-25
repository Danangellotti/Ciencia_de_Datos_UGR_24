# Función para intentar sumar un número y una cadena con manejo de excepción TypeError
def sumar_numero_y_cadena(num, cadena):
    try:
        # Intentar realizar la suma
        resultado = num + cadena
        # Mostrar el resultado si no ocurre un error
        print(f"El resultado de la suma es: {resultado}")
    except TypeError:
        # Capturar el error de tipo y mostrar un mensaje de error
        print("Error: No se puede sumar un número y una cadena.")

# Llamar a la función con un número y una cadena
sumar_numero_y_cadena(10, "Hola")