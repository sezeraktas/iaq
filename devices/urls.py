from rest_framework import routers
from .views import DeviceViewSet

router = routers.DefaultRouter()
router.register(r'', DeviceViewSet, 'devices')

urlpatterns = router.urls
