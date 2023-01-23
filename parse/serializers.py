from rest_framework import serializers

from .models import ParseCnab


class ParseCnabSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParseCnab
        fieds = "__all__"

        read_only_fields = [
            "type_of_transaction"
            "value",
            "CPF",
            "card",
            "hour",
            "owner",
            "store_name"
        ]

        extra_kwargs = {'file': {'write_only': True}}
