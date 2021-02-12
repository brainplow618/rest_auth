from django.conf.urls import url, include
from .views import StudentsViewSet, ModulesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("students", StudentsViewSet, basename="students")
router.register("modules", ModulesViewSet, basename="modules")

urlpatterns = [
    url('', include(router.urls))
]