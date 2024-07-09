import uuid

from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from .tasks import resize_images
from .utils import rename_post_img_video

User = get_user_model()


class Post(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, db_index=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts", db_index=True
    )
    caption = models.TextField(_("message"), blank=True)
    img = models.ImageField(
        _("image"),
        upload_to=rename_post_img_video,
        validators=[FileExtensionValidator(["png", "jpg", "jpeg", "gif"])],
        blank=True,
        null=True,
    )
    date_posted = models.DateTimeField(
        _("date created"), auto_now_add=True, db_index=True
    )
    date_updated = models.DateTimeField(_("date updated"), auto_now=True)

    def __str__(self):
        return f"Post-{self.id}-{self.author.first_name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.img:
            resize_images.delay(self.img.path, self.img.name)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ("-date_posted",)
        indexes = [
            models.Index(fields=["author", "date_posted"]),
        ]


class LikePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, db_index=True)
    LIKE_CHOICES = (
        ("Upvote", "Upvote"),
        ("Downvote", "Downvote"),
    )
    value = models.CharField(choices=LIKE_CHOICES, max_length=10)

    class Meta:
        unique_together = ("user", "post")

    def __str__(self) -> str:
        return f"{self.user.first_name}-{self.post.id}-{self.value}"


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comment"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_comment"
    )
    message = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    upvoted = models.ManyToManyField(
        User, related_name="users_comment_upvote", blank=True, default=None
    )

    class Meta:
        ordering = ("date_added",)

    @property
    def number_of_upvote(self) -> int:
        return self.upvoted.all().count()

    def __str__(self) -> str:
        return f"Comment-{self.id}-{self.author.first_name}"


class ReponseComment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_reponse_comment"
    )
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="reponse_comment"
    )
    message = models.CharField(blank=True, null=True, max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.author.first_name} {self.author.last_name}"


class upvoteComment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_upvote_comment"
    )
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="upvote_comment"
    )
    upvote_CHOICES = (
        ("Upvote", "upvote"),
        ("Downvote", "Downvote"),
    )
    value = models.CharField(choices=upvote_CHOICES, max_length=10)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}   -   Comment Id: {self.post.id}"
