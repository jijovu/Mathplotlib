import matplotlib.pyplot as plt
import numpy as np

x =np.array([0,1,2,3,4,5])
y =np.array([0,4,2,6,3,8])

plt.subplot(2,3,1)
plt.plot(x,y)
plt.title("Plot-1")

x =np.array([0,4,2,6,3,8])
y =np.array([0,1,2,3,4,5])

plt.subplot(2,3,2)
plt.plot(x,y)
plt.title("Plot-2")

x =np.array([0,1,2,3,4,5])
y =np.array([0,4,2,6,3,8])

plt.subplot(2,3,3)
plt.plot(x,y)
plt.title("Plot-3")

x =np.array([0,4,2,6,3,8])
y =np.array([0,1,2,3,4,5])

plt.subplot(2,3,4)
plt.plot(x,y)
plt.title("Plot-4")

x =np.array([0,1,2,3,4,5])
y =np.array([0,4,2,6,3,8])

plt.subplot(2,3,5)
plt.plot(x,y)
plt.title("Plot-5")

x =np.array([0,4,2,6,3,8])
y =np.array([0,1,2,3,4,5])

plt.subplot(2,3,6)
plt.plot(x,y)
plt.title("Plot-6")

plt.suptitle("PLOT")
plt.show()

