from django.test import TestCase
from blog.forms import CommentForm
from blog.models import Post, Author, Tag
from datetime import date
from unittest.mock import patch, Mock


@patch('django_recaptcha.fields.ReCaptchaField.clean', Mock(return_value=True))
class CommentFormTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name='Israel', last_name='Israeli', email_address='test@pageview.com')
        self.tag = Tag.objects.create(caption='Test-Tag')
        self.post = Post.objects.create(
            title='Test Post',
            excerpt='Preview of Test Post',
            image=None,
            date=date.today(),
            slug='test-post',
            content='Some test content.',
            author=self.author,
        )
        self.post.tags.add(self.tag)
        self.valid_data = {
            'user_name': 'Test User',
            'user_email': 'test@user.com',
            'text': 'This is a test comment.',
            'captcha': 'test'
        }

    def test_valid_form(self):
        form = CommentForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_invalid_email(self):
        invalid_data = self.valid_data.copy()
        invalid_data['user_email'] = 'invalid-email'
        form = CommentForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('user_email', form.errors)

    def test_missing_user_name(self):
        invalid_data = self.valid_data.copy()
        del invalid_data['user_name']
        form = CommentForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('user_name', form.errors)

    def test_missing_text(self):
        invalid_data = self.valid_data.copy()
        del invalid_data['text']
        form = CommentForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('text', form.errors)
