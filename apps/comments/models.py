from django.db import models
from django.contrib.auth import get_user_model

from apps.posts.models import Post

User = get_user_model()

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')
    message = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    upvoted = models.ManyToManyField(User, related_name='users_comment_upvote', blank=True, default=None)
    
    class Meta:
        ordering = ('date_added',)
    
    @property
    def number_of_upvote(self) -> int:
        return self.upvoted.all().count()
    
    def __str__(self) -> str:
        return f"Comment-{self.id}-{self.author.first_name}"

class ReponseComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reponse_comment')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='reponse_comment')
    message = models.CharField(blank=True, null=True, max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.author.first_name} {self.author.last_name}"

class upvoteComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_upvote_comment')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='upvote_comment')
    upvote_CHOICES = (
        ('Upvote', 'upvote'),
        ('Downvote', 'Downvote'),
    )
    value = models.CharField(choices=upvote_CHOICES, max_length=10)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}   -   Comment Id: {self.post.id}"