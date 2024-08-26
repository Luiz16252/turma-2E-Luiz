#Phytom Divisão

def dividir_numeros(dividendo, divisor):
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        return "Error: División por cero no permitida."
    except Exception as e:
        return f"Error: {e}"

# Exemplo de uso
numerador = float(input("Digite o numero que deseja dividir: "))
denominador = float(input("Digite o numero divisor: "))

resultado = dividir_numeros(numerador, denominador)
print("O resultado da divisão é:", resultado)