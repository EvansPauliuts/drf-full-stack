from rest_framework import status

from core.fixtures.post import post
from core.fixtures.user import user


class TestUserViewSet:
    endpoint = '/api/user/'

    def test_list(self, client, user):
        pass

    def test_retrieve(self, client, user):
        pass

    def test_create(self, client, user):
        pass

    def test_update(self, client, user):
        pass
