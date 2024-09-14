from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('create_user/', views.create_user),
    path('api-auth/', include('rest_framework.urls')),
    path('user/<int:chat_id>/', views.get_user, name='get_user'),
    path('user/<int:chat_id>/update/', views.update_user, name='update_user'),
    path('new-ref/', views.new_ref, name='new_ref'),
    path('user-ref/<int:chat_id>/', views.UserReferralsView.as_view(), name='user-referrals'),
    path('level_info/<int:level_id>', views.get_level, name='get_level'),
    path('user-ranking/', views.UserRankingView.as_view(), name='user-ranking'),
    path('get_cards/', views.get_cards, name='get_card'),
    path('get_tasks/<int:chat_id>', views.get_tasks, name='get_tasks'),
    path('complete_task/<int:chat_id>/<int:task_id>', views.complete_task, name='completed')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
