from rest_framework.routers import SimpleRouter
from .views import ItemsPage, OrderAdd
from django.urls import path

router = SimpleRouter()
router.register('api/items', ItemsPage)

urlpatterns = [
    path('api/order-add/', OrderAdd.as_view())
]
urlpatterns += router.urls
