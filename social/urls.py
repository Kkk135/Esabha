from django.urls import path
from . import views
from django.views.generic import View
from django.views.generic.base import RedirectView

urlpatterns = [
    path('home/',views.home),
    path('about/',views.about),
    path('contact/',views.contact),

    path('profile/edit/<int:pk>',views.ProfileUpdateView.as_view(success_url='/social/home')),

    path('post/create/',views.PostCreateView.as_view(success_url='/social/home')),
    path('post/',views.PostListView.as_view()),
    path('post/<int:pk>',views.PostDetailView.as_view()),
    path('post/delete/<int:pk>',views.PostDeleteView.as_view()),

    path('profile/',views.ProfileListView.as_view()),
    path('profile/<int:pk>',views.ProfileDetailView.as_view()),
    path('profile/follow/<int:pk>',views.follow),
    path('',RedirectView.as_view(url="/social/home"))

]
