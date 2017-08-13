#Programa para calcular e
#Hecho por @neriphy

from math import *
import webbrowser

n = 0
limite = int(input("Introduzca la cantidad de numeros para sumar: "))
respuesta = 0

while limite >= n:
	respuesta = (1/(factorial(n))) + respuesta
	print(respuesta)
	print("Suma numero:",n,"de",limite)
	n = n + 1

print("\nEl programa hizo un total de", limite, "sumas y obtuvo que e es aproximadamente:")
print(respuesta)


print("Si te ha servido este pequeño programa sigueme en Twitter")
webbrowser.open("https://twitter.com/neriphy")