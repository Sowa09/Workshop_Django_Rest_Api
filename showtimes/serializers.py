from rest_framework import serializers
from showtime.models import Cinema, Screening


class CinemaSerializer(serializers.ModelSerializer):
    movies = serializers.HyperlinkedRelatedField(many=True, slug_field='movies_details')

    class Meta:
        model = Cinema
        fields = ['__all__']


