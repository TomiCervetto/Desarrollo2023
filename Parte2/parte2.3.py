import random

def generar_lista_de_atletas():
	"""
	Esta función genera aleatoriamente los datos de 20 atletas que participaron de una maratón.
	Devuelve una lista de atletas donde cada atleta es un diccionario con los campos:
		- nombre: el nombre del atleta
		- numero: el número con el que participó en la maratón
		- tiempo_llegada: la cantidad de segundos que tardó en llegar
	"""
	lista_atletas = []
	nombres = ('Daniel', 'Alejandro', 'Pablo', 'Hugo', 'Álvaro', 'Adrián', 'David', 'Sergio', 'Diego')
	apellidos = ('García', 'Rodríguez', 'González', 'Fernández', 'López', 'Martínez', 'Sanchez', 'Pérez')	
	for i in range(1, 21):
		atleta = {
			"nombre": random.choice(nombres)+" "+random.choice(apellidos),
			"numero": i,
			"tiempo_llegada": random.random()*120
		}
		lista_atletas.append(atleta)
	return lista_atletas

def recibir_lista(l):
	for i in l:
		print(f"Numero atleta: {i['numero']}, Nombre: {i['nombre']}")
		print(f"Tiempo de llegada: {i['tiempo_llegada']} segundos")	

def atleta_ganador(l):
	menor_tiempo = l[0]
	for i in l:
		if i["tiempo_llegada"] < menor_tiempo:
			menor_tiempo = i["tiempo_llegada"]
			atleta = i["numero"]
	return atleta

def devolver_datos(n, l):
	for i in l:
		if i["numero"] == n:
			nombre = i["nombre"]
			numero = n
			tiempo_llegada = i["tiempo_llegada"]
	return (nombre, numero, tiempo_llegada)
			
lista = generar_lista_de_atletas()
recibir_lista(lista)
numero_atleta = atleta_ganador(lista)
print(f"El atleta ganador es el numero: {numero_atleta}")
num = print(f"Ingresar el numero del atleta: ")
(nom, num, tl ) = devolver_datos(num, lista)
print("Atleta solicitado:")
print(f"Numero: {num}, Nombre: {nom}, Tiempo llegada: {tl}")