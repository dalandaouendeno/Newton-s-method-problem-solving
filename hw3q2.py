#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#hw3 question2

"""""""""""""""
Problem 2: Use Newton’s method to solve the two-dimensional system
    x**0.2 + y**0.2 - 2 = 0
    x**0.1 + y**0.4 - 2 = 0
    
For this problem, set an initial guess of (x, y) = (2.0, 2.0) and allow the error tolerance level
at tol = 1e - 6. You can set the maximum iteration at your discretion

"""""""""""""""""""""
#importing libraries
import shutil
import numdifftools as nd
import numpy as np
import pandas as pd


def jacobian(f, x, dx):
    n = len(x)
    jac = np.zeros([n,n])
    e = np.eye(n) * dx
    
    for i in range(n):
        for j in range(n):
            jac[i][j] = (f(x+e[j])[i] - f(x-e[j])[i]) / (2*dx)
    return jac


# Define & print dash so when we print we get a separtion with other questions
# add a space
print()
# get the terminal's size
columns = shutil.get_terminal_size().columns
#print(dash)
# add a space
print()
# get the terminal's size
columns = shutil.get_terminal_size().columns 
print("Question 2 Solutions".center(columns)) #question 2 centered
print () #space

#defining the function where x[0] is x anf x[1] is y
def f(x):
     f = np.zeros(2) #using numpy f is returning 2 array
     f[0] = x[0]**0.2 + x[1]**0.2 - 2   #first equation
     f[1] = x[0]**0.1 + x[1]**0.4 - 2   #second equation
     return f #return the 2 array of f

# Define the newton function with 4 parameters
def newton(f, xguess,jacobian, tol, maxiter):
 
    print()
    print("iteration         x                  y")
    print(45*"-")

    #for loop that goes until the max iteration +1
    for i in range(maxiter+1): 
              
        Z = f(xguess) 
        jac = jacobian(f, xguess,dx=1e-7)        
        x0 = np.linalg.solve(jac, -Z) #dx        
        x1 = xguess + x0

        print("%4d %18.7f %18.7f" % (i+1, x1[0], x1[1]))
             
        if np.linalg.norm(x0) < tol:
            break
        
        else:
            xguess = x1

    print(45*"-")
    return x1

#check tolerance 
#read each step 

# defening the main function that allows us to write our input into the newton's function
def main():

    x0 = [2.0, 2.0] #x,y guess
    tol = 0.000001  #tolerance input 1e-6
    maxiter = 6    #maximum of iteration

    #new value of the newton's function output 
    #calling the function putting our values
    sol = newton(f, x0, jacobian, tol, maxiter) #change one of the statement 
    
    print()
    print()
    print("The Optimal solution for is:", sol)  #print the solution

main() #return the main function