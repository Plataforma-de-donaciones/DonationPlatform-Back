from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Users
from .serializers import UsersSerializer
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
import logging
from django.contrib.auth.hashers import make_password

class UsersListView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]

class UsersCreateView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Obtiene la contraseña en texto plano del cuerpo JSON de la solicitud
        plain_password = self.request.data.get('user_password', '')

        # Encripta la contraseña utilizando make_password
        hashed_password = make_password(plain_password)

        request.data['user_password'] = hashed_password

        # Crea el usuario utilizando el serializador
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Devuelve una respuesta HTTP 201 (Creación exitosa)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UsersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
       # Implementación de eliminación lógica
       instance.user_state = 0
       instance.erased_at = timezone.now()  # Marcar la fecha de eliminación
       instance.save()

class UserSearchView(generics.ListAPIView):
    serializer_class = UsersSerializer  # Asegúrate de tener un serializador de usuarios configurado

    def post(self, request):
        user_name = self.request.data.get('user_name', '')  # Obtiene el valor del nombre de usuario del cuerpo JSON
        user_email = self.request.data.get('user_email', '')  # Obtiene el valor del correo electrónico del cuerpo JSON
        
        logger = logging.getLogger(__name__)
        logger.debug("Valor de username: %s", user_name)
        logger.debug("Valor de email: %s", user_email)
       
        queryset = Users.objects.filter(
            Q(user_name__exact=user_name) | Q(user_email__exact=user_email)
        )
        logger.debug("Consulta sql generada:", str(queryset.query))
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
