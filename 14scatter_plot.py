import matplotlib.pyplot as plt
import numpy as np

x =np.array([64,67,25,46,64,86,47,85,55,48,41])
y =np.array([56,43,75,35,54,89,45,12,54,26,33])

plt.scatter(x,y,color='blue')

x =np.array([56,43,75,35,54,89,45,12,54,26,33])
y =np.array([44,66,23,44,63,86,47,86,54,84,14])
colors =np.array(["red","green","yellow","black","pink","cyan","orange","purple","beige","brown","gray"])
plt.scatter(x,y,c=colors)
plt.show()


