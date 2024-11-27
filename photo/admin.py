from django.contrib import admin
from .models import Type, Rarity, ImageModel, Category, PhotoPost

# 既存のCategoryAdminを使用
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

# 既存のPhotoPostAdminを使用
class PhotoPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

# 既存のImageModelAdminを使用
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'rarity', 'category', 'image')  # カテゴリを追加
    search_fields = ('name', 'type__name', 'rarity__level', 'category__title')  # カテゴリを追加

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Rarity)
class RarityAdmin(admin.ModelAdmin):
    list_display = ('id', 'level')
    search_fields = ('level',)

# Category、PhotoPost、ImageModelの登録を一箇所にまとめる
admin.site.register(Category, CategoryAdmin)
admin.site.register(PhotoPost, PhotoPostAdmin)
admin.site.register(ImageModel, ImageModelAdmin)