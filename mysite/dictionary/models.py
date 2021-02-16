
from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Word(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    word = models.CharField('Слово', max_length=200)
    word_url = models.SlugField('URL страницы слова')
    description = models.TextField('Значение слова')
    created_date = models.DateTimeField('Дата создания', default=timezone.now)
    published_date = models.DateTimeField('Дата публикации',blank=True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.word

    def get_absolute_url(self):
        return reverse("word_detail", args={"word_url": [str(self.word_url)]})