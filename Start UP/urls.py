from django.urls import path
from .views import user_list, other_page

urlpatterns = [
    path('', user_list, name='user_list'),
    path('other/', other_page, name='other_page'),
]