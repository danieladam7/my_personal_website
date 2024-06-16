from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import StartPageView, AllPostsView, SinglePostView, ContactView, SkillsView


class UrlsTest(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, StartPageView)

    def test_skills_url_is_resolved(self):
        url = reverse('skills')
        self.assertEqual(resolve(url).func.view_class, SkillsView)

    def test_all_posts_url_is_resolved(self):
            url = reverse('posts-page')
            self.assertEqual(resolve(url).func.view_class, AllPostsView)