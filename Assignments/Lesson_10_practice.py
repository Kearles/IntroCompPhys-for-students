#Lesson_10_practice

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = (1/(2* np.pi))* np.e**((-1*x**2)/2)

plt.figure(figsize=(10,6))
plt.plot(x,y, linewidth= 0.5, color='green')
plt.title('Gaussian Distribution Graph')
plt.xlabel('x')
plt.ylabel('y=(1/(2* np.pi))* np.e**((-1*x**2)/2)')
plt.grid(True)

plt.show()



"""marker_list = ['o','s','p','^','v','>','<','D','*','H']

x = np.arange(-1,1,0.1)
# generate and plot the parabola
for i,marker in enumerate(marker_list):
    # generate the parabola
    a = i
    y = x**2 + a

    # generate a label
    label = f'a={a}'

    # plot the parabola for each marker type
    plt.plot(x, y, marker=marker, label=label)

# some labels
plt.xlabel('$x$')
plt.ylabel('$y(x)$')
plt.title('A Family of Parabolas $y=x^2+a$')

# add a legend
plt.legend(loc='upper center', ncol=3)

plt.show()"""

