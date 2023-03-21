import matplotlib.pyplot as plt
import random

#starting values
a = 0.9
b=-0.6013
c=2.0
d=0.5


#number of iterations
i = 100000

#firts value of x and y 
x0 = -0.72
y0 = -0.64

#creating list and the second values
xaxis = []
yaxis = []
xadd = (x0**2)-(y0**2)+ (a*x0)+(b*y0)
xaxis.append(xadd)
yadd = (2*x0*y0)+(c*x0)+(d*y0)
yaxis.append(yadd)


#generating the rest of the values
for i in range(0,10+i):
    x = xaxis[i]
    y = yaxis[i]
    xadd = (x**2)-(y**2)+ (a*x)+(b*y)
    yadd = (2*x*y)+(c*x)+(d*y)
    xaxis.append(xadd)
    yaxis.append(yadd)




#formatting and color change of points 

size = 0.5
#color = ['black']

colors = []
for i in range(len(xaxis)):
    colors.append((random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
#print(xaxis)
#print(yaxis)
plt.scatter(xaxis, yaxis, s=size, c=colors)


#axis labels and graph title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Thinkerbell graph')

plt.show()