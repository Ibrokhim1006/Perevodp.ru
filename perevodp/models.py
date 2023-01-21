from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Catgeoriya(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=250,verbose_name="Ф.И.О")
    img = models.ImageField(upload_to='artist/',default='perevod/photo.png',verbose_name="Фото артист")
    catgeor_id = models.ForeignKey(Catgeoriya,on_delete=models.CASCADE,verbose_name="Выберите букву")

    def __str__(self):
        return self.name


class Pesni(models.Model):
    title = models.CharField(max_length=250,verbose_name="Название песни русское.")
    en_title = models.CharField(max_length=250,null=True,blank=True,verbose_name="Название песни на английском")
    ru_content = RichTextUploadingField(default=None,verbose_name="Текст песни русский.")
    en_content = RichTextUploadingField(default=None,verbose_name="Тексты на английском языке")
    id_artist = models.ForeignKey(Artist,on_delete=models.CASCADE,verbose_name='Певица')

    def __str__(self):
        return self.title