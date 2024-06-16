from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import StartPageView, AllPostsView, SinglePostView, ContactView, SkillsView


class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, StartPageView)
