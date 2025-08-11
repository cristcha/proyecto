from rest_framework import serializers
from .models import Empleado

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Empleado
        fields = ['identificacion', "username", "first_name", "last_name", "email", "celular", "password", "fecha_nacimiento", "id_perfil"]