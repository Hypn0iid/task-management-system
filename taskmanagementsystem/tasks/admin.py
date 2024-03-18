from django.contrib import admin
from django.contrib.auth.models import Group

#Remover grupos
admin.site.unregister(Group)