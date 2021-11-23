from django.shortcuts import render
import numpy as np
from json import dumps

from descente.opti.algo_desc import grad_desc_pas_armijo, grad_desc_pas_fixe, grad_desc_pas_var, grad_desc_pas_var2, grad_desc_pas_wolfe, newton_local
from descente.opti.exception import InvalidPas
from descente.opti.experimentation import experiment_pas, experiment_pas2
from descente.opti.fonction import f, grad_f
from descente.opti.utils import save_f, save_f2

def index(request):
    return render(request, 'descente/index.html' )

def pasFixe(request): 
    stag_sol=True
    stag_cour=True
    with_max=True
    try:
        request.GET['stag_sol']
    except:
        stag_sol=False
    try:
        request.GET['stag_cour']
    except:
        stag_cour=False
    try:
        request.GET['with_max']
    except:
        with_max=False
    try: 
        pas= float(request.GET['pas'])
        x0 = float(request.GET['x0'])
        y0 =float(request.GET['y0'])
        precision =float(request.GET['precision'])
        iterMax=0
        if(with_max):
            iterMax=float(request.GET['iterMax'])

        (pointmin,nbreIter) = grad_desc_pas_fixe(f,grad_f,np.array([x0 , y0]),precision,pas,iter_max=iterMax, stag_cour=stag_cour,stag_sol=stag_sol, with_max=with_max)
        (X,Y)=experiment_pas(np.array([x0 , y0]),precision,0.1,0.01)
        datas=experiment_pas2(np.array([x0 , y0]),precision,0.1,1,0.01)
        save_f2(datas,"datasPasFixe.txt")
        reponse = {
            'pointmin':pointmin,
            'nbreIter':nbreIter ,
            'ok': True ,
            'datas': datas,
            'x': dumps(X),
            'y': dumps(Y)
        }
    except InvalidPas:
        reponse ={
            'invalidPas' : True,
            'messageError' : " Il y'a divergence pour le pas choisie",
        }
    except:
        reponse ={}
    return render(request, 'descente/pasFixe.html',reponse)

def pasOptimale(request):
    stag_sol=True
    stag_cour=True
    with_max=True
    try:
        request.GET['stag_sol']
    except:
        stag_sol=False
    try:
        request.GET['stag_cour']
    except:
        stag_cour=False
    try:
        request.GET['with_max']
    except:
        with_max=False

    try: 
        x0 = float(request.GET['x0'])
        y0 =float(request.GET['y0'])
        precision =float(request.GET['precision'])
        iterMax=0
        if(with_max):
            iterMax=float(request.GET['iterMax'])
        (pointmin,nbreIter) = grad_desc_pas_var(f,grad_f,np.array([x0 , y0]),precision, iter_max=iterMax, stag_cour=stag_cour,stag_sol=stag_sol, with_max=with_max)
        datas=grad_desc_pas_var2(f,grad_f,np.array([x0 , y0]),precision, iter_max=iterMax, stag_cour=stag_cour,stag_sol=stag_sol, with_max=with_max)
        save_f(datas,"datasPasOptimal.txt")
        reponse = {
            'pointmin':pointmin,
            'nbreIter':nbreIter ,
            'datas': datas,
            'ok': True 
        }
    except:
        reponse ={}
    return render(request, 'descente/pasOptimale.html',reponse)

def newtonLocal(request):
    stag_sol=True
    stag_cour=True
    with_max=True
    try:
        request.GET['stag_sol']
    except:
        stag_sol=False
    try:
        request.GET['stag_cour']
    except:
        stag_cour=False
    try:
        request.GET['with_max']
    except:
        with_max=False

    try: 
        x0 = float(request.GET['x0'])
        y0 =float(request.GET['y0'])
        precision =float(request.GET['precision'])
        iterMax=0
        if(with_max):
            iterMax=float(request.GET['iterMax'])
        (pointmin,nbreIter) = newton_local(f,grad_f,np.array([x0 , y0]),precision, iter_max=iterMax, stag_cour=stag_cour,stag_sol=stag_sol, with_max=with_max)
        reponse = {
            'pointmin':pointmin,
            'nbreIter':nbreIter ,
            'ok': True 
        }
    except:
        reponse ={}
    return render(request, 'descente/newtonLocal.html',reponse)
def pasWolfe(request):
    stag_sol=True
    stag_cour=True
    with_max=True
    try:
        request.GET['stag_sol']
    except:
        stag_sol=False
    try:
        request.GET['stag_cour']
    except:
        stag_cour=False
    try:
        request.GET['with_max']
    except:
        with_max=False

    try: 
        x0 = float(request.GET['x0'])
        y0 =float(request.GET['y0'])
        precision=float(request.GET['precision'])
        iterMax=0
        if(with_max):
            iterMax=float(request.GET['iterMax'])
        (pointmin,nbreIter) = grad_desc_pas_wolfe(f,grad_f,np.array([x0 , y0]),precision, iter_max=iterMax, stag_cour=stag_cour,stag_sol=stag_sol, with_max=with_max)
        reponse = {
            'pointmin':pointmin,
            'nbreIter':nbreIter ,
            'ok': True 
        }
    except:
        reponse ={}
    return render(request, 'descente/pasWolfe.html',reponse)

def pasArmijo(request):
   
    stag_sol=True
    stag_cour=True
    with_max=True
    try:
        request.GET['stag_sol']
    except:
        stag_sol=False
    try:
        request.GET['stag_cour']
    except:
        stag_cour=False
    try:
        request.GET['with_max']
    except:
        with_max=False
    
    try: 
        x0 = float(request.GET['x0'])
        y0 =float(request.GET['y0'])
        precision =float(request.GET['precision'])
        iterMax=0
        if(with_max):
            iterMax=float(request.GET['iterMax'])
        print("ok1")
        (pointmin,nbreIter) = grad_desc_pas_armijo(f,grad_f,np.array([x0 , y0]),precision, iter_max=iterMax, stag_cour=stag_cour,stag_sol=stag_sol, with_max=with_max)
        reponse = {
            'pointmin':pointmin,
            'nbreIter':nbreIter ,
            'ok': True 
        }
    except:
        reponse ={}
    return render(request, 'descente/pasArmijo.html',reponse)

def gaussNewton(request):
    return render(request, 'descente/gaussNewton.html')
