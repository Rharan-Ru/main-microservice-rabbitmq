from django.urls import path
from .views import LikeView


urlpatterns = [
    path('like', LikeView.as_view(), name='like-view'),
    path('like/<int:pk>', LikeView.as_view(), name='like-view-post')
]
