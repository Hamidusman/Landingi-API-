from django.urls import path
from . import views
urlpatterns = [
    path('experience', views.experience.as_view()),
    path('education', views.education.as_view())
]