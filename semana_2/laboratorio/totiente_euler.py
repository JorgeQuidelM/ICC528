def encontrar_factores_primos(n):
    factores_primos = []
    divisor = 2

    while n > 1:
        if n % divisor == 0 and es_primo(divisor):
            factores_primos.append(divisor)
            n = n // divisor
        else:
            divisor += 1

    return factores_primos


def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def conteo_de_elementos(lista):
    lista_recurrencias = {}

    for elemento in lista:
        if elemento in lista_recurrencias:
            lista_recurrencias[elemento] += 1
        else:
            lista_recurrencias[elemento] = 1

    return lista_recurrencias


def funcion_totiente_euler(num):

    if es_primo(num):
        return num - 1

    factores_primos = encontrar_factores_primos(num)
    potencias_de_factores = conteo_de_elementos(factores_primos)

    ans = 1
    for factor, potencia in potencias_de_factores.items():
        ans *= (factor ** (potencia - 1)) * (factor - 1)
    return ans


def test():
    n = 13
    factores_primos = encontrar_factores_primos(n)
    print(factores_primos)
    print(conteo_de_elementos(factores_primos))
    print(funcion_totiente_euler(n))

    n = 12
    factores_primos = encontrar_factores_primos(n)
    print(factores_primos)
    print(conteo_de_elementos(factores_primos))
    print(funcion_totiente_euler(n))


if __name__ == '__main__':
    test()
