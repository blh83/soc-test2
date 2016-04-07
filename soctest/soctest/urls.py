from django.conf.urls import include, url
from django.contrib import admin
from contactmgr.views import (
    csv_upload,
    delete_records,
    SuccessView,
)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contactmgr/$', csv_upload, name='csv_upload'),
    url(r'^delete/$', delete_records, name='delete_records'),
    url(r'^success/', SuccessView.as_view(), name='success_view'),
]
