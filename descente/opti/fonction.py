from numpy import array

#champ scalaire 
def f(x):
    return float(((1/2)*pow(x[0], 2)) + ((7/2)*pow(x[0], 2)))

def grad_f(x):
    return array([x[0] , 7*x[1]])

def hessian_f(x):
    return array([
        [1,0],
        [0,7]
    ])

#champ vectoriel 
def F(x):
    return array([f(x),f(x-1)])

def J(x):
    return array(
        grad_f(x).tolist,
        grad_f(x-1).tolist
)
