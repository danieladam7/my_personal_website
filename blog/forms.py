from django import forms

from .models import Comment
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField(label="", widget=ReCaptchaV2Checkbox)

    class Meta:
        model = Comment
        exclude = ["post", "approved"]
        labels = {
            "user_name": "Your Name",
            "user_email": "Your Email",
            "text": "Your Comment",
        }
