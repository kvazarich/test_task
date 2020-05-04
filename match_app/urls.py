from django.urls import path

import match_app.views as views

urlpatterns = [
    path('<int:pk>/', views.match_detail),
    path('', views.match_list)
]