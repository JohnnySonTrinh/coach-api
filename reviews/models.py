from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Custom validator for GitHub URL
github_validator = RegexValidator(
    regex=r'^https?://github\.com/[a-zA-Z0-9-]+(/[a-zA-Z0-9-]+)*/*$',
    message="Enter a valid GitHub repository URL.",
    code='invalid_github'
)


class Review(models.Model):
    """
    Model for a review post. stores the title, content, github repo, 
    live website, image, created_at, updated_at.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField(max_length=1000, blank=True)
    github_repo = models.URLField(
        blank=True,
        max_length=255,
        validators=[github_validator]
    )
    live_website = models.URLField(
        blank=True,
        max_length=255,
    )
    image = models.ImageField(
        upload_to='images/',
        default='../default_post_xw5she',
        max_length=255,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.id} - {self.title}'
