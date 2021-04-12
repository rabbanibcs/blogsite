from django.urls import path
from .views import ( PostListView,
                     PostDetailView,
                     PostCtreateView,
                     PostUpdateView,
                     PostDeleteView,
                     UserPostsView)
from . import views

urlpatterns = [
    path('user/<str:username>/', UserPostsView.as_view(),name='user-posts'),
    path('', PostListView.as_view(), name='blog-home'),
    path('<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='blog-update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='blog-delete'),
    path('new/', PostCtreateView.as_view(), name='blog-create'),
    path('about/', views.about, name='blog-about'),
]