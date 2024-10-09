from django.shortcuts import render

from petstagram.pets.models import Pet


# Create your views here.


def pet_add(request):
    return render(request, 'pets/pet-add-page.html')


def pet_details(request, username: str, slug: str):
    pet = Pet.objects.get(slug=slug)
    pet_photos = pet.pet_photos.all()

    context = {
        'pet': pet,
        'pet_photos': pet_photos,
    }
    return render(request, 'pets/pet-details-page.html', context)


def pet_edit(request, username: str, slug: str):
    return render(request, 'pets/pet-edit-page.html')


def pet_delete(request, username: str, slug: str):
    render(request, 'pets/pet-delete-page.html')

