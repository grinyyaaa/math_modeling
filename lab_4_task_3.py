import numpy as np

g = 10

def maxenergy(m, h, v0):
    kinetics = (m*v0**2)/2
    potential = m*g*h
    fullenergy = kinetics + potential
    print(fullenergy)
    
m = 5
h = 15
v0 = 20

maxenergy(m, h, v0)