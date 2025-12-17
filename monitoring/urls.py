from django.urls import path
from .views import DeviceListView,DeviceSummaryView
urlpatterns=[
 path('devices/',DeviceListView.as_view()),
 path('devices/<int:id>/summary/',DeviceSummaryView.as_view()),
]
