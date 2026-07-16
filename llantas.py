#Compra de llantas con precio por volumen
#Una llantería vende llantas con el siguiente esquema de precios:
#* Si el cliente compra menos de 5 llantas: el precio es de 80 USD por llanta.
#* Si el cliente compra 5 llantas o más: el precio es de 70 USD por llanta.
#Solicite la cantidad de llantas que el cliente desea comprar y calcule el total que debe pagar.

llantas = int(input("Ingrese la cantidad de llantas que desea comprar: "))
if llantas < 5:
    precio_por_llanta = 80
else:
    precio_por_llanta = 70 
total_a_pagar = llantas * precio_por_llanta
print(f"El total a pagar es: {total_a_pagar} USD")