from rest_framework import generics, permissions
from coachAPI.permissions import IsOwnerOrReadOnly
from likes.models import Like
from likes.serializers import LikeSerializer

class LikeList(generics.ListCreateAPIView):
    # List all likes or create a new like.
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    # Retrieve, update or delete a like.
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]