from .models import *
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'fam', 'name', 'otc', 'phone']

class CoordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']

class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['data', 'title']

class PerevalSerializer(WritableNestedModelSerializer):
    user = UsersSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    images = ImageSerializer(many=True)
    class Meta:
        model = Pereval
        fields = ['id', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'user', 'coords', 'level', 'images', 'status']
        read_only_fields = ['id']