from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram.common.forms import CommentForm, SearchForm
from petstagram.common.models import Like
from petstagram.photos.models import Photo


def index(request):
    all_photos = Photo.objects.all()
    comment_form = CommentForm()
    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        all_photos = all_photos.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])

    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form,
    }

    return render(request, 'common/home-page.html', context)


def like_functionality(request, photo_id):
    liked_photo = Like.objects.filter(
        to_photo_id=photo_id
    )

    if liked_photo:
        liked_photo.delete()
    else:
        like = Like(to_photo_id=photo_id)
        like.save()

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')


def share_functionality(request, photo_id):
    copy(request.META.get('HTTP_HOST') + resolve_url('details-photo', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def comment_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    form = CommentForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')












