from rest_framework import serializers

from .models import ParseCnab


class ParseCnabSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParseCnab
        fields = "__all__"

        extra_kwargs = {'id': {'read_only': True}}
