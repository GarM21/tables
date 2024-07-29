from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TableCellViewSet, TableRowViewSet, TableColumnViewSet

router = DefaultRouter()
router.register(r'table-cells', TableCellViewSet)
router.register(r'table-rows', TableRowViewSet)
router.register(r'table-columns', TableColumnViewSet)

urlpatterns = [
    path('', include(router.urls)),
]