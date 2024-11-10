from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from petstagram.accounts.forms import AppUserCreationForm, ProfileEditForm
from petstagram.accounts.models import Profile


UserModel = get_user_model()


class RegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class CustomLoginView(LoginView):
    template_name = 'accounts/login-page.html'


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'accounts/profile-details-page.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_likes = (photos.like_set.count() for photos in self.object.user.photos.all())
        context['total_likes'] = sum(total_likes)

        total_pets = self.object.user.pets.all().count
        context['total_pets'] = total_pets

        total_photos = self.object.user.photos.all().count()
        context['total_photos'] = total_photos


        return context


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={
                'pk': self.object.pk
            }
        )


def profile_delete(request, pk):
    return render(request, 'accounts/profile-delete-page.html')


class ProfileDeleteView(DeleteView):
    model = Profile
    success_url = reverse_lazy('index')
    template_name = 'accounts/profile-delete-page.html'
