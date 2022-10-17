from django.urls import include, path

from .views import TagList, TagRetrieve


urlpatterns = [
    path('tags/', TagList.as_view()),
    path('tags/<int:pk>/', TagRetrieve.as_view()),
]