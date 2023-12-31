from django.shortcuts import render
from rest_framework import generics, permissions, status
from django.db.models import Q
from .models import Moderator
from .serializers import ModeratorSerializer
from django.utils import timezone
from rest_framework.response import Response
from users.models import Users
from rest_framework.views import APIView

class ModeratorListView(generics.ListCreateAPIView):
    queryset = Moderator.objects.all()
    serializer_class = ModeratorSerializer
    permission_classes = [permissions.IsAuthenticated]
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        data_with_user_info = []
        for moderator_data in response.data:
            user_id = moderator_data.get('user')
            try:
                user = Users.objects.get(id=user_id)
                user_info = {
                    'user_id': user.id,
                    'user_name': user.user_name,
                    'user_email': user.user_email,
                }
                moderator_data['user_info'] = user_info
            except Users.DoesNotExist:
                moderator_data['user_info'] = None

            data_with_user_info.append(moderator_data)

        response.data = data_with_user_info
        return response

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user')
        start_date = request.data.get('start_date')
        organization_id = request.data.get('organization_id')
        moderator_state = request.data.get('moderator_state')

        try:
            user = Users.objects.get(id=user_id)
        except Users.DoesNotExist:
            return Response({'message': 'El usuario no existe'}, status=status.HTTP_400_BAD_REQUEST)

        if user.user_state != 1:
            return Response({'message': 'El usuario debe estar activo para crear un moderador'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ModeratorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Moderator.objects.all()
    serializer_class = ModeratorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
       instance.moderator_state = 0
       instance.erased_at = timezone.now()  
       instance.save()


class ModeratorSearchView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        search_param = request.data.get('search', '')

        if search_param:
            moderators = Moderator.objects.filter(
                Q(user__user_name__icontains=search_param) |
                Q(user__user_email__icontains=search_param)
            )

            serializer = ModeratorSerializer(moderators, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'message': 'Ingrese un parámetro de búsqueda válido.'}, status=status.HTTP_400_BAD_REQUEST)
