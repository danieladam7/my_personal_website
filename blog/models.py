from django.db import models
from django.core.validators import MinLengthValidator

# Tag model to represent the tags associated with blog posts


class Tag(models.Model):
    caption = models.CharField(max_length=20, help_text="Enter a tag caption")

    def __str__(self):
        return self.caption

# Author model to represent the authors of blog posts


class Author(models.Model):
    first_name = models.CharField(
        max_length=100, help_text="Enter the first name of the author")
    last_name = models.CharField(
        max_length=100, help_text="Enter the last name of the author")
    email_address = models.EmailField(
        help_text="Enter the author's email address")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


# Post model to represent blog posts
class Post(models.Model):
    title = models.CharField(
        max_length=150, help_text="Enter the title of the post")
    excerpt = models.CharField(
        max_length=200, help_text="Enter a short excerpt of the post")
    image = models.ImageField(
        upload_to="posts", help_text="Upload an image for the post")
    date = models.DateField(
        auto_now=True, help_text="The date when the post was created or updated")
    slug = models.SlugField(unique=True, db_index=True,
                            help_text="Enter a unique slug for the post")
    content = models.TextField(validators=[MinLengthValidator(
        10)], help_text="Enter the content of the post")
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts", help_text="Select the author of the post")
    tags = models.ManyToManyField(Tag, help_text="Select tags for the post")

    def __str__(self):
        return self.title


# Comment model to represent comments on blog posts
class Comment(models.Model):
    user_name = models.CharField(
        max_length=120, help_text="Enter the name of the user")
    user_email = models.EmailField(
        help_text="Enter the email address of the user")
    text = models.TextField(max_length=400, help_text="Enter the comment text")
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments", help_text="Select the post to comment on")
    approved = models.BooleanField(default=False)
