"""Module for currency serializers."""

from rest_framework.serializers import ModelSerializer

from mobile_wallet.currency.models import Currency


class CurrencySerializer(ModelSerializer):
    """Class definition for Currency serializers."""

    class Meta:
        """Class Meta for Currency serializers."""

        model = Currency
        fields = '__all__'
