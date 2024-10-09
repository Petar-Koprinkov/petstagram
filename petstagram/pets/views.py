from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.pets.forms import PetAddForm, PetEditForm, PetDeleteForm
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
    comment_form = CommentForm()

    context = {
        'pet': pet,
        'pet_photos': pet_photos,
        'comment_form': comment_form,
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
    pet = Pet.objects.get(slug=slug)
    form = PetDeleteForm(instance=pet)

    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=1)

    context = {
        'pet': pet,
        'form': form,
    }

    return render(request, 'pets/pet-delete-page.html', context)
