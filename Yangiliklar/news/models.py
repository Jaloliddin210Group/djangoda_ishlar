from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Kategoriya nomi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        ordering = ['title']

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="Sarlovha")
    content = models.TextField(verbose_name="Yangilik matni", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti ")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqti")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name="Yangilik rasmi ", blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Chop qilinganligi ")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
        ordering=['created_at','content']

