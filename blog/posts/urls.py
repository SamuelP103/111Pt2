from django.urls import path
from posts import views


urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("new/", views.PostCreateView.as_view(), name="new"),
    path("<int:pk>/edit/", views.PostUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="delete"),
    path("password_change/", views.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/",views.PasswordChangeDoneView.as_view(), name="password_change_done"),
]