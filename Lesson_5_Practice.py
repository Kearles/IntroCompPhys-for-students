result,item = 0,0
while item < 4: 
    item += 1 
    result += item 
    if result > 3: 
        break 
print(result)

# we can use 'enumerate' for access to both the integer index and value
"""names = ['Mal', 'Zoe', 'Wash', 'Inara', 'Jayne', 'Kaylee', 'Simon', 'River', 'Book']
for idx,name in enumerate(names):
    print('%d\t%s' % (idx,name))"""

"""n = ['   one   ', '   two   ', '   three  ']

print([num.strip() for num in n])

n = ['   one   ', '   two   ', '   three   ']
stripped = []
for cn in n:
    stripped.append(cn.strip())
print(stripped)

odd = [i for i in range(10) if i % 2] 
print(odd) #should take out even numbers

cnum = [complex(x,y) for x in range(5) for y in range(5) if abs(complex(x,y)) < 3]
print(cnum)"""


"""primes = []

for num in range(2, 51):
    is_prime = True

    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)

print(primes)

#  define this function
def add(a,b):
    '''Add two numbers.'''
    c = a+b
    print(c)
def add_one_liner(a,b): return a+b

#Note these adds only work for 2 inputs (a,b) but not three inputs (a,b,c)
add(10,11) #integers
add(100.2,200.1) #floats
add(219,-11.5) #testing mixing
add('red','sox')
#add('red',1) will not work because cannot add string and int."""
def add(a,b):
    '''Add two numbers.'''
    c = a+b
    print(c)
def add_one_liner(a,b): return a+b
func = add
func(10,10)

def cube(x): return x**3
cubes = [cube(x) for x in range(1,25)]
print(cubes)

def f(x): return 5*x**2 + x

f = [f(x) for x in range(1,10)]
print(f)

# functions as filters
def odd(x): return (x%2)
odds = [i for i in range(1,10) if odd(i)]
print(odds)

def square(x): 
    return x**2
[square(x) for x in range(5)]
# using a lambda
sq = lambda x: x**2
[sq(x) for x in range(5)]

student_tuples = [('john', 'A', 22), ('jane', 'B', 19),('dave', 'B', 23)]
sorted(student_tuples, key=lambda student: student[2])   # sort by age and also figuring out what a lambda does


leap_years = [x for x in range(2006,2026) if (x % 4 ==0 and x % 100 != 0) or (x % 400 ==0)]
print(leap_years)
