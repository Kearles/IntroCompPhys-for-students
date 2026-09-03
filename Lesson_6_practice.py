import math # modules are repositories we can import and use
dir(math) # dir will give yoou a list of methods in a module

print(math.sqrt(88.6821))

π = math.pi
print(f'{π:.16f}')
print(f'{π:.5f}') # the number gives the digits after 3.

print(math.sqrt.__doc__)
print(math.__name__)

import time
print(time.strftime("%a, %d %b %Y   %H:%M:%S +0000",time.gmtime())) #how to do time. 

from time import *
print(strftime("%m/%d/%Y %H:%M:%S",gmtime())) #how to get month/day/year hour/min/second instead of all the extra info from the above time

#we can import only selected parts from math
from math import sin,cos
from math import pi as π

print(sin(2*π/3)+cos(π/3)/sin(π/3)) #should be ~1.443...

# %load ../include/mymodule.py
'''
A python module to exhibit the use of the __main__ name.
'''

from foo import leibniz_pi,Monte_Carlo_pi #testing if i made a module named foo
print(leibniz_pi(100_000))
print(Monte_Carlo_pi(100_000))
