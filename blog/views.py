from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView, View
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from .models import Post
from .forms import CommentForm


class ContactView(TemplateView):
    template_name = "blog/contact.html"


class SkillsView(TemplateView):
    template_name = "blog/skills.html"


class BasePostListView(ListView):
    model = Post
    ordering = ["-date"]

    def get_queryset(self):
        return super().get_queryset()


class StartPageView(BasePostListView):
    template_name = "blog/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset[:3]


class AllPostsView(BasePostListView):
    template_name = "blog/all-posts.html"
    context_object_name = "all_posts"


class SinglePostView(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        context = self._get_context(post)
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            send_mail(
                'New Comment Awaiting Approval', (
                    f'A new comment by:{comment.user_name}\n'
                    f'Email:({comment.user_email}), is awaiting your approval.\n'
                    f'Comment: {comment.text}'
                ),            settings.DEFAULT_FROM_EMAIL,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            # Notify the user that the comment is awaiting approval
            messages.add_message(request, messages.INFO,
                                 f'Dear {comment.user_name},\n\nThank you for your comment on my blog post. Your comment is awaiting approval and will be visible once approved.')

            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        context = self._get_context(post, comment_form)
        return render(request, "blog/post-detail.html", context)

    def _get_context(self, post, comment_form=None):
        if comment_form is None:
            comment_form = CommentForm()
        # Using select_related and prefetch_related to reduce the number of queries
        post_tags = post.tags.all()
        comments = post.comments.all().order_by("-id")
        return {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.filter(approved=True).order_by("-id"),
        }
