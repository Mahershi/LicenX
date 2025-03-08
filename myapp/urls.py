from rest_framework import routers
from .views import UserView, InstanceView


router = routers.DefaultRouter()

router.register('user', UserView)
router.register('instance', InstanceView)

urlpatterns = []

urlpatterns += router.urls
