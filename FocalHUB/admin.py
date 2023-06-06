from django.contrib import admin
from FocalHUB.models import Post,Like, Comment

# Register your models here.

class SiteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, SiteAdmin)
admin.site.register(Like, SiteAdmin)
admin.site.register(Comment, SiteAdmin)