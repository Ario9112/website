from django.contrib import admin
from .models import Article,Catagory
# Register your models here.

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ("position","title","slug","status")
    list_filter = ("status",)
    search_fields = ("title","slug")
    prepoulated_fields = {"slug":("title",)}
admin.site.register(Catagory,CatagoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","slug","published")
    list_filter = ("published","status")
    search_fields = ("title","description")
admin.site.register(Article,ArticleAdmin)