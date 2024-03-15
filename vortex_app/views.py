from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
    
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {
            'user': str(request.user),
            'email': str(request.user.email),
            'first_name': str(request.user.first_name),
            'last_name': str(request.user.last_name),
        }
        return Response(content)
