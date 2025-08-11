from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token

from usuarios.models import Empleado

from django.shortcuts import get_object_or_404
    
@api_view(['POST'])
def signUp(request):
    
    # Crear registro
    serializer = UserSerializer(data=request.data)
    
    # Validar si es valido
    if serializer.is_valid():
        
        # Guardar usuario
        serializer.save()
        
        # Asignar usuario a variable
        user = Empleado.objects.get(username=request.data['username'])
        
        # Asignar contraseña cifrada
        user.set_password(request.data['password'])        

        # Guardar cambios
        user.save()
        
        # Crear token
        token = Token.objects.create(user=user)
        
        return Response({"token": token.key, "detalle": "Usuario Creado", "user": serializer.data})
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    
    # Obtener datos del usuario según el nombre de usuario
    user = get_object_or_404(Empleado, username=request.data["username"])
    
    # Validar contraseña
    if not user.check_password(request.data["password"]):
        return Response({ "detalle": "Error en la autenticación"}, status=status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)
    # Asignar instancia usuario
    serializer = UserSerializer(instance=user)
    
    return Response({"token": token.key, "detalle": "Autenticación satisfactoria", "user": serializer.data})

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def testToken(request):
    return Response({"{} está autenticado".format(request.user.email)})