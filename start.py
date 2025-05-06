import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


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

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(X,Y,Z,cmap='nipy_spectral_r')
plt.show()