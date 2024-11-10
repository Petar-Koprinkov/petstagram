from django.contrib.auth.views import LogoutView
from django.urls import path, include

from petstagram.accounts import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', include([
        path('<int:pk>/', views.ProfileDetailsView.as_view(), name='profile-details'),
        path('<int:pk>/edit/', views.ProfileEditView.as_view(), name='profile-edit'),
        path('<int:pk>/delete/', views.profile_delete, name='profile-delete'),
    ])),
]


