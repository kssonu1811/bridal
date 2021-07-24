from bridal_function import views
from django.urls import path

my_app = "bridal_function"
urlpatterns = [
    path('bridal',views.bridal, name='bridal'),
    path('bridal/<int:id>/', views.bridal_detail, name='bridal_detail'),
]