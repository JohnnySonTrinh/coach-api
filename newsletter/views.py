from rest_framework import generics, permissions
from coachAPI.permissions import IsOwnerOrReadOnly
from newsletter.models import Newletter
from newsletter.serializers import NewletterSerializer

class NewletterListCreateView(generics.ListCreateAPIView):
    """
    API view for listing and creating newsletters.
    """
    queryset = Newletter.objects.all()
    serializer_class = NewletterSerializer
    permission_classes = [permissions.AllowAny]

class NewletterRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating and deleting newsletters.
    """
    queryset = Newletter.objects.all()
    serializer_class = NewletterSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
