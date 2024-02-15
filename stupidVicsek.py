# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 15:57:42 2023

@author: wamma
"""

import numpy as np
import random
import matplotlib.pyplot as plt


plt.figure(figsize=(8, 8))  
plt.gca().set_aspect('equal')


shape = 100         #box shape
n = 50              #Number of birds
accel = 3        #acceleration 
time = 10000        #time of the simulation
start = 0
# matrice avec le nombre des oiseuax avec L1 = x,y / L2 = dx, dy / 
flock = np.zeros((n,2,2))


for bird in flock :
    bird[0][0] =  0
    bird[0][1] =  0
    bird[1][0] =  0
    bird[1][1] =  0
    
while start <= time :
    plt.clf() 
    plt.xlim(-shape/2, shape/2)
    plt.ylim(-shape/2, shape/2)
    for bird in flock :
        x = bird[0][0]
        y = bird[0][1]
        plt.plot(x,y, 'o',color='red')
        bird[1][0] = random.uniform(-accel,accel)
        bird[1][1] = random.uniform(-accel,accel)
        bird[0][0] = ( bird[0][0] + bird[1][0] + shape/2) % shape - shape/2
        bird[0][1] = ( bird[0][1] + bird[1][1] + shape/2) % shape - shape/2

    plt.grid(True) 
    plt.pause(0.01) 
    start +=1

plt.show()


















# TODO


# make the fucking thing work with r and a an angle, 
# try and figure out the acceleration and velocity in order to not add up franatically 
# apply flocking behaviour
# apply repelling force when near neighbour boids/ birds
# see if I can make the animation non choppy



















    
    


