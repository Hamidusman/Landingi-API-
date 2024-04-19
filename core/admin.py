from django.contrib import admin
from .models import Experience, Education, Link, Profile, CustomUser
# Register your models here.

admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Link)
admin.site.register(Profile)
admin.site.register(CustomUser)