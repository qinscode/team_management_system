from django.urls import path
from .views import (
    MemberListView,
    MemberDetailView,
    MemberCreateView,
    MemberUpdateView,
    about_view
)

urlpatterns = [
    path('', MemberListView.as_view(), name='member-list'),
    path('member/<int:pk>/', MemberDetailView.as_view(), name='member-detail'),
    path('member/new/', MemberCreateView.as_view(), name='member-create'),
    path('member/<int:pk>/edit/', MemberUpdateView.as_view(), name='member-update'),
    path('about/', about_view, name='about'),
] 