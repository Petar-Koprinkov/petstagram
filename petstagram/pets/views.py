from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from petstagram.common.forms import CommentForm
from petstagram.pets.forms import PetAddForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


class AddPetView(LoginRequiredMixin, CreateView):
    model = Pet
    form_class = PetAddForm
    template_name = 'pets/pet-add-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.user = self.request.user
        pet.save()
        return super().form_valid(form)


class PetDetailView(LoginRequiredMixin, DetailView):
    model = Pet
    context_object_name = 'pet'
    template_name = 'pets/pet-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['pet_photos'] = self.object.pet_photos.all()
        return context


class EditPetView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/pet-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('pet-details', kwargs={'username': self.kwargs['username'], 'slug': self.kwargs['slug']})

    def test_func(self):
        pet = get_object_or_404(Pet, slug=self.kwargs['slug'])
        if self.request.user != pet.user:
            return self.request.user == pet.user


class DeletePetView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pet
    template_name = 'pets/pet-delete-page.html'
    form_class = PetDeleteForm

    def get_success_url(self):
        return reverse_lazy(
            'profile-details', kwargs={'pk': self.request.user.pk}
        )

    def get_initial(self):
        pet = self.get_object()
        return pet.__dict__

    def get_form_kwargs(self):
        kwargs = {
            'data': self.get_initial(),
        }

        return kwargs

    def test_func(self):
        pet = get_object_or_404(Pet, slug=self.kwargs['slug'])
        if self.request.user != pet.user:
            return self.request.user == pet.user
