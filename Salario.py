#Calcular el salario que debe recibir una persona teniendo en cuenta lo siguiente, 
#el salario básico mensual se ingresa por teclado, el número de horas extras se ingresa por teclado, 
#el tipo de horas extras que puede trabajar la persona son; horas extras diurna, 
#el valor de una hora extra diurna corresponde a 25% más del valor de la hora normal de trabajo, 
#horas extras nocturnas el valor de una hora extra nocturna corresponde a 35% más del valor de la hora normal de trabajo,
#horas extras festivas el valor de una hora extra festiva corresponde a 75% más del valor de la hora normal de trabajo, 
#horas extras dominicales el valor de una hora extra dominica corresponde a 100% más del valor de la hora normal de trabajo.
#El número de horas extras que trabaja la persona se ingresan por teclado. Al trabajador le descuenta del total de lo que 
#recibe el 4% para salud y el 4% para pensión. Se debe tener presente que el trabajador puede fallar uno o más días y si 
#es así se debe descontar ese día(s) del salario básico. El algoritmo debe mostrar salario básico, 
#total de ingresos por horas extras, descuentos y total a pagar. 
#(Para calcular el día se debe dividir el salario básico en 30 y el valor de una hora es igual al día dividió en 8 horas diarias).

print("Bienvenido ALUCARD COMPANY.\n")
nombre = input("Ingrese nombre del trabajador:\n ").lower()
SalarioBasico = float(input("Ingrese el salario básico: "))
dias_faltados = float(input("Ingrese la cantidad de días faltados:\n "))
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

#Cálculos base
valor_dia = SalarioBasico / 30
valor_hora_normal = valor_dia / 8

# Descuento por días faltados
descuento_dias_faltados = dias_faltados * valor_dia

# Valor horas extras
valor_hora_diurna = valor_hora_normal * (1 + hrasExtrasDiurna)
valor_hora_nocturna = valor_hora_normal * (1 + hrasExtrasNocturna)
valor_hora_festiva = valor_hora_normal * (1 + hrasExtrasFestiva)
valor_hora_dominical = valor_hora_normal * (1 + hrasExtrasDominical)

# Total por horas extras
total_horas_extras = (
    (horas_ext_diurnas * valor_hora_diurna) +
    (horas_ext_nocturnas * valor_hora_nocturna) +
    (horas_ext_festivas * valor_hora_festiva) +
    (horas_ext_dominicales * valor_hora_dominical)
)
#subtotal
subtotal = SalarioBasico - descuento_dias_faltados + total_horas_extras

#Descuentos de salud y pensión
descuento_salud = subtotal * descuentoSalud
descuento_pension = subtotal * descuentoPension

#total a pagar
total_a_pagar = subtotal - descuento_salud - descuento_pension


# Mostrar resultados
print("\n" + "=" * 30)
print("\n--- PAGO NOMINA ---")
print(f"Nombre del trabajador: {nombre}")
print(f"Salario básico: ${SalarioBasico:,.0f}")
print(f"Descuento por días faltados: ${descuento_dias_faltados:,.0f}")
print(f"Total horas extras: ${total_horas_extras:,.0f}")
print(f"Descuento salud (4%): ${descuento_salud:,.0f}")
print(f"Descuento pensión (4%): ${descuento_pension:,.0f}")
print(f"Total a pagar: ${total_a_pagar:,.0f}")
print("\nALUCARD COMPANY le agradece por su trabajo y dedicación.")
print("\n" + "=" * 30)