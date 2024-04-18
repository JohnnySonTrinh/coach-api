from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

github_validator = RegexValidator(
    regex=r'^https?://github\.com/[a-zA-Z0-9-]+/?$',
    message="Enter a valid GitHub URL that ends with a username.",
    code='invalid_github'
)

linkedin_validator = RegexValidator(
    regex=r'^https?://www\.linkedin\.com/in/[a-zA-Z0-9-]+/?$',
    message="Enter a valid LinkedIn URL that ends with a username.",
    code='invalid_linkedin'
)

class Profile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    github = models.URLField(
        max_length=255,
        blank=True,
        validators=[github_validator]
    )
    linkedin = models.URLField(
        max_length=255,
        blank=True,
        validators=[linkedin_validator]
    )
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default_profile_xw5she'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.owner}'s profile"

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)