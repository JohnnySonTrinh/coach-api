from django.db import models
from django.contrib.auth.models import User
from reviews.models import Review

class Like(models.Model):
    # Like model, related to Review and User
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(
        Review,
        related_name='likes',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'review']

    def __str__(self):
        return f'{self.owner} likes {self.review}'