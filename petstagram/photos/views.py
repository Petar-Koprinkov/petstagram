from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from petstagram.photos.forms import PhotoAddForm, PhotoEditForm
from petstagram.photos.models import Photo


class AddPhotoView(CreateView):
    model = Photo
    template_name = 'photos/photo-add-page.html'
    form_class = PhotoAddForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.user = self.request.user
        photo.save()
        return super().form_valid(form)


class PhotoDetailView(LoginRequiredMixin, DetailView):
    model = Photo
    template_name = 'photos/photo-details-page.html'
    context_object_name = 'photo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comment_set.all()
        context['likes'] = self.object.like_set.all()
        self.object.has_liked = self.object.like_set.filter(user=self.request.user).exists()
        return context


class PhotoEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Photo
    template_name = 'photos/photo-edit-page.html'
    form_class = PhotoEditForm
    success_url = reverse_lazy('index')
    context_object_name = 'photo'

    def test_func(self):
        photo = get_object_or_404(Photo, pk=self.kwargs['pk'])
        return self.request.user == photo.user

@login_required
def photo_delete(request, pk):
    photo = Photo.objects.get(pk=pk)

    if photo.user != request.user:
        return HttpResponseForbidden()

    photo.delete()
    return redirect('index')
