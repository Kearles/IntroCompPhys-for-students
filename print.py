import math

# setting a variable

"""(a = 1.7E-6
print (a)

print(type(a)) # checking the type of a variable

b = 1.2 + 3.1

print(b)

print(type(b))

x = 1

x += 2

x

x -= 1
print(x)

x *= 2
print(x)

x  /= 2
print(x)

x **=2
print(x)

x %= 3
print(x)

x //= 2
print(x))""" 

"""(x,y,z = 1,2,3 # can assign multiple variables at the same time
print(x + y + z)

c = 2 + 1.5j # use j or J for imaginary parts
print(c)

d = 1j * complex(0,1)
print(d)

print((1+2j)/(1+1J))

a = 1.5 + 0.5j
print('Real[a] =', a.real) # meant to give real part of a
print('Imag[a] =', a.imag) # meant to give imaginary part of a

a = 1.5 + 0.5j
print('|a| = ', abs(a))

a = 3 +3j

b = a +1j 

print('|b| = ', abs(b)) # gives magnitude of b

b = 3 +4j
print('|b| = ', abs(b)) # test to see if answer is same as above
)"""

b = 5

a = (3.0*1.0)/5.0

b = 3.0*(1.0/5.0)

print(a == b)

import sys
sys.float_info

eps = sys.float_info.epsilon
truthiness = abs(a-b) < eps
print(truthiness)

s = ' Hello ' 
print(s*4)

s = '12345'
print(len(s))

help() # for help
help(str) #for help with a type
