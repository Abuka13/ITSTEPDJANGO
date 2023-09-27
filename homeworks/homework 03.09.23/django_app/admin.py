from django.contrib import admin
from django_app import models

admin.site.register(models.Category)



class ArticleAdmin(admin.ModelAdmin):
    list_display = ("headline",)
    list_display_links = ("headline",)
    list_editable = ()
    list_filter = ("headline", "categories")
    filter_horizontal = ("categories",)
    fieldsets = (
        (
            "Основное",
            {"fields": ("headline",)},
        ),
        (
            "Основное 2",
            {"fields": ("categories",)},
        ),
        (
            "Основное 3",
            {"fields": ("description",)},
        ),
        (
            "Основное 4",
            {"fields": ("date",)},
        ),
    )
    search_fields = ["headline", "categories"]


admin.site.register(models.Article, ArticleAdmin)

