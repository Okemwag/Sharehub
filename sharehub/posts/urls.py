from rest_framework import routers

from .views import LikePostViewSet, PostViewSet

app_name = 'sharehub.posts'

router = routers.DefaultRouter()
# router.register(r"posts", PostViewSet)
# router.register(r"likes", LikePostViewSet)

router.register("posts", PostViewSet, basename="posts")
router.register("likes", LikePostViewSet, basename="likes")


urlpatterns = router.urls
