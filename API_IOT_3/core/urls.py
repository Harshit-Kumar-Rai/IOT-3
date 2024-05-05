
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views.device_viewset import DeviceViewSet, DeviceTypeViewSet, DeviceInstallationViewSet, DeviceInstallImageViewSet
from app.views.address_viewset import AddressViewSet,GetAllCityOfStateAddressCustomView, GetAllStateAddressCustomView, GetAllWardOfStateAddressCustomeView
from app.views.entity_viewset import EntityViewSet, EntityRoleViewSet, EntityTypeViewSet
from app.views.iot_data_viewswt import IOTDataViewSet
from app.views.person_viewset import PersonViewSet
from app.views.rd_viewset import RDViewSet
from app.views.contact_type_viewset import AddressTypeViewSet
# from app.views.person_viewset import Person

router = DefaultRouter()
router.register('device', DeviceViewSet, basename='device')
router.register('device-type', DeviceTypeViewSet, basename='device-type')
router.register('device-installation', DeviceInstallationViewSet, basename='device-installation')
router.register('device-image', DeviceInstallImageViewSet, basename='device-image')

router.register('address', AddressViewSet, basename='address')

#entity endpoints
router.register('entity', EntityViewSet, basename='entiy')
router.register('entity-type', EntityTypeViewSet, basename='entiy-type')
router.register('entity-role', EntityRoleViewSet, basename='entiy-role')

router.register('iotdata', IOTDataViewSet, basename='iotdata')
router.register('person', PersonViewSet, basename='person')
router.register('register-device', RDViewSet, basename='rrgister-device')

router.register('address-type', AddressTypeViewSet, basename='address-type')
urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
    path('api2/', include('app.urls')),
    path('api/get-city/<int:state_id>/', GetAllCityOfStateAddressCustomView.as_view()),
    path('api/get-state/<int:country_id>/', GetAllStateAddressCustomView.as_view()),
    path('api/get-ward/<int:state_id>/', GetAllWardOfStateAddressCustomeView.as_view()),
]
