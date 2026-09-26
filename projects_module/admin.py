from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Skill)
admin.site.register(models.Project)
admin.site.register(models.ProjectImage)
admin.site.register(models.ProjectChallenge)
admin.site.register(models.ProjectFeature)

