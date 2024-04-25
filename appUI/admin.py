from django.contrib import admin
from .models import UploadedImage

class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)

admin.site.register(UploadedImage, ImageAdmin)
