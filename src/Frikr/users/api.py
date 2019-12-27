from django.contrib.auth.models import User
from users.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from users.permissions import UserPermission

class UserListAPI(APIView):

    permission_classes = (UserPermission,)

    def get(self, request):
        self.check_permissions(request)
        paginator = PageNumberPagination()
        users = User.objects.all()
        paginator.paginate_queryset(users, request)
        serializer = UserSerializer(users, many=True)
        serializer_users = serializer.data #list of dicts

        return paginator.get_paginated_response(serializer_users)

    def post(self, request):
        self.check_permissions(request)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPI(APIView):

    permission_classes = (UserPermission,)

    def get(self, request, pk):
        self.check_permissions(request)
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)

        return Response(serializer.data)

    def put(self, request, pk):
        self.check_permissions(request)
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            updated_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        self.check_permissions(request)
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        