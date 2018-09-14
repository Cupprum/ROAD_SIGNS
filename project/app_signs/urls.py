from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.welcome_page, name='welcome_page'),
    path('choose_category/', views.choose_category, name='choose_category'),
    path('show_sign/', views.show_sign, name='show_sign'),
    path('question/', views.question, name='question'),
    path('register/', views.register, name='register')
]

urlpatterns += staticfiles_urlpatterns()
