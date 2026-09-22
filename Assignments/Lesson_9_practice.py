# Challenge at top of lesson 9 in bottom oof Lesson 8 practice

import numpy as np

#Individual challenge: do a 5x5 matrix with numbers with rows row 1= 0,1,2,3,4  row 2= 10,11,12,13,14 row 3= 20,21,22,23,24 row 4= 30,31,32,33,34 and row 5= 40,41,42,43,44

M = np.array([
    [0,1,2,3,4],
    [10,11,12,13,14],
    [20,21,22,23,24],
    [30,31,32,33,34],
    [40,41,42,43,44]
])

print(M)
print(M[0,2:4]) #gives [2 3]
print(M[1:3,1:3]) #gives [11,12] and [21 22]
print(M[:,2]) #gives [2 12 22 32 42]
print(M[:,4]) #should give [4 14 24 34 44]

print(M[2::2,::3]) #should give [20 23] and [40 43]

#use copies to avoid changing slices
M2 = np.copy(M)
print(M2)

"""#example of slice changing in original array
M[2::2,::3] = -1000
print(M) # should change [20 23] and [40 43] to -1000"""

#This avoids changing original array by making a new array that is a copy of the original and changing it
M2[2::2,::3] = 1000 # the first 2 tells what row to go to (0,4), the second 2 tells to space every other row, and the 3 tells what column to go to (0,4)
print(M2)

import matplotlib.pyplot as plt

#import pylab may import both numpy and matplotlib but not all numpy may be in there
"""print(plt.style.available)

plt.style.use('../include/notebook.mplstyle')

#first plot
plt.plot[0,2,8,15,25]

# can use all the python tricks we have learned so far
x = list(range(6))
plt.plot(x,[xi**2 for xi in x])

# We can use numpy array operations to simplify things
x = np.arange(0,6,0.001)
plt.plot(x,x**2)
plt.figure(num=3)
plt.plot(x,x**1.5,x,x**2,x,x**2.5)

# grids
plt.plot(x,0*x,x,x,x,-x)
plt.grid(True)"""

#I have extracted the processed data sets corresponding to the LIGO strain observation time series in Hanford, WA (H1) and Livingston, LA (L1) and uploaded them as
# ../data/ligo_data.dat
#The numerical predictions from general relativity for a binary black hole merger are included as
#../data/nr_prediction.da

#Download the data sets, load them and produce a plot comparing the observations to the theoretical prediction. 
#  Make sure to label all axes and add a legend labeling your curves.  Compare with the top right hand panels of Figure 1 in the linked paper.

from pathlib import Path

data_dir = Path(__file__).resolve().parent / "../data" #getting data
ligo_data = np.loadtxt(data_dir / "ligo_data.dat") #loading data
nr_prediction = np.loadtxt(data_dir / "nr_prediction.dat") #lodaing prediction data

#plot to compare both
plt.figure()
plt.plot(ligo_data[:, 0], ligo_data[:, 1], label="LIGO strain")
plt.plot(nr_prediction[:, 0], nr_prediction[:, 1], label="Numerical relativity prediction")
plt.xlabel("Time (s)")
plt.ylabel("Strain")
plt.legend()
plt.tight_layout()
plt.show()





