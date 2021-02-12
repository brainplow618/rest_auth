from django.conf.urls import url, include
from .views import PostsViewSet, PostsratesViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("posts", PostsViewSet, basename="posts")
router.register("posts-rates", PostsratesViewSet, basename="posts-rates")

urlpatterns = [
    url('', include(router.urls))
]
