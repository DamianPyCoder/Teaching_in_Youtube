# CTRL + B              para ejecutar en sublime


# ------------------> LISTAS <------------------

miLista=["Amanda","Baltasar","Carlos","David","Esther"]
miListaDos=["Manuel","Noelia"]
miListaUnida=miLista+miListaDos #creamos otra lista que es el resultado de sumar dos listas
miListaDosDoblada=["Manuel","Noelia"] *2

print(miLista[0]) #accede al índice 0


print(miLista[:]) #accede a todos los índices


print(miLista[0:2]) #imprime todos desde el 0 inclusive, hasta el 2 exclusive


print(miLista[:2]) #lo mismo que si fuese 0:2


print(miLista[2:]) #debe acceder a los elementos desde indice 2 hasta el final


print(miLista[-1]) #indice negativo empieza a contar desde final, cuenta desde 1 y no desde 0


# para añadir elementos al final
miLista.append("Fernando")

# para añadir elementos donde queramos
miLista.insert(2,"Berta")

# para agregar varios elementos
miLista.extend(["Gemma","Helena","Inma"])

# saber en que índice está un elemento
miLista.index("Amanda")

# saber si un elemento está o no en la lista, devuelve boolean
print("Pepe" in miLista)

# borrar elementos
miLista.remove("Baltasar")

# borrar el último elemento de la lista
miLista.pop()




# ------------------> TUPLAS <------------------

miTupla=("Amanda","Baltasar","Carlos","David","Esther")
miTuplaUnitaria=("Jose",) # es una tupla de un solo elemento y deben llevar una coma al final

myList=list(miTupla) # convertimos una tupla en una LISTA

myTupla=tuple(miLista) # convertimos una lista en una TUPLA

print(miTupla.count("Amanda")) # para saber cuantas veces se encuentra un elemento

print(len(miTupla)) # me indica CUANTOS elementos hay en la tupla


#asignar automaticamente elementos de una tupla a variables
miTuplaDos=("Jose",30,1,1995)
nombre, dia, mes, anio=miTuplaDos




# ------------------> DICCIONARIO <------------------


miDiccionario={"Alemania":"Berlin","Tailandia":"Bangkok","España":"Barcelona"}

print(miDiccionario["Tailandia"]) 	# para imprimir la clave Tailandia
print(miDiccionario)				# para imprimir todo el diccionario

miDiccionario["Italia"]="Lisboa"	# para agregar un nuevo elemento
miDiccionario["Italia"]="Roma" 		# para asignar un nuevo valor a una clave. Lo que hace es sobreescribir, no pueden haber dos claves iguales

del miDiccionario["Italia"]			# para elimiar un elemento

# asignar valores de tupla a un diccionario
miDiccionarioDeNombres={miTupla[0]:"Jefe", miTupla[1]:"SubJefe", miTupla[2]:"Empleado"}









# ------------------> CONDICIONALES CON DATO POR TECLADO <------------------
print("introduce la nota: ")
notaAlumno=input() # TODO lo introducido con input lo considera txt, por eso lo pasaremos a int en la parte de abajo

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
	return valoracion


print(evaluacion(int(notaAlumno)))	# para llamar a la funcion evaluacion



# ------------------> CONDICIONALES <------------------
# if, elif, else

edad=int(input("Introduce tu edad: "))

if 0<edad<100:
	print("La edad es correcta")
else:
	print("La edad no es correcta")


# operadores AND, OR, IN

if modulo in (1,2,3):
	print("estudias los tres primeros modulos")
else:
	print("estudias otros modulos")





# ------------------> CONVERTIR DATOS <------------------

str() 	# A STRING
int() 	# A INT
float()	# a FLOAT






# ------------------> BUCLE FOR <------------------

for i in ["primavera","verano","invierno"]:
	print(i)
#	print("hola ", end)		# el END lo usamos para que no haya salto de linea
#	print("hola", end=" ")	# el END lo usamos para determinar como termina la linea


# recorrer string
email=False

for i in "DamianMolin@gmail.com":
	if(i=="@" or i=="."):
		email=True

if email==True:
	print("El email es correcto")
else:
	print("El email no es correcto")




# ------------------> BUCLE FOR en RANGO <------------------

for i in range(5):
	print(f"valor de la variable {i}") # para unir txts con variables sin usar operadores de concatenacion o similares
	print("valor de la variable " +i)

for i in range(5,10) # para que la lista se desde cinco a diez

for i in range(5,100,8) # para que la lista sea desde cinco a cien, pero cuente de ocho en ocho

len(variableNombre) # para saber la longitud de la variable

for i in range(len(variableNombre)) 




# ------------------> FUNCIONES <------------------ 
Def funcionNueva():
	return numeros




# ------------------> GENERADORES <------------------ 
# Son como funciones, pero no hacen todo el código de golpe sino que van generando codigo vuelta a vuelta

# https://www.youtube.com/watch?v=ucaHqGII350&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=20
# es más eficiente que las funciones en casos como generar de forma infinita código y solo querer que se genere de uno en uno

Def funcionGeneraNumeros():
	yield numeros

devuelveNumeros=funcionGeneraNumeros() #es un objeto iterable donde guardaré lo que genere la funcion

print(next(devuelveNumeros)) #para que vaya imprimiendo uno a uno los datos que genera





# ------------------> EXCEPCIONES <------------------ 

def divide(num1,num2):
	try:						# si no puede ejecutarlo irá al except
		return num1/num2
	except ZeroDivisionError:
		print("No se puede dividir entre cero")
		return "Operación erronea"
	finally:
		print("Esta parte del codigo se ejecutará siempre, incluso habiendo excepciones")

# PARA HACER VARIOS UNO BAJO EL OTRO
#	except ValueError:
#		print("Los valores introducidos no son correctos")
#	except ZeroDivisionError:
#		print("...")


# PARA HACER UNO GENERAL, AUNQUE ES MENOS RECOMENDADO
#	except:
#		print("Ha ocurrido un error")



# ------------------> LANZAR EXCEPCIONES <------------------ 
# PARA CONTROLAR O LANZAR EXCEPCIONES USAMOS EL RAISE

# if edad<0:
#	raise TypeError("No se permite edades negativas")




# ------------------> P O O <------------------ 

class Coche():				# creamos la clase Coche

	def __init__(self):			# es el CONSTRUCTOR, se llama init, en java tiene el mismo nombre que la clase, pero en python no
								# con el constructor creamos un estado inicial, y al crear el objeto siempre se creará con estas características iniciales
		self.largoChasis=250	# PROPIEDADES de la clase coche, será algo común en todos los objetos que creemos de la clase coche
		self.anchoChasis=120
		self.__ruedas=4			# ENCAPSULAMOS, con dos guiones bajos __ al principio de la palabra, lo que hacemos es encapsular y protegemos la propiedad evitando que se pueda modificar desde fuera de la clase
		self.enMarcha=False


	def arrancar(self):							# establecemos el COMPORTAMIENTO con el método, el metodo a diferencia de la función pertenece a la clase
		self.enMarcha=True						# self hace referencia al objeto perteneciente a la clase, es como el this de Java


	def estado(self):
		if (self.enMarcha):
			return "El coche está en marcha"
		else:
			return "El coche está parado"


miCoche=Coche()			# Para instanciar una clase, ejemplarizar la clase o crear el primer objeto, ponemos un nombre y escribimos un igual y el nombre de la clase. No usamos operador New como si hacemos en java


print("El largo del coche es: ",miCoche.largoChasis)


miCoche.arrancar()
print(miCoche.estado())



# CREAMOS UNA SEGUNDA INSTANCIA

miCoche2=Coche()















