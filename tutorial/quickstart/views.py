from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    APIエンドポイントの設定
    ModelViewSetを継承することでCRUDすべてが可能になる
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    APIエンドポイントの設定
    ModelViewSetを継承することでCRUDすべてが可能になる
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
