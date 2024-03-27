from django.contrib import admin
from .models import *

admin.site.register(Sponsor)
admin.site.register(Student)
admin.site.register(StudentSponser)
admin.site.register(University)