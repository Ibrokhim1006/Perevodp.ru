from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Pesni(models.Model):
    title = models.CharField(max_length=250,verbose_name="Название песни русское.")
    en_title = models.CharField(max_length=250,null=True,blank=True,verbose_name="Название песни на английском")
    ru_content = RichTextUploadingField(default=None,verbose_name="Текст песни русский.")
    en_content = RichTextUploadingField(default=None,verbose_name="Тексты на английском языке")
    create_date = models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title