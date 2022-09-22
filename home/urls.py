from django.urls import path, reverse_lazy
from . import views
from .views import UploadBook, EditBook, DeleteBook

urlpatterns = [
    path('', views.index, name='home'),
    path('createbook', UploadBook.as_view(success_url=reverse_lazy('home')), name='createbook'),
    path('editbook/<int:pk>', EditBook.as_view(success_url=reverse_lazy('home')), name='editbook'),
    path('deletebook/<int:pk>', DeleteBook.as_view(success_url=reverse_lazy('home')), name='deletebook'),
    path('search', views.searchquery, name='search')
]

