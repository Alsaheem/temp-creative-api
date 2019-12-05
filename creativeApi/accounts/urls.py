from django.urls import path,include
from .views import UserProfileViewset,UserFollowAPIView

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('profiles', UserProfileViewset)

urlpatterns = [
    path('view/',UserFollowAPIView.as_view()),
    path('', include(router.urls))
]