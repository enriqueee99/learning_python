# PI = 3.1415 #constante todo mayusculas
# MY_NAME = 'Anthony'
# MY_NAME = 'Enriqueee'
# print(PI, MY_NAME)





#---------------------------------------------------------
# decima = 100
# print(decima) #100
# print(type('hello')) #class str
# print('bye' + ' world') #bye world
# print(type(8.7)) #float
# a, b = 10, 21
# print(a+b) #31


#L I S T  #si cambian son arreglos :V   ----------------------------------------------------------

# [10,20,30,40,50]
# ['hello', 'bye', 'good luck']
# print(type([10, 'hello', True]))
# []

# miLista = []
# miLista.append(1)
# miLista.append(2)
# miLista.append(3)
# miLista.append(1000)

# print(miLista[3]) #1000
# print(miLista)


# #for in
# for x in miLista: print (x)


# number_list = [1,2,3,4,5]
# print(number_list, type(number_list)) #list
# number_list_tupla = (1,2,3)
# tupla_to_list = list(number_list_tupla)
# print(number_list_tupla, type(number_list_tupla)) #tupla
# print(tupla_to_list, type(tupla_to_list)) #tupla to list

# rang = list(range(1, 10))
# print(rang) #[1-9]
# #print(dir(tupla_to_list))
# print(5 in rang) #true
# print(10 in rang) #false

# colors = ['yellow', 'blue', 'red ']
# print(colors)
# # colors[1] = 'green'
# # print(colors) #and green
# # colors.append('violet')
# # print(colors) #and violet
# # colors.extend(['black', 'white']) #los paso en una lista para tener 5 elementos
# # print(colors)

# colors.insert(1, 'violet') #insert after yellow
# print(colors)

# colors.insert(len(colors), 'holis') #inser after de last position tomando la longitud yes spanglish xd
# print(colors)
# colors.pop() #remueve  por ser ultimo
# colors.remove('yellow') #mas especifico
# print(colors)
# colors.sort() #ordena de a -z
# print(colors)
# colors.sort(reverse=True) #ordena de z -a 
# print(colors)
# print(colors.index('blue')) #2



#T U P L A S    #listas que no cambian  ---------------------------------------------- 
# print(type((10, 'hello', True, 30,40)))
# ()

# #dictionaries   #son objetos
# directorie = {
# "name": "Anthony",
# "Apellido": "Candelario",
# "novia": "Dally."
# }
# print(type(directorie))

# #clave/valor
# direcotieNumbers = {
#     "codigo": 12345,
#     "noombre": 'anthony',
#     'fecha': 20
# }



#------------------------------------------------------------------------------ xd
# str = 'hello world'
# #(dir(str))
# new_str = str.upper()
# replace_str = str.replace('hello', 'bai')
# print(replace_str)
# print(str.startswith('holitas')) #false
# print(str.endswith('world'))
# print(new_str)
# print(str) #bai world
# print(str.find('o')) #return the position xd
# print(str.split()) #separa apartir del espacio
# print(len(str)) #lenght
# print(str.index('o')) #cuenta a partir de la posicion

# print(' '.join(['dallerlyn', 'lasso', 'vera'])) #une
# print(' y '.join(['jugar', 'pelear']))
# print(" ".join("antthony")) #separa
# print(str.strip('world')) #corta y deja solo world

# dally = 'dally'
# antho = 'antho'
# print(f'{dally} y {antho} se aman uwu') #necesito la f antes

str = 'Hello World!'
# print (str)          # Prints complete string
# print (str[0])       # Prints first character of the string
print (str[2:5])    # Prints characters starting from 3rd to 5th
# print (str[2:])     # Prints string starting from 3rd character
# print (str * 2)     # Prints string two times
# print (str + "TEST")# Prints concatenated string
tup = (11, 1997, 2000);
print(dir(tup))




#N U M B E R S  --------------------------------------------------------
#print(2**3, 10 % 3) #elevar al cubo y modulo
# age = input('insert your age: ') #10
# new_age = int(age) + 10
# print(type(new_age), new_age) #int 20
# print(type(age), age) #str 10




#S E T S agrega al inicio  ---------------------------------------------------------------
# days = {'lunes', 'martes', 'miercoles'}
# print(type(days))
# print('lunes' in days) #true
# print('martes' in days) #false
# newDays = days.add('jueves') #jueves primero
# #del(days) #days
# print(days)




#D Y C T I O N A R I E S ------------------------------------------------
# product = {
#     'name': 'book',
#     'price': 4.99,
#     'quantity': 3
# }

# person = {
#     'first_name': 'anthony',
#     'last_name': 'candelario',
#     'age': 22
# }

# print(type(person)) #dict
# print(person.keys()) #llaves
# print(person.values()) #valor
# #del person elimina
# print(person.clear()) #none




#C O N D I C I O N A L E S --------------------------------------
# x = 40
# if x < 30:
#     print('x es menor que 30')
# elif x == 30:
#     print('ambos son iguales')
# else:
#     print('x es mayor')

# #necesito llaves para mis if anidados :'v
# name = 'anthony'
# last = 'candelarssio'
# if name == 'anthony':
#     if last == 'candelario':
#         print ('you are anthony candelario')
#     else:
#         print('you are not anthony candelario') 
# else: 
#     print('you are not anthony :c')


#and or
# if name == 'anthony' and last == 'candelario':
#     print('si soy anthony candelario')
# else:
#     print('no eres anthony')

#L O O P S ------------------------------------
# fruits = ['apples', 'banana', 'pear', 'grapes']
# for fruit in fruits:
#      if fruit == 'apples':
#          print('ya tienes manzana')
#      print(fruit)

# #necesito sumar el contador :'v
# count = 4
# while count <= 10:
#     print(count)
#     count = count + 1




#F U N C T I O N S ------------------------------------------------
# def add(n1, n2):
#      print(n1 + n2)

# print(add(1,5))

# sust = lambda n_one, n_two : n_one - n_two
# print(sust(20,10))



#M O D U L S ------------------------------------------------------------
# import datetime

# print(datetime.date.today()) #fecha
# print(datetime.timedelta(minutes=100)) #100 min en una hora   1:40

# from datetime import timedelta, date

# print(timedelta(minutes=100))
# print(date.today())

# from fmath import add, sust
# add(1,2)
# sust(2,1)