from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from Authentication.serializers import SignupSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    req_data = request.data
    user_obj = SignupSerializer(data=req_data)
    if user_obj.is_valid():
        user = user_obj.save()
        token = Token.objects.create(user=user)
        return Response(data={'token': token.key})
    return Response(data=user_obj.errors, status=400)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data['username']
    password = request.data['password']
    user = User.objects.get(username=username)
    if user.check_password(raw_password=password):
        token, abc = Token.objects.get_or_create(user=user)
        return Response(data={'token': token.key})
    return Response(data={'msg': "wrong password"}, status=400)
