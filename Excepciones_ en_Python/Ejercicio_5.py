# Programa para dividir dos números con manejo de ZeroDivisionError y ValueError

try:
    # Solicitar al usuario que ingrese dos números
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    
    # Intentar realizar la división
    resultado = num1 / num2
    
    # Mostrar el resultado si no ocurre un error
    print(f"El resultado de {num1} / {num2} es: {resultado}")

except ZeroDivisionError:
    # Capturar el error de división por cero
    print("Error: No se puede dividir entre cero.")
    
except ValueError:
    # Capturar el error de valor no válido (si el usuario no ingresa un número)
    print("Error: Ingresa un número válido.")