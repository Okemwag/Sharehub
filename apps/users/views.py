# Description: This file will contain the views for the users app.


from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CustomUserSerializer
from .models import CustomUser


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    Allow GET and POST requests.
    """
    queryset = CustomUser.objects.all().order_by("-date_joined")
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "email"
    lookup_value_regex = "[^/]+"

