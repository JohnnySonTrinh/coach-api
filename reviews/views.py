from rest_framework import generics, permissions
from coachAPI.permissions import IsOwnerOrReadOnly
from .models import Review
from .serializers import ReviewSerializer

class ReviewList(generics.ListCreateAPIView):
    """
    List all reviews or create a review if user is logged in.
    The perform_create method is overridden to associate 
    the review with the logged in user.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a review.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]