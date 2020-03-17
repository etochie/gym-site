from time import time
import pytest

from pytils.translit import slugify
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestModels:

    def test_article_slug_gen(self):
        title = 'Article title for test'

        test_time = str(int(time()))
        test_slug = '{}-{}'.format(slugify(title[:20]), test_time)

        article = mixer.blend('articles.Article', title=title)
        assert article.slug == test_slug



       
