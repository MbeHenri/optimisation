from numpy import NaN
from descente.opti.algo_desc import grad_desc_pas_fixe
from descente.opti.fonction import f, grad_f

def experiment_pas(x0,e,min,ecart):
    pas=min
    X=[]
    Y=[]
    while True:
        try:
            b=grad_desc_pas_fixe(f,grad_f,x0,e,pas)
            Y.append(b[1])
        except: 
            return (X,Y)
        X.append(pas)
        pas+=ecart
def experiment_pas2(x0,e,min,max,ecart):
    pas=min
    T=[]
    while pas<=max:
        try:
            b=grad_desc_pas_fixe(f,grad_f,x0,e,pas)
            T.append((pas,b[1]))
        except: 
            T.append((pas,"DIV"))
        pas+=ecart
    return T