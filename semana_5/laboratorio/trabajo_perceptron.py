import numpy as np


def derivada_sigmoide(x):
    return funcion_sigmoide(x) * (1 - funcion_sigmoide(x))


def funcion_escalon(x):
    return 1 if x >= 0 else 0


def funcion_sigmoide(x):
    fx = 1 / (1 + np.exp(-x))
    return float(fx)


def funcion_softmax(entradas):
    exp_entradas = [np.exp(x) for x in entradas]
    suma = np.sum(exp_entradas)
    salidas = [e / suma for e in exp_entradas]
    return [round(float(s), 3) for s in salidas]


def suma_ponderada(entradas, pesos):
    producto_punto = np.dot(entradas, pesos)
    return producto_punto.astype(float).tolist()


def aplicar_sesgo_y_f_activacion(suma, sesgo, f_activacion):
    if isinstance(suma, list):
        suma_con_sesgo = [s + sesgo for s in suma]
        return [f_activacion(s) for s in suma_con_sesgo]
    elif isinstance(suma, (int, float)):
        return f_activacion(suma + sesgo)


def perceptron_simple(entradas, pesos, sesgo, f_activacion):
    suma = suma_ponderada(entradas, pesos)
    return aplicar_sesgo_y_f_activacion(suma, sesgo, f_activacion)


def red_neuronal(entradas, pesos_por_capas, sesgos, funciones):
    capas = [entradas]
    for pesos, sesgo, funcion in zip(pesos_por_capas, sesgos, funciones):
        entradas = perceptron_simple(entradas, pesos, sesgo, funcion)
        capas.append(entradas)
    return entradas, capas


def error_cuadratico_medio(output, target):
    error = 0
    for o, t in zip(output, target):
        error += (o - t) ** 2
    return error / len(output)


def generar_matriz_rand(n_filas, n_columnas):
    matriz = np.random.rand(n_filas, n_columnas)
    return np.round(matriz, 2)


def generar_entrada(x, y):
    return x.tolist() + y.tolist()


def generar_movimiento_aleatorio(num, x_min, x_max, y_min, y_max):
    x = np.random.uniform(x_min, x_max, num)
    y = np.random.uniform(y_min, y_max, num)
    return x, y


def generar_movimiento_lineal(x_min, x_max, num, m, b):
    x = np.linspace(x_min, x_max, num)
    y = m * x + b
    return x, y


def generar_movimiento_circular(r, num):
    theta = np.linspace(0, 2 * np.pi, num)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y


def test_perceptron_simple():
    print("------------------ TEST PERCEPTRÓN SIMPLE ------------------")
    entradas = [0.1, 0.5, 0.2]
    pesos = [0.4, 0.3, 0.6]
    sesgo = 0.5

    prediccion = perceptron_simple(entradas, pesos, sesgo, funcion_escalon)
    print(f"Entradas: {entradas}")
    print(f"Salida: {prediccion}")


def test_rna():
    print("------------------ TEST RNA ------------------")
    pesos_capa_1 = [
        [0.15, 0.20],
        [0.25, 0.30]
    ]

    pesos_capa_2 = [
        [0.40, 0.45],
        [0.50, 0.55]
    ]

    pesos_por_capa = [pesos_capa_1, pesos_capa_2]
    entrada_inicial = [0.05, 0.10]
    sesgos = [0.35, 0.60]
    funciones = [funcion_sigmoide, funcion_sigmoide]

    salida_final, capas = red_neuronal(entrada_inicial, pesos_por_capa, sesgos, funciones)
    print(f"Entradas: {entrada_inicial}")
    print(f"Capas: {capas}")
    print(f"Capa Salida: {salida_final}")
    print(f"Softmax en Salida: {funcion_softmax(salida_final)}")


def test_lineal():
    print("------------------ TEST MOVIMIENTO LINEAL ------------------")

    x, y = generar_movimiento_lineal(-5, 5, 10, 3, 1)
    entradas = generar_entrada(x, y)

    pesos_capa_1 = generar_matriz_rand(20, 16)
    pesos_capa_2 = generar_matriz_rand(16, 3)

    pesos_por_capa = [pesos_capa_1, pesos_capa_2]
    funciones_por_capa = [funcion_sigmoide, funcion_sigmoide]
    sesgos_por_capa = [-0.5, 0.3]

    salida, capas = red_neuronal(entradas, pesos_por_capa, sesgos_por_capa, funciones_por_capa)
    print(f"Entradas: {entradas}")
    print(f"Capas: {capas}")
    print(f"Capa Salida: {salida}")
    print(f"Softmax en Salida: {funcion_softmax(salida)}")
    error = error_cuadratico_medio(salida, [1, 0, 0])
    print(f"Error: {error}")


def test_circular():
    print("------------------ TEST MOVIMIENTO CIRCULAR ------------------")

    x, y = generar_movimiento_circular(10, 10)
    entradas = generar_entrada(x, y)

    pesos_capa_1 = generar_matriz_rand(20, 16)
    pesos_capa_2 = generar_matriz_rand(16, 3)

    pesos_por_capa = [pesos_capa_1, pesos_capa_2]
    funciones_por_capa = [funcion_sigmoide, funcion_sigmoide]
    sesgos_por_capa = [-0.5, 0.3]

    salida, capas = red_neuronal(entradas, pesos_por_capa, sesgos_por_capa, funciones_por_capa)
    print(f"Entradas: {entradas}")
    print(f"Capas: {capas}")
    print(f"Capa Salida: {salida}")
    print(f"Softmax en Salida: {funcion_softmax(salida)}")
    error = error_cuadratico_medio(salida, [0, 1, 0])
    print(f"Error: {error}")


def test_aleatorio():
    print("------------------ TEST MOVIMIENTO ALEATORIO ------------------")

    x, y = generar_movimiento_aleatorio(10, -5, 5, -5, 5)
    entradas = generar_entrada(x, y)

    pesos_capa_1 = generar_matriz_rand(20, 16)
    pesos_capa_2 = generar_matriz_rand(16, 3)

    pesos_por_capa = [pesos_capa_1, pesos_capa_2]
    funciones_por_capa = [funcion_sigmoide, funcion_sigmoide]
    sesgos_por_capa = [-0.5, 0.3]

    salida, capas = red_neuronal(entradas, pesos_por_capa, sesgos_por_capa, funciones_por_capa)
    print(f"Entradas: {entradas}")
    print(f"Capas: {capas}")
    print(f"Capa Salida: {salida}")
    print(f"Softmax en Salida: {funcion_softmax(salida)}")
    error = error_cuadratico_medio(salida, [0, 0, 1])
    print(f"Error: {error}")


test_perceptron_simple()
test_rna()
test_lineal()
test_circular()
test_aleatorio()
