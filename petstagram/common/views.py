from django.shortcuts import render, redirect

from petstagram.common.models import Like
from petstagram.photos.models import Photo


# Create your views here.


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



