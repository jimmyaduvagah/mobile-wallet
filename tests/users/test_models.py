from django.test import TestCase
from model_mommy import mommy

from mobile_wallet.users.models import User


class TestUserModel(TestCase):

    def test_create_user(self):
        att = mommy.make(User, first_name="Jommy", last_name="Jones",
        email="testuser@asante.com", password="p@$$1%^&")
        assert User.objects.count() == 1
        

    # def test_str_representation(self):
    #     att = mommy.make(
    #         Currency, title="God's plan lyrics", _create_files=True)
    #     assert str(att) == "God's plan lyrics"

    #     # delete the created folder
    #     year = timezone.now().year
    #     folder_path = '/tmp/{}'.format(year)
    #     if os.path.isdir(folder_path):
    #         shutil.rmtree(folder_path)
