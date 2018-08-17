from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.welcome_page, name='welcome_page'),
    path('test1/', views.index, name='index'),
    path('test2/', views.index2, name='index2')
]

urlpatterns += staticfiles_urlpatterns()
