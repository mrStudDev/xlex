from django.urls import path
from . views import PostsListView, PostsSingleView, CategoryView, AddPostView, AddCategoryView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', PostsListView.as_view(), name='posts-list'),
    path('<int:pk>', PostsSingleView.as_view(), name='post-single'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    #path('images/', ImageView(), name = 'image-upload'),
]
