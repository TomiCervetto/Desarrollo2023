import random

lista = []

for i in range (1, 10):

    valor = random.randint(1, 20)

    lista.append(valor)

print(lista)

num = int(input("ingrese un valor: "))

def revisarMayor(lista):
    mayor = 0
    for i in range(10):
        if lista[i] > num:
            mayor = mayor + 1
    return mayor

revisarMayor(lista)

print(f"La cantidad de numeros mayores es de {mayor}")

def promediar(lista):
    suma = 0
    for i  in range(10):
        suma=  lista[i] + suma
    promedio = suma / 10
    return promedio

promediar(lista)

print(f"El promedio de la lista es de: {promedio}")

def MayorMenor(lista):
    grande = 0
    menor = 20
    for i in range(10):
        if lista[i] > grande:
            grande = lista[i]
        
        if lista[i] < menor:
            menor = lista[i]
    return(grande, menor)





