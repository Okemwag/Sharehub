import logging
from typing import Any, Dict

from django.core.exceptions import ObjectDoesNotExist
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .exceptions import PostDoesNotExist
from .models import LikePost
from .selectors import (get_all_posts, get_trending_posts, get_user_posts)
from .serializers import LikePostSerializer, PostSerializer

logger = logging.getLogger(__name__)


class PostViewSet(viewsets.ModelViewSet):
    queryset = get_all_posts()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["author"]
    search_fields = ["caption"]

    def create(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            data: Dict[str, Any] = request.data
            data["author"] = request.user.id
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(f"Error creating post: {e}")
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def like(self, request: Any, pk: int = None) -> Response:
        try:
            post = self.get_object()
            like, created = LikePost.objects.get_or_create(user=request.user, post=post)
            if not created:
                like.delete()
                return Response({"message": "Unliked"}, status=status.HTTP_200_OK)
            return Response({"message": "Liked"}, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            logger.error(f"Post with id {pk} does not exist")
            raise PostDoesNotExist()
        except Exception as e:
            logger.error(f"Error liking post: {e}")
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def my_posts(self, request: Any) -> Response:
        try:
            queryset = get_user_posts(request.user.id)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error retrieving my posts: {e}")
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"], permission_classes=[AllowAny])
    def search(self, request: Any) -> Response:
        try:
            query: str = request.query_params.get("q", "")
            queryset = search_posts(query)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error searching posts: {e}")
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"], permission_classes=[AllowAny])
    def trending(self, request: Any) -> Response:
        try:
            queryset = get_trending_posts()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error retrieving trending posts: {e}")
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class LikePostViewSet(viewsets.ModelViewSet):
    queryset = LikePost.objects.all()
    serializer_class = LikePostSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user", "post"]

    def create(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            data: Dict[str, Any] = request.data
            data["user"] = request.user.id
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(f"Error creating like: {e}")
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            instance = self.get_object()
            if instance.user == request.user:
                self.perform_destroy(instance)
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(
                {"message": "You are not allowed to delete this"},
                status=status.HTTP_403_FORBIDDEN,
            )
        except ObjectDoesNotExist:
            logger.error(f"Like with id {kwargs['pk']} does not exist")
            return Response(
                {"message": "Like does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            logger.error(f"Error deleting like: {e}")
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            queryset = self.queryset.filter(user=request.user)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error listing likes: {e}")
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            instance = self.get_object()
            if instance.user == request.user:
                serializer = self.get_serializer(instance)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                {"message": "You are not allowed to view this"},
                status=status.HTTP_403_FORBIDDEN,
            )
        except ObjectDoesNotExist:
            logger.error(f"Like with id {kwargs['pk']} does not exist")
            return Response(
                {"message": "Like does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            logger.error(f"Error retrieving like: {e}")
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        try:
            instance = self.get_object()
            if instance.user == request.user:
                serializer = self.get_serializer(
                    instance, data=request.data, partial=True
                )
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                {"message": "You are not allowed to update this"},
                status=status.HTTP_403_FORBIDDEN,
            )
        except ObjectDoesNotExist:
            logger.error(f"Like with id {kwargs['pk']} does not exist")
            return Response(
                {"message": "Like does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            logger
