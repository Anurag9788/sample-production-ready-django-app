from django.contrib import admin

# Register your models here.
from .models import Test,Test2
admin.site.register(Test)
admin.site.register(Test2)