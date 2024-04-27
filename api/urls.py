# from django.urls import path, include
# from api import views 

# urlpatterns = [    
#     path('',views.index,name="index"),
# ]

#ESTA ES LA FORMA DE CREAR LA RUTA DE UNA API REST CON DJANGO FRAMEWORK 

from rest_framework  import routers
from .api import ApiViewSet

ruta= routers.DefaultRouter()
ruta.register('api/empleados',ApiViewSet,'api')

urlpatterns = ruta.urls


