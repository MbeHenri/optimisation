from numpy import dot, inf, copy
from numpy.core.fromnumeric import transpose
from numpy.linalg.linalg import norm, solve


import descente.opti.fonction as fg
from descente.opti.exception import InvalidPas

## conditions
# critere d'arret
def cond(f,grad_f,e,xk,xk_1,k,iter_max,stag_sol,stag_cour,with_max):
    return ( 
        (norm(grad_f(xk))<e) 
        or (stag_sol and norm(xk-xk_1)<e*norm(xk)) 
        or (stag_cour and abs(f(xk)-f(xk_1)) < e*abs(f(xk_1))) 
        or (with_max and k >= iter_max) )

# condition de test 
def is_valid(grad_f,xk) : 
    return not(xk[0]==inf or xk[0]==-inf or xk[1]==inf or xk[1]==-inf)


## algorithme de descente de gradient 
# algorihthe de descente de gradient a pas fixe
def grad_desc_pas_fixe(x0,e,s):
    xk=copy(x0)
    xn=[xk]
    g=fg.grad_f(xk)
    while(norm(g) > e): 
        xk=copy(xk-s*g)
        if(not is_valid(fg.grad_f,xk)):
            raise InvalidPas("un maivais pas a été")
        g=fg.grad_f(xk)
        xn.append(xk)
    return (xk,xn)
def grad_desc_pas_fixe_v(grad_f,x0,e,s):
    xk=copy(x0)
    xn=[xk]
    g=grad_f(xk)
    while(norm(g) > e): 
        xk=copy(xk-s*g)
        if(not is_valid(grad_f,xk)):
            raise InvalidPas("un maivais pas a été")
        g=grad_f(xk)
        xn.append(xk)
    return (xk,xn)
def grad_desc_pas_fixe_vc(f,grad_f,x0,e,s,iter_max=0,stag_sol=False,stag_cour=False,with_max=False):
    xk=copy(x0)
    xk_1=x0-x0
    xn=[xk]
    g=grad_f(xk)
    k=0
    while(not cond(f,grad_f,e,xk,xk_1,k,iter_max,stag_sol,stag_cour,with_max)):
        xk_1=xk
        xk=copy(xk-s*g)
        if(not is_valid(grad_f,xk)):
            raise InvalidPas("un maivais pas a été")
        g=grad_f(xk)
        xn.append(xk)
        k=k+1
    return (xk,xn)

# algorithme de descente de gradient a pas variable 
def grad_desc_pas_var(x0,e):
    xk=copy(x0)
    g=fg.grad_f(xk)
    xn=[xk]
    while(norm(g) > e):
        #choix de sk
        sk=xk[0]*xk[0]
        sk=(sk+49*xk[1]*xk[1])/(sk+343*xk[1]*xk[1])

        #calcul de sk+1
        xk=copy(xk-sk*g)
        g=fg.grad_f(xk)
        xn.append(xk)
    return (xk,xn)

def grad_desc_pas_var_vc(f,grad_f,x0,e,iter_max=0,stag_sol=False,stag_cour=False,with_max=False):
    xk=copy(x0)
    xk_1=x0-x0
    k=0
    sk=0
    g=grad_f(xk)
    T=[(xk,f(xk),sk,g)]

    while not cond(f,grad_f,e,xk,xk_1,k,iter_max,stag_sol,stag_cour,with_max):
        #choix de sk
        sk=xk[0]*xk[0]
        sk=(sk+49*xk[1]*xk[1])/(sk+343*xk[1]*xk[1])

        #calcul de sk+1
        xk_1=xk
        xk=copy(xk-sk*g)
        g=grad_f(xk)
        T.append((xk,f(xk),sk,g))
    
    return (xk,T)

## methode de newton locale
def newton_local(x0,e):
    xk=copy(x0)
    xn=[xk]
    g=fg.grad_f(xk)
    while(norm(g) > e):
        #recherche de dk
        dk=solve(fg.hessian_f(xk),-g)

        #calcul de sk+1
        xk=xk=copy(xk+dk)
        g=fg.grad_f(xk)
        xn.append(xk)
    return (xk,xn)

def newton_local_v(Hf,grad_f,x0,e):
    xk=copy(x0)
    xn=[xk]
    g=grad_f(xk)
    while(norm(g) > e):
        #recherche de dk
        dk=solve(Hf(xk),-g)

        #calcul de sk+1
        xk=xk=copy(xk+dk)
        g=grad_f(xk)
        xn.append(xk)
    return (xk,xn)

def newton_local_vc(f,Hf,grad_f,x0,e,iter_max=0,stag_sol=False,stag_cour=False,with_max=False):
    xk=copy(x0)
    xk_1=x0-x0
    k=0
    xn=[xk]
    g=grad_f(xk)
    while(not cond(f,grad_f,e,xk,xk_1,k,iter_max,stag_sol,stag_cour,with_max)):
        #recherche de dk
        dk=solve(Hf(xk),-g)

        #calcul de sk+1
        xk=xk=copy(xk+dk)
        g=grad_f(xk)
        xn.append(xk)
        k=k+1
    return (xk,xn)

## methode de gauss-newton (conserne un champ vectoriel)
# a gerer a cause de la condition d'arrets
def gauss_newton(F,J,x0,e):
    xk=copy(x0)
    xn=[xk]
    while(
        
                     ):
        #recherche de dk+1
        t=transpose(J(xk))
        d=solve(dot(t,J(xk)),-dot(t,F(xk)))

        #calcul de sk+1
        xk=xk=copy(xk+d)
        xn.append(xk)
    return (xk,xn)