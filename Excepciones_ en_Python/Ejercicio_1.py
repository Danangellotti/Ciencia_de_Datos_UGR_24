# Programa para dividir dos números con manejo de ZeroDivisionError y ValueError

def dividir_numeros():
    try:
        # Solicitar al usuario que ingrese dos números
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        # Intentar realizar la división
        resultado = num1 / num2
        
    except ZeroDivisionError:
        # Capturar el error de división por cero
        print("Error: No se puede dividir entre cero.")
        return
    
    except ValueError:
        # Capturar el error de valor no válido (si el usuario no ingresa un número)
        print("Error: Ingresa un número válido.")
        return
    
    else:
        # Si no hay errores, mostrar el resultado
        print(f"El resultado de {num1} / {num2} es: {resultado}")

# Llamar a la función
dividir_numeros()
