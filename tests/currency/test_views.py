import os

from django.conf import settings
from django.urls import reverse
from rest_framework.test import APITestCase

from tests.utils import LoggedInMixin


class ServeMediaViewTests(LoggedInMixin, APITestCase):

    def setUp(self):
        super(ServeMediaViewTests, self).setUp()
        self.filename = 'test.txt'
        self.path = os.path.join(
            settings.MEDIA_ROOT, self.filename)
        with open(self.path, 'w') as f:
            f.write('test')

    def tearDown(self):
        os.unlink(self.path)
        super(ServeMediaViewTests, self).tearDown()

    def test_serve_media(self):
        url = reverse(
            'serve_media', kwargs={'path': 'test.txt'})
        resp = self.client.get(url)
        assert resp.status_code == 200
        assert resp['Content-Disposition'] == 'attachment; filename="b\'test.txt\'";' \
                                              ' filename*=UTF-8\'\'test.txt'
