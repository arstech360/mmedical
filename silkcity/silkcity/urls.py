"""silkcity URL Configuration

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
from django.contrib import admin
from django.urls import path
from .views import Login,signup,table,billing,signIn,postsignIn,postserial,doctor,adddoctor,dashboard,adoctor,deletedoc,slip,paystatement,billpay,testinfo,deletetest
from django.urls import re_path as url
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',signIn,name='index'),
path('', signIn),
url('login',Login,name='login'),
url('signup',signup,name='signup'),
url('table',table,name='table'),
url('billing',billing,name='billing'),
path('postsignIn/',postsignIn,name='postsignIn'),
path('postserial/',postserial,name='postserial'),
path('doctor/',doctor,name='doctor'),
path('adddoctor/',adddoctor,name='adddoctor'),
path('dashboard/',dashboard,name='dashboard'),
path('adoctor/',adoctor,name='adoctor'),
path('deletedoc<docid>/',deletedoc,name='deletedoc'),
path('slip/',slip,name='slip'),
path('paystatement/',paystatement,name='paystatement'),
path('billpay/',billpay,name='billpay'),
path('testinfo/',testinfo,name='testinfo'),
path('deletetest<docid1>/',deletetest,name='deletetest'),



]
