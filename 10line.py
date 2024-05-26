import matplotlib.pyplot as plt
import numpy as np

y1points =np.array([0,4,2,6,4,8])
y2points =np.array([0,2,1,3,2,4])

plt.plot(y1points,linestyle='dashdot',color='#35E9B4',linewidth='5')
plt.plot(y2points)
plt.show()