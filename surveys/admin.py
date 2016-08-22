from django.contrib import admin
from surveys.models import *

# Register your models here.

admin.site.register(Survey)
admin.site.register(Distribution)
admin.site.register(Market)
admin.site.register(Locale)
admin.site.register(SourceType)
