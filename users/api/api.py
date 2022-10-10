from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from users.models import User
from users.api.serializers import UserSerializer, UserListSerializer

@api_view(['GET', 'POST'])
def user_api_view(request):

    if request.method == 'GET':
        users = User.objects.all().values('id', 'username', 'email', 'password', 'name')
        users_serializer = UserListSerializer(users, many = True)
        return Response(users_serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status = status.HTTP_201_CREATED)
        return Response(user_serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, id):
    user = User.objects.filter(id = id).first()
    if user:
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status = status.HTTP_200_OK)

        elif request.method == 'PUT':
            user_serializer = UserSerializer(user, data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status = status.HTTP_200_OK)
            return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            user.delete()
            return Response({'message': 'usuario eliminado'}, status = status.HTTP_200_OK)
    return Response({ 'message': 'No se encontro al usuario'}, status = status.HTTP_400_BAD_REQUEST)
