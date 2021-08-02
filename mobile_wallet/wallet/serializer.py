from rest_framework.serializers import ModelSerializer

from mobile_wallet.wallet.models import Wallet, AccountEntry, Transaction


class WalletSerializer(ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'


class AccountEntrySerializer(ModelSerializer):
    class Meta:
        model = AccountEntry
        fields = '__all__'


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
