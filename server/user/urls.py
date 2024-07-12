from django.urls import path
from .views import UserView, Authenticate

urlpatterns = [
    path('', UserView.as_view()),
    path('login/', Authenticate.as_view()),
    path('auth/', Authenticate.as_view())
]
