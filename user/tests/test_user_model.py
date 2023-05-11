import pytest
from user.models import User


pytestmark = pytest.mark.django_db


class TestUserModel:
    def test_user_model_empty(self):
        count = User.objects.count()

        assert count == 0

    def test_user_model_add_user(self):
        c_user = User.objects.create_user(
            email='test@mail.com',
            username='test_user',
            password='testpass1234',
            first_name='test',
            last_name='user'
        )

        query = User.objects.all()
        count = query.count()
        user = query.get(pk=1)

        assert count == 1
        assert c_user.email == user.email
        assert c_user.username == 'test_user'
