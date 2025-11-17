from django.db import models

class Car(models.Model):
    vid_CHOICES = [
        ('хетчбек', 'хетчбек'),
        ('седан', 'седан'),
        ('универсал', 'универсал'),
        ('купе', 'купе'),
        ('кроссовер', 'кроссовер'),
        ('пикап', 'пикап'),
        ('внедорожник', 'внедорожник'),
        ('минивэн', 'минивэн'),
        ('фургон', 'фургон'),
        ('кроссовер', 'кроссовер'),
        ('пикап', 'пикап'),
        ('внедорожник', 'внедорожник'),
        ('минивэн', 'минивэн'),
        ('фургон', 'фургон'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    vid = models.CharField(choices=vid_CHOICES)
    year = models.PositiveIntegerField()
    whatcost = models.PositiveIntegerField(help_text="How much cost?")
    picture = models.ImageField(upload_to='posters/')

    def __str__(self):
        return self.title
