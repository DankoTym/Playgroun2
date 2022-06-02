from django.contrib import admin
from django.urls import path, include  #acá agregué el include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppCoder/', include('AppCoder.urls')),        #esto es para incluir las urls.py del la App, se debe hacer para cada app dentro de nuestro proyecto

]
