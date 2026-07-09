# Entrada de datos
salario_basico = float(input("Ingrese el salario básico mensual: "))
dias_faltados = int(input("Ingrese el número de días faltados: "))
horas_ext_diurnas = float(input("Ingrese la cantidad de horas extras diurnas trabajadas:\n "))
horas_ext_nocturnas = float(input("Ingrese la cantidad de horas extras nocturnas trabajadas:\n "))
horas_ext_festivas = float(input("Ingrese la cantidad de horas extras festivas trabajadas:\n "))
horas_ext_dominicales = float(input("Ingrese la cantidad de horas extras dominicales trabajadas:\n "))  

hrasExtrasDiurna =0.25
hrasExtrasNocturna =0.35
hrasExtrasFestiva =0.75
hrasExtrasDominical =1.0
descuentoSalud = 0.04
descuentoPension = 0.04

# Cálculos base
valor_dia = salario_basico / 30
valor_hora_normal = valor_dia / 8
descuento_faltas = dias_faltados * valor_dia

# Variables acumuladoras
total_horas_extras = 0

# Menú bonito
print("\n" + "=" * 40)
print("      MENÚ DE HORAS EXTRAS")
print("=" * 40)
print("d -> Diurna")
print("n -> Nocturna")
print("f -> Festiva")
print("o -> Dominical")
print("x -> Salir")
print("=" * 40)

# Ciclo while
while True:
    tipo = input("\nIngrese el tipo de hora extra: ").lower()

    if tipo == "x":
        break

    horas = int(input("Ingrese la cantidad de horas: "))

    if tipo == "d":
        valor_extra = valor_hora_normal * (1 + hrasExtrasDiurna)
        nombre = "Diurna"
    elif tipo == "n":
        valor_extra = valor_hora_normal * (1 + hrasExtrasNocturna)
        nombre = "Nocturna"
    elif tipo == "f":
        valor_extra = valor_hora_normal * (1 + hrasExtrasFestiva)
        nombre = "Festiva"
    elif tipo == "o":
        valor_extra = valor_hora_normal * (1 + hrasExtrasDominical)
        nombre = "Dominical"
    else:
        print("Tipo no válido. Intente de nuevo.")
        continue

    pago_extra = horas * valor_extra
    total_horas_extras += pago_extra

    print(f"Horas {nombre}: {horas}")
    print(f"Pago por este registro: ${pago_extra:,.0f}")

# Cálculo final
subtotal = salario_basico - descuento_faltas + total_horas_extras
descuento_salud = subtotal * descuentoSalud 
descuento_pension = subtotal * descuentoPension
total_pagar = subtotal - descuento_salud - descuento_pension

# Mostrar resultados
print("\n" + "=" * 40)
print("           RESULTADOS")
print("=" * 40)
print(f"Salario básico:        ${salario_basico:,.0f}")
print(f"Valor del día:         ${valor_dia:,.0f}")
print(f"Valor hora normal:     ${valor_hora_normal:,.0f}")
print(f"Descuento por faltas:   ${descuento_faltas:,.0f}")
print(f"Total horas extras:     ${total_horas_extras:,.0f}")
print(f"Descuento salud (4%):   ${descuento_salud:,.0f}")
print(f"Descuento pensión (4%): ${descuento_pension:,.0f}")
print(f"TOTAL A PAGAR:          ${total_pagar:,.0f}")
print("=" * 40)
