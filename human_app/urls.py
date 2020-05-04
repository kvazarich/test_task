from django.conf.urls import url
from django.urls import include
from rest_framework import routers

import human_app.views as views

router = routers.DefaultRouter()

router.register(r'', views.HumansViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]