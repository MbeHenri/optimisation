from numpy.linalg import norm
from numpy.linalg.linalg import solve

from descente.opti.recherche_pas import search_armijo, search_wolfe
from descente.opti.exception import InvalidPas

## conditions
# critere d'arret pour un champ scalaire
def cond(f,grad_f,e,xk,xk_1,k,iter_max,stag_sol,stag_cour,with_max):
    return ( 
        (norm(grad_f(xk))<e) 
        or (stag_sol and norm(xk-xk_1)<e*norm(xk)) 
        or (stag_cour and abs(f(xk)-f(xk_1)) < e*abs(f(xk_1))) 
        or (with_max and k >= iter_max) )

# condition de test 
def is_valid(grad_f,xk) : 
    return not(xk[0]==float('inf') or xk[0]==-float('inf') or xk[1]==float('inf') or xk[1]==-float('inf'))


## algorithme de descente de gradient 
# algorihthe de descente de gradient a pas fixe

def grad_desc_pas_fixe(f,grad_f,x0,e,s,iter_max=0,stag_sol=False,stag_cour=False,with_max=False):
    xk=x0
    xk_1=x0-x0
    g=grad_f(xk)
    k=0
    while(not cond(f,grad_f,e,xk,xk_1,k,iter_max,stag_sol,stag_cour,with_max)):
        xk_1=xk
        xk=xk-s*g
        if(not is_valid(grad_f,xk)):
            raise InvalidPas("un maivais pas a été donné")
        g=grad_f(xk)
        k=k+1
    return (xk,k)

def grad_desc_pas_armijo(f,grad_f,x0,e,iter_max=0,stag_sol=False,stag_cour=False,with_max=False):
    xk = x0
    dk = -grad_f(x0)
    xk_1=x0-x0
    k=0
    while(not cond(f,grad_f,e,xk,xk_1,k,iter_max,stag_sol,stag_cour,with_max)):
        sk = search_armijo(f,grad_f,0.0001,xk ,dk)
        xk_1=xk
        xk = xk + sk*dk
        dk = -grad_f(xk)
        k=k+1
    return (xk,k)

def grad_desc_pas_wolfe(f,grad_f,x0,e,iter_max=0,stag_sol=False,stag_cour=False,with_max=False):
    xk = x0
    dk = -grad_f(x0)
    xk_1=x0-x0
    k=0
    while(not cond(f,grad_f,e,xk,xk_1,k,iter_max,stag_sol,stag_cour,with_max)):
        sk = search_wolfe(f,grad_f,0.0001,0.99,xk ,dk)
        xk_1=xk
        xk = xk + sk*dk
        dk = -grad_f(xk)
        k=k+1
    return (xk,k)
    
# algorithme de descente de gradient a pas variable 
def grad_desc_pas_var(f,grad_f,x0,e,iter_max=0,stag_sol=False,stag_cour=False,with_max=False):
    xk=x0
    xk_1=x0-x0
    g=grad_f(xk)
    sk=0
    k=0
    while not cond(f,grad_f,e,xk,xk_1,k,iter_max,stag_sol,stag_cour,with_max):
        #choix de sk
        sk=xk[0]*xk[0]
        sk=(sk+49*xk[1]*xk[1])/(sk+343*xk[1]*xk[1])

        #calcul de sk+1
        xk_1=xk
        xk=xk-sk*g
        g=grad_f(xk)
        k=k+1
    return (xk,k)

# algorithme de descente de gradient a pas variable 
def grad_desc_pas_var2(f,grad_f,x0,e,iter_max=0,stag_sol=False,stag_cour=False,with_max=False):
    xk=x0
    xk_1=x0-x0
    g=grad_f(xk)
    sk=0
    k=0
    T=[(k,f(xk),norm(g),sk,xk[0],xk[1])]
    while not cond(f,grad_f,e,xk,xk_1,k,iter_max,stag_sol,stag_cour,with_max):
        #choix de sk
        sk=xk[0]*xk[0]
        sk=(sk+49*xk[1]*xk[1])/(sk+343*xk[1]*xk[1])

        #calcul de sk+1
        xk_1=xk
        xk=xk-sk*g
        g=grad_f(xk)
        k=k+1
        T.append((k,f(xk),norm(g),sk,xk[0],xk[1]))
    return T

## methode de newton locale
def newton_local(f,Hf,grad_f,x0,e,iter_max=0,stag_sol=False,stag_cour=False,with_max=False):
    xk=x0
    xk_1=x0-x0
    g=grad_f(xk)
    k=0
    while(not cond(f,grad_f,e,xk,xk_1,k,iter_max,stag_sol,stag_cour,with_max)):
        #recherche de dk
        dk=solve(Hf(xk),-g)

        #calcul de sk+1
        xk_1=xk
        xk=xk+dk
        g=grad_f(xk)
        k=k+1
    return (xk,k)

## methode de gauss-newton (conserne un champ vectoriel)
# a gerer a cause de la condition d'arrets
def gauss_newton(F,J,x0,e):
    xk=x0
    xk_1=x0-x0
    k=0
    return (xk,k)