from rest_framework import serializers
from .models import WheelSpecification, BogieCheckSheet

class WheelSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelSpecification
        fields = '__all__'

class BogieCheckSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieCheckSheet
        fields = '__all__'
