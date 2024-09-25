# Programa para manejar la excepción FileNotFoundError e intentar crear el archivo si no existe

try:
    # Intentar abrir un archivo que no existe en modo lectura
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)

except FileNotFoundError:
    # Capturar la excepción y mostrar un mensaje de error
    print("Error: El archivo no existe.")
    
    # Intentar crear el archivo si no existe
    with open("archivo_inexistente.txt", "w") as archivo:
        archivo.write("Este es un nuevo archivo creado porque el original no existía.")
    print("El archivo ha sido creado correctamente.")