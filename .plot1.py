import matplotlib.pyplot as plt
import numpy as np

x =np.array([1,2,3,4,5,6])
y =np.array([2,4,1,5,2,6])

plt.xlim(1,8)
plt.ylim(1,8)
plt.title("Some cool customizations!")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")


plt.plot(x,y,'o:g',ms=10,mec='k',mfc='b',ls='dashed',lw='3',color='g')
plt.show()