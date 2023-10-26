from django.db import models

class Photo(models.Model):
    photo = models.ImageField(verbose_name="фото", upload_to="users/avatars", default=None, null=True, blank=True)

    class Meta:
        """Вспомогательный класс"""

        app_label = "django_app"



