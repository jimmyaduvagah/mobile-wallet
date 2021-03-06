"""Configuration for users app."""

from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Configuration class for users app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mobile_wallet.users'
