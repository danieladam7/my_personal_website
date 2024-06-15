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
