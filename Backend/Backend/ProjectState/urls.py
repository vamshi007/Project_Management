from rest_framework import routers
from .views import  ProjectStateViewSets
router = routers.SimpleRouter()
router.register(r'', ProjectStateViewSets)

urlpatterns = router.urls
