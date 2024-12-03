from django.contrib import admin
from django.urls import path
from authentication.views import home, user_login  # Import home and user_login here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Route to home view
    path('login/', user_login, name='login'),  # Route to login view
]
