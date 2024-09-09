from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(
        to=Movie, on_delete=models.PROTECT, related_name="reviews"
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(
                limit_value=0,
                message="Avaliação não pode ser inferior a zero estrelas!",
            ),
            MaxValueValidator(
                limit_value=5,
                message="Avaliação não pode ser superior a cinco estrelas!",
            ),
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.movie