import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from math import sqrt

def f(x,y):
    return (x**2-1)**2+y**2

xmin=-2
xmax=2
ymin=-2
ymax=2
delta=0.1
x=np.arange(xmin,xmax+delta,delta)
y=np.arange(ymin,ymax+delta,delta)

X,Y=np.meshgrid(x,y)
Z=f(X,Y)


def afficherNormal(path):
    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')
    ax.plot_surface(X,Y,Z,cmap='nipy_spectral_r')
    plt.show()

def afficherGroupeDeNiveau():
    cont=plt.contour(X, Y, Z,levels=[0.1,0.3,0.5,1,1.5,2,2.5,3])
    plt.clabel(cont)
    plt.title('courbes de niveau ')
    plt.show()

def gradf(x, y):
    df_dx = 4 * x * (x**2 - 1)
    df_dy = 2 * y
    return df_dx, df_dy

def norme(x,y):
    return (x**2+y**2)**0.5

def descente(xinit,yinit,pas,epsilon,nmax):    
    x=xinit
    y=yinit
    grad = gradf(x,y)
    n=0
    path = [[x,y]]

    while ((n<nmax) and np.any(norme(grad[0], grad[1]) > epsilon)):
        x = x - pas * grad[0]
        y = y - pas * grad[1]
        path.append([x,y])
        grad = gradf(x,y)
        n+=1
    return path

afficherNormal(descente(X,Y,0.1,0.1,1000))