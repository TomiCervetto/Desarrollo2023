""" SUMA"""
n1 = int(input())
n2 = int(input())
n3 = int(input())

suma = n1 + n2 + n3

print(f"El resultado de la suma es: {suma}")

"""Promedio Temperaturas"""

lunes = int(input("Temperatura dia Lunes: "))
martes = int(input("Temperatura dia Martes: "))
miercoles = int(input("Temperatura dia Miercoles: "))
jueves = int(input("Temperatura dia Jueves: "))
viernes = int(input("Temperatura dia Viernes: "))

Promedio = (lunes + martes + miercoles + jueves + viernes) / 5

print(f"El promedio de la semana es de {Promedio}")

"""Bitcoins a Pesos"""

bitcoin= int(input("ingrese la cantidad de bitcoins: "))

print(f"El valor en pesos es de: {bitcoin * 80000000}")


"""Descuento de Supermercado"""


Costo = int(input("Ingrese el monto de la compra: "))

if(Costo >= 3500):
    Total = Costo - Costo * 0.10

else:
    Total = Costo


print(f"El importe a pagar es de {Total}")

"""Club Deportivo"""


nombre= int(input("Ingrese el nombre del pibe: "))
edad = int(input("Ingrese la edad: "))


if(edad >= 13 and edad <= 15):
    categoria = "infantil"

elif(edad > 15 and edad <= 17):
    categoria = "cadete"

elif(edad > 17 and edad <= 19):
    categoria = "juvenil"

elif(edad > 19):
    categoria = "mayores"

print(f"{nombre} esta en la categoria {categoria}")


"""Asado"""

invitados = int(input("Ingrese la cantidad de invitados: "))

precio = float(input("ingrese el precio de 1kg de carbe: "))

pedido = invitados * 0.7

Costo = pedido * precio

print(f"La cantidad de Kg de carne que se va a pedir es de: {pedido}")
print(f"El dinero que se necesita el franquito para pagar es de: {Costo}")





