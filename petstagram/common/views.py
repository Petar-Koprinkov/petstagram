from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram.common.models import Like
from petstagram.photos.models import Photo


def index(request):
    all_photos = Photo.objects.all()

    context = {
        'all_photos': all_photos
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
