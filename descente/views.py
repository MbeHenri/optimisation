from django.shortcuts import render
import numpy as np
from json import dumps

from descente.opti.algo_desc import grad_desc_pas_fixe, grad_desc_pas_var, newton_local
from descente.opti.exception import InvalidPas
from descente.opti.experimentation import convergence_pas

def index(request):
    return render(request, 'descente/index.html' )

def pasFixe(request): 
    try: 
        pas= float(request.GET['pas'])
        x0 = float(request.GET['x0'])
        y0 =float(request.GET['y0'])
        precision =float(request.GET['precision'])
        (pointmin,liste) = grad_desc_pas_fixe(np.array([x0 , y0]),precision , pas)
        (X,Y)=convergence_pas(np.array([x0 , y0]),precision,0.1,0.01)
        reponse = {
            'pointmin':pointmin,
            'liste':liste ,
            'ok': True ,
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
    try: 
        x0 = float(request.GET['x0'])
        y0 =float(request.GET['y0'])
        precision =float(request.GET['precision'])
        (pointmin,liste) = grad_desc_pas_var(np.array([x0 , y0]),precision )
        reponse = {
            'pointmin':pointmin,
            'liste':liste ,
            'ok': True 
        }
    except:
        reponse ={}
    return render(request, 'descente/pasOptimale.html',reponse)

def newtonLocal(request):
    try: 
        x0 = float(request.GET['x0'])
        y0 =float(request.GET['y0'])
        precision =float(request.GET['precision'])
        (pointmin,liste) = newton_local(np.array([x0 , y0]),precision )
        reponse = {
            'pointmin':pointmin,
            'liste':liste ,
            'ok': True 
        }
    except:
        reponse ={}
    return render(request, 'descente/newtonLocal.html',reponse)

def gaussNewton(request):
    return render(request, 'descente/gaussNewton.html')
