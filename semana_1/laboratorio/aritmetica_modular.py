def modulo(a, b):
    div = a // b
    return a - (b * div)


def suma_mod(a, b, mod):
    return modulo(a + b, mod)


def resta_mod(a, b, mod):
    return modulo(a - b, mod)


def multiplicacion_mod(a, b, mod):
    return modulo(a * b, mod)


def mcd_euclides(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def mcd_euclides_rec(a, b):
    if b == 0:
        return a
    return mcd_euclides_rec(b, a % b)


def euclides_extendido(a, b):
    # ax + by = mcd(a,b)
    x0, x1, y0, y1 = 1, 0, 0, 1

    while b != 0:
        q = a // b
        a, b = b, a % b

        # Actualizamos x0 y x1
        x0, x1 = x1, x0 - q * x1
        # Actualizamos y0 y y1
        y0, y1 = y1, y0 - q * y1

    return a, x0, y0


def euclides_extendido_rec(a, b):
    # ax + by = mcd(a,b)
    # (b % a)x1 + ay1 = a(y1-(b // a)x1) + bx1 = mcd(b % a, a)

    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = euclides_extendido_rec(b % a, a)

    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y


def inverso_modular(a, m):
    mcd, x, y = euclides_extendido(a, m)

    if mcd != 1:
        return None

    return x % m


def test():
    a, mod = 13, 5
    ans_mod = modulo(a, mod)
    print(f"{a} (mod {mod}): {ans_mod}")

    a, b = 14, 7
    ans_suma = suma_mod(a, b, mod)
    print(f"({a} + {b}) (mod {mod}): {ans_suma}")

    ans_resta = resta_mod(a, b, mod)
    print(f"({a} - {b}) (mod {mod}): {ans_resta}")

    a, b = 6, 4
    ans_mult = multiplicacion_mod(a, b, mod)
    print(f"({a} * {b}) (mod {mod}): {ans_mult}\n")

    a, b = 12, 32
    ans_mcd = mcd_euclides(a, b)
    print(f"MCD({a}, {b}): {ans_mcd}")
    ans_mcd_rec = mcd_euclides_rec(a, b)
    print(f"MCD({a}, {b}): {ans_mcd_rec}\n")

    a, b = 77, 30
    mcd, x, y = euclides_extendido(a, b)
    print(f"MCD({a}, {b}) = {mcd}, donde {a}*{x} + {b}*{y} = {mcd}")
    mcd, x, y = euclides_extendido_rec(a, b)
    print(f"MCD({a}, {b}) = {mcd}, donde {a}*{x} + {b}*{y} = {mcd}\n")

    a, m = 4, 7
    inverso = inverso_modular(a, m)
    if inverso is None:
        print(f"{a} y {m} no son coprimos, no existe inverso módulo {m}.")
    else:
        print(f"El inverso de {a} módulo {m} es: {inverso}")


if __name__ == '__main__':
    test()
