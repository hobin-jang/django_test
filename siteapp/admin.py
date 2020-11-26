from django.contrib import admin
from .models import Content, Comment, Recomment, Profile
# Register your models here.

admin.site.register(Content)
admin.site.register(Comment)
admin.site.register(Recomment)
admin.site.register(Profile)