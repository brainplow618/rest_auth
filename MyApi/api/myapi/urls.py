from django.conf.urls import url,include
from .views import firstfunction
from rest_framework.routers import DefaultRouter
from .views import CarSpaceViewset

router = DefaultRouter()
router.register('car-space', CarSpaceViewset, basename= 'car-space')

urlpatterns = [
    url('first', firstfunction),
    url('', include(router.urls))
]