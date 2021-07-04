#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
# name = input('What´s you name: ?')
# print('Hello ' + name)


#Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética 
# print( ((3+2) / (2*5))**2 )


#sueldo por hora
# horas = float(input('Cuantas horas ha trabajado?: '))
# paga_por_horas = float(input('Cuanto cobra por horas?: '))
# sueldo = horas * paga_por_horas
# print('su sueldo es de: ', sueldo)


#suma de n primeros numeros
# n = int(input('value to X: '))
# suma = n * (n + 1) / 2
# print(f'La suma de los {n} primeros numeros es: ',suma)


#IMC
# peso = float(input("¿Cuál es tu peso en kg? "))
# estatura = float(input("¿Cuál es tu estatura en metros?"))
# imc = round(peso / estatura**2, 2) #redondea a 2 decimales
# print("Tu índice de masa corporal es ", imc)


#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

# n = float(input('Primer numero: '))
# m = float(input('Segundo numero: '))
# c = round(n / m)
# r = round(n % m, 2)

# print(f'El cociente de {round(n)} / {round(m)} es: {c}')
# print(f'El residuo es: {r}')


#capital anual formula cantidad * 
# cantidad = float(input('cantidad inicial a invertir: '))
# interes = float(input('interes de porcentaje anual: '))
# años = int(input('años?: '))
# capital_anual = round((interes / 100 + 1)**años, 2)
# print(f'El capital anual estimado es de: {capital_anual}')


#nombre veces
# nombre = input('cual es su nombre?: ')
# veces = int(input('cuantas veces desea repetir su nombre?: '))
# print((nombre + '\n') * veces)

#nombre mayuscula minuscula y len
# name = input('cuál es su nombre?: ')
# print(name.capitalize())
# print(name.lower())
# print(name.upper())
# print(f'{name} tiene {len(name)} letras')


#frase al revez xd
# frase = input("Introduce una frase: ")
# print(frase[::-1])

#vocal a mayuscula
# frase = input('escriba una frase: ')
# vocal = input('que vocal desea convertir a mayuscula?: ')
# print(frase.replace(vocal, vocal.upper()))

#cambio de dominio por 
# name = input('primer nombre: ')
# apellido = input('primer apellido: ')
# cedula = input('cedula: ')
# print(f'Su correo institucional es: {apellido}-{name}{cedula[6:10]}@unesum.edu.ec')

print(list(1, 4, 7))