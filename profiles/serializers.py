from rest_framework import serializers
from .models import Profile
from followers.models import Follower

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return obj.owner == request.user

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user,
                followed=obj.owner
            ).first()
            return following.id if following else None
        return None
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
            'is_owner',
            'following_id'
        ]
    