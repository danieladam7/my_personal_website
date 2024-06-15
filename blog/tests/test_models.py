from datetime import date
from django.test import TestCase
from ..models import *
from django.core.files.uploadedfile import SimpleUploadedFile
<< << << < HEAD
== == == =
>>>>>> > bfb22a6264c1d9aac70ea8c9bf9da4b79066902b


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
        self.image = SimpleUploadedFile(
            name='test_image.jpg', content=b'file_content', content_type='image/jpeg')

        self.post = Post.objects.create(
            title='Test Post',
            excerpt='Preview of Test Post',
            image=self.image,
            date=date.today(),
            image=self.image
            date='15/06/2024',
            >>>>>> > bfb22a6264c1d9aac70ea8c9bf9da4b79066902b
            slug='test-post',
            content='Some test conent.',
            author=self.author,
        )

        self.post.tags.add(self.tag1, self.tag2)

    def test_post_title(self):
        self.assertEqual(self.post.title, 'Test Post')

    def test_post_excerpt(self):
        self.assertEqual(self.post.excerpt, 'Preview of Test Post')

    def test_image_name(self):
        self.assertEqual(self.image.name, 'test_image.jpg')

    def test_image_upload(self):
        self.image.open()
        self.assertEqual(self.post.image.read(), b'file_content')
        self.image.close()

    def test_post_date(self):
        self.assertEqual(self.post.date, date.today())

    def test_post_slug(self):
        self.assertEqual(self.post.slug, 'test-post')

    def test_post_content(self):
        self.assertEqual(self.post.content, 'Some test conent.')

    def test_post_author(self):
        self.assertEqual(self.post.author, self.author)

    def test_post_tag1(self):
        self.assertIn(self.tag1, self.post.tags.all())

    def test_post_tag2(self):
        self.assertIn(self.tag2, self.post.tags.all())

    def test_post_str(self):
        self.assertEqual(str(self.post), 'Test Post')
