from django.contrib import admin
from .models import BoardAllContentList


# Image 클래스를 inline으로 나타낸다.
# class ImageInline(admin.TabularInline):
#     model = Image

# # # BoardAllContentList 클래스는 해당하는 image 객체를 리스트로 관리하는 한다. 


class Boardadmin(admin.ModelAdmin):
    search_fields = ['content']
    # inlines = [ImageInline, ]

# admin.site.register(Image, Boardadmin)
admin.site.register(BoardAllContentList, Boardadmin)
