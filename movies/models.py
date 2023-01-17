from django.core import validators
from django.db import models


class Movie(models.Model):
  name = models.CharField(
    max_length=80,
    blank=False,
    validators=[
      validators.MinLengthValidator(2),
      validators.MaxLengthValidator(80),
      validators.RegexValidator(r'[^0-9a-zA-Z]',message='Enter value', code='no_blanks'),
    ]
  )
  rating = models.IntegerField(
    default=0,
    validators=[
      validators.MaxValueValidator(5),
      validators.MinValueValidator(1),
    ]
  )

  def __str__(self):
    return self.name + ':' + str(self.rating)
