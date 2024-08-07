from rest_framework.routers import DefaultRouter

# ViewSets
from .views import ElectionViewSet, ElectoralProfileViewSet

router = DefaultRouter()
router.register(r'profiles', ElectoralProfileViewSet, basename='electoral_profiles')
router.register(r'', ElectionViewSet, basename='elections')

urlpatterns = router.urls
