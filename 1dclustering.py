import numpy as np
import matplotlib.pyplot as plt
x = [1,2,4,7,8,9]
x = [1,2,7,8,15,17]

gapvalues = []
# Calculating the gap between each data point
for i in range(len(x)-1):
    gapvalues.append(x[i+1]-x[i])
# Gapvalues has each gap between each data point
gapvalues = np.array(gapvalues)
# Data
x = np.array(x)
# Finds the location/index of the largest gap
maxgapindex = np.argmax(gapvalues)
# Finds the highest data point in the first cluster
divider = x[maxgapindex]
# Labels clusters as 0 and 1
y= np.where(x<=divider, 0, 1)
plt.scatter(x, np.zeros(len(x)),c=y,cmap="RdYlGn")
plt.yticks([])
