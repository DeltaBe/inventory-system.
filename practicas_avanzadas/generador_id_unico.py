from random import randint

print("***Generador unico de id***")
#declaracion de las variables
nombre=input("Ingrese su nombre: ")
apellido=input("ingrese apellido: ")
Nacimiento=input("ingrese su año de nacimiento: ")
aleatorio=randint(1000,9999)
#convertmos a minusculas
nombre_1=nombre.upper()[0:2]
apellido_1=apellido.upper()[0:2]
Nacimiento_1=Nacimiento[2:4]

id_unico=f'{nombre_1}{apellido_1}{Nacimiento_1}{aleatorio}'

print(f'Hola {nombre},')
print(f'tu nueva id generado por el sistema es el siguiente : ')
print(f'{id_unico}')
print('felicidades')



