from django.urls import path
from rest_framework import routers
from views import UserView


router = routers.DefaultRouter()

router.register('user', UserView)


urlpatterns = []

urlpatterns += router.urls
