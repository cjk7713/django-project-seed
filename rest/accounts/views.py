from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer
from .permissions import IsStaffOrTargetUser
from rest_framework import generics
from rest_framework import authentication, permissions


class AccountsIdView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        resp = {
            'id': request.user.id
        }

        return Response(resp)


class AccountsRootView(generics.ListCreateAPIView):
    """
    Handles all requests to /accounts/
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    model = User

    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),