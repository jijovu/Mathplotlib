import matplotlib.pyplot as plt 
import numpy as np

x =np.array([5,4,3,5,3,5,6,12,4,6])
y =np.array([99,76,55,40,66,83,50,34,65,45])

colors=([0,10,20,30,40,50,60,70,80,90])
plt.scatter(x,y,c=colors,cmap='viridis')
plt.colorbar()

plt.show()