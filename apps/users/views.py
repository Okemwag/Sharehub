# Description: This file will contain the views for the users app.


from rest_framework import permissions, viewsets

from .models import CustomUser
from .serializers import CustomUserSerializer


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

