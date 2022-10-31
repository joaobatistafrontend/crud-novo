from unicodedata import name
from django.urls import path
from .views import IndexView,IndexList,IndexCreat,IndexUpdate, IndexDelete

urlpatterns = [
    path('', IndexView.as_view(), name='index' ),
    path('list/', IndexList.as_view(), name='list' ),
    path('creat/', IndexCreat.as_view(), name='creat' ),
    path('update/<int:pk>/', IndexUpdate.as_view(), name='update' ),
    path('delete/<int:pk>/', IndexDelete.as_view(), name='delete'),
]
