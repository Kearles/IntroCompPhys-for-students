#warmup
# Given two strings, return their concatenation, except omit the first character of each.
s1 = 'hello'
s2 = 'there'
#output --> 'ellohere'
print(s1[1:5], s2[1:5], sep='')

l1 =[1,2,3,4,5]
#make output [5,1,2,3,4]
l1[0:5] =[5,1,2,3,4]
print(l1)


"""keys = ['theory','experiment','computational']
values = [3, 4, 10]
physics_256 = dict(zip(keys, values))
print(physics_256)

print('experiman' in physics_256)  # False
print('computational' in physics_256)  # True

physics_256.keys() #list of keys

del physics_256['experiment']
print(physics_256)"""

"""d = (5,7,8) #Tuple
print(d[1])
           #d[1] = 9  should not work because Tuples are immutable

q,r,s = 1,2,3
t = 4,5,6
print(r) #should give 2
q,r,s = t
print(r) #should give 5

import random
x = random.randint(1,50)

if x < 25:
    print("X is smaller than 25")
if x == 1:
    print(1)
else:
    print("x is bigger than 25")"""

"""# logical operators are: and,or,not
x = 10
y = 25
if x > 0 and y > 0:
    print('both true')

if not x < 1:
    print ('x is big')
for i in range(6):
    print(i)

scores = {'Cavaliers':95, 'Suns':106, 'Spurs':87, '76ers':115}
for team,wins in scores.items():
    print('The %s are doing' %team, end=' ')
    if wins >= 100:
        print('well')
    elif 90 < wins < 100:
        print('okay')
    elif wins < 90:
        print('poorly')
    else:
        print('great')

# test whether a list is empty
l = list(range(5))
while l:
    print(l.pop())"""
