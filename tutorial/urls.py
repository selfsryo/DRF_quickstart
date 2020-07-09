from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # Routerを使ってルーティング
    path('', include(router.urls)),
    # BrowsableAPIのログインURLも定義
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
