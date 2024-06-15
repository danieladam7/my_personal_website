from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from ..models import Post, Author, Tag, Comment
from datetime import date


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
                content='Some test conent.',
                author=self.author,
            )
            post.tags.add(self.tag)


    def test_start_page_view_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_start_page_view_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_start_page_view_context_contains_posts(self):
        response = self.client.get(reverse('index'))
        self.assertIn('posts', response.context)