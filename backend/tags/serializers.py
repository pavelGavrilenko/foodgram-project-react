from rest_framework import serializers

from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'name',
            'color',
            'slug'
        )
        lookup_field = 'id'
        extra_kwargs = {'url': {'lookup_field': 'id'}}