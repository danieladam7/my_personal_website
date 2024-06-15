from django.test import TestCase
from ..models import *


class TagModelTest(TestCase):

    def setUp(self):
        self.tag = Tag.object.create(captio='Test-tag')

    def test_tag_creation(self):
        self.assertEqual(self.tag.caption, "Test-tag")

    def test_tag_str(self):
        self.assertEqual(str(self.tag), "Test-tag")
