from rest_framework import serializers

from .models import Aup, Reservation


class AupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aup
        fields = ('creation_time', 'validity_time_since', 'validity_time_to', 'requests')


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ('airspace_structure',
                  'lower_limit',
                  'upper_limit',
                  'activation_date',
                  'deactivation_date',
                  'activation_time',
                  'deactivation_time',
                  )
