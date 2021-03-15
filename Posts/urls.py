from django.urls import path
from Posts.views import Postcreateview, Postdetailview, Postdeleteview

app_name = 'Posts'

urlpatterns = [
    path('detail/<int:pk>/',Postdetailview.as_view(),name='detail-view'),
    path('create/',Postcreateview.as_view(),name='create-post'),
    path('<pk>/delete',Postdeleteview.as_view(),name='delete-post'),
]
