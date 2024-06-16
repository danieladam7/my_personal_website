from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from ..models import Post, Author, Tag, Comment
from datetime import date
from unittest.mock import patch


class ContactViewTest(TestCase):
    def test_contact_view_status_code(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_contact_view_template(self):
        response = self.client.get(reverse('contact'))
        self.assertTemplateUsed(response, 'blog/contact.html')


class SkillsViewTest(TestCase):
    def test_skills_view_status_code(self):
        response = self.client.get(reverse('skills'))
        self.assertEqual(response.status_code, 200)

    def test_skills_view_template(self):
        response = self.client.get(reverse('skills'))
        self.assertTemplateUsed(response, 'blog/skills.html')


class StartPageViewTest(TestCase):
    def setUp(self):
        self.patcher = patch('django.core.files.storage.Storage.save')
        self.mock_save = self.patcher.start()
        self.mock_save.return_value = 'test_image.jpg'

        self.author = Author.objects.create(
            first_name='Israel', last_name='Israeli', email_address='test@pageview.com')
        self.tag = Tag.objects.create(caption='Test-Tag')
        self.image = SimpleUploadedFile(
            name='test_image.jpg', content=b'file_content', content_type='image/jpeg')
        for i in range(5):
            post = Post.objects.create(
                title=f'Test Post {i}',
                excerpt='Preview of Test Post',
                image=self.image,
                date=date.today(),
                slug=f'test-post-{i}',
                content='Some test content.',
                author=self.author,
            )
            post.tags.add(self.tag)

    def tearDown(self):
        self.patcher.stop()

    def test_start_page_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_start_page_view_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_start_page_view_context_contains_posts(self):
        response = self.client.get(reverse('home'))
        self.assertIn('posts', response.context)

    def test_start_page_view_context_posts_length(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(len(response.context['posts']), 3)


class AllPostsViewTest(TestCase):
    def setUp(self):
        self.patcher = patch('django.core.files.storage.Storage.save')
        self.mock_save = self.patcher.start()
        self.mock_save.return_value = 'test_image.jpg'

        self.author = Author.objects.create(
            first_name='Israel', last_name='Israeli', email_address='test@pageview.com')
        self.tag = Tag.objects.create(caption='Test-Tag')
        self.image = SimpleUploadedFile(
            name='test_image.jpg', content=b'file_content', content_type='image/jpeg')
        for i in range(5):
            post = Post.objects.create(
                title=f'Test Post {i}',
                excerpt='Preview of Test Post',
                image=self.image,
                date=date.today(),
                slug=f'test-post-{i}',
                content='Some test content.',
                author=self.author,
            )
            post.tags.add(self.tag)

    def test_all_posts_view_status_code(self):
        response = self.client.get(reverse('posts-page'))
        self.assertEqual(response.status_code, 200)

    def test_all_posts_view_template(self):
        response = self.client.get(reverse('posts-page'))
        self.assertTemplateUsed(response, 'blog/all-posts.html')

    def test_all_posts_view_context(self):
        response = self.client.get(reverse('posts-page'))
        self.assertIn('all_posts', response.context)

    def test_all_posts_view_context_length(self):
        response = self.client.get(reverse('posts-page'))
        self.assertEqual(len(response.context['all_posts']), 5)


class SinglePostViewTest(TestCase):
    def setUp(self):
        self.patcher = patch('django.core.files.storage.Storage.save')
        self.mock_save = self.patcher.start()
        self.mock_save.return_value = 'test_image.jpg'

        self.author = Author.objects.create(
            first_name='Israel', last_name='Israeli', email_address='test@pageview.com')
        self.tag = Tag.objects.create(caption='Test-Tag')
        self.image = SimpleUploadedFile(
            name='test_image.jpg', content=b'file_content', content_type='image/jpeg')
        for i in range(5):
            post = Post.objects.create(
                title=f'Test Post {i}',
                excerpt='Preview of Test Post',
                image=self.image,
                date=date.today(),
                slug=f'test-post-{i}',
                content='Some test content.',
                author=self.author,
            )
            post.tags.add(self.tag)
