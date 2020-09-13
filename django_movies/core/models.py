from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from model_utils import Choices

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)
    general_audiences = "G"
    parental_guidance_suggested = "PG"
    parents_strongly_cautioned = "PG-13"
    restricted = "R"
    adults_only = "NC-17"
    age_limit_choices = Choices(
        (0, 'kids', 'kids'),
        (1, 'teens', 'teens'),
        (2, 'adults', 'adults'),
        # (general_audiences, "G"),
        # (parental_guidance_suggested, "PG"),
        # (parents_strongly_cautioned, "PG-13"),
        # (restricted, "R"),
        # (adults_only, "NC-17")

    )
    age_limit=models.IntegerField(null=True, blank=True, choices=age_limit_choices)

    def __str__(self):
        return self.name

class Director(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"{self.name}"


class Movie(models.Model):
    title = models.CharField(max_length=120)
    rating = models.IntegerField(null=True, validators=[MaxValueValidator(10), MinValueValidator(1)])
    released = models.DateField()
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
    director = models.ForeignKey(Director, null=True, on_delete=models.SET_NULL)
    countries = models.ManyToManyField(Country, null=True, related_name="movies")

    class Meta:
        unique_together = ('title', 'released', 'director')

    def __str__(self):
        return f"{self.title} from {self.released}"

