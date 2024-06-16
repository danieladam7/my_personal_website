from django.urls import path

from .views import StartPageView, AllPostsView, SinglePostView, ContactView, SkillsView

urlpatterns = [
    path("", StartPageView.as_view(), name="home"),
    path("skills", SkillsView.as_view(), name="skills"),
    path("posts/<slug:slug>", SinglePostView.as_view(),
         name="post-detail-page"),
    path("posts", AllPostsView.as_view(), name="posts-page"),
    path('contact/', ContactView.as_view(), name='contact')
]
