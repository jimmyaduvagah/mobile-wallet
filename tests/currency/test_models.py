from django.test import TestCase
from model_mommy import mommy

from mobile_wallet.currency.models import Currency


class TestCurrencyModel(TestCase):

    def test_create_currency(self):
        att = mommy.make(Currency, currency_iso_code="KES",country="Kenya")
        assert Currency.objects.count() == 1
        

    # def test_str_representation(self):
    #     att = mommy.make(
    #         Currency, title="God's plan lyrics", _create_files=True)
    #     assert str(att) == "God's plan lyrics"

    #     # delete the created folder
    #     year = timezone.now().year
    #     folder_path = '/tmp/{}'.format(year)
    #     if os.path.isdir(folder_path):
    #         shutil.rmtree(folder_path)
