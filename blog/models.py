from django.db import models
from django.urls import reverse # Новый импорт


class game(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    GAME_CHOICES = (
    ('horror','HORROR'),
    ('shuting', 'SHUTING'),
    ('adventure','ADVENTURE'),
    ('simulator','SIMULATOR'),
    ('arcad','ARCAD'),
)
    genre = models.CharField(choices=GAME_CHOICES, max_length = 10)
    price = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self): # Тут мы создали новый метод
        return reverse('post_detail', args=[str(self.id)])
    
class Image(models.Model):
    post = models.ForeignKey(game, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/post_images/')