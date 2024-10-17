from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createaccount', views.createaccount, name='createaccount'),
    path("login/",views.login_page,name="login_page"),
    path("logout/",views.logout_page,name="logout_page"),
    path("headlines",views.headlines,name="headlines"),
    path("search",views.search,name="search"),
    path("sports",views.sports,name="sports"),
    path("technology",views.technology,name="technology"),
    path("entertainments",views.entertainments,name="entertainments"),
    path("health",views.health,name="health"),
    path("business",views.business,name="business"),
    path("politics",views.politics,name="politics"),
    path("weather",views.weather,name="weather"),
    path("adminpanel",views.adminpanel,name="adminpanel"),
    path("help",views.help,name="help"),
    path("profile/<str:pk>/",views.profile,name="profile"),
    path('newsdetails/<str:pk>/',views.newsdetails,name="newsdetails"),

]