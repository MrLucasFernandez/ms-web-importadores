from rest_framework import serializers
from .models import Importador

class ImportadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Importador
        fields = '__all__'