from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    # Serializer for the Review model
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return obj.owner == request.user

    class Meta:
        model = Review
        fields = [
            'id',
            'owner',
            'title',
            'content',
            'github_repo',
            'live_website',
            'image',
            'created_at',
            'updated_at'
        ]