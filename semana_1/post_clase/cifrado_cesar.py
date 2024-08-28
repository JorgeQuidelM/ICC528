def cifrar(mensaje, clave, alfabeto):
    mensaje_cifrado = ''
    for letra in mensaje:
        if letra.lower() in alfabeto:
            posicion = alfabeto.index(letra.lower())
            nueva_pos = (posicion + clave) % len(alfabeto)
            letra_cifrada = alfabeto[nueva_pos]
            mensaje_cifrado += letra_cifrada.upper() if letra.isupper() else letra_cifrada.lower()
        else:
            mensaje_cifrado += letra
    return mensaje_cifrado


def descifrar(mensaje, clave, alfabeto):
    mensaje_descifrado = ''
    for letra in mensaje:
        if letra.lower() in alfabeto:
            posicion = alfabeto.index(letra.lower())
            nueva_pos = (posicion - clave) % len(alfabeto)
            letra_descifrada = alfabeto[nueva_pos]
            mensaje_descifrado += letra_descifrada.upper() if letra.isupper() else letra_descifrada
        else:
            mensaje_descifrado += letra
    return mensaje_descifrado
