import matplotlib.pyplot as plt
import numpy as np

x =np.array([1,2,4,6])
y =np.array(["a","b","c","d"])

plt.subplot(1,2,1)
plt.bar(x,y,color='blue',width=0.5)

x =np.array(["a","b","c","d"])
y =np.array([1,2,4,6])
plt.subplot(1,2,2)

plt.barh(x,y,color='red',height=0.5)
plt.show()