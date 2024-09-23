from semana_1.laboratorio.aritmetica_modular import inverso_modular, mcd_euclides
from semana_2.laboratorio.teorema_chino_resto import crt
from semana_2.laboratorio.square_and_multiply import fast_modular_exp

import random


def miller_rabin(n, k=40):
    if n <= 1:
        return False

    if n <= 3:
        return True

    if n % 2 == 0:
        return False

    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = fast_modular_exp(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = fast_modular_exp(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def generar_primo(bits):
    while True:
        p = random.getrandbits(bits)
        if p % 2 == 0:
            continue
        if miller_rabin(p):
            return p


def generar_claves_rsa(p, q):
    totiente = (p - 1) * (q - 1)

    e = generar_primo(16)

    while e >= totiente or mcd_euclides(e, totiente) != 1:
        e = generar_primo(16)

    d = inverso_modular(e, totiente)

    return e, d


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


def cifrar_mensaje(m, e, n):
    numeros = convertir_mensaje_a_numeros(m)
    numeros_cifrados = []
    for num in numeros:
        num_cifrado = fast_modular_exp(num, e, n)
        numeros_cifrados.append(num_cifrado)
    return numeros_cifrados


def descifrar_mensaje(c_numeros, d, n):
    numeros_desc = []
    for num in c_numeros:
        num_desc = fast_modular_exp(num, d, n)
        numeros_desc.append(num_desc)
    return numeros_desc


def descifrar_crt(c_numeros, d, p, q):
    dp = d % (p - 1)
    dq = d % (q - 1)

    numeros_desc = []

    for num in c_numeros:
        mp = fast_modular_exp(num, dp, p)
        mq = fast_modular_exp(num, dq, q)

        num_desc = crt([mp, mq], [p, q])
        numeros_desc.append(num_desc)

    return numeros_desc


def test():
    p = generar_primo(1024)
    q = generar_primo(1024)
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
    print(convertir_numeros_a_mensaje(mensaje_descifrado))


if __name__ == '__main__':
    test()
