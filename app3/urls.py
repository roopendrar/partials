from django.urls import path
from app3 import views
app_name="app3"


urlpatterns = [
    path('trail/',views.trails,name="trail"),
    path('profile/',views.profile,name="profile"),
]