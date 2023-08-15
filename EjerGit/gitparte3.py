print("1- Ingresar valor 1 \n 2- Ingresar valor 2 \n 3- Mostrar suma \n 4- Mostrar resta \n 5- Mostrar multiplicacion \n 6- Mostrar division \n 7- Salir ")

numero = 10
while numero != 7:
    numero = int (input("Ingrese el numero de la operacion que desee realizar: "))
    if numero == 1:
        valor1 = int(input("Ingrese el valor 1: "))
        senial = senial + 1

    elif numero == 2:
        valor2 = int(input("Ingrese el valor 2: "))
        senial = senial + 1
    
   
    elif numero == 3:
        if senial >= 2:
            print(f"El resultado de la suma es: {valor1 + valor2}")
        else:
            print("Debe ingresar el valor 1 y 2 antes de realizar una operacion")
    
    elif numero == 4:
        if senial >= 2:
            print(f"El resultado de la resta es: {valor1 - valor2}")
        else:
            print("Debe ingresar el valor 1 y 2 antes de realizar una operacion")
    
    elif numero == 5:
        if senial >= 2:
            print(f"El resultado de la multiplicacion es: {valor1 * valor2}")
        else:
            print("Debe ingresar el valor 1 y 2 antes de realizar una operacion")

    elif numero == 6:
        if senial >= 2:
            print(f"El resultado de la division es: {valor1 / valor2}")
        else:
            print("Debe ingresar el valor 1 y 2 antes de realizar una operacion")
