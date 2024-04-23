from django.db import IntegrityError
from rest_framework import serializers
from .models import Newletter

class NewletterSerializer(serializers.ModelSerializer):
    """
    Serializer for the Newletter model.
    """
    class Meta:
        model = Newletter
        fields = ['id', 'email', 'created_at', 'is_active']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                {'detail': 'You have already subscribed to the newsletter.'}
            )

