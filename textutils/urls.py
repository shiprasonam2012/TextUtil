"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views
from . import views2
from django.contrib import admin
from django.urls import path

#video 7 codeWith Harry
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name = 'index'),
    path('analyze', views.analyze, name= 'analyze'),
    path('replaceText', views2.index, name = 'index'),
    path('analyze2', views2.analyze, name= 'analyze'),
    path('textOp2Strings', views.index1, name='index'),
    path('analyze3', views.textOp2Strings, name= 'analyze')

    # path('textUtil',)
    # path('removePuntuation',views.removepunc, name = 'removepunc'),
    # path('captalizedFirst',views.capfirst, name = 'capfirst'),
    # path('newlineremover',views.newlineremover, name = 'newlineremover'),
    # path('spaceremover',views.spaceremover, name = 'spaceremover'),
    # path('charcount',views.charcount, name = 'charcount'),
    # path('usingtempl',views.usingtempl, name = 'usingtempl'),
    
    

]
