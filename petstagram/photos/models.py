from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from petstagram.pets.models import Pet
from petstagram.photos.validators import MaxSizePhotoValidator

UserModel = get_user_model()


class Photo(models.Model):
    photo = models.ImageField(
        upload_to='photo',
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

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='photos',
    )