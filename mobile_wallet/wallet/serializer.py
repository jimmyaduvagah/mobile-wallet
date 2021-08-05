"""Define serializers for wallet app."""

from rest_framework.serializers import ModelSerializer

from mobile_wallet.wallet.models import Wallet, AccountEntry, Transaction


class WalletSerializer(ModelSerializer):
    """Wallet Serializer class."""

    class Meta:
        """Wallet Serializer meta class."""

        model = Wallet
        fields = '__all__'


class AccountEntrySerializer(ModelSerializer):
    """AccountEntry Serializer class."""

    class Meta:
        """AccountEntry Serializer meta class."""

        model = AccountEntry
        fields = '__all__'


class TransactionSerializer(ModelSerializer):
    """Transaction Serializer class."""

    class Meta:
        """Transaction Serializer meta class."""

        model = Transaction
        fields = '__all__'
