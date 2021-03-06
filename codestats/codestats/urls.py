"""codestats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin
from sapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', views.register),
    url(r'^login/', views.login_app),
    url(r'^$', views.index),
    url(r'^logout/', views.logout_app),
    url(r'^recommend/', views.recommend),
    url(r'^charts/', views.charts),
    url(r'^heatmap/', views.heatmap),
    url(r'^airquality/', views.airquality),
    url(r'^cropchart/', views.cropchart),
    url(r'^index/', views.index),
    url(r'^chatbot/', views.chatbot),
    url(r'^compare/', views.compare),
    url(r'^to_do/', views.to_do),
    url(r'^gallery/', views.gallery),
    url(r'^reminders/', views.reminders),
    url(r'^send_sms/', views.send_sms),
    url(r'^facedetect/',views.facedetect),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
