from django.urls import path
from content.views import ContentAPI,ContentChangeAPI


urlpatterns = [
    path('contents/',ContentAPI.as_view(),name="content_page"),
    path('contents/<int:pk>/',ContentChangeAPI.as_view(), name="delete_content")
]