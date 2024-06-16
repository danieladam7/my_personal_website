from django.test import TestCase
from blog.forms import CommentForm
from blog.models import Post, Author, Tag
from datetime import date
from unittest.mock import patch


class CommentFormTest(TestCase):
    @patch('django_recaptcha.fields.ReCaptchaField.clean', return_value=True)
    def setUp(self, mock_clean):
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

    @patch('django_recaptcha.fields.ReCaptchaField.clean', return_value=True)
    def test_valid_form(self, mock_clean):
        form = CommentForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    @patch('django_recaptcha.fields.ReCaptchaField.clean', return_value=True)
    def test_invalid_email(self, mock_clean):
        invalid_data = self.valid_data.copy()
        invalid_data['user_email'] = 'invalid-email'
        form = CommentForm(data=invalid_data)
        self.assertIn('user_email', form.errors)

    @patch('django_recaptcha.fields.ReCaptchaField.clean', return_value=True)
    def test_missing_user_name(self, mock_clean):
        invalid_data = self.valid_data.copy()
        del invalid_data['user_name']
        form = CommentForm(data=invalid_data)
        self.assertIn('user_name', form.errors)
