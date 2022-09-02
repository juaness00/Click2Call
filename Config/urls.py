from django.urls import path
from . import views
from .views import dashboard, success
urlpatterns = [
    path('', views.index, name = 'index'),
    path('test/', views.test, name = 'test'),
    path('test/dashboard/',dashboard),
    path('test/dashboard/settings/success/',success),
    path('test/dashboard/settings/', views.settings, name = 'settings')
]