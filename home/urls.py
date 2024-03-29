from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('convert', views.convert, name='convert'),
    path('download', views.download, name='download'),
    path('documentation', views.documentation, name='documentation'),
]