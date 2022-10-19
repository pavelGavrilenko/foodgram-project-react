from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TagList, TagRetrieve, TagView


# urlpatterns = [
#     path('tags/', TagList.as_view()),
#     path('tags/<int:pk>/', TagRetrieve.as_view()),
# ]

router = DefaultRouter()
router.register('tags', TagView, basename='tags')

urlpatterns = [
    path('', include(router.urls)),
]