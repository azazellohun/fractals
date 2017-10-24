from matplotlib import pyplot as plt
import numpy as np
from math import sin, cos, pi

# print to file
# loopCount = 10
# print ('number of points: ' + str(2^[2*(loopCount-1)]+1))

import matplotlib.pyplot as plt
import numpy as np
from numpy import sin,cos,sinh,cosh,sqrt,vstack,hstack,zeros,eye, pi
from copy import deepcopy

def Rot(fi):
    return np.array([[cos(fi), sin(fi)],[-sin(fi), cos(fi)]])

class Fractal:
           
    def __init__(self, x0=0, y0=0, x1=1, y1=0):
        self.points_x = [x0, x1]
        self.points_y = [y0, y1]
        self.point_count = 2 
        self.iter_number = 0
        
    def draw(self):
        self.fig = plt.figure(figsize=(8, 8))
        self.ax = self.fig.add_subplot(1, 1, 1)        
        self.ax.plot(self.points_x, self.points_y, color='k')
        self.ax.set_xlim([0, 1])
        self.ax.set_ylim([-0.4, 0.6])
        plt.show()

        print("N = {}".format(self.iter_number))
        
    def iterate(self, N):
        self.iter_number += N
        
        for i in range(N):            
            copy_x, copy_y = deepcopy(self.points_x), deepcopy(self.points_y)
            for j in range(len(copy_x)- 1): 
                new_x, new_y = self.iteration_spet([copy_x[j], copy_y[j]], [copy_x[j+1], copy_y[j+1]])
                self.points_x[j*(3)+j+1 : j*(3)+j+1] = new_x
                self.points_y[j*(3)+j+1 : j*(3)+j+1] = new_y
     
    def iteration_spet(self, A, B):
        self.point_count += 3
        x0,y0,x1,y1 = *A, *B
        
        AB_3rd = np.array([x1-x0, y1-y0]) / 3
        E = np.array(A) + AB_3rd
        F = E + np.dot(Rot(-pi/3), AB_3rd) 
        G = B - AB_3rd
        F = G - np.dot(Rot(pi/3), AB_3rd) 
        
        x_insert, y_insert = zip(E, F, G)
         
        return x_insert, y_insert
           

frac = Fractal()

frac.iterate(1)
frac.draw()


def pointMaker(A, B, fi):
    # create 5 points (10 coords) from 2 points (4 coords):
    RCCW = np.array([[cos(fi), -sin(fi)], [sin(fi), cos(fi)]])
    E = np.array([(B[0]-A[0])/3.0+A[0], (B[1]-A[1])/3.0+A[1]])     # vA + vAB/3
    F = E + np.dot(E, RCCW)                                        # rotate vE, origin: E
    RCW = np.array([[cos(-fi), -sin(-fi)], [sin(-fi), cos(-fi)]])  # rotate other way
    G = F + np.dot(E, RCW)

    ind = points[0].index(A[0])+1
    for i in [E, F, G]:
        points[0].insert(ind, i[0])
        points[1].insert(ind, i[1])
        ind += 1
    return points


def draw():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(points[0], points[1], color='k')
    # ax.set_xlim([0, 1])
    ax.set_ylim([-0.4, 0.6])
    plt.show()

A0, B0 = [0, 0], [1, 0]
points = [[A0[0], B0[0]], [B0[1], A0[1]]]
# print pointMaker(A0, B0, -pi/3)

it = 0
iteration = 1
while it <= iteration:
    fi = -pi/3
    nPoints = len(points[0])
    for j in range(nPoints-1):
        i = points[0].index(j)-j*3 #**it 
        A, B = [points[0][i], points[1][i]], [points[0][i+1], points[1][i+1]]
        pointMaker(A, B, fi)
        print points[1], j
        draw()
    it += 1

# draw()
