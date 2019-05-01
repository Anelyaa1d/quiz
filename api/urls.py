from django.urls import path, re_path
from api import views

urlpatterns = [
    path('api/post_lists/<int:pk>', views.post_list)
]