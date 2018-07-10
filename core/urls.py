from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^speech/', views.giveresponse, name="response"),
    url(r'^', views.home, name="same"),
]
