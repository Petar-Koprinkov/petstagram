from django.urls import path, include

from petstagram.accounts import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.login, name='login'),
    path('profile/', include([
        path('<int:pk>/', views.profile_details, name='profile-details'),
        path('<int:pk>/edit/', views.profile_edit, name='profile-edit'),
        path('<int:pk>/delete/', views.profile_delete, name='profile-delete'),
    ])),
]


