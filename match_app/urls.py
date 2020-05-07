from django.conf.urls import url
from django.urls import include
from rest_framework import routers

import match_app.views as views

router = routers.DefaultRouter()

router.register(r'', views.MatchViewSet, basename='MatchViewSet')

urlpatterns = [
    url(r'^', include(router.urls))
]