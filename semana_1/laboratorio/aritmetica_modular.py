def modulo(a, b):
    div = a // b
    return a - (b * div)


def suma_mod(a, b, mod):
    return modulo(a + b, mod)


def resta_mod(a, b, mod):
    return modulo(a - b, mod)


def multiplicacion_mod(a, b, mod):
    return modulo(a * b, mod)


def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def mcd(a, b):
    while b != 0:
        temp = a
        a = b
        b = modulo(temp, b)
    return a


def inversa_modular(a, mod):
    if (mcd(a, mod) != 1):
        print("No son coprimos")


def euclides_extendido(a, b):
    x0 = 1
    x1 = 0
    y0 = 0
    y1 = 1

    while b != 0:
        q = a // b  # Cociente
        r = a % b  # Residuo

        a = b
        b = r

        temp_x0 = x1
        temp_y0 = y1
        x1 = x0 - q * x1
        y1 = y0 - q * y1
        x0 = temp_x0
        y0 = temp_y0

    return a, x0, y0


def inverso_modular(a, m):
    mcd, x, y = euclides_extendido(a, m)

    if mcd != 1:
        return None

    return x % m


ans_mod = modulo(13, 5)
ans_suma = suma_mod(14, 17, 5)
ans_resta = resta_mod(14, 17, 5)
ans_mult = multiplicacion_mod(6, 4, 5)
print(f"13 (mod 5): {ans_mod}")
print(f"(14 + 17) (mod 5): {ans_suma}")
print(f"(14 - 17) (mod 5): {ans_resta}")
print(f"(6 * 4) (mod 5): {ans_mult}\n")

ans_mcd = mcd(270, 192)
print(f"MCD(270, 192): {ans_mcd}\n")

a = 123
b = 234
mcd, x, y = euclides_extendido(a, b)
print(f"MCD({a}, {b}) = {mcd}, donde {a}*{x} + {b}*{y} = {mcd}\n")


a = 4
m = 7

inverso = inverso_modular(a, m)
if inverso is None:
    print(f"{a} y {m} no son coprimos, no existe inverso módulo {m}.")
else:
    print(f"El inverso de {a} módulo {m} es: {inverso}")



