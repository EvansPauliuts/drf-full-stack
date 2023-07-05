import pytest

from core.comment.models import Comment
from core.fixtures.post import post
from core.fixtures.user import user


@pytest.fixture
def comment(db, user, post):
    return Comment.objects.create(author=user, post=post, body='Test Comment Body')
