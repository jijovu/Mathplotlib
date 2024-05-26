import matplotlib.pyplot as plt
import numpy as np

x =np.random.randint(100,size=(100))
y =np.random.randint(100,size=(100))

size=np.random.randint(100,size=(100))
colors=np.random.randint(100,size=(100))
plt.scatter(x,y,s=size,alpha=0.4,c=colors,cmap='nipy_spectral')

plt.colorbar()
plt.show()