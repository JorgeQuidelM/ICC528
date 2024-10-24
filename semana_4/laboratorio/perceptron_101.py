import numpy as np


def suma_ponderada(entradas, pesos):
    producto_punto = np.dot(entradas, pesos)
    return producto_punto.astype(float).tolist()


def funcion_lineal(x):
    return x


def funcion_escalon(x):
    return 1 if x >= 0 else 0


def funcion_softmax(entradas):
    exp_entradas = [np.exp(x) for x in entradas]
    suma = np.sum(exp_entradas)
    salidas = [e / suma for e in exp_entradas]
    return [round(float(s), 3) for s in salidas]


def funcion_logistica(x):
    fx = 1 / 1 + np.exp(-x)
    return round(float(fx), 2)


def aplicar_sesgo_y_f_activacion(suma, sesgo, f_activacion):
    if isinstance(suma, list):
        suma_con_sesgo = [s + sesgo for s in suma]
        return [f_activacion(s) for s in suma_con_sesgo]
    elif isinstance(suma, (int, float)):
        return f_activacion(suma + sesgo)


def perceptron(entradas, pesos, sesgo, f_activacion):
    suma = suma_ponderada(entradas, pesos)
    return aplicar_sesgo_y_f_activacion(suma, sesgo, f_activacion)


def red_neuronal(entradas, pesos_por_capas, sesgos, funciones):
    for pesos, sesgo, funcion in zip(pesos_por_capas, sesgos, funciones):
        entradas = perceptron(entradas, pesos, sesgo, funcion)
    return entradas


def test_1():
    entradas = [0.1, 0.5, 0.2]
    pesos = [0.4, 0.3, 0.6]
    sesgo = 0.5

    prediccion = perceptron(entradas, pesos, sesgo, funcion_escalon)
    print("------------------ TEST 1 ------------------")
    print(f"Entradas: {entradas}")
    print(f"Salida: {prediccion}")


def test_2():
    print("------------------ TEST 2 ------------------")
    # Definición de las capas
    pesos_capa_1 = [
        [3, 2],  # Pesos para la primera neurona en la capa oculta
        [1, 4]  # Pesos para la segunda neurona en la capa oculta
    ]

    pesos_capa_2 = [
        [3, 5],  # Pesos para la primera neurona en la capa de salida
        [2, 1]  # Pesos para la segunda neurona en la capa de salida
    ]

    pesos_por_capa = [pesos_capa_1, pesos_capa_2]

    entrada_inicial = [1, 2]
    sesgos = [1, 1]
    funciones = [funcion_lineal, funcion_lineal]

    salida_final = red_neuronal(entrada_inicial, pesos_por_capa, sesgos, funciones)

    print(f"Pesos Capa Entrada: {pesos_capa_1}")
    print(f"Pesos Capa Oculta: {pesos_capa_2}")
    print(f"Capa Salida: {salida_final}")


def test_3():
    print("------------------ TEST 3 ------------------")
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
    funciones = [funcion_logistica, funcion_logistica]

    salida_final = red_neuronal(entrada_inicial, pesos_por_capa, sesgos, funciones)
    print(f"Capa Salida: {salida_final}")

    print(f"Softmax en Salida: {funcion_softmax(salida_final)}")


test_1()
test_2()
test_3()
