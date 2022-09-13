from django.urls import path
from . import views
from .views import dashboard, success
from django.views.generic.base import RedirectView
urlpatterns = [
    path('', RedirectView.as_view(url='login/'), name='login'),
    path('login/', views.login, name = 'login'),
    path('register/',views.register, name = 'register'),
    path('login/dashboard/',dashboard),
    path('login/dashboard/info/success/',success),
    path('login/dashboard/info/', views.info, name = 'info')
]