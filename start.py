import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from math import sqrt

def f(x, y):
    return (x**2 - 1)**2 + y**2

def gradf(x, y):
    df_dx = 4 * x * (x**2 - 1)
    df_dy = 2 * y
    return df_dx, df_dy

def norme(x, y):
    return sqrt(x**2 + y**2)

def descente(xinit, yinit, pas, epsilon, nmax):    
    x = xinit
    y = yinit
    a, b, c = [x], [y], [f(x, y)]
    grad = gradf(x, y)
    n = 0

    while n < nmax and norme(grad[0], grad[1]) > epsilon:
        x = x - pas * grad[0]
        y = y - pas * grad[1]
        a.append(x)
        b.append(y)
        c.append(f(x, y))
        grad = gradf(x, y)
        n += 1

    print(n)
    return a, b, c

xmin = -2
xmax = 2
ymin = -2
ymax = 2
delta = 0.1
x = np.arange(xmin, xmax + delta, delta)
y = np.arange(ymin, ymax + delta, delta)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

a, b, c = descente(2, 2, 0.1, 0.1, 1000)

def afficherNormal():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='nipy_spectral_r')
    ax.plot(a, b, c, 'ok:', ms=4, linewidth=2) 
    plt.title("Nappe 3D avec descente de gradient")
    plt.show()

def afficherGroupeDeNiveau():
    cont = plt.contour(X, Y, Z, levels=[0.1, 0.3, 0.5, 1, 1.5, 2, 2.5, 3])
    plt.clabel(cont)
    plt.plot(a, b, 'ok:', ms=2, linewidth=1) 
    plt.title("Courbes de niveau avec descente de gradient")
    plt.show()

afficherNormal()
afficherGroupeDeNiveau()
