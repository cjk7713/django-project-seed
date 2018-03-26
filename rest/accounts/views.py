from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer
from .permissions import IsStaffOrTargetUser
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets
from oauth2_provider.contrib.rest_framework import IsAuthenticatedOrTokenHasScope


class AccountCreateView(generics.CreateAPIView):
    """
    Creates a new account.
    """
    permission_classes = (permissions.AllowAny,)
    model = User
    serializer_class = UserSerializer


class AccountView(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Returns the logged in user.

    patch:
    Updates the logged in user.

    put:
    Updates the logged in user.

    delete:
    Deletes the logged in user.
    """
    model = User
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrTokenHasScope, ]
    required_scopes = ['write', 'read']

    def get_object(self):
        return self.request.user
    
        def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            if "password" in request.data:
                instance.set_password(request.data['password'])
                instance.save()
            else:
                serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
