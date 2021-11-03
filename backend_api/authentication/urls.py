from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('test', views.index, name='index'),
    path('auth/', include(router.urls)),
    path('auth/api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]