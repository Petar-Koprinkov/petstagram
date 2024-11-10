from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from petstagram.common.forms import CommentForm
from petstagram.pets.forms import PetAddForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


class AddPetView(CreateView):
    model = Pet
    form_class = PetAddForm
    template_name = 'pets/pet-add-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': 1})

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.user = self.request.user
        pet.save()
        return super().form_valid(form)


class PetDetailView(DetailView):
    model = Pet
    context_object_name = 'pet'
    template_name = 'pets/pet-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['pet_photos'] = self.object.pet_photos.all()
        return context


class EditPetView(UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/pet-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('pet-details', kwargs={'username': self.kwargs['username'], 'slug': self.kwargs['slug']})


class DeletePetView(DeleteView):
    model = Pet
    template_name = 'pets/pet-delete-page.html'
    form_class = PetDeleteForm
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})

    def get_initial(self):
        pet = self.get_object()
        return pet.__dict__

    def get_form_kwargs(self):
        kwargs = {
            'data': self.get_initial(),
        }

        return kwargs
