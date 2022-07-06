from rest_framework import routers
from .views import EventViewSet

router = routers.DefaultRouter()
router.register(r'', EventViewSet, 'events')

urlpatterns = router.urls
