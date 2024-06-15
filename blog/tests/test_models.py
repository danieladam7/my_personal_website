from django.test import TestCase
from ..models import *


class TagModelTest(TestCase):

    def setUp(self):
        self.tag = Tag.objects.create(caption='Test-tag')

    def test_tag_caption(self):
        self.assertEqual(self.tag.caption, "Test-tag")

    def test_tag_str(self):
        self.assertEqual(str(self.tag), "Test-tag")


class AuthorModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name='Israel', last_name='Israeli', email_address='test@test.com')

    def test_author_first_name(self):
        self.assertEqual(self.author.first_name, 'Israel')

    def test_author_last_name(self):
        self.assertEqual(self.author.last_name, 'Israeli')

    def test_author_email_address(self):
        self.assertEqual(self.author.email_address, 'test@test.com')

    def test_author_full_name(self):
        self.assertEqual(self.author.full_name, 'Israel Israeli')

    def test_author_str(self):
        self.assertEqual(str(self.author), 'Israel Israeli')


class PostModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name='Israel', last_name='Israeli', email_address='test@test.com')

        self.tag1 = Tag.objects.create(caption='Tag 1')
        self.tag2 = Tag.objects.create(caption='Tag 2')

        self.post = Post.objects.create(
            title='Test Post',
            excerpt='Preview of Test Post',
            image='',
            date='15/06/2024',
            slug='test-post',
            content='Some test conent.',
            author=self.author,
            tags=self.post.tags.add(self.tag1, self.tag2)
        )

    def test_post_title(self):
        self.assertEqual(self.post.title, 'Test Post')

    def test_post_excerpt(self):
        self.assertEqual(self.post.excerpt, 'Preview of Test Post')

    def test_post_date(self):
        self.assertEqual(self.post.date, '15/06/2024')
