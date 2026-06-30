from django.urls import path
from .views import *

urlpatterns = [
    path("upload/", upload_resume),
    path("history/", resume_history),
    path("history/<int:id>/", resume_detail),
]