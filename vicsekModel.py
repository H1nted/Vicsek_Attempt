# -*- coding: utf-8 -*-
"""
Created on Thu May 25 01:48:33 2023

@author: wamma
"""

import matplotlib.pyplot as plt
import numpy as np
import random


a = 100 #box dimension
n = 1   #number of birds
R = 2 #Radius of interactions
bruit = 1 # np.random.normal(0,np.pi)
angle_min = 0.0     
angle_max = np.pi  
v0 = 0.0001 
timeBEGIN = 0
timeMAX = 1000
dt = 0.0001

plt.figure(figsize=(8, 8))  
plt.gca().set_aspect('equal')


horde = np.zeros((n, 3, 1))


for b in range(len(horde)) :
     horde[b][0] = random.uniform((-a/2-0.1), (a/2-0.1))
     horde[b][1] = random.uniform(angle_min,angle_max)
     horde[b][2] = 1

print(horde)
while timeBEGIN <= timeMAX:
    plt.clf()  # Clear the plot at each iteration
    plt.xlim(-a/2, a/2)
    plt.ylim(-a/2, a/2)
    for bird in horde:
            #projection sur x et y        
            x = bird[0]*np.cos(bird[1])
            y = bird[0]*np.sin(bird[1])

            #dessiner notre point
            plt.plot(x, y, 'o', color='blue')  # Plotting bird positions as blue dots 
            #Recherche des voisins
            neighbors = []
            for friend in horde :
                x_friend = friend[0]*np.cos(friend[1])
                y_friend = friend[0]*np.sin(friend[1])
                distance = np.sqrt((x-x_friend)**2 +(y-y_friend)**2)
                if (distance <= R and distance != 0) :
                    neighbors.append(friend)
                    
            neighborsNP = np.array(neighbors) #changement en tableaux NumPy pour la smmation rapide
            #sommation des angles
            if len(neighborsNP > 0) :
                sommeAngles = np.sum(neighborsNP[:,1])/np.sum(neighborsNP[:,2])
            else :
                sommeAngles = 0
            #avancement
            #angle
            bruitdt = bruit*np.random.normal(0,np.pi)
            bird[1] = sommeAngles + bruitdt
            #Position

            bird[0] = (bird[0] + v0*dt*bird[1])%a -a/2
            
            
        
        
         
    plt.grid(True)
    plt.pause(0.001)  # Pause to allow the plot to update
     




plt.show()     