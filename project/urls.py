from django.urls import path, include

urlpatterns = [
    path('', include('todos.urls')),
    path("unicorn/", include("django_unicorn.urls")),
]
