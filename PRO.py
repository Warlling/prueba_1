import random

elementos = "@=+-.,7¿1234567890-abcdefghijklmnopqrstuvwxyz"
pass_lenght = int(input("Introduzca la longitud de su contraseña: "))

password = ""
for i in range(pass_lenght):
    password += random.choice(elementos)  # Se concatena el carácter a la variable 'password'

print("Contraseña generada:", password)