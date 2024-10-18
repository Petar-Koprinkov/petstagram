from django.urls import path, include

from petstagram.photos import views

urlpatterns = [
    path('add/', views.AddPhotoView.as_view(), name='add-photo'),
    path('<int:pk>/', include([
        path('', views.PhotoDetailView.as_view(), name='details-photo'),
        path('edit/', views.PhotoEditView.as_view(), name='edit-photo'),
        path('delete/', views.photo_delete, name='delete-photo'),
    ]))
]