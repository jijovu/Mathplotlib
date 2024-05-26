import matplotlib.pyplot as plt
import numpy as np

x =np.array([1,15,5,10,8,17,4,18,6,16])
mylabels =np.array(["1%","15%","5%","10%","8%","17%","4%","18%","6%","16%"])
myexplode =np.array([0,0,0,0,0,0,0.3,0,0,0])
mycolors =["blue","cadetblue","chocolate","crimson","cyan","darkorchid","ghostwhite","orangered","orchid","palegreen"]

plt.pie(x,labels=mylabels,startangle=90,explode=myexplode,shadow=True,colors=mycolors)
plt.legend(title ="Percentage")
plt.show()
