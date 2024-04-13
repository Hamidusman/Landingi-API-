from django.urls import path
from . import views
urlpatterns = [
    path('experience', views.ExperienceListCreate.as_view()),
    path('experience/<int:id>', views.ExperienceRetrieveUpdate.as_view()),
    path('education', views.education.as_view()),
    path('link', views.link.as_view()),
    path('profile', views.ProfileListCreate.as_view())
]