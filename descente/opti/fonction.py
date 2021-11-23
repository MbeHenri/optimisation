import numpy as np

#champ scalaire 
def f(x):
    return (1/2)*x[0]**2 + (7/2)*x[1]**2

def grad_f(x):
    return np.array([x[0] , 7*x[1]])

def hessian_f(x):
    return np.array([
        [1,0],
        [0,7]
    ])

#champ vectoriel 
def F(x):
    return np.array([f(x),f(x-1)])

def J(x):
    return np.array([
        [x[0] , 7*x[1]],
        [x[0]-1 , 7*x[1]-1]
    ])
