from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/projects/', include('projects.urls')),
    path('api/achievements/', include('achievements.urls')),
    path('api/posts/', include('posts.urls')),
    path('api/academics/', include('academics.urls')),
    path('api/users/', include('users.urls')),
]