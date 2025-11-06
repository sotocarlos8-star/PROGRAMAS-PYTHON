INSTITUTO TECNOLOGICO DE PACHUCA
# NOMBRE ALUMNO: Carlos Bolaños Soto
# MATERIA: Algoritmos y Lenguaje de Programación
# GRUPO: A
#DOCENTE: Emilio Mario Peña
#NOMBRE PRACTICA: Un mensaje del usuario, mostrado 3 veces
# DESCRIPCIÓN: Solicita al usuario un numero que introdusca un mensaje y mostrar 3 veces.

import os

os.system("cls")

num=1
suma=0

while num<=10:
    suma=num+suma
    num=num+1

print("\nLa suma de los primeros 10 números enteros positivos es: ", suma)