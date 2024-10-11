import random


def generar_coef_polinomio(grado, min, max, s):
    coeficientes = []
    for _ in range(grado):
        r = random.randint(min, max)
        coeficientes.append(r)
    coeficientes.insert(0, s)
    return coeficientes


def formatear_polinomio(coeficientes):
    terminos = []
    for i, coef in enumerate(coeficientes):
        if coef != 0:
            termino = f"{coef}"
            if i == 0:
                terminos.append(termino)
            elif i == 1:
                terminos.append(f"{termino}x")
            else:
                terminos.append(f"{termino}x^{i}")

    polinomio = " + ".join(terminos)
    return polinomio


def evaluar_polinomio(coeficientes, x):
    valor = 0
    for i, coef in enumerate(coeficientes):
        valor += coef * (x ** i)
    return valor


def generar_partes(coeficientes, valores_x):
    partes = []
    for x in valores_x:
        y = evaluar_polinomio(coeficientes, x)
        partes.append((x, y))
    return partes


def polinomio_lagrange(x, puntos):
    n = len(puntos)
    y = 0
    for i in range(n):
        termino = puntos[i][1]
        for j in range(n):
            if i != j:
                a = (x - puntos[j][0])
                b = (puntos[i][0] - puntos[j][0])
                termino *= a / b
        y += termino
    return y


def seleccionar_subconjunto_aleatorio(partes, cantidad):
    return random.sample(partes, cantidad)


def reconstruir_secreto_shamir(partes):
    secreto = polinomio_lagrange(0, partes)
    return round(secreto)


def test():
    clave = 3523
    grado = 3
    min_coef = -10
    max_coef = 10

    coeficientes = generar_coef_polinomio(grado, min_coef, max_coef, clave)
    print(f"Coeficientes: {coeficientes}")

    valores_x = [-3, 1, 5, 7, 10, 15]

    partes = generar_partes(coeficientes, valores_x)
    print(f"Partes del secreto: {partes}")

    subconjunto_partes = seleccionar_subconjunto_aleatorio(partes, grado + 1)
    print(f"Subconjunto de partes: {subconjunto_partes}")

    secreto_reconstruido = reconstruir_secreto_shamir(subconjunto_partes)
    print(f"Secreto reconstruido: {secreto_reconstruido}")


if __name__ == '__main__':
    test()
