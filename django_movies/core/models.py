from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)
    general_audiences = "G"
    parental_guidance_suggested = "PG"
    parents_strongly_cautioned = "PG-13"
    restricted = "R"
    adults_only = "NC-17"
    age_limit_choices = [
        (general_audiences, "G"),
        (parental_guidance_suggested, "PG"),
        (parents_strongly_cautioned, "PG-13"),
        (restricted, "R"),
        (adults_only, "NC-17")
    ]
    age_limit=models.CharField(max_length=5, null=True, blank=True, choices=age_limit_choices, default=general_audiences)

    def __str__(self):
        return self.name

class Director(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=120)
    rating = models.IntegerField(null=True, validators=[MaxValueValidator(10), MinValueValidator(1)])
    released = models.DateField()
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
    director = models.ForeignKey(Director, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.title} from {self.released}"

