from django.urls import path
from .views import post_list_view, PostCreateView,PostListView, login_required


urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts_list'),
    path('create-post/', login_required(PostCreateView.as_view()), name='create_post')  #باید حتما یه تابع باشه و کلاس نمی‌تونه باشه path رو بنویسیم چون آرگمان دوم این .as_view() ها ما وقتی می‌خواهیم آدرس‌دهی کنیم باید اونCBV توی 
]