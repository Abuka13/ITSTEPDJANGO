from django.db import models
class Suggests(models.Model):
    author = models.CharField(max_length=300, verbose_name="Имя")
    title = models.CharField(max_length=300, verbose_name="Наименование")
    image = models.ImageField("Изображение", upload_to="images/posts")
    description = models.TextField(verbose_name="Описание")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    class Meta:
        """Вспомогательный класс"""

        app_label = "django_app"
        ordering = ("-date", "title")
        verbose_name = "Предложение"
        verbose_name_plural = "Предложения"

    def __str__(self):
        return self.title   