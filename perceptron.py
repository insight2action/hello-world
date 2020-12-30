#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 15:20:41 2017

@author: jvanhulse

Implement a simple liear perceptron algorithm

"""
import numpy as np

data = [(-.45, 4.3, -1), (-.31, 5.6, -1),(.4, 2.1, -1), 
        (1.3, 4.4, -1),(3.2, 7, -1),
        (4.6, 5.3, 1),(5.5,1.2,1),(7.3,7.4,1)]

#initialize the weights
w1 = .23
w2 = .49
w0 = 1.7

#enter other user-defined parameters
learningRate = 1000 
maxIterations = 100     #don't run more than maxIterations to find a solution


#############################################
#initialize 2 key variables
iterations = 0 
numErrors = len(data)

# Main loop
while numErrors > 0 and iterations < maxIterations:
    numErrors = 0 
    iterations +=1

    for i in range(0, 7):
        pred = int(np.sign(data[i][0] *w1 + data[i][1] * w2 + w0))
        if pred != data[i][2]:
            numErrors +=1
            error = data[i][2] - pred
        else:
            error = 0    
        #weight update formulas
        w1 += learningRate * error * data[i][0]
        w2 += learningRate * error * data[i][1]
        w0 += learningRate * error 

print("*************************")
print("Final Statistics:")
print("Iterations %d" % iterations)
print("Weights: w0: %f, w1: %f, w2: %f" % (w0, w1, w2))
#######################################################