from django.urls import path
from .views import login_view, generate_code

urlpatterns = [
    path('', login_view, name='login'),
    path('code/', generate_code, name='generate_code'),
]
