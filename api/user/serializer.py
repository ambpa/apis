from rest_framework import serializers

from . import services


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    is_staff = serializers.BooleanField()

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        return services.UserDataClass(**data)

class BlackListedTokenSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    token = serializers.CharField(read_only=True)
    timestamp = serializers.DateTimeField(read_only=True)
    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        return services.BlackListedTokenDataClass(**data)
