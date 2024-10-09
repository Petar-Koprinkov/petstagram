from django.shortcuts import render, redirect
from petstagram.pets.forms import PetAddForm, PetEditForm
from petstagram.pets.models import Pet


def pet_add(request):
    form = PetAddForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('profile-details', pk=1)

    context = {
        'form': form
    }

    return render(request, 'pets/pet-add-page.html', context)


def pet_details(request, username: str, slug: str):
    pet = Pet.objects.get(slug=slug)
    pet_photos = pet.pet_photos.all()

    context = {
        'pet': pet,
        'pet_photos': pet_photos,
    }
    return render(request, 'pets/pet-details-page.html', context)


def pet_edit(request, username: str, slug: str):
    pet = Pet.objects.get(slug=slug)
    form = PetEditForm(request.POST or None, instance=pet or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('pet-details', username, slug)

    context = {
        'pet': pet,
        'form': form
    }

    return render(request, 'pets/pet-edit-page.html', context)


def pet_delete(request, username: str, slug: str):
    render(request, 'pets/pet-delete-page.html')
