from django.contrib import admin
from index.models import *;
# Register your models here.

admin.site.register(User)
admin.site.register(Choices)
admin.site.register(Questions)
admin.site.register(Answer)
admin.site.register(Form)
admin.site.register(Responses)