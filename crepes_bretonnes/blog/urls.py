"""
URL configuration for crepes_bretonnes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from blog import views

urlpatterns = [
    path('accueil/', views.home,),
    path('article/<int:id>', views.articleById, name= 'articleById'),
    path('article/', views.article,),
    path('article/view/<int:id_article>', views.view_article, name='aricle_view'),
    path('redirection/', views.redirect_view),
    path('', views.tpl, name='tpl'),
    path('addition/<int:nombre1>/<int:nombre2>', views.addition, name='addition'),
    path('first_contact/<str:nom>/<str:prenom>', views.first_contact, name='first_contact'),
]
