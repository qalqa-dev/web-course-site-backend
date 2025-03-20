from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    imgUrl = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = [
            "id",
            "first_name",
            "middle_name",
            "last_name",
            "contact",
            "role",
            "imgUrl",
        ]

        def get_imgUrl(self, obj):
            return obj.img.url
