"""Define Configuration for wallet app."""

from django.apps import AppConfig


class WalletConfig(AppConfig):
    """Configuration class for users app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mobile_wallet.wallet'
