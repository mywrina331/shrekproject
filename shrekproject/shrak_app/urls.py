from django.urls import path
from .views import index
from .views import top_sellers
from .views import advertisement_post
from .views import advertisement_detail

urlpatterns = [
    path('', index, name='index'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', advertisement_post, name='adv-post'),
    path('advertisement/<int:pk>', advertisement_detail, name='adv-detail')
]