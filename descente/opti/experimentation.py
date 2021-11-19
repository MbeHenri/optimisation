from numpy import NaN
from descente.opti.algo_desc import grad_desc_pas_fixe

def convergence_pas(x0,e,min,ecart):
    pas=min
    X=[]
    Y=[]
    while True:
        try:
            b=grad_desc_pas_fixe(x0,e,pas)
            Y.append(len(b[1])-1)
        except: 
            return (X,Y)
        X.append(pas)
        pas+=ecart
    return (X,Y)