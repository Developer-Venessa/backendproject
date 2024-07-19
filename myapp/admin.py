from django.contrib import admin
from .models import People
from .models import Contact

# Register your models here.
admin.site.register(People)

admin.site.register(Contact)