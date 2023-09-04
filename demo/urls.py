from django.urls import path
# from .views import post_list, post_detail
from demo import views

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('search/', views.search_results, name='search_results'),
    path('categoria/<slug:category_slug>/', views.post_list_by_category, name="post_list_by_category"),
    path('<int:year>/<int:month>/<slug:slug_url>/', views.post_detail, name="post_detail"),
    path('sobre/', views.about, name='about'),  
]
