from django.db import models
from django.contrib.auth.models import User

class Follower(models.Model):
    """
    Followers model, related to 'owner' and 'followed'.
    'owner' is the user who is following another user.
    'followed' is the user who is being followed.
    We need to set 'related_name' to 'followers' so that 
    we can access the followers of a user.
    """
    owner = models.ForeignKey(
      User,
      on_delete=models.CASCADE,
      related_name='following'
    )
    followed = models.ForeignKey(
      User,
      on_delete=models.CASCADE,
      related_name='followers'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['owner', 'followed']
        ordering = ['created_at']

    def __str__(self):
        return f'{self.owner} {self.followed}'