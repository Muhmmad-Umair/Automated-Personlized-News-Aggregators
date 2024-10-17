from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(User)
admin.site.register(News)
admin.site.register(NewsCategory)
admin.site.register(Review)
admin.site.register(Notification)
admin.site.register(Help)