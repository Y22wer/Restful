"""Restful URL Configuration

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
import imp
from django.contrib import admin
from django.urls import path,include

from RESTful_test.views import AuthorView,AuthorDtailView 
from RESTful_test.views import PublishView,PublishDtailView ,PublishView_set
urlpatterns = [
    path('admin/', admin.site.urls),
    path("stu/",include("rest.urls")),
    
    path("aut/",AuthorView.as_view() ),
    path("aut/<int:id>",AuthorDtailView.as_view() ),  #最基礎demo
    
    path("pub/",PublishView.as_view() ),
    path("pub/<int:id>",PublishDtailView.as_view() ),#進階試圖demo
    
    #高階試圖demo
    path("pub_Viewset/",PublishView_set.as_view({'get':'list', 'post':'create'}) ), #requset方法對應 + 執行類方法 
    path("pub_Viewset/<int:id>",PublishView_set.as_view( {"get":"retrieve" ,"put":"update","delete":"delete"} )    ),
    
]