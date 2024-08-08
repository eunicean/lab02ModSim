import numpy as np
import matplotlib.pyplot as plt

# Definir las funciones del campo vectorial
def f(x, y):
    return -18 + 6*x + 2*y - x*y

def g(x, y):
    return 33 - 10*x - 3*y + x**2

def dx_dt(x, y):
    return f(x, y) / g(x, y)

def dy_dt(x, y):
    return 1  # Dado que estamos considerando dy/dx, lo tomamos como 1 para la representación gráfica

# Crear una malla de puntos en el espacio xy
x = np.linspace(0, 10, 20)
y = np.linspace(-2, 3, 20)
X, Y = np.meshgrid(x, y)
U = dx_dt(X, Y)
V = dy_dt(X, Y)

# Puntos de equilibrio
puntos_equilibrio = [(3, 0), (9, 0), (16/5, 1)]

# Crear el gráfico del campo vectorial
plt.figure(figsize=(10, 8))
plt.quiver(X, Y, U, V, color='b')

# Marcar los puntos de equilibrio
for px, py in puntos_equilibrio:
    plt.plot(px, py, 'ro')  # 'ro' indica puntos rojos

# Agregar etiquetas y título
plt.title('Campo Vectorial con Puntos de Equilibrio')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

# Mostrar el gráfico
plt.show()
