from django.db.models import Count
from rest_framework import generics, filters
from coachAPI.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer

class ProfileList(generics.ListCreateAPIView):
    # List all profiles or create a new profile
    queryset = Profile.objects.annotate(
        reviews_count=Count('owner__review', distinct=True),
        followers_count=Count('owner__followers', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'reviews_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    # Retrieve, update or delete a profile
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        reviews_count=Count('owner__review', distinct=True),
        followers_count=Count('owner__followers', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer