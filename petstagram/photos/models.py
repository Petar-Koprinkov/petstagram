from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import MaxSizePhotoValidator


class Photo(models.Model):
    photo = models.ImageField(
        upload_to='media/photo',
        validators=[MaxSizePhotoValidator(5)]
    )

    description = models.TextField(
        validators=[
            MinLengthValidator(10),
            MaxLengthValidator(300)
        ],
    )

    location = models.CharField(
        max_length=30,
    )

    tagged_pets = models.ManyToManyField(
        to=Pet,
        blank=True,
        related_name='pet_photos',
    )

    date_of_publication = models.DateField(
        auto_now_add=True,
    )