from rest_framework.routers import DefaultRouter

# Views
from .views import RegisterViewSet, LoginViewSet, UsersViewSet

router = DefaultRouter()
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'users', UsersViewSet, basename='users')

urlpatterns = router.urls
