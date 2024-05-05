from django.urls import path
from rest_framework.routers import DefaultRouter
from app.views.device_viewset import DeviceViewSet
from app.views.custom_viewset import AddressListCustom
from app.views.address_viewset import GetAddressThroughJoin
router = DefaultRouter()
router.register('device', DeviceViewSet, basename='device')

urlpatterns =[
  # path('filter-api/', router.urls)
  path('entities/<int:entity_id>/addresses/', AddressListCustom.as_view(), name='entity-addresses'),
  path("joins/", GetAddressThroughJoin.as_view())

]