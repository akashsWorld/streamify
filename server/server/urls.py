from django.urls import path, include

urlpatterns = [
    path('user/', include('user.urls')),
    path('media/', include('media.urls'))
]
