from rest_framework import serializers
from .models import SampleTest

class SampleTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleTest
        fields = '__all__'