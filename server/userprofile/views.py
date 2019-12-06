from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Profile
from . serializers import ProfileSerializer
from django.contrib.auth.models import User

from . serializers import ProfileSerializer


#Profile View
class ProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        profileData = [Profile.objects.get(user__username=request.user)]
        serializer = ProfileSerializer(profileData, many=True)
        return Response(serializer.data)


