"""ccmProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from myapp import views


urlpatterns = [
	path('admin/', admin.site.urls),
	url(r'^$',views.index),
    url(r'^index/$', views.index),
	url(r'^boss/(\w+)/$',views.bossPage),
	url(r'^IEs/(\w+)/$',views.IEsPage),
	url(r'^foreman/(\w+)/$',views.foremanPage),
	url(r'^oper/(\w+)/$',views.operPage),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),

]
if settings.DEBUG :
	urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)
