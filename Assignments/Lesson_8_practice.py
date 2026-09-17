import numpy as np

# Using Numpy!
#data = np.genfromtxt('../data/sho_energy.dat',names=True, comments='#')
#print(f'Total Energy = {np.average(data["Kinetic"]+data["Potential"]):5.3f}K')
#print(f'Exact Energy = {0.5/np.tanh(1.0):5.3f}K')

print(np.sqrt(1.234))

# can deal with complex numbers
print(np.conjugate(1+3j))

#Important part of NumPy is creating arrays
""" Print.py thing
a = np.array([0,1,2,3,4])
print(a)
b = np.array([n for n in range(100)])
print(b)

# It will try to guess the type dynamically unless specified

a = np.array([0,1,2],dtype=float)
print(a)

# a[0] = "float"  #this will not work because it cannot change them from floats into string. must stay same type.

print(b.dtype) #using .dtype to check type of array

a = np.arange(0,10,0.5) #arange is range for arrays. Note that range is first two numbers (0,10) and step is third number (0.5)
#this means that there should be 20 sqrts listed b/c step is 0.5 and range is 0 to 10.

#testing if zeros and ones work
print(np.sqrt(a))

a0 = np.zeros(10)
a1 = np.ones(10)

a2 = np.zeros_like(a1)

print(a0) #should give 0 0 0 0 0 0 0 0 0 0
print(a1) #should give 1 1 1 1 1 1 1 1 1 1 
print(a2) #should give 0 0 0 0 0 0 0 0 0 0 
"""
"""
a = np.linspace(0,1,10) #linespace divides a region into N pieces (so 0,1 in 10 pieces)
print(a)

l = np.logspace(0, 10, 10, base=np.e) #logspace used to divide exponential funcitons in to pieces
print(l) #should print e^N from e^0 to e^10 in 10 pieces

r = np.random.random(100) #we seen this before... random numbers
print(r)

# making an array of squares
#%timeit [i**2 for i in range(1000)]
#%timeit np.arange(1000)**2

a = np.arange(10)**3
print(a) #should print all values of 10**3 from 0-9 (last number never included)
print(a[1]) #should print 1**3
print(a[:3]) #should print the first 3 **3s so 0**3 1**3 and 2**3
print(a[-1:-3:-1]) #should print going backwards from 9 down so 9**3 and the one between 7**3 and 9**3

a1 = np.arange(0.0,2.0*np.pi,np.pi/6)
a2 = np.ones_like(a1)
print(a1)
print(a2)

print(np.log(a1+a2))

print(2*(a1+a2))

print((np.pi*a1)/a2**3)

#multidimensional Arrays

M = np.array([[3,4,5,6],[7,8,9,10]]) #note number of individual arrays [] must be same ex: [2,3,4] and [11,12,14] both have 3 inside

print(M)
print(M.shape) #tells info about array
print(M.size) #tells total num of elements in M

print(M[1,3]) #unsure what this does yet but it gave me 10. Its called an index using simple list of indicies.

M.flatten().reshape(2,4)
#We can pass array creation functions the size of a desired multi-dimensional array
M1 = np.ones([3,3]) #creates 3x3 matrix of 1s
print(M1)
Id = np.identity(3) #Makes det of matrix I think
print(Id)

# can go beyond matrices
M0 = np.zeros([3,3,3]) #makes 3x3 matrix of 0s 3 times
print(M0)

# there are some special matrix creaters
II = np.identity(4, dtype=int)
print(II) #will give a 4x4 matrix that is solved.
"""
#challenge is find indicies of non-zero elements from [1,2,0,0,4,0]
#create array of uniformly distributed random numbs b/w 1 & 3 and explore how avg depends on length of array
# show a 10x10 matrix is idempotent
#explore Meshgrid method and use it to evaluate matrix  Z = X^2 + Y^2  on a 10x10 grid between -1,1.

w = np.array([1,2,0,0,4,0])
print(np.nonzero(w))
 #(Random #s 1,3)

q = np.random.uniform(1, 3, size=5)

print(q)
print('Average',np.mean(q))

q = np.random.uniform(1, 3, size=50)

print(q)
print('Average',np.mean(q))

q = np.random.uniform(1, 3, size=150)

print(q)
print('Average',np.mean(q))
#As you increase length of array, the mean gets closer to 2

Id = np.identity(10) #10x10 matrix
print(np.matmul(Id,Id)) #Checks multiplying 10x10 by itself
print(np.array_equal(np.matmul(Id,Id),Id)) #sees if Id^2 = Id

#Z = x^2 + Y^2 from -1,1

x = np.linspace(-1,1,10) #splits numbs -1,1 in 10 pieces for x
y = np.linspace(-1,1,10) #splits numbs -1,1 in 10 pieces for y

X, Y = np.meshgrid(x,y) #meshgrid method

Z = X**2 + Y**2 #Formula z  = x^2 + y^2

print(Z)

print('Z shape', Z.shape)

# Using Numpy!
#data = np.genfromtxt('../data/sho_energy.dat',names=True, comments='#')
#print(f'Total Energy = {np.average(data["Kinetic"]+data["Potential"]):5.3f}K')
#print(f'Exact Energy = {0.5/np.tanh(1.0):5.3f}K')

print(np.sqrt(1.234))

# can deal with complex numbers
print(np.conjugate(1+3j))

#Important part of NumPy is creating arrays
"""
a = np.array([0,1,2,3,4])
print(a)
b = np.array([n for n in range(100)])
print(b)

# It will try to guess the type dynamically unless specified

a = np.array([0,1,2],dtype=float)
print(a)

# a[0] = "float"  #this will not work because it cannot change them from floats into string. must stay same type.

print(b.dtype) #using .dtype to check type of array

a = np.arange(0,10,0.5) #arange is range for arrays. Note that range is first two numbers (0,10) and step is third number (0.5)
#this means that there should be 20 sqrts listed b/c step is 0.5 and range is 0 to 10.

#testing if zeros and ones work
print(np.sqrt(a))

a0 = np.zeros(10)
a1 = np.ones(10)

a2 = np.zeros_like(a1)

print(a0) #should give 0 0 0 0 0 0 0 0 0 0
print(a1) #should give 1 1 1 1 1 1 1 1 1 1 
print(a2) #should give 0 0 0 0 0 0 0 0 0 0 
"""
"""
a = np.linspace(0,1,10) #linespace divides a region into N pieces (so 0,1 in 10 pieces)
print(a)

l = np.logspace(0, 10, 10, base=np.e) #logspace used to divide exponential funcitons in to pieces
print(l) #should print e^N from e^0 to e^10 in 10 pieces

r = np.random.random(100) #we seen this before... random numbers
print(r)

# making an array of squares
#%timeit [i**2 for i in range(1000)]
#%timeit np.arange(1000)**2

a = np.arange(10)**3
print(a) #should print all values of 10**3 from 0-9 (last number never included)
print(a[1]) #should print 1**3
print(a[:3]) #should print the first 3 **3s so 0**3 1**3 and 2**3
print(a[-1:-3:-1]) #should print going backwards from 9 down so 9**3 and the one between 7**3 and 9**3

a1 = np.arange(0.0,2.0*np.pi,np.pi/6)
a2 = np.ones_like(a1)
print(a1)
print(a2)

print(np.log(a1+a2))

print(2*(a1+a2))

print((np.pi*a1)/a2**3)

#multidimensional Arrays

M = np.array([[3,4,5,6],[7,8,9,10]]) #note number of individual arrays [] must be same ex: [2,3,4] and [11,12,14] both have 3 inside

print(M)
print(M.shape) #tells info about array
print(M.size) #tells total num of elements in M

print(M[1,3]) #unsure what this does yet but it gave me 10. Its called an index using simple list of indicies.

M.flatten().reshape(2,4)
#We can pass array creation functions the size of a desired multi-dimensional array
M1 = np.ones([3,3]) #creates 3x3 matrix of 1s
print(M1)
Id = np.identity(3) #Makes det of matrix I think
print(Id)

# can go beyond matrices
M0 = np.zeros([3,3,3]) #makes 3x3 matrix of 0s 3 times
print(M0)

# there are some special matrix creaters
II = np.identity(4, dtype=int)
print(II) #will give a 4x4 matrix that is solved.
"""
#challenge is find indicies of non-zero elements from [1,2,0,0,4,0]
#create array of uniformly distributed random numbs b/w 1 & 3 and explore how avg depends on length of array
# show a 10x10 matrix is idempotent
#explore Meshgrid method and use it to evaluate matrix  Z = X^2 + Y^2  on a 10x10 grid between -1,1.

w = np.array([1,2,0,0,4,0])
print(np.nonzero(w))
 #(Random #s 1,3)

q = np.random.uniform(1, 3, size=5)

print(q)
print('Average',np.mean(q))

q = np.random.uniform(1, 3, size=50)

print(q)
print('Average',np.mean(q))

q = np.random.uniform(1, 3, size=150)

print(q)
print('Average',np.mean(q))
#As you increase length of array, the mean gets closer to 2

Id = np.identity(10) #10x10 matrix
print(np.matmul(Id,Id)) #Checks multiplying 10x10 by itself
print(np.array_equal(np.matmul(Id,Id),Id)) #sees if Id^2 = Id

#Z = x^2 + Y^2 from -1,1

x = np.linspace(-1,1,10) #splits numbs -1,1 in 10 pieces for x
y = np.linspace(-1,1,10) #splits numbs -1,1 in 10 pieces for y

X, Y = np.meshgrid(x,y) #meshgrid method

Z = X**2 + Y**2 #Formula z  = x^2 + y^2

print(Z)

print('Z shape', Z.shape)