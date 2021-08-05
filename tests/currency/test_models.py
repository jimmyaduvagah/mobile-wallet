import os
import shutil

from django.test import TestCase
from django.utils import timezone
from model_mommy import mommy

from mobile_wallet.currency.models import Currency


class TestCurrencyModel(TestCase):

    def test_get_directory(self):
        att = mommy.make(Currency, title="Freaky Friday", _create_files=True)
        created = att.created
        assert path == "{year}/{month}/{day}/{att_id}_{filename}".format(
            year=created.strftime('%Y'), month=created.strftime('%m'),
            day=created.strftime('%d'), att_id=att.id,
            filename='freaky_friday_lil_dicky.mp3'
        )

    def test_str_representation(self):
        att = mommy.make(
            Currency, title="God's plan lyrics", _create_files=True)
        assert str(att) == "God's plan lyrics"

        # delete the created folder
        year = timezone.now().year
        folder_path = '/tmp/{}'.format(year)
        if os.path.isdir(folder_path):
            shutil.rmtree(folder_path)
