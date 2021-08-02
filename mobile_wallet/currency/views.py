from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from mobile_wallet.currency.serializer import CurrencySerializer, Currency


class CurrencyViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing User instances.
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()
