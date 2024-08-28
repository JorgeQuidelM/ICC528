from cifrado_cesar import cifrar, descifrar

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
#mensaje = input("Ingrese el mensaje: ")
#clave = int(input("Ingrese la clave de desplazamiento: "))

mensaje = "Hola Mundo"
clave = 5

mensaje_cifrado = cifrar(mensaje, clave, alfabeto)
mensaje_descifrado = descifrar(mensaje_cifrado, clave, alfabeto)

print(f"Mensaje original: {mensaje}")
print(f"Mensaje cifrado (clave {clave}): {mensaje_cifrado}")
print(f"Mensaje descifrado: {mensaje_descifrado}\n")

mensaje = "Bienvenido"
clave = 30

mensaje_cifrado = cifrar(mensaje, clave, alfabeto)
mensaje_descifrado = descifrar(mensaje_cifrado, clave, alfabeto)

print(f"Mensaje original: {mensaje}")
print(f"Mensaje cifrado (clave {clave}): {mensaje_cifrado}")
print(f"Mensaje descifrado: {mensaje_descifrado}\n")


mensaje = "Lorem ipsum"
clave = 13

mensaje_cifrado = cifrar(mensaje, clave, alfabeto)
mensaje_descifrado = descifrar(mensaje_cifrado, clave, alfabeto)

print(f"Mensaje original: {mensaje}")
print(f"Mensaje cifrado (clave {clave}): {mensaje_cifrado}")
print(f"Mensaje descifrado: {mensaje_descifrado}\n")


