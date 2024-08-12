from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    path('create_user/', views.create_user),
    path('user/<int:pk>/', views.get_user_info),
    path('api-auth/', include('rest_framework.urls')),
    path('user/<int:chat_id>/', views.get_user, name='get_user'),
    path('user/<int:chat_id>/update/', views.update_user, name='update_user'),
]
