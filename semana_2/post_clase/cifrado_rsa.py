from semana_2.laboratorio.totiente_euler import es_primo
from semana_1.laboratorio.aritmetica_modular import inverso_modular, mcd_euclides
from semana_2.laboratorio.teorema_chino_resto import crt

import random


def generar_primo(min, max):
    num_primo = random.randint(min, max)
    while not es_primo(num_primo):
        num_primo = random.randint(min, max)
    return num_primo


def generar_claves_rsa(primo_p, primo_q):
    totiente = (primo_p - 1) * (primo_q - 1)

    clave_publica_e = generar_primo(2, totiente)
    while mcd_euclides(clave_publica_e, totiente) != 1:
        clave_publica_e = generar_primo(2, totiente)

    clave_privada_d = inverso_modular(clave_publica_e, totiente)

    return clave_publica_e, clave_privada_d


def convertir_mensaje_a_numeros(mensaje):
    numeros = []
    for caracter in mensaje:
        numeros.append(ord(caracter))
    return numeros


def convertir_numeros_a_mensaje(numeros):
    cadena = ''
    for numero in numeros:
        cadena += chr(numero)
    return cadena


def cifrar_mensaje(mensaje, clave_publica_e, modulo_n):
    mensaje_numerico = convertir_mensaje_a_numeros(mensaje)
    numeros_cifrados = []
    for numero in mensaje_numerico:
        numero_cifrado = (numero ** clave_publica_e) % modulo_n
        numeros_cifrados.append(numero_cifrado)
    return numeros_cifrados


def descifrar_mensaje(mensaje_cifrado, clave_privada_d, modulo_n):
    numeros_descifrados = []
    for numero in mensaje_cifrado:
        numero_descifrado = (numero ** clave_privada_d) % modulo_n
        numeros_descifrados.append(numero_descifrado)
    return convertir_numeros_a_mensaje(numeros_descifrados)


def descifrar_crt(mensaje_cifrado, clave_privada_d, primo_p, primo_q):
    dp = clave_privada_d % (primo_p - 1)
    dq = clave_privada_d % (primo_q - 1)

    numeros_descifrados = []

    for caracter_cifrado in mensaje_cifrado:
        mp = caracter_cifrado ** dp % primo_p
        mq = caracter_cifrado ** dq % primo_q

        numero_descifrado = crt([mp, mq], [primo_p, primo_q])
        numeros_descifrados.append(numero_descifrado)

    return convertir_numeros_a_mensaje(numeros_descifrados)


def test():
    p, q = 61, 53
    n = p * q

    mensaje_original = 'Hola'
    representacion_numerica = convertir_mensaje_a_numeros(mensaje_original)
    print(f'Representación numérica de "{mensaje_original}": {representacion_numerica}')

    e, d = generar_claves_rsa(p, q)
    print(f'Clave pública (e): {e}, Clave privada (d): {d}')

    mensaje_cifrado = cifrar_mensaje('Hola', e, n)
    print(f'Mensaje cifrado: {mensaje_cifrado}')

    mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, d, n)
    print(f'Mensaje descifrado: {mensaje_descifrado}')

    mensaje_descifrado = descifrar_crt(mensaje_cifrado, d, p, q)
    print(f'Mensaje descifrado (CRT): {mensaje_descifrado}')


if __name__ == '__main__':
    test()
