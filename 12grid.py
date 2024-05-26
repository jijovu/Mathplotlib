import matplotlib.pyplot as plt
import numpy as np 

x =np.array([1,2,3,4,5,6,7])
y =np.array([20,18,22,20,25,18,25])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}


plt.title("Internet Speed",loc ='left',fontdict=font1)
plt.xlabel("Time",fontdict=font2)
plt.ylabel("Speed",fontdict=font2)

plt.grid(axis ='x',color='green',ls='--')
plt.plot(x,y)
plt.show()