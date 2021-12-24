from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import registration_view, UserDetails, UserList    # logout_view


urlpatterns = [
    path('register/', registration_view, name='register'),
    path('user/<int:pk>', UserDetails.as_view(), name='user_details'),
    path('user/', UserList.as_view(), name='user_list'),

    # JWT Part.
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
