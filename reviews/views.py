from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from coachAPI.permissions import IsOwnerOrReadOnly
from .models import Review
from .serializers import ReviewSerializer

class ReviewList(generics.ListCreateAPIView):
    """
    List all reviews or create a review if user is logged in.
    The perform_create method is overridden to associate 
    the review with the logged in user.
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__following__followed__profile',
        'likes__owner__profile',
        'owner__profile',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a review.
    """
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Review.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')