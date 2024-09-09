from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.ForeignKey(
        to=Genre, 
        on_delete=models.PROTECT,
        related_name="movies"
    )
    release_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(
        to=Actor, 
        related_name="movies"
    )
    resume = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title