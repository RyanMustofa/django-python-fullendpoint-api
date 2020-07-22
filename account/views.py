from django.shortcuts import render
from django.contrib.auth import get_user_model
from account.serializers import AccountCreateSerializers, AccountSerializers
from rest_framework import decorators,response,permissions,status
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.AllowAny])
def register(request):
    serializer = AccountCreateSerializers(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return response.Response(res,status.HTTP_201_CREATED)
    else:
        return response.Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])
def users(request):
    serializer = AccountSerializers(data=request.user)
    if serializer.is_valid():
        account = serializer.save()
        if account:
            return Response(serializer.data)
    return Response(serializer.errors,status.HTTP_401_UNAUTHORIZED)
