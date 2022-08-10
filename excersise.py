import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,6,18])
y=np.array([3,10,12,20])
plt.plot(x,y,'o:r',mec='g',mfc='g')
plt.show()




x = np.array([12,14,16,18,20,22,24])
y = np.array([100,200,250,400,300,450,500])

plt.plot(x, y)

plt.xlabel("Temperature (celsius)")
plt.ylabel("Sales")

plt.show()
