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
x_surf=np.arange(xmin,xmax+delta,delta)
y_surf=np.arange(ymin,ymax+delta,delta)

X_surf,Y_surf=np.meshgrid(x_surf,y_surf)
Z_surf=f(X_surf,Y_surf)


def afficherNormal(path):
    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')
    ax.plot_surface(X_surf,Y_surf,Z_surf,cmap='nipy_spectral_r', alpha=0.8) # Added alpha for better visibility
    
    # Extract x, y coordinates from the path
    path_x = [p[0] for p in path]
    path_y = [p[1] for p in path]
    # Calculate z coordinates for the path
    path_z = [f(p[0], p[1]) for p in path]
    
    # Plot the path on the 3D surface
    ax.plot(path_x, path_y, path_z, color='r', marker='o', markersize=5, label='Chemin de descente')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('f(X, Y)')
    ax.set_title('Surface et chemin de descente de gradient')
    ax.legend()
    
    plt.show()

def afficherGroupeDeNiveau():
    cont=plt.contour(X_surf, Y_surf, Z_surf,levels=[0.1,0.3,0.5,1,1.5,2,2.5,3])
    plt.clabel(cont)
    plt.title('courbes de niveau ')
    plt.show()

def gradf(x, y):
    df_dx = 4 * x * (x**2 - 1)
    df_dy = 2 * y
    return df_dx, df_dy

def norme(vx,vy):
    return (vx**2+vy**2)**0.5

def descente(xinit,yinit,pas,epsilon,nmax):    
    x=xinit
    y=yinit
    grad = gradf(x,y)
    n=0
    path = [[x,y]]

    # Ensure gradient norm is calculated correctly for the loop condition
    while ((n < nmax) and (norme(grad[0], grad[1]) > epsilon)):
        x = x - pas * grad[0]
        y = y - pas * grad[1]
        path.append([x,y])
        grad = gradf(x,y)
        n+=1
        # Added a safety break for divergence
        if np.isnan(x) or np.isnan(y):
            print("Divergence: NaN values encountered.")
            break
            
    print(f"Descente terminée après {n} iterations.")
    print(f"Point final : ({x:.4f}, {y:.4f})")
    print(f"Valeur de f au point final : {f(x,y):.4f}")
    return path

x_depart = -1.5
y_depart = 1.5
pas_descente = 0.05
epsilon_stop = 1e-4
max_iterations = 1000

descent_path = descente(x_depart, y_depart, pas_descente, epsilon_stop, max_iterations)

afficherNormal(descent_path)