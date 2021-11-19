
from django.urls.conf import path

from . import views

urlpatterns = [
    path('pasFixe', views.pasFixe, name='pasFixe'),
    path('pasOptimale', views.pasOptimale, name='pasOptimale'),
    path('newtonLocal', views.newtonLocal, name='newtonLocal'),
    path('gaussNewton', views.gaussNewton, name='gaussNewton')
]