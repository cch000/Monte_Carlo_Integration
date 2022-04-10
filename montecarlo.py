import numpy as np
import time

start = time.time()


def func1(x):
    # función f(x)
    return np.pi * (1 - x ** 2)


# Integración de Montecarlo de la función f(x) entre a y b
def mc_integration(func, a, b, n):
    # Generador de n números aleatorios equidistantes comprendidos entre a y b
    vals = np.random.uniform(a, b, n)
    # Sustitución de cada uno de los números aleatorios en la función f(x)
    y = [func(val) for val in vals]

    integ = (b - a) / n * np.sum(y)

    return integ


# Sustitución de los parámetros en la función mc_integration
print(f"Solución del método de Montecarlo: {mc_integration(func1, -1, 1, 10000000): .9f}")

end = time.time()

# Tiempo de ejecución

print(f"Hecho en: {(end - start): .2f}s")
