from django.db import models
from django.utils import timezone


class Post(models.Model):
    '''
    🚀
    Este modelo representa un Post
    cuenta con todas las variables necesarias
    para crear uno
    '''

    # 👩‍🎨 Un autor como su nombre lo indica el creador del Post
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # 🖋 Titulo del Post
    title = models.CharField(max_length=200)
    # 📖 Todo el texto que contiene nuestro post
    text = models.TextField()
    # 🕔 Fecha en la que fue creado
    created_date = models.DateTimeField(
            default=timezone.now)
    # ✅ Fecha en la que se publicará
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
