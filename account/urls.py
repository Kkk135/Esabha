from django.urls import path
from .import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns =[
    path('',views.indexview,name="home"),
    path('dashboard/',views.dashboardview,name="dashboard"),
    path('login/',LoginView.as_view(success_url="/social/home"),name="login_url"),
    path('register/',views.registerview,name="register_url"),
    path('logout/',LogoutView.as_view(next_page='dashboard'),name="logout_url"),

]
