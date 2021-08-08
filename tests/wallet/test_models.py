from django.db import transaction
from django.test import TestCase
from model_mommy import mommy

from mobile_wallet.currency.models import Currency
from mobile_wallet.users.models import User
from mobile_wallet.wallet.models import (Wallet, AccountEntry,
    Transaction)
from mobile_wallet.wallet.models import (create_cr_entry,
                                         create_dr_entry, post_transaction)
from mobile_wallet.currency.models import (get_user_currency_rate,
                                           get_usd_amount)


class TestWalletModel(TestCase):

    def setUp(self) -> None:
        super().setUp()
        mommy.make(Currency, currency_iso_code="KES",country="Kenya")
        mommy.make(User, first_name="Jommy", last_name="Jones",
            email="testuser@asante.com", password="p@$$1%^&")

    def test_create_wallet(self):
        owner = User.objects.get(email="testuser@asante.com")
        currency = Currency.objects.first()
        mommy.make(Wallet, owner=owner,currency_default=currency)
        assert Wallet.objects.count() == 1
        

    # def test_str_representation(self):
    #     att = mommy.make(
    #         Currency, title="God's plan lyrics", _create_files=True)
    #     assert str(att) == "God's plan lyrics"

    #     # delete the created folder
    #     year = timezone.now().year
    #     folder_path = '/tmp/{}'.format(year)
    #     if os.path.isdir(folder_path):
    #         shutil.rmtree(folder_path)




class TestTransactionModel(TestCase):

    def setUp(self) -> None:
        super().setUp()

        mommy.make(Currency, currency_iso_code="KES",country="Kenya")
        mommy.make(User, first_name="Jommy", last_name="Jones",
            email="testuser1@asante.com", password="p@$$1%^&")
        mommy.make(User, first_name="Kate", last_name="Jones",
            email="testuserKate@asante.com", password="p@$$1%^&")
        owner1 = User.objects.get(email="testuser1@asante.com")
        owner2 = User.objects.get(email="testuserKate@asante.com")
        currency = Currency.objects.first()
        mommy.make(Wallet, owner=owner1,currency_default=currency)
        mommy.make(Wallet, owner=owner2,currency_default=currency)


    def test_create_transaction(self):
        user_wallet_1 = Wallet.objects.get(owner__email="testuser1@asante.com")
        user_wallet_2 = Wallet.objects.get(owner__email="testuserKate@asante.com")
        rate = get_user_currency_rate(user_wallet_1.currency_default)
        usd_amount = get_usd_amount(rate, 1500)
        dr_entry = create_dr_entry(user_wallet_2, 1500, 'D')
        cr_entry = create_cr_entry(user_wallet_1, 1500, 'T')

        mommy.make(Transaction, dr_entry=dr_entry, cr_entry=cr_entry)
        assert Transaction.objects.count() == 1

