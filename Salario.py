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

print("\n" + "=" * 55)
print("                      ALUCARD COMPANY")
print("                      COLILLA DE PAGO")
print("=" * 55)
nombre = input("Ingrese nombre del trabajador: ").upper()
identificacion = input("Ingrese número de identificación: ")
cargo = input("Ingrese cargo del trabajador: ").upper()
SalarioBasico = float(input("Ingrese el salario básico: "))
dias_faltados = int(input("Ingrese la cantidad de días faltados: "))
horas_ext_diurnas = float(input("Ingrese la cantidad de horas extras diurnas trabajadas: "))
horas_ext_nocturnas = float(input("Ingrese la cantidad de horas extras nocturnas trabajadas: "))
horas_ext_festivas = float(input("Ingrese la cantidad de horas extras festivas trabajadas: "))
horas_ext_dominicales = float(input("Ingrese la cantidad de horas extras dominicales trabajadas: "))  
hrasExtrasDiurna =0.25
hrasExtrasNocturna =0.35
hrasExtrasFestiva =0.75
hrasExtrasDominical =1.0
descuentoSalud = 0.04
descuentoPension = 0.04

#Cálculos base
valor_dia = SalarioBasico /30
valor_hora_normal = valor_dia / 8

# Descuento por días faltados
descuento_dias_faltados = dias_faltados * valor_dia

# Valor horas extras
valor_hora_diurna = valor_hora_normal * (1 + hrasExtrasDiurna)
valor_hora_nocturna = valor_hora_normal * (1 + hrasExtrasNocturna)
valor_hora_festiva = valor_hora_normal * (1 + hrasExtrasFestiva)
valor_hora_dominical = valor_hora_normal * (1 + hrasExtrasDominical)

# Total por horas extras
pago_diurnas = horas_ext_diurnas * valor_hora_diurna
pago_nocturnas = horas_ext_nocturnas * valor_hora_nocturna
pago_festivas = horas_ext_festivas * valor_hora_festiva
pago_dominicales = horas_ext_dominicales * valor_hora_dominical
total_horas_extras = pago_diurnas + pago_nocturnas + pago_festivas + pago_dominicales

#subtotal
subtotal = SalarioBasico - descuento_dias_faltados + total_horas_extras


#Descuentos de salud y pensión
descuento_salud = subtotal * descuentoSalud
descuento_pension = subtotal * descuentoPension

#total a pagar
total_a_pagar = subtotal - descuento_salud - descuento_pension


# Mostrar resultados
print("=" * 55)
print("                 PAGO DE NÓMINA")
print("=" * 55)
print(f"{'DATOS DEL TRABAJADOR':^55}")
print("=" * 55)
print(f"{'Nombre:':20} {nombre}")
print(f"{'Identificación:':20} {identificacion}")
print(f"{'Cargo:':20} {cargo}")

print("\n" + "-" * 55)
print(f"{'CONCEPTOS DE PAGO':^55}")
print("-" * 55)
print(f"{'Salario básico':25} ${SalarioBasico:>15,.0f}")
print(f"{'Valor del día':25} ${valor_dia:>15,.0f}")
print(f"{'Valor hora normal':25} ${valor_hora_normal:>15,.0f}")
print(f"{'Días faltados':25} {dias_faltados:>15}")
print(f"{'Descuento por faltas':25} -${descuento_dias_faltados:>14,.0f}")

print("\n" + "-" * 55)
print(f"{'DETALLE DE HORAS EXTRAS':^55}")
print("-" * 55)
print(f"{'Diurnas':25} ${pago_diurnas:>15,.0f}")
print(f"{'Nocturnas':25} ${pago_nocturnas:>15,.0f}")
print(f"{'Festivas':25} ${pago_festivas:>15,.0f}")
print(f"{'Dominicales':25} ${pago_dominicales:>15,.0f}")
print(f"{'Total horas extras':24} +${total_horas_extras:>14,.0f}")

print("\n" + "-" * 55)
print(f"{'LIQUIDACIÓN FINAL':^55}")
print("-" * 55)
print(f"{'Subtotal':25} ${subtotal:>15,.0f}")
print(f"{'Salud (4%)':24} -${descuento_salud:>14,.0f}")
print(f"{'Pensión (4%)':24} -${descuento_pension:>14,.0f}")
print("=" * 55)
print(f"{'TOTAL A PAGAR':24} ${total_a_pagar:>15,.0f}")
print("=" * 55)

print("\nGracias por su dedicación y compromiso.")
print("ALUCARD COMPANY le desea un excelente día.")