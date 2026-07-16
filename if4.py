#Un supermercado realiza una promoción mediante la cual el cliente recibe un descuento dependiendo de un número entero entre 1 y 100 que se escoge al azar. Solicite el monto total de la compra (en USD) y el número que le tocó al cliente. Aplique las siguientes reglas:
#* Si el número es menor a 74: el descuento es del 15 % sobre el total de la compra.
#* Si el número es mayor o igual a 74: el descuento es del 20 % sobre el total de la compra.
#Salida esperada: valor del descuento aplicado y total a pagar.

import random

numero = random.randint(1, 100)
monto_compra = float(input("Ingrese el monto total de la compra (en USD): "))
desc_1 = 0.15
desc_2 = 0.20

if numero < 74:
    descuento = monto_compra * desc_1
else:
    descuento = monto_compra * desc_2

total_a_pagar = monto_compra - descuento

print(f"El número escogido al azar es: {numero}")
print(f"Valor del descuento aplicado: ${descuento:.2f}")
print(f"Total a pagar: ${total_a_pagar:.2f}")