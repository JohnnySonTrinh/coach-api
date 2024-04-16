from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    # Serializer for the Profile model
    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'name',
            'github',
            'linkedin',
            'bio',
            'image',
            'created_at',
            'updated_at',
        ]