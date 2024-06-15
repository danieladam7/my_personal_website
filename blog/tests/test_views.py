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
