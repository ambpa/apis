from rest_framework import serializers

from user import serializer as user_serializer

from . import services


class ExcursionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    content = serializers.CharField()
    date_published = serializers.DateTimeField(read_only=True)
    date_last_update = serializers.DateTimeField(required=False)
    user = user_serializer.UserSerializer(read_only=True)
    minimum_user = serializers.IntegerField()
    maximum_user = serializers.IntegerField()
    end_booking_time = serializers.DateTimeField()
    time_excursion = serializers.DurationField()
    start_time_excursion = serializers.DateTimeField()
    meeting_place = serializers.CharField()
    price = serializers.DecimalField(max_digits=10,
                                     decimal_places=2
                                     )

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        return services.ExcursionDataClass(**data)


class ReservationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    content = serializers.CharField()
    date_published = serializers.DateTimeField(read_only=True)
    user = user_serializer.UserSerializer(read_only=True)
    excursion = ExcursionSerializer(read_only=True)

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        return services.ReservationDataClass(**data)