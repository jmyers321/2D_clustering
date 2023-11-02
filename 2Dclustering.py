import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

X,y=make_blobs(n_samples=500,cluster_std=0.2,centers=2,random_state=1)
'''
Creates 2 clusters from 2D data


brainstorm

Sort the points by x-values
find all of the values of the distances between points in the x dimension
Find the largest gap

Sort the points by y-values
find all of the values of the distances between points in the y dimension
Find the largest gap

find the largest gap between the two sorts
Define the clusters on that axis
'''

X = np.array([[0,0],[1,0],[5,0],[7,0]])

# suited for Y axis clustering
X = np.array([[4,6],[2,2],[3,6],[2.5,1],[5,6]])

# suited for X axis clustering
X = np.array([[0,0],[2,1],[6,0],[7,2]])

# diagonal
X = np.array([[0,0],[1,0],[4,3],[5,4]])

X = np.array([[0,0],[1,0],[-5,4],[-4,3]])

X,y=make_blobs(n_samples=10000,cluster_std=0.5,centers=2)


plt.axis('equal')
df = pd.DataFrame(X,columns=['X Axis','Y Axis'])
sortedvalues = df.sort_values('X Axis')
sortedvalues.reset_index(inplace=True, drop=True)
datagaps = []
sortedvalues=sortedvalues.values
sortedvaluesX=sortedvalues

for i in range(len(sortedvalues)-1):
    datagaps.append(sortedvalues[i+1,0]-sortedvalues[i,0])

 # number of rows
    
maxgapindex = np.argmax(datagaps)
# Finds the highest data point in the first cluster
dividerX = sortedvalues[maxgapindex]
# Labels clusters as 0 and 1
xmax = np.max(datagaps)






sortedvalues = df.sort_values('Y Axis')
sortedvalues.reset_index(inplace=True, drop=True)
datagaps = []
sortedvalues=sortedvalues.values

for i in range(len(sortedvalues)-1):
    datagaps.append(sortedvalues[i+1,1]-sortedvalues[i,1])

 # number of rows
    
maxgapindex = np.argmax(datagaps)
# Finds the highest data point in the first cluster
dividerY = sortedvalues[maxgapindex]
# Labels clusters as 0 and 1
#clusters = (np.where(sortedvalues<=divider[0], 0, 1))
ymax=np.max(datagaps)
sortedvaluesY=sortedvalues
    
if ymax >= xmax:
    clustered1 = sortedvaluesY[:,1]
    clustered2 = np.where(clustered1<=dividerY[1],0,1)
    print(clustered2)
    print('Y axis clustering')
    plt.scatter(sortedvaluesY[:,0], sortedvaluesY[:,1],s=0.2,c=clustered2)
else:
    clustered1 = sortedvaluesX[:,0]
    clustered2 = np.where(clustered1<=dividerX[0],0,1)
    print(clustered2)
    print('X axis clustering')
    plt.scatter(sortedvaluesX[:,0], sortedvaluesX[:,1],s=0.5,c=clustered2)
