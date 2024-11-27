from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ImageListView
# URLパターンを逆引きできるように名前を付ける
app_name = 'photo'

# URLパターンを登録する変数
urlpatterns = [
     # photoアプリへのアクセスはviewsモジュールのIndexViewを実行
     path('', views.IndexView.as_view(), name='index'),
     path('post/',views.CreatePhotoView.as_view(),name='post'),
     path('post_done/',
          views.PostSuccessView.as_view(),
          name='post_done'),
     path('photos/<int:category>',
          views.CategoryView.as_view(),
          name='photos_cat'
          ),
     path('user-list/<int:user>',
          views.UserView.as_view(),
          name='user_list'
          ),
     path('photo-detail/<int:pk>',
          views.DetailView.as_view(),
          name='photo_detail'
          ),
     path('mypage/',views.MypageView.as_view(),name='mypage'),
     path('photo/<int:pk>/delete/',
          views.PhotoDeleteView.as_view(),
          name='photo_delete'
          ),
     path(
          'contact/',
          views.ContactView.as_view(),
          name='contact'),
     path(
          'favorite/',
          views.FavoriteView.as_view(),
          name='favorite'),
     path(
          'In_detail/',
          views.InDetailView.as_view(),
          name='In_detail'),
     path('gallery/',
          views.image_gallery,
          name='image_gallery'),
     path('images/', ImageListView.as_view(), name='image_list'),
]
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

