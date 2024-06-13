from typing import Optional
from django.db.models import QuerySet, Q
from .models import Post, LikePost


def get_all_posts() -> QuerySet[Post]:
    return Post.objects.all()


def get_user_posts(user_id: int) -> QuerySet[Post]:
    return Post.objects.filter(author_id=user_id)


def search_posts(query: str) -> QuerySet[Post]:
    return Post.objects.filter(
        Q(caption__icontains=query) | Q(author__first_name__icontains(query))
    )


def get_trending_posts(limit: int = 5) -> QuerySet[Post]:
    return Post.objects.order_by("-date_posted")[:limit]


def get_post_by_id(post_id: int) -> Optional[Post]:
    try:
        return Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return None


def get_like_for_post(user_id: int, post_id: int) -> Optional[LikePost]:
    try:
        return LikePost.objects.get(user_id=user_id, post_id=post_id)
    except LikePost.DoesNotExist:
        return None
