"""User app views"""
from django.shortcuts import get_object_or_404
from rest_framework import viewsets , status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.serializers import CustomUserSerializer , UserListSerializer , UpdateUserSerializer
from users.models import User


class UserViewSet(viewsets.GenericViewSet):
    model = User
    serializer_class = CustomUserSerializer
    list_serializer_class = UserListSerializer
    queryset = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects\
                            .filter(is_active=True)\
                            .values('id', 'username', 'email', 'first_name', 'location', 'employer','user_type','title')
        return self.queryset
    
    
    def list(self, request):
        users = self.get_queryset()
        users_serializer = self.list_serializer_class(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = UpdateUserSerializer(user)
        return Response(user_serializer.data)
    
    def update(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = UpdateUserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'User information updated correctly'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'There are errors in the update',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
