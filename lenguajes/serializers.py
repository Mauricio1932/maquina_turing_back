from rest_framework import serializers
from lenguajes.models import Conjunto

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conjunto
        fields = ['conjuntos']

