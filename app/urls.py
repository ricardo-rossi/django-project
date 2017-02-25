"""sayhello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [

    # handles requests for '/'
    # Routes to index() controller method on views.py
    url(r'^$', views.index),

    # handles requests for '/main'
    # Routes to main() controller method on views.py
    url(r'^main$', views.main),

    # handles requests for '/login'
    # Routes to login() controller method on views.py
    url(r'^login$', views.login),

    # handles requests for '/register'
    # Routes to register() controller method on views.py
    url(r'^register', views.register),

    # handles requests for '/appointments'
    # Routes to appointments() controller method on views.py
    url(r'^appointments', views.appointments),

    # Example of a url route using parameters
    # This route will match any of these /users/1  /users/2 but not /users/bob
    # url(r'^users/(?P<user_id>[\d]+$)', views.user)

]
