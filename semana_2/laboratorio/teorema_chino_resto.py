from semana_1.laboratorio.aritmetica_modular import inverso_modular, mcd_euclides


def mcd_lista(numeros):
    if not numeros:
        return None

    mcd_resultado = numeros[0]
    for numero in numeros[1:]:
        mcd_resultado = mcd_euclides(mcd_resultado, numero)
    return mcd_resultado


def crt(coeficientes, modulos):
    if len(coeficientes) != len(modulos):
        return None

    if mcd_lista(modulos) != 1:
        return None

    producto_modulos = 1
    for mod in modulos:
        producto_modulos *= mod

    lista_m = []
    for mod in modulos:
        m = producto_modulos // mod
        lista_m.append(m)

    lista_inv_m = []
    for m, mod in zip(lista_m, modulos):
        inv_m = inverso_modular(m, mod)
        lista_inv_m.append(inv_m)

    x = 0
    for coeficiente,m,inv_m in zip(coeficientes, lista_m, lista_inv_m):
        x += coeficiente * m * inv_m
    x %= producto_modulos

    return x


def test():
    lista_coeficientes = [2, 3, 2]
    lista_modulos = [3, 5, 7]

    for coeficiente, modulo in zip(lista_coeficientes, lista_modulos):
        print(f'x = {coeficiente} mod {modulo}')

    resultado = crt(lista_coeficientes, lista_modulos)
    print("x:", resultado)


if __name__ == "__main__":
    test()
