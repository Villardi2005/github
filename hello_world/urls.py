from django.urls import path
from . import views

urlpatterns = [
    path('cadastroprofessor/', views.cadastro_professor, name='cadastro_professor'),
]
from django.contrib import admin
from django.urls import path
from hello_world.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),  
]

