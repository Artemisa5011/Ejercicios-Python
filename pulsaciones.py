#Calcule el numero de pulsaciones que debe tener una persona cada 10 segundos de ejercicio aerobico,
#segun su sexo y edad. Solicite la edad (en anos) y el sexo (F = femenino, M = masculino), y aplique:
# Sexo femenino: num_pulsaciones = (220 − edad) / 10
# Sexo masculino: num_pulsaciones = (210 − edad) / 10
#Imprima el numero de pulsaciones recomendadas.

edad = int(input("Ingrese su edad (en años): "))
sexo = input("Ingrese su sexo (F = femenino, M = masculino): ").upper()
pulsa=10
fem=220
masc=210

if sexo == "F":
    num_pulsaciones = (fem - edad) / pulsa
elif sexo == "M":
    num_pulsaciones = (masc - edad) / pulsa
else:
    print("Sexo no valido. Por favor, ingrese 'F' para femenino o 'M' para masculino.")

print(f"El numero de pulsaciones recomendadas es: {num_pulsaciones}")