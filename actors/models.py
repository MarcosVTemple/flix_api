from django.db import models


NATIONALITY_CHOICES = (
    ("urss", "União Soviética"),
    ("BRAZIL", "Brasil"),
    ("USA", "USA"),
)


class Actor(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100, choices=NATIONALITY_CHOICES, null=True, blank=True
    )

    def __str__(self) -> str:
        return self.name
