from django.contrib import admin


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['conversation']
