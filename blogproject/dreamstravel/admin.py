from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Articles)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Subscribe)
admin.site.register(Comments)