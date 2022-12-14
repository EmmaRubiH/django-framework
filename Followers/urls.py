from django.urls import path
from Followers import views

urlpatterns = [
    path('Followers/', views.FollowerList.as_view()),
    path('followers/<int:pk>/', views.FollowerDetail.as_view())
]
