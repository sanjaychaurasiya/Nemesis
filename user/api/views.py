from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegistrationSerializer
from rest_framework import generics
from .serializers import UserDetailSerializer
from django.contrib.auth.models import User


@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Registration Successfull"
            data['username'] = account.username
            data['email'] = account.email

            # JWT
            refresh = RefreshToken.for_user(user=account)
            data['token'] = {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }
        else:
            data = serializer.errors
        return Response(data)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
