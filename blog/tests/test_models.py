from datetime import date
from django.test import TestCase
from ..models import Post, Author, Tag, Comment
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest.mock import patch, mock_open


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
    @patch('django.core.files.storage.Storage.save')
    @patch('django.core.files.storage.Storage.open')
    @patch('django.core.files.storage.Storage.exists')
    def setUp(self, mock_exists, mock_open, mock_save):
        mock_save.return_value = 'test_image.jpg'
        mock_exists.return_value = False
        mock_open.return_value = mock_open(read_data=b'file_content')

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

    @patch('django.core.files.storage.Storage.open', new_callable=mock_open, read_data=b'file_content')
    def test_image_upload(self, mock_open):
        with self.post.image.open():
            self.assertEqual(self.post.image.read(), b'file_content')

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


class CommentModelTest(TestCase):
    @patch('django.core.files.storage.Storage.save')
    def setUp(self, mock_save):
        mock_save.return_value = 'test_image.jpg'
        self.author = Author.objects.create(
            first_name='Israel', last_name='Israeli', email_address='test@test.com')

        self.tag = Tag.objects.create(caption='Test-Comment-Tag')
        self.image = SimpleUploadedFile(
            name='test_image.jpg', content=b'file_content', content_type='image/jpeg')

        self.post = Post.objects.create(
            title='Test Post',
            excerpt='Preview of Test Post',
            image=self.image,
            date=date.today(),
            slug='test-post',
            content='Some test conent.',
            author=self.author,
        )

        self.post.tags.add(self.tag)

        self.comment = Comment.objects.create(
            user_name='Comment Tester',
            user_email='comment@tester.com',
            text='This is a test comment.',
            post=self.post,
            approved=False
        )

    def test_user_name(self):
        self.assertEqual(self.comment.user_name, 'Comment Tester')

    def test_user_email(self):
        self.assertEqual(self.comment.user_email, 'comment@tester.com')

    def test_text(self):
        self.assertEqual(self.comment.text, 'This is a test comment.')

    def test_post(self):
        self.assertEqual(self.comment.post, self.post)

    def test_approved(self):
        self.assertFalse(self.comment.approved)
