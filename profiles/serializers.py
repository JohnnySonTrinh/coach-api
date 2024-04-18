from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return obj.owner == request.user

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
            'is_owner'
        ]