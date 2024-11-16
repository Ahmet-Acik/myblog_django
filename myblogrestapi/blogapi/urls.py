from django.urls import path
from . import views

"""
URL configuration for the blogapi application.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/stable/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

Routes:
    - '' : Renders the index view.
    - 'posts/' : Renders the get_posts view.
    - 'posts/create/' : Renders the create_post view.
    - 'posts/<int:pk>/' : Renders the post_detail view for a specific post identified by primary key (pk).
"""


urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.get_posts, name="get_posts"),
    path("posts/create/", views.create_post, name="create_post"),
    path("posts/<int:pk>/", views.post_detail, name="post_detail"),
]
