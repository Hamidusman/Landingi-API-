from django.urls import path
from . import views
urlpatterns = [
    path('experience', views.ExperienceListCreate.as_view()),
    path('experience/<int:id>', views.ExperienceRetrieveUpdate.as_view()),
    path('education', views.EducationListCreate.as_view()),
    path('education/<int:id>', views.EducationItem.as_view()),
    path('links', views.LinkListCreate.as_view()),
    path('links/<int:id>', views.LinkItem.as_view()),
    path('profile', views.ProfileListCreate.as_view()),
    path('profile/<int:id>', views.ProfileItem.as_view()),
    path('register', views.Register.as_view())
]