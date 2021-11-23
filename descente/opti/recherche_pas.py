import random as rd
from numpy import dot

# recherche lineaire du pas suivant la condition d'amidjio
def search_armijo(f,grad_f,e,x,d):
    #intervalle de de choix de depart [0,5]
    s= rd.random()*5
    while f(x+s*d) > (f(x) + e*s*dot(grad_f(x),d)):
        s=s/2
    return s

# recherche lineaire du pas suivant les conditions de wolfe
def search_wolfe(f, grad_f, e1, e2, x, d ):
    INFINI = float('inf')
    s_moin = 0
    s_plus = INFINI
    wolfe_condition = False

    #intervalle de de choix de depart [0,5]
    sk = rd.random()*5
    while(wolfe_condition == False):
        if(f(x + sk*d) > f(x) + e1*sk*dot(grad_f(x),d)):
            s_plus = sk
            sk = (s_moin + s_plus)/2
        elif dot(grad_f(x + sk*d) , d) < e2*dot(grad_f(x) , d):
            s_moin = sk
            if s_plus < INFINI:
                sk = (s_moin + s_plus)/2
            else:
                sk = 2*sk
        else:
            wolfe_condition = True
            
    return sk
    

