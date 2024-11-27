from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    title = models.CharField(verbose_name='カテゴリ', max_length=20)
    def __str__(self):
        return self.title


class PhotoPost(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=200)
    comment = models.TextField(verbose_name='コメント')
    image1 = models.ImageField(verbose_name='イメージ1', upload_to='photos')
    image2 = models.ImageField(verbose_name='イメージ2', upload_to='photos', blank=True, null=True)
    image3 = models.ImageField(verbose_name='イメージ3', upload_to='photos', blank=True, null=True)
    image4 = models.ImageField(verbose_name='イメージ4', upload_to='photos', blank=True, null=True)
    posted_at = models.DateTimeField(verbose_name='投稿日時', auto_now_add=True)
    
    def __str__(self):
        return self.title

from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Rarity(models.Model):
    level = models.CharField(max_length=50)

    def __str__(self):
        return self.level

class ImageModel(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    rarity = models.ForeignKey(Rarity, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # カテゴリを追加
    image = models.ImageField(upload_to='image_poke/')

    def __str__(self):
        return self.name





